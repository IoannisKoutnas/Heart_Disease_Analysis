# Heart Disease Diagnostic & Clinical Analysis

## Overview
This repository contains a comprehensive data science notebook designed to analyze patterns, relationships, and risk factors associated with heart disease. Working with a dataset of 900,000 patient-level clinical observations (630,000 training records and 270,000 test records), this project performs thorough preliminary inspection, data integrity checks, and clinical outlier analysis.

## Project Structure
- `train.csv`: Training dataset containing patient clinical records and target classifications.
- `test.csv`: Test dataset containing patient clinical features.
- `Heart_Disease_Analysis.ipynb`: Main Jupyter Notebook covering data loading, cleaning, EDA, and statistical interpretation.
- `requirements.txt`: Python package dependencies.

## Key Features & Chapters
1. **Project Initialization & Setup**: Environment configuration and visual styling using Seaborn and Matplotlib.
2. **Data Inspection**: Dimensionality and structure check across demographic and clinical variables (e.g., Blood Pressure, Cholesterol, EKG results, ST Depression).
3. **Data Integrity**: Assessment of missingness and duplicate records to ensure baseline quality.
4. **Clinical Outlier Analysis**: Interquartile Range (IQR) statistical filtering applied to Blood Pressure and Cholesterol, with domain-specific evaluation for data retention.
5. **Target Distribution**: Class balance analysis to guide evaluation metric choices (Recall, Precision, F1-Score, ROC-AUC).
