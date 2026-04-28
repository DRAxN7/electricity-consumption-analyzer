def analyze_data(df):
    try:
        if df is None:
            print("Error: No data available for analysis")
            return None

        total_consumption = df['consumption_kwh'].sum()
        average_consumption = df['consumption_kwh'].mean()
        peak_load = df['peak_load_kwh'].max()

        if peak_load == 0:
            print("Error: Peak Load cannot be zero")
            return None

        load_factor = average_consumption / peak_load

        rate_per_kwh = 8
        estimated_bill = total_consumption * rate_per_kwh

        highest_day = df.loc[df['consumption_kwh'].idxmax()]
        lowest_day = df.loc[df['consumption_kwh'].idxmin()]

        return (
            total_consumption,
            average_consumption,
            peak_load,
            load_factor,
            estimated_bill,
            highest_day,
            lowest_day
        )

    except KeyError as e:
        print(f"Missing Column Error: {e}")
        return None

    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
        return None

    except Exception as e:
        print(f"Unexpected Error: {e}")
        return None