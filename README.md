# fintech-review-analytics

Mobile banking review analytics project for Ethiopian banks using Google Play Store data.
This project was developed as part of an analytics consultancy case study focused on understanding customer satisfaction, complaints, and feature requests for mobile banking applications in Ethiopia.

## Project Objective

The goal of this project is to:

* Scrape user reviews from the Google Play Store
* Clean and preprocess the review data
* Prepare an analysis-ready dataset for NLP and sentiment analysis
* Identify recurring customer pain points and feature requests
* Support data-driven recommendations for Ethiopian banks

The project currently includes review collection and preprocessing for:

* Commercial Bank of Ethiopia Mobile Banking App
* Bank of Abyssinia
* Dashen Bank

---

## 🚀 Quick Start

### Prerequisites

- Python 3.9 or higher
- Git
- Virtual environment

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/semegn19/fintech-review-analytics.git
cd fintech-review-analytics
```

2. **Create and activate virtual environment**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python -m venv venv
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

## 🔄 CI/CD Pipeline

GitHub Actions automatically runs on:
- Every push and pull requests to `main` 

**Checks include**:
- running requirements.txt

# Data Source

Reviews were collected from the Google Play Store using the Python library:

* [google-play-scraper](https://github.com/JoMingyu/google-play-scraper?utm_source=chatgpt.com)

Source platform:

* Google Play Store

---

# Scraping Methodology

The scraping process was implemented using Python and the `google-play-scraper` package.
| 
## Fields Collected

The following fields were extracted from each review:

* Review ID
* Review Text
* Rating (1–5)
* Review Date
* Bank Name
* Source Platform

## Collection Process

The scraper:

1. Connected to the Google Play Store API
2. Retrieved app metadata
3. Downloaded the newest reviews using:

   * language = English (`lang='en'`)
   * country = Ethiopia (`country='et'`)
   * sort order = newest reviews
4. Extracted relevant review fields into a structured Pandas DataFrame
5. Saved the cleaned dataset as CSV

## Review Volume

A target of 500 reviews was requested for the initial scrape.

# Date Range Used

Reviews were collected using the `Sort.NEWEST` option from the Google Play Store scraper.

The dataset includes the most recent reviews available at the time of scraping.

Dates were normalized into the format:

```text
YYYY-MM-DD
```
Date range for CBE: 2026-03-01 to 2026-05-12
Date range for BOA: 2025-02-14 to 2026-05-13
Date range for Dashen: 2022-07-16 to 2026-02-26


# Preprocessing Steps

The raw review data was cleaned and standardized before analysis.

## Cleaning Operations

### 1. Duplicate Removal

Duplicate reviews were removed using the unique `review_id`.

### 2. Missing Value Handling

Rows missing:

* review text
* rating

were removed from the dataset.

### 3. Text Cleaning

Review text was cleaned by:

* removing extra whitespace
* removing newline inconsistencies
* trimming leading/trailing spaces

Unicode characters, emojis, and Amharic text were preserved to maintain original sentiment and multilingual feedback.

### 4. Date Normalization

Dates were converted into:

```text
YYYY-MM-DD
```

format using Pandas datetime processing.

### 5. Rating Validation

Only ratings between:

```text
1–5
```

were retained.

---

# Output Dataset

The cleaned dataset contains the following columns:

| Column | Description       |
| ------ | ----------------- |
| review | User review text  |
| rating | Star rating (1–5) |
| date   | Review date       |
| bank   | Bank/app name     |
| source | Data source       |

Output file:

```text
data/processed/{bank_name}_reviews_clean.csv
```

---

# Project Structure

```text
fintech-review-analytics/
│
├── data/
│   └── processed/
│
├── notebooks/
│
├── scripts/
│   ├── preprocessing.py
│   └── text_cleaner.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

# Limitations Encountered

Several limitations were encountered during the scraping process:

## 1. Google Play Store Review Availability

The scraper only returns reviews made publicly available through the Play Store API.

Some older reviews may not be accessible.

## 2. Language Variability

Reviews include:

* English
* Amharic
* emojis
* mixed-language text

No translation or language filtering was applied during preprocessing.

## 3. Review Bias

Google Play reviews may overrepresent:

* highly dissatisfied users
* highly satisfied users

and may not reflect the full customer population.

## 4. Dynamic Ratings

App ratings and reviews continuously change over time.
Results represent a snapshot of the Play Store at the time of collection.
