# --------------------------------------------------------------
# Import Necessary Libraries
# --------------------------------------------------------------


# --------------------------------------------------------------
# Read the files
# --------------------------------------------------------------

control_df = pd.read_csv("../data/raw/control_group.csv",sep = ";")

test_df = pd.read_csv("../data/raw/test_group.csv",sep = ";")


# --------------------------------------------------------------
# Find Null and Duplicate Valuess and Remove Them
# --------------------------------------------------------------

# Null Values ---------

def remove_null_values(df):
    # Print the count of null values in each column
    print("Null values count in each column:")
    null_counts = df.isnull().sum()
    print(null_counts)

    if null_counts.sum() == 0:
        print("DataFrame has no null values")
    else:
        # Remove rows with null values and update the DataFrame
        df = df.dropna()
        print("Shape after removing null values:")
        print(df.shape)


# Duplicate Values ---------

def check_and_remove_duplicates(df):
    # Check for duplicate rows
    duplicate_count = df.duplicated().sum()
    
    if duplicate_count > 0:
        # Print the number of duplicate rows
        print(f"Number of duplicate rows: {duplicate_count}")

        # Remove duplicate rows and update the DataFrame
        df = df.drop_duplicates()
        
        print("Duplicate rows removed.")
    else:
        print("No duplicate rows found.")
        

# Reset Index ---------


def reset_dataframe_index(df):
    # Reset the index and drop the old index
    df = df.reset_index(drop=True)

# --------------------------------------------------------------
# Export dataset
# --------------------------------------------------------------

control_df.to_pickle("../data/processed/01_control_df_processed.pkl")
test_df.to_pickle("../data/processed/01_test_df_processed.pkl")