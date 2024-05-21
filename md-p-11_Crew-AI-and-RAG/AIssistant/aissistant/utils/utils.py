import pandas as pd

def convert_date():
    # Read the CSV file
    df = pd.read_csv('./data/Airplane_Crashes_and_Fatalities_Since_1908.csv')

    # Convert the 'Date' column to datetime
    df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')

    # Save the dataframe back to CSV
    df.to_csv('Airplane_Crashes_and_Fatalities_Since_1908.csv', index=False)


def add_year_col():

    # Read the CSV file
    df = pd.read_csv('./data/Airplane_Crashes_and_Fatalities_Since_1908.csv')

    # Extract the year from the 'Date' column
    df['Year'] = pd.to_datetime(df['Date']).dt.year

    # Rearrange the columns to put 'Year' before 'Date'
    cols = df.columns.tolist()
    cols = cols[-1:] + cols[:-1]
    df = df[cols]

    # Save the dataframe back to CSV
    df.to_csv('Airplane_Crashes_and_Fatalities_Since_1908.csv', index=False)


if __name__ == '__main__':
    # convert_date()
    add_year_col()