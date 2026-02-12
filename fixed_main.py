import traci
import time
import csv

SUMO_CONFIG = "sumo/config/traffic.sumocfg"
TLS_ID = "C"

incoming_edges = ["N2C", "S2C", "E2C", "W2C"]

def start_sumo():
    traci.start(["sumo-gui", "-c", SUMO_CONFIG])

def apply_fixed_signal():
    """
    Fixed cycle:
    40s North-South
    40s East-West
    """
    traci.trafficlight.setPhase(TLS_ID, 0)
    traci.trafficlight.setPhaseDuration(TLS_ID, 40)

def main():
    start_sumo()
    step = 0
    MAX_STEPS = 300

    total_waiting_time = 0
    vehicle_observations = 0
    queue_lengths = []
    throughput = 0

    csv_file = open("evaluation/fixed_metrics.csv", "w", newline="")
    writer = csv.writer(csv_file)
    writer.writerow(["Step", "AvgWaitingTime", "QueueLength"])

    print("\n🚦 Fixed-Time Traffic Control Started\n")

    while step < MAX_STEPS:

        if (
            traci.simulation.getMinExpectedNumber() == 0
            and len(traci.vehicle.getIDList()) == 0
        ):
            print("\n✅ Traffic cleared — ending simulation")
            break

        traci.simulationStep()
        time.sleep(0.1)

        # Apply fixed control every 40 seconds
        if step % 40 == 0:
            if (step // 40) % 2 == 0:
                traci.trafficlight.setPhase(TLS_ID, 0)
                traci.trafficlight.setPhaseDuration(TLS_ID, 40)
            else:
                traci.trafficlight.setPhase(TLS_ID, 2)
                traci.trafficlight.setPhaseDuration(TLS_ID, 40)

        # ================= Metrics =================
        current_wait = 0
        vehicles = traci.vehicle.getIDList()

        for v in vehicles:
            current_wait += traci.vehicle.getWaitingTime(v)

        avg_wait = current_wait / len(vehicles) if vehicles else 0

        queue = 0
        for edge in incoming_edges:
            for v in traci.edge.getLastStepVehicleIDs(edge):
                if traci.vehicle.getSpeed(v) < 0.1:
                    queue += 1

        queue_lengths.append(queue)
        throughput += traci.simulation.getArrivedNumber()

        writer.writerow([step, avg_wait, queue])

        total_waiting_time += current_wait
        vehicle_observations += len(vehicles)

        step += 1

    traci.close()
    csv_file.close()

    print("\n📊 Fixed Metrics saved to evaluation/fixed_metrics.csv")
    print("🛑 Simulation closed")

if __name__ == "__main__":
    main()
