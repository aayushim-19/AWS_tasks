def clean_dataframe(df):
    # Example cleaning
    df = df.dropna()              # remove nulls
    df.columns = df.columns.str.lower()
    return df