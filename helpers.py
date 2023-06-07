def print_unique_values(df, columns):
    total_rows = df.shape[0]
    for column in columns:
        unique_values = df[column].unique()
        print("Unique values of '{}':".format(column))
        for value in unique_values:
            if pd.isnull(value):
                count = df[column].isnull().sum()
            else:
                count = df[df[column] == value].shape[0]
            percentage = (count / total_rows) * 100
            print("   {} (Count: {}, Percentage: {:.2f}%)".format(value, count, percentage))



def convert_columns_to_float(df, columns):
    for column in columns:
        df[column] = pd.to_numeric(df[column], errors='coerce')


