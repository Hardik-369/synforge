import pandas as pd
from faker import Faker

# Initialize Faker
fake = Faker()

# --- PII Detection and Faker Mappings ---
# This dictionary maps common PII column name keywords to Faker methods.
# The key is a keyword to search for in a column name (case-insensitive).
# The value is the Faker method to generate replacement data.
PII_FAKER_MAPPING = {
    "name": fake.name,
    "firstname": fake.first_name,
    "lastname": fake.last_name,
    "email": fake.email,
    "phone": fake.phone_number,
    "address": fake.address,
    "street": fake.street_address,
    "city": fake.city,
    "state": fake.state,
    "zip": fake.zipcode,
    "country": fake.country,
    "ssn": fake.ssn,
    "social_security_number": fake.ssn,
    "credit_card": fake.credit_card_number,
    "birthdate": fake.date_of_birth,
    "dob": fake.date_of_birth,
}

def find_pii_columns(columns: list[str]) -> dict[str, callable]:
    """
    Identifies PII columns from a list of column names based on keywords.

    Args:
        columns: A list of column names from the DataFrame.

    Returns:
        A dictionary where keys are the identified PII column names and
        values are the corresponding Faker functions to generate data.
    """
    identified_pii = {}
    for col in columns:
        col_lower = col.lower()
        for keyword, faker_func in PII_FAKER_MAPPING.items():
            if keyword in col_lower:
                identified_pii[col] = faker_func
                # Move to the next column once a keyword is matched
                break
    return identified_pii

def anonymize_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Anonymizes a DataFrame by replacing data in identified PII columns.

    Args:
        df: The input pandas DataFrame.

    Returns:
        A new DataFrame with PII columns anonymized.
    """
    pii_columns = find_pii_columns(df.columns)

    if not pii_columns:
        print("No PII columns detected. Returning original data.")
        return df

    print(f"Anonymizing columns: {list(pii_columns.keys())}")

    # Create a copy to avoid modifying the original DataFrame
    df_anonymized = df.copy()

    num_rows = len(df_anonymized)

    for col_name, faker_func in pii_columns.items():
        # Generate a full column of fake data
        df_anonymized[col_name] = [faker_func() for _ in range(num_rows)]

    print("✅ DataFrame anonymized successfully.")
    return df_anonymized
