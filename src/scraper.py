import requests
from bs4 import BeautifulSoup
from settings import BASE_URL


def get_car_info(car):
    car_info = car.find('div', {'class': "newCarListUnit_metaTags"}).find_all('span')
    return {
        "Car Name": car.find('div', {'class': "newCarListUnit_header"}).find('a').text.strip(),
        "Car Image": car.find('div', {'class': "newCarListUnit_img_wrap"}).find('img')['data-original'],
        "Car Link": f"{BASE_URL}{car.find('div', {'class': 'newCarListUnit_header'}).find('a')['href'].strip('/')}",
        "Car Brand": car_info[0].find('a').text,
        "Car Model": car_info[1].find('a').text,
        "Car Color": car_info[2].text,
        "Car KM": car_info[3].text.replace(' Km', '').replace(',', ''),
        "Seller Place": car_info[4].text,
        "Date": car.find('div', {'class': "newCarListUnit_otherData"}).find('span').text,
        "Car Price": car.find('div', {'class': "newCarListUnit_footer"}).find('a').text.replace(' EGP', '').replace(',',
                                                                                                                    '')
    }


def scrape_cars(num_pages):
    cars_details = []
    print(f"Scraping {num_pages} pages...")
    for k in range(num_pages):
        url = f"{BASE_URL}page/{k + 1}"
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "lxml")
        all_cars = soup.find("div", {'class': 'CarListWrapper'}).find_all('div', {'class', 'newCarListUnit_contain'})

        for car in all_cars:
            car_details = get_car_info(car)
            cars_details.append(car_details)
    return cars_details
