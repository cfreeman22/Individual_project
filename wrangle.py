import pandas as pd
import numpy as np

import acquire as aqr
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


def loan_raw_summary():


    '''
    This function brings in the raw telco data and prints the summary statistics,   columns, info, shape and churn preview
    '''
    df = aqr.get_loan_data() 
    print("COLUMNS NAMES OF SBA Loan DATASET")
    print('')
    print(df.columns)
    print('')
    print('====================================================================================')
    print("THE SHAPE OF SBA Loan DATASET")
    print('')
    print(f'The SBA Loan dataset has {df.shape[0]} rows and {df.shape[1]} columns')
    print('')
    print('====================================================================================')
    print("SBA Loan INFO AND DATA TYPES, NEEDS TO EXAMINE TOTAL CHARGES MORE")
    print('')
    print(df.info())
    print('')
    print('====================================================================================')
    print("SBA Loan SUMMARY STATISTICS")
    print('')
    print(df.describe())
    print('')
    print('====================================================================================')
    print("CHECKING FOR NULLS ....")
    print('')
    print(df.isna().sum())
    print('')
    print('====================================================================================')
    
    return df


def prep_loan():
    '''
    This function will walk through all of the cleaning and data prep 
    process needed to explore and model the SA Loan data set
    '''
    df = aqr.get_loan_data()
    
    #renaming columns transforming to lower letters
    df.rename(columns=lambda c: c.lower(), inplace=True)
    
    df.zipcode = df.zipcode.astype('str')
    df.id = df.id.astype('str')
     
    
    return df
    

def split_loan():

    '''
    Takes in a dataframe and return train, validate, test subset dataframes
    '''
    #bringing in our raw dataframme passing to the prep function
    
    df = prep_loan()
    
    #passing to the prep function
    
    train, test = train_test_split(df, test_size = .2, random_state=123, stratify=df.paid_status)
    train, validate = train_test_split(train, test_size=.3, random_state=123, stratify=train.paid_status)
    print(f'train_encoded, shape: {train.shape}')
    print(f'validate_encoded, shape: {validate.shape}')
    print(f'test_encoded, shape: {test.shape}')
    return train, validate, test