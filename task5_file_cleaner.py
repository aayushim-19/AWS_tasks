import json
import pandas as pd
from utils import clean_dataframe

def lambda_handler(event, context):
    # Example: input CSV path (mock)
    file_path = "/tmp/input.csv"

    # Dummy CSV creation (for test)
    with open(file_path, "w") as f:
        f.write("Name,Age\nAayushi,22\n,25")

    df = pd.read_csv(file_path)