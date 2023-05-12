import xml.etree.ElementTree as ET

tree = ET.parse('cd_catalog.xml')
root = tree.getroot()


titles = []
artists = []
countries = []
prices = []
years = []


for cd in root.findall('CD'):
    titles.append(cd.find('TITLE').text)
    artists.append(cd.find('ARTIST').text)
    countries.append(cd.find('COUNTRY').text)
    prices.append(cd.find('PRICE').text)
    years.append(cd.find('YEAR').text)


count =  0
while count <= 25:
    print([titles[count], artists[count], countries[count], prices[count], years[count]])
    count =  count +1

