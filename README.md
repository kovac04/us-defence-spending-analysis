# 353-Project

Overview

This repository contains scripts and data for analyzing the correlation between freedom variables and terrorist attacks, and US spendings on defense in various regions.
Required Libraries

    pandas
    numpy
    sklearn
    matplotlib
    seaborn
    statsmodels

Usage

    Data Preprocessing: Run the data.ipynb Jupyter notebook to preprocess the data. This notebook handles data cleaning, feature engineering, and prepares the dataset for analysis.

    Region Mapping: Execute the regionMapping.py script to map regions. This script categorizes countries into regions based on the data.

    Analysis: Run the analysis files (featureAnalysis.py, correlationHeatmap.py, etc.) to perform specific analyses. Each analysis file outputs separate pieces of analysis with corresponding names in the project report PDF.

Files Produced

    Data Preprocessing:
        US-defence.csv
        merged.csv
        oil_reserves_per_country.csv
        terror_and_oil.csv
        terrorist-attacks.csv
    Region Mapping:
        merged_with_region.csv: Dataset with regions mapped to each country.
    Analysis:
        Output analysis pieces with corresponding names in the project report PDF.

Order of Execution

    data.ipynb
    regionMapping.py
    Analysis files (analysis1.ipynb, analysis2.ipynb, etc.)

Contributors

    Abdurisaq Heban
    Navid Ahmed
    Uros Kovacevic

License

This project is licensed under the MIT License.
