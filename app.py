import pandas as pd
import tkinter as tk
from tkinter import filedialog
import os

def select_csv_file():
    # Create a Tkinter window and hide it
    root = tk.Tk()
    root.withdraw()
    # Open a file dialog to select a CSV file
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    return file_path

def csv_to_excel(csv_file, excel_file):
    # Read the CSV file
    df = pd.read_csv(csv_file)
    # Write the data to an Excel file
    df.to_excel(excel_file, index=False)

# Select CSV file
csv_file = select_csv_file()

if csv_file:
    # Get the directory path where the CSV file is located
    csv_directory = os.path.dirname(csv_file)
    # Get the filename of the CSV file without extension
    csv_filename = os.path.splitext(os.path.basename(csv_file))[0]
    # Define the output Excel file name with the name of the CSV file and the word "converted"
    excel_filename = f"{csv_filename}_converted.xlsx"
    excel_file = os.path.join(csv_directory, excel_filename)

    # Call the function to convert CSV to Excel
    csv_to_excel(csv_file, excel_file)

    print(f"The CSV file '{csv_file}' has been converted to '{excel_file}' successfully.")
else:
    print("No CSV file selected.")
