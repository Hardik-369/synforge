import pandas as pd
from sdv.metadata.single_table import SingleTableMetadata
from sdv.single_table import CTGANSynthesizer

def generate_synthetic_data(
    data: pd.DataFrame,
    model_name: str = "ctgan",
    num_rows: int = 1000,
    ) -> pd.DataFrame:
    """
    Generates synthetic data using a specified model from the SDV library.

    Args:
        data: The input pandas DataFrame (should be anonymized).
        model_name: The name of the model to use (e.g., "ctgan").
        num_rows: The number of synthetic rows to generate.

    Returns:
        A new DataFrame containing the generated synthetic data.
    """
    print(f"Starting synthetic data generation with model: {model_name}")

    # --- Model Selection ---
    if model_name.lower() == "ctgan":
        print("Detecting metadata from the data...")
        metadata = SingleTableMetadata()
        metadata.detect_from_dataframe(data)

        synthesizer = CTGANSynthesizer(
            metadata,
            epochs=10 # Using fewer epochs for a quick test run
        )
    else:
        print(f"Error: Model '{model_name}' is not supported. Please use 'ctgan'.")
        return pd.DataFrame()

    print("Fitting the synthesizer to the data... (This may take a while)")
    synthesizer.fit(data)

    print(f"Generating {num_rows} synthetic rows...")
    synthetic_data = synthesizer.sample(num_rows=num_rows)

    print("✅ Synthetic data generated successfully.")
    return synthetic_data
