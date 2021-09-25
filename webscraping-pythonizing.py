import requests
from bs4 import BeautifulSoup

r = requests.get('https://pythonizing.github.io/data/example.html')
content = r.content

soup = BeautifulSoup(content, 'html.parser')
all_divs = soup.find_all('div', {'class': 'cities'})
one_div = soup.find('div', {'class': 'cities'})

london_text = all_divs[0].find_all('h2')[0].text

cities = []
for item in all_divs:
    cities.append(item.find_all('h2')[0].text)

cities_content = []
for item in all_divs:
    cities_content.append(item.find_all('p')[0].text)

with open('cities', 'w') as file:
    for index, citie in enumerate(cities):
        file.writelines(f'{citie}, {cities_content[index]}\n')
