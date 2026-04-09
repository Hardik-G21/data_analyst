Day 5 Progress Report

Setup Status
* VS Code and Jupyter Notebook working properly
* Virtual environment (`.venv`) active
* Libraries installed: pandas, matplotlib, seaborn
* CSV files correctly structured and accessible

Environment is stable for data analysis.

Task Inventory
* Loaded and cleaned dataset using pandas
* Converted `Date` column to datetime format
* Performed weekly resampling of sales data
* Created line chart for revenue trend
* Used `groupby()` to analyze sales by product
* Identified Top 3 products using `nlargest()`
* Created bar chart for comparison
* Generated pivot table and correlation heatmap

Debugging Log
1. KeyError: 'Date'

Problem:Column not found
Solution:**

* Checked columns using `print(df.columns)`
* Removed incorrect separator and cleaned column names

2. ModuleNotFoundError (pandas)
Problem:pandas not installed in `.venv`
Solution:**

```bash
python -m pip install pandas matplotlib seaborn
```

3. File Path Error
Problem: Unicode path issue
Solution: Used `/` instead of `\` in file paths

Key Insights
* Clean data is essential before analysis
* Resampling helps understand trends over time
* Visualizations make insights clearer

Aha! Moment
"Proper data cleaning and formatting are the foundation of meaningful analysis."

Conclusion
Day 5 focused on EDA, including data cleaning, aggregation, and visualization. It strengthened my ability to analyze and interpret data effectively.
