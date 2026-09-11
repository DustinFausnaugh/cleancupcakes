# Cupcake Sales Data Cleaning & Analysis

A Python/pandas project that cleans a messy small business sales dataset and turns it into actionable business insights.

## Problem

Small businesses often have sales data that's messy and hard to act on with inconsistent naming, mixed formatting, and missing values that build up over time from manual entry. This project simulates that scenario with a realistic cupcake shop sales dataset, then cleans and analyzes it to answer real business questions like which flavors sell best and when the business is busiest.

## What's Messy in the Data
Flavor names entered inconsistently (e.g. "RedVelvet", "red velvet", "Red Velvet Cupcake" all referring to the same product)
Prices stored as text, with inconsistent formatting (some with a dollar signs, some without)
A handful of clear data-entry errors in price (e.g. a 300 dollar cupcake, a 0.03 dollar cupcake)
Order dates stored in two different formats
Missing values in both the flavor and quantity columns
## Approach
Inspected the raw data to identify each of the issues above (.head(), .info(), .unique())
Standardized flavor names by normalizing text (stripping whitespace, lowercasing) and mapping remaining variants to one clean value per flavor
Cleaned the price column: removed stray characters, converted to a numeric type, and filtered out clear outlier/typo values
Converted order dates (mixed formats) into a proper datetime type
Dropped rows with missing flavor or quantity values
Engineered new columns — revenue (quantity × price) and month (extracted from the date) — to support analysis
Summarized the cleaned data to answer specific business questions
## Tools Used
Python
pandas
openpyxl (for exporting results to Excel)
Currently extending this project with SQL/relational database concepts as part of a database processing course
## Results

From the cleaned dataset, the analysis shows:

Revenue by flavor: which flavors generate the most revenue
Revenue by month: how sales trend over time
Average order value: a baseline for what a typical sale looks like
Revenue by day / highest revenue day per month: the business's busiest periods

Results are exported to a multi tab Excel file so they're usable without needing to touch any code.

## How to Run It
Install dependencies: pip install pandas openpyxl
Run the cleaning script: python cleanCupcakes.py
Cleaned data and summary results are written to cupcake_analysis.xlsx in the project folder
## What I'd Do Differently at Scale

With a larger or growing dataset, this would move from a flat CSV into a proper relational database, with SQL used to filter and aggregate data before it's ever loaded into pandas. The cleaning logic could also be automated to run on a schedule, so results stay current without manual re-exports.
