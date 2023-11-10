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
# Visualize Numeric Columns Distribution
# --------------------------------------------------------------

def plot_histograms(test_df, control_df):
    num_columns = min(len(test_df.columns) - 3, len(control_df.columns) - 3)
    num_rows = (num_columns + 3) // 4
    fig, axs = plt.subplots(nrows=num_rows, ncols=4, figsize=(12, 10))

    for i, (test_column, control_column) in enumerate(zip(test_df.columns[3:], control_df.columns[3:])):
        row = i // 4
        col = i % 4
        axs[row, col].hist(test_df[test_column], bins=20, alpha=0.5, label='Test Data', color='blue')
        axs[row, col].hist(control_df[control_column], bins=20, alpha=0.5, label='Control Data', color='orange')
        axs[row, col].set_title(f'{test_column}')
        axs[row, col].legend()

    # Remove empty subplots
    for i in range(num_columns, num_rows * 4):
        fig.delaxes(axs.flatten()[i])

    plt.tight_layout()
    plt.show()

plot_histograms(test_df, control_df)

# --------------------------------------------------------------
# Visualize Metrics over time of Campaign
# --------------------------------------------------------------

def plot_metrics_over_time(control_df, test_df):
    
    fig, axs = plt.subplots(nrows=3, ncols=2, figsize=(12, 8))

    # Metrics to plot
    metrics = ['# of Purchase', 'Spend [USD]', 'Reach', '# of Website Clicks', '# of View Content', '# of Add to Cart']

    
    for i, metric in enumerate(metrics):
        row = i // 2
        col = i % 2
        axs[row, col].plot(control_df['Date'], control_df[metric], label='Control', marker='o', linestyle='-', color='blue')
        axs[row, col].plot(test_df['Date'], test_df[metric], label='Test', marker='o', linestyle='-', color='orange')
        axs[row, col].set_title(f'{metric} Over Time')
        axs[row, col].set_xlabel('Date')
        axs[row, col].set_ylabel(metric)
        axs[row, col].legend(loc='upper left')
        axs[row, col].grid(True)

    
    plt.tight_layout()
    plt.subplots_adjust(hspace=1, wspace=0.3)
    for ax in axs.flat:
        ax.tick_params(axis='x', labelrotation=45)

    plt.show()

# --------------------------------------------------------------
# Calculate Average KPI's per campaign
# --------------------------------------------------------------

def print_average_metrics(df):
    required_columns = ['CPA', 'CPC', 'AOV', 'CAC', 'Conversion Rate']

    if set(required_columns).issubset(df.columns):
        average_values = df[required_columns].mean()
        print(f"Average Metrics for {df.name}:")
        for metric, value in average_values.items():
            if metric == 'Conversion Rate':
                print(f"{metric}: {value:.2f}%")
            else:
                print(f"{metric}: ${value:.2f}")
        print("\n")
    else:
        print(f"{df.name} is missing one or more of the required columns: {', '.join(required_columns)}")
        
    
# --------------------------------------------------------------
# Visualize KPI's over time of Campaign
# --------------------------------------------------------------

def plot_kpis_over_time(control_df, test_df):
    fig, axs = plt.subplots(nrows=2, ncols=3, figsize=(16, 8))

    # Metrics to plot
    metrics = ['CPC', 'CPA', 'AOV', 'CTR', 'Conversion Rate']

    for i, metric in enumerate(metrics):
        row = i // 3
        col = i % 3
        axs[row, col].plot(control_df['Date'], control_df[metric], label='Control', marker='o', linestyle='-', color='blue')
        axs[row, col].plot(test_df['Date'], test_df[metric], label='Test', marker='o', linestyle='-', color='orange')
        axs[row, col].set_title(f'{metric} Over Time')
        axs[row, col].set_xlabel('Date')
        axs[row, col].set_ylabel(metric)
        axs[row, col].legend(loc='upper left')
        axs[row, col].grid(True)

    # Create an empty subplot
    row = 1
    col = 2
    axs[row, col].axis('off')

    plt.tight_layout()
    plt.subplots_adjust(hspace=0.5, wspace=0.3)

    for ax in axs.flat:
        ax.tick_params(axis='x', labelrotation=45)

    plt.show()

plot_kpis_over_time(control_df, test_df)

