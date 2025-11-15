import requests, re, pprint
from bs4 import BeautifulSoup
from openpyxl import Workbook

url = 'https://www.jumia.com.ng/catalog/?q=airpods'
response = requests.get(url)
jumia = response.text


airpod_names = []
airpod_links = []
airpod_prices = []
airpod_ratings = []
airpod_votes = []

new_soup = BeautifulSoup(jumia, 'html.parser')

airpod_link = new_soup.find_all(name='a', class_= 'core' )

for link in airpod_link:
    airpod_links.append('www.jumia.com' + link.get('href').strip())

    airpod_name_tag = link.find(name='h3', class_='name').get_text().strip()
    airpod_names.append(airpod_name_tag)

    airpod_price_tag = link.find(name='div', class_='prc').getText().strip()
    airpod_prices.append(airpod_price_tag)

    airpod_rating = link.find(name= 'div', class_= 'stars _s')
    if airpod_rating:
        airpod_ratings.append(airpod_rating.getText().strip())
    else:
        airpod_ratings.append('')

    airpod_vote_tag = link.find(name='div', class_='rev')
    if airpod_vote_tag:
        airpod_votes.append(re.search(r'\((\d+)\)\Z', airpod_vote_tag.getText().strip()).group(1))
    else:
        airpod_votes.append('')



wb = Workbook()
ws = wb.active
sheet_titles= ['Name', 'Link','Price','Rating','Votes']
ws.append(sheet_titles)

for num in range(len(airpod_names)):
    ws.append([airpod_names[num], airpod_links[num], airpod_prices[num], airpod_ratings[num],airpod_votes[num]])

wb.save('033_webscraping_bs4_python\Scrapped_file.xlsx')




#nb : airpod_link = home url + airpod_tag.get(element)