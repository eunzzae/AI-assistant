from bs4 import BeautifulSoup
import requests
import json

class WeatherApi:
    def __init__(self, api_key):
        self.sevice_key = api_key
        
    # 1.기온 정보
    def weather_temp(self, location):
        html = requests.get(f'https://search.naver.com/search.naver?query={location}+날씨')
        # html
        soup = BeautifulSoup(html.text, 'html.parser')
        # 날씨 정보
        weather_data1 = soup.find('div',{'class':'weather_info'})
        address = soup.find('div',{'class':'title_area _area_panel'}).find('h2',{'class':'title'}).text
        # 현재 온도
        temperature = weather_data1.find('div',{'class':'temperature_text'}).text.strip()[5:]
        return "{address}의 온도는 {temperature} 입니다."

    # 2.날씨 상태   
    def weather_sta(self, location):
        html = requests.get(f'https://search.naver.com/search.naver?query={location}+날씨')
        # html
        soup = BeautifulSoup(html.text, 'html.parser')
        # 날씨 정보
        weather_data1 = soup.find('div',{'class':'weather_info'})
        address = soup.find('div',{'class':'title_area _area_panel'}).find('h2',{'class':'title'}).text
        
        # 날씨 상태
        weather_Status = weather_data1.find('span',{'class':'weather before_slash'}).text
        return f"{address}의 날씨 상태는 {weather_Status} 입니다."

        
    # 3.대기 상태   
    def weather_air(self, location):
        html = requests.get(f'https://search.naver.com/search.naver?query={location}+날씨')
        # html
        soup = BeautifulSoup(html.text, 'html.parser')
        # 날씨 정보
        weather_data1 = soup.find('div',{'class':'weather_info'})
        address = soup.find('div',{'class':'title_area _area_panel'}).find('h2',{'class':'title'}).text
        # 공기 
        air= soup.find('ul',{'class':'today_chart_list'})
        infos = air.find_all('li',{'class':'item_today'})
        for info in infos:
            return info.text.strip()

