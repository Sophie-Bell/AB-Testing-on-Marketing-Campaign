# --------------------------------------------------------------
# Import Necessary Libraries
# --------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pickle
from scipy.stats import mannwhitneyu

# --------------------------------------------------------------
# Read the files
# --------------------------------------------------------------

with open("../data/processed/control_df_processed.pkl", "rb") as file:
    control_df = pickle.load(file)
    
with open("../data/processed/test_df_processed.pkl", "rb") as file:
    test_df = pickle.load(file)
    
# --------------------------------------------------------------
# CPA
# --------------------------------------------------------------

# Perform Mann-Whitney U test for CPA
statistic_cpa, p_value_cpa = mannwhitneyu(control_df['CPA'], test_df['CPA'])

print(f'Mann-Whitney U Test for CPA:\n'
      f'Statistic = {statistic_cpa:.4f}\n'
      f'p-value = {p_value_cpa:.4f}\n')

# Interpret the results
alpha = 0.05  # Set your significance level
if p_value_cpa < alpha:
    print('Reject the null hypothesis for CPA. There is a significant difference.')
else:
    print('Fail to reject the null hypothesis for CPA. There is no significant difference.')


# --------------------------------------------------------------
# CPC
# --------------------------------------------------------------

# Perform Mann-Whitney U test for CPC
statistic_cpc, p_value_cpc = mannwhitneyu(control_df['CPC'], test_df['CPC'])

# Print the results
print(f'Mann-Whitney U Test for CPC:\n'
      f'Statistic = {statistic_cpc:.4f}\n'
      f'p-value = {p_value_cpc:.4f}\n')

# Interpret the results
alpha = 0.05  # Set your significance level
if p_value_cpc < alpha:
    print('Reject the null hypothesis for CPC. There is a significant difference.')
else:
    print('Fail to reject the null hypothesis for CPC. There is no significant difference.')

# --------------------------------------------------------------
# Converstion Rate
# --------------------------------------------------------------

# Perform Mann-Whitney U test for Conversion Rate
statistic_conversion, p_value_conversion = mannwhitneyu(control_df['Conversion Rate'], test_df['Conversion Rate'])

print(f'Mann-Whitney U Test for Conversion Rate:\n'
      f'Statistic = {statistic_conversion:.4f}\n'
      f'p-value = {p_value_conversion:.4f}\n')

# Interpret the results
alpha = 0.05  # Set your significance level
if p_value_conversion < alpha:
    print('Reject the null hypothesis for Conversion Rate. There is a significant difference.')
else:
    print('Fail to reject the null hypothesis for Conversion Rate. There is no significant difference.')

# --------------------------------------------------------------
# CTR
# --------------------------------------------------------------

# Perform Mann-Whitney U test for CTR
statistic_ctr, p_value_ctr = mannwhitneyu(control_df['CTR'], test_df['CTR'])

# Print the results
print(f'Mann-Whitney U Test for CTR:\n'
      f'Statistic = {statistic_ctr:.4f}\n'
      f'p-value = {p_value_ctr:.4f}\n')

alpha = 0.05  # Set your significance level
if p_value_ctr < alpha:
    print('Reject the null hypothesis for CTR. There is a significant difference.')
else:
    print('Fail to reject the null hypothesis for CTR. There is no significant difference.')


# --------------------------------------------------------------
# AOV
# --------------------------------------------------------------

# Perform Mann-Whitney U test for AOV
statistic_aov, p_value_aov = mannwhitneyu(control_df['AOV'], test_df['AOV'])

# Print the results
print(f'Mann-Whitney U Test for AOV:\n'
      f'Statistic = {statistic_aov:.4f}\n'
      f'p-value = {p_value_aov:.4f}\n')

# Interpret the results
alpha = 0.05  # Set your significance level
if p_value_aov < alpha:
    print('Reject the null hypothesis for AOV. There is a significant difference.')
else:
    print('Fail to reject the null hypothesis for AOV. There is no significant difference.')