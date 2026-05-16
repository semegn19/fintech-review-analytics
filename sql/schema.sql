CREATE TABLE IF NOT EXISTS banks
(
    bank_id SERIAL PRIMARY KEY,
    bank_name VARCHAR(255) UNIQUE,
)

CREATE TABLE IF NOT EXISTS reviews
(
    review_id SERIAL PRIMARY KEY,

    bank_id INT REFERENCES banks(bank_id),

    review_text TEXT,

    rating INT CHECK (rating BETWEEN 1 AND 5),

    review_date DATE,

    sentiment_label VARCHAR(50),

    sentiment_score NUMERIC(8,6)
        CHECK (sentiment_score BETWEEN -1 AND 1),

    identified_theme VARCHAR(255),

    source VARCHAR(50)
)