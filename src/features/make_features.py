# --------------------------------------------------------------
# Import Necessary Libraries
# --------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pickle

# --------------------------------------------------------------
# Read the files
# --------------------------------------------------------------

with open("../data/interim/01_control_df_processed.pkl", "rb") as file:
    control_df = pickle.load(file)
    
with open("../data/interim/01_test_df_processed.pkl", "rb") as file:
    test_df = pickle.load(file)

# --------------------------------------------------------------
# Calculate and Add KPI's
# --------------------------------------------------------------

def calculate_and_add_kpis(df):
    # Calculate Cost Per Click (CPC)
    df['CPC'] = df['Spend [USD]'] / df['# of Website Clicks']

    # Calculate Cost Per Acquisition (CPA)
    df['CPA'] = df['Spend [USD]'] / df['# of Purchase']

    # Calculate Average Order Value (AOV)
    df['AOV'] = df['Spend [USD]'] / df['# of Purchase']
    
    # Calculate CTR
    df['CTR'] = (df['# of Website Clicks'] / df['# of Impressions']) * 100
    
    # Calculate Conversion Rate
    df['Conversion Rate'] = (df['# of Purchase'] / df['# of Website Clicks']) * 100

    return df


# --------------------------------------------------------------
# Export dataset
# --------------------------------------------------------------

control_df.to_pickle("../data/processed/control_df_processed.pkl")
test_df.to_pickle("../data/processed/test_df_processed.pkl")