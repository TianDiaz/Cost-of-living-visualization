import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog


def calculate_cost_of_living(csv_file):
    # Data Collection
    # The 'csv_file' is from the user
    data = pd.read_csv(csv_file)

    # Check if the required columns exists in the DataFrame
    required_columns = ['Food', 'Housing', 'Clothes', 'Transportation', 'Personal Care', 'Entertainment']
    missing_columns = [col for col in required_columns if col not in data.columns]
    if missing_columns:
        raise KeyError(f"The following columns are missing in the DataFrame: {', '.join(missing_columns)}")

    # Data Analysis
    # Calculating the total cost of living by summing up the expenses in each category
    data['Total_Cost_of_Living'] = data[['Food', 'Housing', 'Clothes', 'Transportation', 'Personal Care', 'Entertainment']].sum(axis=1)

    # Calculating the national average cost of living
    national_average = data['Total_Cost_of_Living'].mean()
    return data, national_average


def plot_cost_of_living(data, national_average):
    # Data Visualization
    # Bar plot for comparing the total cost of living for each province
    plt.figure(figsize=(10, 6))
    bars = plt.bar(data['Province'], data['Total_Cost_of_Living'])
    plt.axhline(y=national_average, color='r', linestyle='dashed', label='National Average')
    plt.xlabel('Province/City')
    plt.ylabel('Total Cost of Living')
    plt.title('Cost of Living Comparison by Province/City')
    plt.legend()
    plt.xticks(rotation=90)

    # Text annotation for the average value
    plt.annotate(f'National Average: {national_average:.2f}',
                 xy=(0, national_average), xycoords='data',
                 xytext=(0, 35), textcoords='offset points',
                 arrowprops=dict(arrowstyle="->", color='r', linewidth=2))

    # Changing the color  and displaying the value of the bar with max and min value
    max_index = data['Total_Cost_of_Living'].idxmax()
    min_index = data['Total_Cost_of_Living'].idxmin()
    # #DA2C38
    bars[max_index].set_color('#DA2C38')  # Set color for the bar with the maximum value
    bars[min_index].set_color('g')  # Set color for the bar with the minimum value
    plt.annotate(f'Max: {data["Total_Cost_of_Living"].max():.2f}',
                 xy=(max_index, data['Total_Cost_of_Living'].max()), xycoords='data',
                 xytext=(10, -16), textcoords='offset points', color='white',
                 ha='left', va='bottom', fontsize=12, bbox=dict(boxstyle="round,pad=0.3", fc="#DA2C38", ec="white", lw=1))
    plt.annotate(f'Min: {data["Total_Cost_of_Living"].min():.2f}',
                 xy=(min_index, data['Total_Cost_of_Living'].min()), xycoords='data',
                 xytext=(10, -16), textcoords='offset points', color='white',
                 ha='left', va='bottom', fontsize=12, bbox=dict(boxstyle="round,pad=0.3", fc="g", ec="white", lw=1))

    plt.tight_layout()
    plt.show()


def browse_file():
    filepath = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if filepath:
        data, national_average = calculate_cost_of_living(filepath)
        plot_cost_of_living(data, national_average)

# Window for the application
root = tk.Tk()
root.title("Cost of Living Analysis")
root.configure(bg='#D1D1D1')

# Size of the main window
window_width = 800
window_height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = int((screen_width / 2) - (window_width / 2))
y_coordinate = int((screen_height / 2) - (window_height / 2))
root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

# Label widget to display the "Cost of Living" text
label = tk.Label(root, text="Cost of Living Analysis", font=("Arial", 50), bg='#D1D1D1')
label.pack(pady=90)

# Button to browse and select the CSV file
button_width = 20
button_height = 1
upload_btn = tk.Button(root, text="Upload CSV File", command=browse_file, font=("Arial", 18), width=button_width, height=button_height, bg='#636363', fg='#faf9f6', cursor='hand2')
upload_btn.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Start the main event loop
root.mainloop()

# Created by TianDiaz - https://github.com/TianDiaz

