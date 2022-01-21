import pandas as pd


def get_loan_data():
    '''
    This function reads csv stored in the computer or ask the user to fetch the data from kaggle.
    '''
    filename = "SBAnational.csv"

    if os.path.isfile(filename):
        return pd.read_csv(filename, index_col=0)
    else:
        print('file not fount locally , please get it from \
              https://www.kaggle.com/mirbektoktogaraev/should-this-loan-be-approved-or-denied')
     
        # Return the dataframe to the calling code
        
    
    