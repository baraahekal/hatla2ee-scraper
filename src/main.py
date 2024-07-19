from scraper import scrape_cars
from storage import save_to_csv, preprocess_and_save
import pandas as pd


def main():
    try:
        num_pages = int(input("Please enter the number of pages you want to scrap: "))
        cars_details = scrape_cars(num_pages)
        save_to_csv(cars_details, '../data/cars_data.csv')
        df = pd.read_csv('../data/cars_data.csv')
        preprocess_and_save(df, '../data/cars_data_preprocessed.csv')
        print("Files created: cars_data.csv and cars_data_preprocessed.csv")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    main()
