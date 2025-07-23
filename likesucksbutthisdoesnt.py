import pandas as pd
import os
import sys
import subprocess

def save_excel_file_with_versioning(df_to_save, output_directory, base_filename):
    print(f"\n--- Preparing to save DataFrame in '{output_directory}' ---")
    
    try:
        if not os.path.exists(output_directory):
            os.makedirs(output_directory, exist_ok=True)
            print(f"Created directory: {output_directory}")
    except Exception as e:
        print(f"Error creating directory '{output_directory}': {e}")
        return None

    excel_filename = base_filename + ".xlsx"
    
    counter = 1
    final_path = os.path.join(output_directory, excel_filename)
    while os.path.exists(final_path):
        versioned_filename = f"{base_filename}_{counter}.xlsx"
        final_path = os.path.join(output_directory, versioned_filename)
        counter += 1

    try:
        print(f"Saving DataFrame to '{final_path}'...")
        df_to_save.to_excel(final_path, index=False)
        print(f"DataFrame saved successfully to: {final_path}\n")
        return final_path
    except ImportError:
        print("Error: 'openpyxl' is not installed. Run: pip install openpyxl")
        return None
    except Exception as e:
        print(f"An error occurred while saving the Excel file: {e}")
        return None

def open_file_on_system(file_path):
    if not file_path or not os.path.exists(file_path):
        print(f"Cannot open file: Path is invalid or file does not exist: {file_path}")
        return
        
    print(f"\n--- Attempting to Open '{file_path}' on your system ---")
    try:
        if sys.platform == "win32":
            os.startfile(os.path.realpath(file_path))
        elif sys.platform == "darwin":
            subprocess.call(['open', file_path])
        else:
            subprocess.call(['xdg-open', file_path])
        print("Opened file successfully. Check your default spreadsheet application.")
    except Exception as e:
        print(f"Could not automatically open the file. Please open it manually from: {file_path}")
        print(f"Error details: {e}")

def export_and_open_dataframe(df_to_export, original_source_path, output_directory='.'):
    print("\n--- Starting DataFrame Export Workflow ---")

    if not isinstance(df_to_export, pd.DataFrame):
        print("Workflow stopped: The provided 'df_to_export' is not a pandas DataFrame.")
        return

    base_name_with_ext = os.path.basename(original_source_path)
    base_name_without_ext = os.path.splitext(base_name_with_ext)[0]

    saved_file_path = save_excel_file_with_versioning(df_to_export, output_directory, base_name_without_ext)
    
    if not saved_file_path:
        print("Workflow stopped: Failed to save Excel file.")
        return

    open_file_on_system(saved_file_path)

    print("\n--- DataFrame Export Completed ---")
