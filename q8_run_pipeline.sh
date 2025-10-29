#!/bin/bash
# Assignment 5, Question 8: Pipeline Automation Script
# Run the clinical trial data analysis pipeline

# NOTE: This script assumes Q1 has already been run to create directories and generate the dataset
# NOTE: Q2 (q2_process_metadata.py) is a standalone Python fundamentals exercise, not part of the main pipeline
# NOTE: Q3 (q3_data_utils.py) is a library imported by the notebooks, not run directly
# NOTE: The main pipeline runs Q4-Q7 notebooks in order

echo "Starting clinical trial data pipeline..." > reports/pipeline_log.txt

# TODO: Run analysis notebooks in order (q4-q7) using nbconvert with error handling
# Use either `$?` or `||` operator to check exit codes and stop on failure
# Add a log entry for each notebook execution or failure
jupyter nbconvert --execute --to notebook q4_exploration.ipynb
jupError4=$?
if [ $jupError4 -ne 0 ]; then
    echo "Error" >> reports/pipeline_log.txt
else
    echo "Success" >> reports/pipeline_log.txt
fi

jupyter nbconvert --execute --to notebook q5_missing_data.ipynb
jupError5=$?
if [ $jupError5 -ne 0 ]; then
    echo "Error" >> reports/pipeline_log.txt
else
    echo "Success" >> reports/pipeline_log.txt
fi

jupyter nbconvert --execute --to notebook q6_transformation.ipynb
jupError6=$?
if [ $jupError6 -ne 0 ]; then
    echo "Error" >> reports/pipeline_log.txt
else
    echo "Success" >> reports/pipeline_log.txt
fi

jupyter nbconvert --execute --to notebook q7_aggregation.ipynb
jupError7=$?
if [ $jupError7 -ne 0 ]; then
    echo "Error" >> reports/pipeline_log.txt
else
    echo "Success" >> reports/pipeline_log.txt
fi


echo "Pipeline complete!" >> reports/pipeline_log.txt
