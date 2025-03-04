import os
import pandas as pd


TIMESHEET_FOLDER = 'timesheets'
SUMMARY_FILE = 'summary.xlsx'

def process_timesheet(file_path, employee_name):
    try:
        df = pd.read_excel(file_path)
        data = df[['Date','Name', 'Status']].copy()
        return data
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return None

def main():
    all_data = []
    for employee_folder in os.listdir(TIMESHEET_FOLDER):
        employee_path = os.path.join(TIMESHEET_FOLDER, employee_folder)
        if os.path.isdir(employee_path):
            print(f"Processing folder: {employee_folder}")
            for file_name in os.listdir(employee_path):
                if file_name.endswith('.xlsx'):
                    file_path = os.path.join(employee_path, file_name)
                    print(f"Processing file: {file_name}")
                    data = process_timesheet(file_path, employee_folder)
                    if data is not None:
                        all_data.append(data)

    if all_data:
        combined_df = pd.concat(all_data)
        combined_df.to_excel(SUMMARY_FILE, index=False)
        print(f"Summary saved to {SUMMARY_FILE}")
    else:
        print("No data found.")

if __name__ == "__main__":
    main()