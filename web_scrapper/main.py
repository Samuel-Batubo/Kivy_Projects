from kivy.core.window import Window
from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from bs4 import BeautifulSoup
import requests
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.imagelist import MDSmartTile
import threading

Window.size=(1000, 600)

class Interface(MDBoxLayout):

    def scraping(self):
        objects = self.ids.scroll_view.children

        if objects:
            self.ids.scroll_view.remove_widget(objects[0])

        self.grid = MDGridLayout(cols= 3,adaptive_height= True,spacing= dp(10),padding= dp(10),row_default_height= dp(200),row_force_default= True)

        self.ids.scroll_view.add_widget(self.grid)

        keyword= self.ids.input_keyword.text
        page= requests.get(f'https://unsplash.com/s/photos/{keyword}')
        soup = BeautifulSoup(page.content, 'lxml')
        rows = soup.find_all('div', class_='ripi6')
        for row in rows:
            figure = row.find_all('figure')

            for i in range(2):
                img = figure[i].find('img', class_='YVj9w')
                source=img['src']
                titles =MDSmartTile(source=source, box_color=[1,1,1,0])
                self.grid.add_widget(titles)

class ScraperApp(MDApp):
    pass


ScraperApp().run()