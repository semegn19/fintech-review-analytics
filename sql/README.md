# Task 3 — Database Engineering

## Objective

The objective of this stage was to design and populate a relational PostgreSQL database capable of storing processed mobile banking review data in a structured, production-oriented format.

The database was designed to support:

* efficient storage,   
* relational integrity,
* future analytics workflows,
* and scalable querying for customer sentiment and thematic analysis.

The implementation followed a simple normalized relational schema separating bank metadata from review-level information.

---

# Database Technology

The database implementation used:

* PostgreSQL
* pgAdmin
* psycopg2

Python was used to automate the ETL (Extract, Transform, Load) process from the processed CSV dataset into PostgreSQL.

---

# Schema Design

Two relational tables were created:

## 1. Banks Table

The `banks` table stores metadata about the banking applications analyzed in the project.

### Columns

| Column    | Description             |
| --------- | ----------------------- |
| bank_id   | Primary key             |
| bank_name | Name of the bank        |

### Design Rationale

This table was separated from the reviews table to:

* reduce redundancy,
* improve normalization,
* and support relational integrity using foreign keys.

Each bank is stored once and referenced by reviews through `bank_id`.

---

## 2. Reviews Table

The `reviews` table stores the processed review-level analytics data.

### Columns

| Column           | Description                            |
| ---------------- | -------------------------------------- |
| review_id        | Primary key                            |
| bank_id          | Foreign key referencing banks table    |
| review_text      | Cleaned review text                    |
| rating           | User star rating (1–5)                 |
| review_date      | Date of review                         |
| sentiment_label  | Predicted sentiment category           |
| sentiment_score  | Sentiment confidence/probability score |
| identified_theme | Assigned business theme                |
| source           | Data source platform                   |

### Design Rationale

The reviews table was designed to centralize:

* customer feedback,
* NLP outputs,
* and thematic classifications

within a single analytics-ready structure.

Foreign key constraints were used to enforce valid relationships between reviews and banks.

---

# Data Validation Constraints

Additional constraints were implemented to improve data quality and integrity.

Examples included:

* rating range validation (`1–5`),
* sentiment score range validation (`-1 to 1`),
* primary key enforcement,
* and foreign key relationships.

These constraints help prevent invalid analytical records from being inserted into the database.

---

# ETL Workflow

The ETL process consisted of the following stages:

## 1. Extract

Processed review data was loaded from cleaned CSV files generated during preprocessing and NLP analysis.

## 2. Transform

Before insertion:

* bank names were mapped to corresponding `bank_id` values,
* and column names were aligned with the database schema.

Intermediate NLP experimentation columns were removed to produce a clean production-style dataset.

## 3. Load

The cleaned and transformed records were inserted into PostgreSQL using Python and psycopg2.

The loading process followed two stages:

1. insert unique banks into the `banks` table,
2. insert review records into the `reviews` table using foreign key mapping.

---

# Data Quality Checks

After loading the data into PostgreSQL, validation queries were executed to verify:

* successful insertion,
* null values in key columns,
* relational consistency,
* average rating per bank,
* and review counts per bank.

These checks ensured the database remained consistent and analysis-ready.

---

# Environment Configuration

Database credentials and connection settings were managed using environment variables stored in a `.env` file.

Sensitive information such as:

* usernames,
* passwords,
* and host configuration

was excluded from version control using `.gitignore`.

This approach improves security and follows standard software engineering practices.

---

# Schema Export

The final relational schema was exported as a SQL schema file (`schema.sql`) and included in the project repository to support reproducibility and database reconstruction.
