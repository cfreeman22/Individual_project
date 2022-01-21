import pandas as pd
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
    


def prep_loan():
    '''
    This function will walk through all of the cleaning and data prep 
    process needed to explore and model the SA Loan data set
    '''
    df = aqr.get_loan_data()
    
    #renaming columns transforming to lower letters
    df.rename(columns=lambda c: c.lower(), inplace=True)
    
    #Rename with meaningfull variables
    df = df.rename(columns={'loannr_chkdgt': 'id', 'name': 'company', 'bank': 'company_bank',
                       'naics':'sector', 'balancegross':'balance','mis_status':'payment_status',
                       'noemp':'num_empl', 'newexist':'is_new_business','retainedjob':'retained_job',
                       'createjob':'created_job', 'lowdoc':'loan_program','urbanrural':'location',
                       'revlinecr':'line_of_credit','chgoffpringr':'debt','grappv':'amount_approved',
                       'sba_appv':'garanteed_by_sba', 'approvalfy':'approval_fin_year', 
                        'disbursementgross':'amount_disbursed','disbursementdate':'disburse_date',
                            'chgoffdate':'default_date','approvaldate':'approval_date' })
    
    # droping rows with nulls 
    df = df.dropna(subset=['company', 'city','state','bankstate','is_new_business','line_of_credit',
                           'loan_program', 'disburse_date','payment_status'])
    
    #Removing $ sings, comas and tranforming to float type for these columns
    cols_to_treat = ['amount_disbursed','balance','debt','amount_approved','garanteed_by_sba']
    
    df[cols_to_treat]= df[cols_to_treat].applymap(lambda x: x.strip('$').replace(',',''))
    
    df[cols_to_treat]= df[cols_to_treat].astype('float')
    
    # approval_fin_year is a mixed type treating and tranfroming to int
    df.approval_fin_year = df.approval_fin_year.replace('1976A',1976)
    
    df.approval_fin_year = df.approval_fin_year.astype('int')
    
    # treating payment status and transforming to float and 0 for paid off 1 for default
    df.payment_status = df.payment_status.replace({'P I F':0, 'CHGOFF':1})
    df.payment_status = df.payment_status.astype('int')
    
    
    # segmenting companies who retained jobs and those who did not
    df.retained_job = np.where((df.retained_job > 0),1,df.retained_job)
    
    # segmenting companies who created jobs and those who did not by 0 and 1s
    df.created_job = np.where((df.created_job > 0),1,df.created_job)
    
    #  segmenting companies who had a line of credit and those who did not and other values by nan
    
    df.line_of_credit = df.line_of_credit.repace({'N':0, 'Y':1})
    df.line_of_credit = df.line_of_credit.repace({'O':0, '1':1})
    
    df.line_of_credit = np.where((df.line_of_credit !=0) and (df.line_of_credit !=1), np.nan, df.line_of_credit)
    
    # convert all dates columns to timeanddate
    
    date_cols = ['approval_date','default_date','approval_date']
    
    df[date_cols] = pd.to_datetime(df[date_cols].stack(), format='%d-%b-%y').unstack()
    
    # proportion of garanteed loan by SBA / on approved amount
    
    df['percent_SBA'] = df.garanteed_by_sba / df.amount_approved
    
    # labeling every sector by selecting their first 2 digits codes
    
    df.sector = df.sector.astype('str').apply(lambda x: x[:2])
    
    #maping to each sector
    
    df.sector = df.sector.map({
    '11': 'Ag/For/Fish/Hunt',
    '21': 'Min/Quar/Oil_Gas_ext',
    '22': 'Utilities',
    '23': 'Construction',
    '31': 'Manufacturing',
    '32': 'Manufacturing',
    '33': 'Manufacturing',
    '42': 'Wholesale_trade',
    '44': 'Retail_trade',
    '45': 'Retail_trade',
    '48': 'Trans/Ware',
    '49': 'Trans/Ware',
    '51': 'Information',
    '52': 'Finance/Insurance',
    '53': 'RE/Rental/Lease',
    '54': 'Prof/Science/Tech',
    '55': 'Mgmt_comp',
    '56': 'Admin_sup/Waste_Mgmt_Rem',
    '61': 'Educational',
    '62': 'Healthcare/Social_assist',
    '71': 'Arts/Entertain/Rec',
    '72': 'Accom/Food_serv',
    '81': 'Other_no_pub',
    '92': 'Public_Admin'})
    
    return df
    
    