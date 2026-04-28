def calculate_metrics(df):
    total_energy = df['Energy_Kwh'].sum()
    average_energy = df['Energy_Kwh'].mean()
    peak_demand = df['Energy_Kwh'].max()
    load_factor = average_energy / peak_demand

    return {
        "Total Energy (Kwh)": total_energy,
        "Average Energy (Kwh)": average_energy,
        "Peak Demand (Kwh)": peak_demand,
        "Load Factor": load_factor
    }
