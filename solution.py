import numpy as np
import matplotlib.pyplot as plt

# Use a white background (reset default style)
plt.style.use("default")

# Read file and process lines manually
with open("imudata.txt", "r") as file:
    lines = file.readlines()

# Extract numerical data, skipping first two columns (date & time)
data = np.array([list(map(float, line.strip().split()[2:])) for line in lines])

# Extract the pitch angle (5th column, index 3 after skipping first two)
pitch_raw = data[:, 3]

# Define moving average function
def moving_average(data, window_size):
    """Compute the moving average for a given window size."""
    averaged_data = np.zeros(len(data))
    for i in range(len(data)):
        if i < window_size:
            averaged_data[i] = np.mean(data[:i+1])  # Handle initial partial window
        else:
            averaged_data[i] = np.mean(data[i-window_size+1:i+1])  # Full window
    return averaged_data

# Define window sizes for moving averages
window_sizes = [2, 4, 8, 16, 64, 128]

# Define x-axis values
x_values = np.arange(len(pitch_raw))

# Define high-quality colors
colors = plt.get_cmap("cool")(np.linspace(0, 1, len(window_sizes)))

# Generate separate plots for each moving average
for i, window in enumerate(window_sizes):
    pitch_avg = moving_average(pitch_raw, window)
    mean_val = np.mean(pitch_avg)
    std_val = np.std(pitch_avg)

    plt.figure(figsize=(12, 6), facecolor="white")  # Set background to white

    # Plot raw data as very light connected lines + scatter points
    plt.plot(x_values, pitch_raw, label="Raw Data (Light Line)", linestyle="-", linewidth=0.6, alpha=0.3, color="gray")
    plt.scatter(x_values, pitch_raw, label="Raw Data (Points)", color="gray", alpha=0.6, s=12, marker="o")

    # Plot moving average as a solid, clear line
    plt.plot(x_values, pitch_avg, label=f"{window}-pt Moving Average", linewidth=2.2, color=colors[i], linestyle="solid", alpha=0.85)

    # Add shaded area for standard deviation
    plt.fill_between(x_values, pitch_avg - std_val, pitch_avg + std_val, color=colors[i], alpha=0.2)

    # Add mean & std deviation annotation
    plt.annotate(f"Mean: {mean_val:.2f}\nStd Dev: {std_val:.2f}",
                 xy=(0.05 * len(pitch_raw), max(pitch_raw) * 0.85),
                 fontsize=14, color="black", bbox=dict(facecolor='white', edgecolor='gray', alpha=0.9))

    # Labels and Title with improved fonts
    plt.xlabel("Sample Index", fontsize=14, fontweight="bold", family="serif")
    plt.ylabel("Pitch Angle (degrees)", fontsize=14, fontweight="bold", family="serif")
    plt.title(f"{window}-pt Moving Average", fontsize=16, fontweight="bold", color=colors[i], family="serif")

    # Customize legend
    plt.legend(fontsize=12, frameon=True, fancybox=True, shadow=True, loc="upper right")

    # Reduce grid intensity for a cleaner look
    plt.grid(alpha=0.5)

    # Save each plot as high-quality PNG & PDF
    plt.savefig(f"pitch_analysis_{window}pt.png", dpi=300, bbox_inches="tight", facecolor="white")
    plt.savefig(f"pitch_analysis_{window}pt.pdf", dpi=300, bbox_inches="tight", facecolor="white")
    plt.show()
