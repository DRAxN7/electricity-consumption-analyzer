from load_data import load_data
from analysis import analyze_data
from visualisation import create_charts
import os

try:
    df = load_data()
    if df is None:
        print("Program stopped because data cannot be loaded")
        exit()

    print(df)

    results = analyze_data(df)

    if results is None:
        print("Program stopped because analysis failed")
        exit()


    (
        total_consumption,
        average_consumption,
        peak_load,
        load_factor,
        estimated_bill,
        highest_day,
        lowest_day
    ) = results

    print(f"Total Consumption: {total_consumption:.3f}")
    print(f"Average Consumption: {average_consumption:.3f}")
    print(f"Peak Load: {peak_load:.3f}")
    print(f"Load Factor: {load_factor:.3f}")
    print(f"Estimated Bill: Rs{estimated_bill:.2f}")

    print("\nHighest Consumption Day:")
    print(highest_day)

    print("\nLowest Consumption Day:")
    print(lowest_day)

    create_charts(df)

except Exception as e:
    print(f"Application Error:{e}")