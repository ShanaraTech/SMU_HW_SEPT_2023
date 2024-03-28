# Module 20  Report Template

## Overview of the Analysis

The purpose of this challenge was to train and evaluate a model based on loan risk, using a dataset of historical lending activity from a peer-to-peer lending services company to build a model that identifies borrowers' creditworthiness.

The variables X and y represented different but related characteristics in the dataset used to assess the borrower's ability to uphold their financial obligations. X represented the features(input variables) while y represented the target(output variable. 

Below are the procedures followed to analyze the data using the machine learning model:
- Import the modules and dependencies
# Split the Data into Training and Testing Sets (Part 1)
- Step 1: Split the Data into Training and Testing Sets
- Step 2: Create the labels set (y) from the “loan_status” column, and then create the features (X) 
  DataFrame from the remaining columns.
- Step 3: Split the data into training and testing datasets using train_test_split.
# Create a Logistic Regression Model with the Original Data (Part 2)
- Step 1: Fit a logistic regression model using the training data (X_train and y_train).
- Step 2: Save the predictions on the testing data labels using the testing feature data (X_test) and 
  the fitted model.
- Step 3: Evaluate the model’s performance by generating a confusion matrix & printing the 
  classification report for the model
- Step 4: Determine the borrower's creditworthiness by evaluating the model's performance based on  
  the score results from the classification report.
-Logistic Regression was used to predict the borrower's creditworthiness based on historical data and past behaviors to accurately predict two possible outcomes, whether they are creditworthy or not.

## Results
* Machine Learning Model 1:
    * Accuracy Scores = the model's rate of accuracy/total expressed in percentages
    * Precision Score = the model's predicated rate and the actual rate of accuracy reported, is 
      equivalent.
    * Recall Score = the model's rate of identifying all reported predictions accurately

## Summary

The logistics model has a high accuracy score of 99%, but it doesn't perform well when predicting high-risk loans compared to healthy loans because the recall score for high-risk loans is 94%, while the recall for healthy loans is 99%. This indicates a high degree of importance for the loan company to accurately predict the likelihood of high-risk applicants defaulting on their loans. Although 94% is a high percentage rate, the business could suffer financial losses if the applicant defaults on the loan, which could be detrimental if the total amount borrowed is considerably high or higher than average. Default loans can result in financial losses in multiple areas for the business including, losses on the loan amount, income expected from interest rates, and additional losses if the value of the asset depreciates over time--each of these financial loss scenarios can negatively impact the loan company's profits, revenues, and slow the rate of growth for business and company operations. y recommendation to the loan company would be to proceed with a high degree of caution and have a strategic plan to mitigate financial losses before approving loans for borrowers the algorithm predicted as high-risk.
