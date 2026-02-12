🚦 AI Self-Healing Traffic Signal Control System

An intelligent rule-based adaptive traffic signal control system built using SUMO (Simulation of Urban Mobility) and TraCI API.

This system dynamically adjusts traffic light timings based on real-time congestion levels and prioritizes emergency vehicles, outperforming traditional fixed-time traffic control.

📌 Project Overview

Traditional traffic signals use fixed timing cycles regardless of traffic density. This often leads to:

-> Increased waiting time
-> Long queue lengths
-> Poor emergency vehicle response

This project introduces an adaptive congestion-aware traffic control system that:
-> Monitors real-time vehicle density
-> Calculates weighted congestion scores
-> Dynamically adjusts green signal durations
-> Gives priority to emergency vehicles
-> Compares performance with fixed-time traffic control

Approach

This is a rule-based adaptive system (not machine learning).

🔹 Congestion Score Calculation
Score = Vehicle_Count + (Queue_Count × 1.5)Score = Vehicle_Count + (Queue_Count × 1.5)
  Queue vehicles are weighted higher to prioritize heavy traffic.

🔹 Dynamic Green Time
| Score Range | Green Time |
| ----------- | ---------- |
| 0           | 15s        |
| < 10        | 18s        |
| 10–20       | 25s        |
| > 20        | 35s        |

🔹 Emergency Handling

If an ambulance is detected:
-> Signal immediately turns green
-> Green held for ~40–45 seconds
->Control resumes normally

📊 Results

The AI-based controller achieved:

✅ Lower average waiting time
✅ Reduced queue length
✅ Better emergency response
✅ More balanced traffic distribution
Compared to the fixed-time system.

🛠 Tech Stack
-> Python
-> SUMO
-> TraCI API
-> Pandas
-> Matplotlib

🧪 How to Run
1️⃣ Install SUMO
Download and install SUMO from the official website.
Add SUMO to your system PATH.

2️⃣ Install Python Dependencies
pip install pandas matplotlib traci

3️⃣ Run AI Controller
python main.py

4️⃣ Run Fixed Controller
python fixed_main.py

5️⃣ Generate Comparison Plots
python evaluation/plots.py


📚 Future Improvements

-> Reinforcement Learning (Q-learning / DQN)
-> Deep Traffic Prediction Models
-> Multi-intersection coordination
-> Computer vision vehicle detection
-> Smart city IoT integration

🏁 Conclusion

This project demonstrates how adaptive rule-based traffic control can outperform traditional fixed-time systems using real-time congestion monitoring and intelligent decision logic.

It serves as a strong foundation for:

-> Intelligent Transportation Systems (ITS)
-> Smart City Research
-> AI-based Infrastructure Optimization
-> Traffic Simulation Research

👩‍💻 Author
Dhanya Shree A
B.Tech CSE
AI & Intelligent Systems Enthusiast