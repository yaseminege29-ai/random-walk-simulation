# Random Walk Simulation Project
# Author: Yasemin
# Description: 2D random walk simulation with MSD analysis
import numpy as np
import matplotlib.pyplot as plt

# parametreler
num_steps = 1000
runs = 50

# --- 1. AŞAMA: TEK RANDOM WALK (görselleştirme için) ---
x, y = [0], [0]

for _ in range(num_steps):
    dx, dy = np.random.randn(), np.random.randn()
    x.append(x[-1] + dx)
    y.append(y[-1] + dy)

# grafik
plt.figure(figsize=(6,6))
plt.plot(x, y, linewidth=1)
plt.scatter(x[0], y[0], color='green', label='Start')
plt.scatter(x[-1], y[-1], color='red', label='End')
plt.title("2D Random Walk Simulation", fontsize=14)
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid()

# --- 2. AŞAMA: MULTIPLE RUNS + ORTALAMA MSD ---
msd_list = []

for r in range(runs):
    x_run, y_run = [0], [0]
    
    for i in range(num_steps):
        dx, dy = np.random.randn(), np.random.randn()
        x_run.append(x_run[-1] + dx)
        y_run.append(y_run[-1] + dy)
    
    msd = np.mean(np.array(x_run)**2 + np.array(y_run)**2)
    msd_list.append(msd)

avg_msd = np.mean(msd_list)

print("Average Mean Squared Displacement over", runs, "runs:", avg_msd)

plt.show()
# --- 3. AŞAMA: MSD vs STEP (zaman analizi) ---

msd_time = np.zeros(num_steps)

for r in range(runs):
    x_run, y_run = [0], [0]
    
    for i in range(num_steps):
        dx, dy = np.random.randn(), np.random.randn()
        x_run.append(x_run[-1] + dx)
        y_run.append(y_run[-1] + dy)
        
        r2 = x_run[-1]**2 + y_run[-1]**2
        msd_time[i] += r2

# ortalama al
msd_time = msd_time / runs

# grafik
plt.figure()
plt.plot(range(num_steps), msd_time)
plt.xlabel("Step")
plt.ylabel("MSD")
plt.title("MSD vs Time (Random Walk)")
plt.grid()
plt.show()
# --- 4. AŞAMA: Farklı step sayıları için ortalama MSD karşılaştırması ---

step_values = [100, 300, 500, 1000, 1500, 2000]
avg_msd_values = []

for steps in step_values:
    msd_list_steps = []

    for r in range(runs):
        x_run, y_run = [0], [0]

        for i in range(steps):
            dx, dy = np.random.randn(), np.random.randn()
            x_run.append(x_run[-1] + dx)
            y_run.append(y_run[-1] + dy)

        msd = np.mean(np.array(x_run)**2 + np.array(y_run)**2)
        msd_list_steps.append(msd)

    avg_msd = np.mean(msd_list_steps)
    avg_msd_values.append(avg_msd)

plt.figure()
plt.plot(step_values, avg_msd_values, marker='o')
plt.title("Average MSD for Different Step Counts")
plt.xlabel("Number of Steps")
plt.ylabel("Average MSD")
plt.grid()
plt.show()