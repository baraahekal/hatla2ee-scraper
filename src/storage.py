import csv
import pandas as pd


def preprocess_and_save(df, filename='cars_data_preprocessed.csv'):
    df['Car KM'] = pd.to_numeric(df['Car KM'], errors='coerce')
    df['Car Price'] = pd.to_numeric(df['Car Price'], errors='coerce')
    df['Car KM'].fillna(df['Car KM'].median(), inplace=True)
    df['Car Price'].fillna(df['Car Price'].median(), inplace=True)
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.dropna()
    df.to_csv(filename, index=False)


def save_to_csv(cars_details, filename='cars_data.csv'):
    keys = cars_details[0].keys()
    with open(filename, 'w', newline='', encoding='utf-8') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(cars_details)
