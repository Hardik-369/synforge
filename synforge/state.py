from pathlib import Path

# Define the cache directory and file paths for state management
CACHE_DIR = Path(".synforge_cache")
SOURCE_DATA_PATH = CACHE_DIR / "source.csv"
ANONYMIZED_DATA_PATH = CACHE_DIR / "anonymized.csv"
SYNTHETIC_DATA_PATH = CACHE_DIR / "synthetic.csv"

def ensure_cache_dir_exists():
    """Creates the cache directory if it doesn't already exist."""
    print(f"Ensuring cache directory exists at: {CACHE_DIR.resolve()}")
    CACHE_DIR.mkdir(exist_ok=True)
