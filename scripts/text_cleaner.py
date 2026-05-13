import pandas as pd
import re

def clean_text(text):
    """Standardize review text: collapse whitespace, strip edges."""
    if pd.isna(text):
        return ''
    text = str(text)
    text = re.sub(r'\s+', ' ', text)  # collapse multiple spaces/newlines
    text = text.strip()               # remove leading/trailing whitespace
    return text