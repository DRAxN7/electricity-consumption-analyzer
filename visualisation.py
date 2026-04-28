import matplotlib.pyplot as plt
import os
def create_charts(df):
    if not os.path.exists("charts"):
        os.makedirs("charts")

    plt.figure(figsize=(8,5))
    plt.plot(df['date'], df['consumption_kwh'], marker='o')
    plt.title('Daily Electricity Consumption')
    plt.xlabel('Date')
    plt.ylabel('Consumption (kWh)')
    plt.grid(True)
    plt.savefig('charts/consumption_chart.png')
    plt.show()

    plt.figure(figsize=(8,5))
    plt.bar(df['date'], df['peak_load_kwh'])
    plt.title('Peak Load by Date')
    plt.xlabel('Date')
    plt.ylabel('Peak Load (kWh)')
    plt.savefig('charts/peak_load_chart.png')
    plt.show()