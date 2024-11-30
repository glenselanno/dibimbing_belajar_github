import pandas as pd

def read_csv_file(file_path):
    try:
        df = pd.read_csv(file_path)
        print("CSV file read successfully!")
        print(df.head())
    except Exception as e:
        print(f"Error reading the CSV file: {e}")

if __name__ == "__main__":
    read_csv_file("username.csv")

