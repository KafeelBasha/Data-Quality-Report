# Data-Quality-Report
Overview of the data using summary statistics, similar to 'dataQualityR' package in R.

Returns a dictionary:
- Generates summary for variables with less than 15% of missing values.
- Returns summary of numeric variables as a data frame with key 'numeric'.
- Returns summary of categorical variables as a data frame with key 'categorical'.
