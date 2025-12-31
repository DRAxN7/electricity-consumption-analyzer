import matplotlib.pyplot as plt

def plot_energy_trend(df):
    plt.figure(figsize=(8, 4))
    plt.plot(df['Date'], df['Energy_Kwh'], marker='o')
    plt.xlabel("Date")
    plt.ylabel("Energy Consumption (kWh)")
    plt.title("Daily Electricity Consumption Trend")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
def plot_energy_bar(df):
    plt.figure(figsize=(8, 4))
    plt.bar(df['Date'], df['Energy_Kwh'])
    plt.xlabel("Date")
    plt.ylabel("Energy Consumption (kWh)")
    plt.title("Daily Electricity Consumption (Bar Chart)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()