import typer
import pandas as pd
import shutil
from pathlib import Path

from synforge.utils import load_csv
from synforge.anonymizer import anonymize_dataframe
from synforge.generator import generate_synthetic_data
from synforge.state import (
    ensure_cache_dir_exists,
    SOURCE_DATA_PATH,
    ANONYMIZED_DATA_PATH,
    SYNTHETIC_DATA_PATH,
)

app = typer.Typer(
    name="synforge",
    help="🧠 SynForge — Turn your real-world tabular data into anonymized, AI-generated synthetic datasets.",
    no_args_is_help=True,
)

@app.callback()
def main():
    """
    Manage the synthetic data generation workflow.
    """
    ensure_cache_dir_exists()

@app.command()
def upload(
    file: Path = typer.Option(..., "--file", "-f", help="Path to the source CSV file."),
):
    """
    Upload, process, and anonymize the source data file.
    """
    print(f"Uploading file: {file}...")
    df = load_csv(file)

    # Save the original data to the cache
    df.to_csv(SOURCE_DATA_PATH, index=False)
    print(f"Saved source data to cache: {SOURCE_DATA_PATH}")

    # Anonymize the data
    df_anonymized = anonymize_dataframe(df)

    # Save the anonymized data to the cache
    df_anonymized.to_csv(ANONYMIZED_DATA_PATH, index=False)
    print(f"Saved anonymized data to cache: {ANONYMIZED_DATA_PATH}")

    print("\n✅ Upload and anonymization complete. Ready to generate synthetic data.")

@app.command()
def generate(
    model: str = typer.Option("ctgan", "--model", "-m", help="Synthetic data model to use."),
    rows: int = typer.Option(None, "--rows", "-r", help="Number of synthetic rows to generate. Defaults to original file's length."),
):
    """
    Generate synthetic data from the uploaded file.
    """
    if not ANONYMIZED_DATA_PATH.exists():
        print("Error: No anonymized data found. Please run the 'upload' command first.")
        raise typer.Exit(code=1)

    print("Loading anonymized data from cache...")
    df_anonymized = pd.read_csv(ANONYMIZED_DATA_PATH)

    # If rows is not specified, default to the original number of rows
    if rows is None:
        rows = len(df_anonymized)
        print(f"Number of rows not specified, defaulting to {rows}.")

    # Generate synthetic data
    synthetic_df = generate_synthetic_data(df_anonymized, model_name=model, num_rows=rows)

    # Save the synthetic data to the cache
    synthetic_df.to_csv(SYNTHETIC_DATA_PATH, index=False)
    print(f"Saved synthetic data to cache: {SYNTHETIC_DATA_PATH}")

    print("\n✅ Synthetic data generation complete. Ready to export.")

@app.command()
def export(
    out: Path = typer.Option(..., "--out", "-o", help="Path to save the exported synthetic CSV file."),
):
    """
    Export the generated synthetic data to a file.
    """
    if not SYNTHETIC_DATA_PATH.exists():
        print("Error: No synthetic data found. Please run the 'generate' command first.")
        raise typer.Exit(code=1)

    print(f"Exporting synthetic data from {SYNTHETIC_DATA_PATH} to {out}...")
    shutil.copy(SYNTHETIC_DATA_PATH, out)

    print(f"\n✅ Synthetic data exported successfully to: {out.resolve()}")

if __name__ == "__main__":
    app()
