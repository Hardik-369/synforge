import pandas as pd
from pathlib import Path
import typer

def load_csv(file_path: Path) -> pd.DataFrame:
    """
    Loads a CSV file into a pandas DataFrame.
    """
    try:
        df = pd.read_csv(file_path)
        print(f"Successfully loaded {file_path.name}. Shape: {df.shape}")
        return df
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        raise typer.Exit(code=1)
    except Exception as e:
        print(f"An error occurred while reading the CSV file: {e}")
        raise typer.Exit(code=1)
