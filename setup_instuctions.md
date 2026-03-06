# Setup Instructions

## 1. Install SUMO Simulator

Download and install **SUMO (Simulation of Urban Mobility)** from the official website.

https://www.eclipse.org/sumo/

After installation, add the SUMO `bin` directory to your system PATH.

Example (Windows):

C:\Program Files (x86)\Eclipse\Sumo\bin

---

## 2. Install Python Dependencies

Make sure Python 3.8 or above is installed.

Install required libraries using:

pip install pandas matplotlib traci

Or install from the requirements file:

pip install -r requirements.txt

---

## 3. Run AI-Based Self-Healing Traffic Controller

python src/main.py

This runs the intelligent traffic signal controller using AI logic.

---

## 4. Run Fixed-Time Traffic Controller

python src/fixed_main.py

This runs the traditional fixed-timing traffic signal system.

---

## 5. Generate Performance Comparison Plots

python src/evaluation/plots.py

This will generate graphs comparing:

* Average waiting time
* Vehicle queue length
* Traffic congestion levels

---

## Output

Results and comparison graphs will be saved inside the `evaluation` or `logs` folders.
