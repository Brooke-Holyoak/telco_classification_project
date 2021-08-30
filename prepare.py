#This is a script for data prep for the Telco Churn dataset

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split

################To Visualize Intial Distributions##################
def num_distributions(df):
    '''
    This functions takes in a dataframe and displays
    the distribution of each numeric column.
    '''
    for col in df.columns:
        if df[col].dtype != 'object':
            plt.hist(df[col])
            plt.title(f'Distribution of {col}')
            plt.show()

################# Prepare Telco Data ########################

def telco_split(df):
    '''
    This function takes in the telco data acquired by get_telco_data,
    performs a split and stratifies species column.
    Returns train, validate, and test dfs.
    '''
    train_validate, test = train_test_split(df, test_size=.2, 
                                        random_state=123, 
                                        stratify=df.churn_Yes)
    train, validate = train_test_split(train_validate, test_size=.3, 
                                   random_state=123, 
                                   stratify=train_validate.churn_Yes)
    return train, validate, test

def prepare_telco_data(df):
    '''
    This function takes in the telco data acquired by get_telco_data,
    and cleans data so that returned df contains no null or blank values,
    each row represents one customer,
    each column contains one variable.
    All unnecessary columns are dropped.
    Columns are renamed for clarity and readability.
    '''
    #dropping rows where there is no value
    df = df[df.tenure != 0]

    #columns to drop are not necessary, nor do they contain needed data
    columns_to_drop = ['payment_type_id', 'internet_service_type_id', 'contract_type_id', 'customer_id', 'phone_service']
    df = df.drop(columns=columns_to_drop)
    
    #change datatype so columns contain numeric values only

    df.total_charges = df.total_charges.astype(float)

    #create dummy columns; keeping yn cols together and others together

    drop_yn_cols = ['gender', 'partner', 'dependents', 'paperless_billing', 'churn']
    dummy_df = pd.get_dummies(df[drop_yn_cols], dummy_na=False, drop_first=[True])

    drop_cols = ['multiple_lines', 'online_security', 'online_backup', 'device_protection', 'tech_support', 'streaming_tv', 'streaming_movies', 'contract_type', 'internet_service_type', 'payment_type']
    dummy_df1 = pd.get_dummies(df[drop_cols], dummy_na=False)

    #Clean this df: remove the no columns
    #the No Internet Service column is redundant, so I'm going to drop all but one, before I concat back onto the df
    redundant_cols = ['multiple_lines_No','online_security_No','online_security_No internet service','online_backup_No', 'online_backup_No internet service','device_protection_No',
    'device_protection_No internet service','tech_support_No', 'tech_support_No internet service','streaming_tv_No','streaming_tv_No internet service','streaming_movies_No']    

    dummy_df1 = dummy_df1.drop(columns=redundant_cols)

    #now I have the columns I want to add back to my original df
    df = pd.concat([df, dummy_df, dummy_df1], axis=1)

    #Now I will drop the columns I created dummy columns for drop_yn_cols and drop_cols

    df = df.drop(columns = drop_yn_cols)
    df = df.drop(columns = drop_cols)

    #now all my columns contain values I can work with, but I do want to rename some for clarity and to remove unnecessary spaces
    df = df.rename(columns = {'senior_citizen' : 'is_senior',
                            'gender_Male': 'is_male', 
                            'partner_Yes': 'has_partner',
                            'dependents_Yes': 'has_dependents',
                            'paperless_billing_Yes': 'paperless_bill',
                            'multiple_lines_No phone service': 'no_phone_service',
                            'multiple_lines_Yes': 'has_multiple_lines',
                            'online_security_Yes': 'has_online_security',
                            'online_backup_Yes': 'has_online_backup', 
                            'device_protection_Yes': 'has_device_protection',
                            'tech_support_Yes': 'has_tech_support',
                            'streaming_tv_Yes': 'streams_tv',
                            'streaming_movies_No internet service': 'no_internet_service',
                            'streaming_movies_Yes': 'streams_movies',
                            'contract_type_Month-to-month': 'mtm_contract',
                            'contract_type_One year': 'one_year_contract',
                            'contract_type_Two year': 'two_year_contract',
                            'internet_service_type_DSL': 'DSL',
                            'internet_service_type_Fiber optic' : 'fiber_optic', 
                            'internet_service_type_None': 'no_internet',
                            'payment_type_Bank transfer (automatic)': 'auto_bank_transfer',
                            'payment_type_Credit card (automatic)': 'auto_credit_card',
                            'payment_type_Electronic check':'auto_e_check',
                            'payment_type_Mailed check': 'mailed_check_payment'})

    #split dataframe into train, validate and test
    train, validate, test = telco_split(df)

    return train, validate, test                       






