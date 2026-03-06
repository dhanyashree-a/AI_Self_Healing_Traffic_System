import traci
import time
import pandas as pd
import os

# ===================== CONFIG =====================
SUMO_CONFIG = "sumo/config/traffic.sumocfg"
TLS_ID = "C"
MAX_STEPS = 300
DEBUG = True   # Set False for silent run

EDGE_PHASE_MAP = {
    "N2C": 0,
    "S2C": 0,
    "E2C": 2,
    "W2C": 2
}

incoming_edges = ["N2C", "S2C", "E2C", "W2C"]

# ===================== START SUMO =====================
def start_sumo():
    traci.start(["sumo-gui", "-c", SUMO_CONFIG])

# ===================== EMERGENCY =====================
def detect_emergency():
    for v in traci.vehicle.getIDList():
        if "ambulance" in v.lower():
            edge = traci.vehicle.getRoadID(v)
            if edge in incoming_edges:
                return edge
    return None

# ===================== SIGNAL =====================
def apply_signal_control(green_time, phase):
    traci.trafficlight.setPhase(TLS_ID, phase)
    traci.trafficlight.setPhaseDuration(TLS_ID, green_time)

# ===================== MAIN =====================
def main():
    start_sumo()
    step = 0

    print("\n🚦 AI-Based Adaptive Traffic Control Started\n")

    last_selected_edge = None
    current_green_remaining = 0
    current_phase = None

    # ===================== METRICS =====================
    steps = []
    waiting_times = []
    queue_lengths = []
    throughputs = []

    while step < MAX_STEPS:

        if (
            traci.simulation.getMinExpectedNumber() == 0
            and len(traci.vehicle.getIDList()) == 0
        ):
            print("\n✅ Traffic cleared — ending simulation gracefully")
            break

        traci.simulationStep()
        time.sleep(0.05)

        # ===================== METRIC COLLECTION =====================
        vehicles = traci.vehicle.getIDList()
        total_wait = sum(traci.vehicle.getWaitingTime(v) for v in vehicles)
        avg_wait = total_wait / len(vehicles) if vehicles else 0

        queue = 0
        for edge in incoming_edges:
            queue += sum(
                1 for v in traci.edge.getLastStepVehicleIDs(edge)
                if traci.vehicle.getSpeed(v) < 0.1
            )

        throughput = traci.simulation.getArrivedNumber()

        steps.append(step)
0
            continue

        if 5 < step < 280:

            if DEBUG:
                print(f"\n⏱ Simulation Step: {step}")

            # ===================== 🚑 EMERGENCY PRIORITY =====================
            emergency_edge = detect_emergency()
            if emergency_edge:
                phase = EDGE_PHASE_MAP[emergency_edge]
                green_time = 40

                apply_signal_control(green_time, phase)
                current_green_remaining = green_time
                current_phase = phase
                last_selected_edge = emergency_edge

                if DEBUG:
                    print(f"🚑 Emergency Vehicle on {emergency_edge}")
                    print(f"🚦 Signal Forced GREEN for {green_time}s")
                    print("-" * 60)

                step += 1
                continue

            # ===================== SMART BALANCED AI =====================
            edge_scores = {}

            for edge in incoming_edges:
                vehicle_count = traci.edge.getLastStepVehicleNumber(edge)
                queue_count = sum(
                    1 for v in traci.edge.getLastStepVehicleIDs(edge)
                    if traci.vehicle.getSpeed(v) < 0.1
                )

                # Balanced weighted score
                score = vehicle_count + (queue_count * 1.8)

                # Fairness penalty (avoid domination)
                if edge == last_selected_edge:
                    score *= 0.75

                edge_scores[edge] = score

            best_edge = max(edge_scores, key=edge_scores.get)
            max_score = edge_scores[best_edge]

            # ===================== CONTROLLED GREEN SCALING =====================
            if max_score >= 25:
                green_time = 35
                density = "Very High"
            elif max_score >= 12:
                green_time = 25
                density = "High"
            else:
                green_time = 18
                density = "Moderate"

            phase = EDGE_PHASE_MAP[best_edge]

            apply_signal_control(green_time, phase)
            current_green_remaining = green_time
            current_phase = phase
            last_selected_edge = best_edge

            if DEBUG:
                print(
                    f"🚦 Selected Edge: {best_edge} | "
                    f"Score: {max_score:.1f} | "
                    f"{density} → Green = {green_time}s"
                )
                print("Active Vehicles:", vehicles)
                print("-" * 60)

        step += 1

    traci.close()

    # ===================== SAVE CSV =====================
    os.makedirs("evaluation", exist_ok=True)

    df = pd.DataFrame({
        "Step": steps,
        "AvgWaitingTime": waiting_times,
        "QueueLength": queue_lengths,
        "Throughput": throughputs
    })

    df.to_csv("evaluation/ai_metrics.csv", index=False)

    print("\n📊 AI Metrics saved to evaluation/ai_metrics.csv")
    print("🛑 Simulation closed gracefully")


if __name__ == "__main__":
    main()
