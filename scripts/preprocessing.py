import pandas as pd

def normalize_dates(df, date_col='date'):
    """
    Convert dates to YYYY-MM-DD format.
    """
    df[date_col] = pd.to_datetime(
        df[date_col],
        errors='coerce'
    ).dt.strftime('%Y-%m-%d')

    return df

def remove_duplicates(df, id_col='review_id'):
    """
    Remove duplicate reviews based on review ID.
    """
    before = len(df)

    df = df.drop_duplicates(
        subset=[id_col],
        keep='first'
    )

    removed = before - len(df)

    print(f"Removed {removed} duplicate reviews")

    return df

def validate_ratings(df):
    """
    Keep ratings between 1 and 5 only.
    """
    before = len(df)

    df = df[
        (df['rating'] >= 1) &
        (df['rating'] <= 5)
    ]

    df['rating'] = df['rating'].astype(int)

    removed = before - len(df)

    print(f"Removed {removed} invalid ratings")

    return df