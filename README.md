# Loan Modeling Project

Which customer is most likely to get a loan?
Presented By Christian Freeman Jan 15, 2011

# Project Planning

## PLAN ==> Acquire ==> Prepare ==> Explore ==> Model &Evaluate ==> Deliver

Understanding consumer behavior can quite chanlenging, especially when the product we offer our customers is a service rather than a tangible physical products. In the case of predicting which customer is most likely to get a loan,, I will perform the following:

- Prepare the data for visualization using a customized module wrangle.py
- Identify patterns and insights
- Document key observations and relationships between variables
- Goals and summary
My goal in this project is to:

- Identify the characteristics of customers who are more likely to get a loan, and the potential reasons for this behavior.
- Build a ML model to predict which customer may sign up for a loan So that recommendations are made based on the findings to help increase the chances of giving a loan the the right customer.I will be using Python, Pandas, Matplotlib, Seaborn, and Scikit-Learn libraries to analyse and create ML classification model.

### Initial Questions
What are unique characteristics of our customers?
What factors increase their chances of getting a loan ?
can we predict loan subscribers ?


## Executive Summary

### Findings Include:

- Many outliers in Income, Mortgage , and CCAvg colums
- Experience column has some 0 values as well as some negative values including -1,-2, -3 . All were converted to absolute value, since replacing with the mean experience of 20 years did not make sense. This is because most customers with these values have less than 30 years of age

## Data Dictionary:

 |Feature             |Description                                     |Dtype  |
 |--------------------|------------------------------------------------|-------|  
 |ID                  |Unique identifier for each customer             |int64  |
 |--------------------|------------------------------------------------|-------|
 |Age                 | Age of the customer                            | int64 |
 |--------------------|------------------------------------------------|-------|
 |Experience          |Numbers of years of experience the customer has | int64 |
 |--------------------|------------------------------------------------|-------|  
 |Income              |The  customer's income.                         |  int64|  
 |--------------------|------------------------------------------------|-------|  
 |ZIPCode             | The customer's zip code                        | int64 | 
 |--------------------|------------------------------------------------|-------|   
 |Family              | The number of Family members the customer has  |int64  |
 |--------------------|------------------------------------------------|-------|   
 |CCAvg               |The average Credit card spending of the customer|float64|
 |--------------------|------------------------------------------------|-------|   
 |Education           | the Educational level undergrad/grad/ pro      |int64  |
 |--------------------|------------------------------------------------|-------|  
 |Mortgage            | Whether or not the customer has mortgage       |int64  |
 |--------------------|------------------------------------------------|-------|  
 |Personal_Loan       | Whether or not customer has a personal loan.   |int64  |
 |--------------------|------------------------------------------------|-------|  
 |Securities_Account  |Whether or not the customer has securities ACC  |int64  |
 |--------------------|------------------------------------------------|-------|  
 |CD_Account          |If the customer has Certificate of Deposit      |int64  |
 |--------------------|------------------------------------------------|-------| 
 |Online              | If the customer uses online banking or not.    |int64  |
 |--------------------|------------------------------------------------|-------|
 |CreditCard          | If the customer has a credit card or not.      |int64  |
 
 
# Steps to Reproduce

You will need to obtain the Loan_Modelling.csv file from  https://www.kaggle.com/itsmesunil/bank-loan-modelling to use for the project.

 
#### Preparation

- Create a workbook.ipynb file to put all work in
- Clean aquired temperature data:
- remove missing values,
- inspect data integrity issues
- ensure columns are proper data type
- reduce outliers
- Create a scale function for future modeling
- nCreate split function for future modeling
- Add all new functions to wrangle.py
- Exploration and Pre-processing

- Explore the target variable using visualization and statistical testing
- create explore.py file to explore the data
- Split data appropriately
- Establish and evaluate baseline model
- create a modeling.py for your models
- Scale features attempt at least 3 combinations of features
- Summarize takeaways and conclusions
 
- Create at least 4 different models and compare their performance

 
 
 
 
 
 
 