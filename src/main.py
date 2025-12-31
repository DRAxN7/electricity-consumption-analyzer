from load_data import load_energy_data
from analysis import calculate_metrics
from visualisation import plot_energy_trend,plot_energy_bar
data = load_energy_data("../data/electricity_data.csv")
metrics = calculate_metrics(data)

for key, value in metrics.items():
    print(f"{key}: {value:.2f}")
plot_energy_trend(data)
plot_energy_bar(data)