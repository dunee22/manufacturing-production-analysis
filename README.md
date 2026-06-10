# Manufacturing Production Analysis
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-darkgreen)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-crimson)
![Status](https://img.shields.io/badge/Status-Complete-success)


## Project Overview
This project analyzes daily manufacturing production data, including production output, defects, and downtime, using Python and data visualization techniques to identify patterns and relationships between variables.


## Dataset
The dataset contains daily manufacturing production data, including production output, defect counts, and downtime minutes. Each row represents one production day and is used to analyze operational performance and relationships between manufacturing variables.


### Dataset Columns
- **Day**: production day
- **Production**: total units produced
- **Defects**: number of defects recorded
- **Downtime_Minutes**: downtime duration in minutes


## Tools Used
- **Python**: core programming language
- **Pandas**: data analysis and manipulation
- **Matplotlib**: data visualization
- **NumPy**: numerical calculations and trend line analysis


## Visualizations
The project includes visual analysis using bar charts and scatter plots to compare manufacturing variables and identify relationships between production metrics.


### Visual Analysis
- **Bar charts**: used to compare daily production output and defect counts.
- **Scatter plot with trend line**: used to analyze the relationship between downtime and defects and identify positive correlation patterns.

### Production by Day
![Production by Day](images/production_by_day.png)

### Defects vs Downtime
![Defects vs Downtime](images/defects_vs_downtime.png)


## Key Statistical Findings

The dataset shows an average daily production of **1,185.71 units**, with a minimum of **900** and a maximum of **1,450 units**. The standard deviation of **182.67** indicates a noticeable variation in daily production levels across the week.

Defects averaged **35.43 per day**, ranging from **18** to **60 defects**. The standard deviation of **15.53** shows that defect counts varied significantly between production days.

Downtime averaged **29.71 minutes per day**, with a minimum of **8 minutes** and a maximum of **70 minutes**. The standard deviation of **21.49 minutes** indicates that downtime was not consistent across the dataset.

The correlation between **Defects** and **Downtime_Minutes** was **0.98**, indicating a very strong positive relationship. This suggests that days with higher downtime tend to be associated with higher defect counts.


## Key Findings
- **Highest production** was recorded on **Friday** with **1450 units**, while the **lowest production** occurred on **Saturday** with **900 units**.
- **Friday** recorded the **lowest number of defects** with **18**, while **Saturday** had the **highest defect count** with **60**.
- A **positive relationship** was observed between **Downtime_Minutes** and **Defects**, suggesting that higher downtime tends to be associated with higher defect counts.


## Future Improvements

* Expand the dataset to include additional production variables and longer time periods.
* Compare production performance by shifts, machines, operators, or product categories.
* Improve visualizations with additional comparisons and reporting features.
* Explore predictive analysis and machine learning applications in future versions.
