import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

def top_phrases(df, bank, theme, ngram_range=(2,2), top_n=10):
    
    subset = df[
        (df['bank'] == bank) &
        (df['identified_theme'] == theme)
    ]

    vec = CountVectorizer(
        stop_words='english',
        ngram_range=ngram_range,
        max_features=top_n
    )

    X = vec.fit_transform(subset['review_text'])

    counts = X.toarray().sum(axis=0)

    result = pd.DataFrame({
        'phrase': vec.get_feature_names_out(),
        'count': counts
    }).sort_values('count', ascending=False)

    return result