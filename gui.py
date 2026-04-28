import tkinter as tk
from tkinter import messagebox

from load_data import load_data
from analysis import analyze_data
from visualisation import create_charts
root = tk.Tk()
root.title("Electricity Consumption Analyzer")
root.geometry("500x500")

result_text = tk.StringVar()

heading = tk.Label(root, text="Electricity Consumption Analyzer", font=("Arial",16,"bold"))
heading.pack(pady=10)

result_label = tk.Label(root, textvariable=result_text, justify="left")
result_label.pack(pady=15)


def run_analysis():
    try:
        df = load_data()
        result = analyze_data(df)

        if result is None:
            messagebox.showerror("Error", "No data found")
            return

        total, avg, peak, lf, bill, high, low = result

        output = f"""
Total Consumption: {round(total,2)}
Average Consumption: {round(avg,2)}
Peak Load: {round(peak,2)}
Load Factor: {round(lf,2)}
Estimated Bill: ₹{round(bill,2)}
"""

        result_text.set(output)

    except Exception as e:
        messagebox.showerror("Error", str(e))


def show_chart():
    df = load_data()
    create_charts(df)


tk.Button(root, text="Run Analysis", width=20, command=run_analysis).pack(pady=5)
tk.Button(root, text="Show Chart", width=20, command=show_chart).pack(pady=5)
tk.Button(root, text="Exit", width=20, command=root.destroy).pack(pady=5)

root.mainloop()