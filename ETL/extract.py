from scrapy import Selector
#from bs4 import BeautifulSoup
#import scrapy
#from scrapy.crawler import CrawlerProcess
import requests
from datetime import datetime


"""
File to download FRED Economic Data. Tried using web scraping techniques.
"""

def execute_direct_link():
    todays_date = datetime.now().strftime("%m_%d_%Y")

    filename = f'housing_data_{todays_date}.csv'
    url = "https://fred.stlouisfed.org/graph/fredgraph.csv?bgcolor=%23e1e9f0&chart_type=line&drp=0&fo=open%20sans&graph_bgcolor=%23ffffff&height=450&mode=fred&recession_bars=on&txtcolor=%23444444&ts=12&tts=12&width=1138&nt=0&thu=0&trc=0&show_legend=yes&show_axis_titles=yes&show_tooltip=yes&id=ASPUS&scale=left&cosd=1963-01-01&coed=2023-07-01&line_color=%234572a7&link_values=false&line_style=solid&mark_type=none&mw=3&lw=2&ost=-99999&oet=99999&mma=0&fml=a&fq=Quarterly&fam=avg&fgst=lin&fgsnd=2020-02-01&line_index=1&transformation=lin&vintage_date=2023-12-10&revision_date=2023-12-10&nd=1963-01-01"
    data = requests.get(url)
    print(data)

    # Write out data to csv file
    with open(filename, 'bw') as f:
        f.write(data.content)
        f.close()
    

def execute_web_scraping():
    """Cant seem to get web scraping to work with a dropdown menu"""
    url = 'https://fred.stlouisfed.org/series/ASPUS'
    html = requests.get(url).content
    sel = Selector(text=html)
    download_button_container = sel.xpath('//div[@id="download-button-container"]')
    #download_button_container.xpath('//*')
    #download_button_container.xpath('//a[id="download-data-csv"]')
    #download_button_container.xpath('//*[@id="fg-download-menu"]').extract()
    #download_button_container.xpath('//*[@id="download-data"]').extract()
