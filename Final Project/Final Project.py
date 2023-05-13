import xml.etree.ElementTree as ET

def parse_xml(filename):
    tree = ET.parse(filename)
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
        prices.append(float(cd.find('PRICE').text))
        years.append(int(cd.find('YEAR').text))

    return titles, artists, countries, prices, years

def display_cd_catalog(filename):
    titles, artists, countries, prices, years = parse_xml(filename)

    for i in range(len(titles)):
        print([titles[i], artists[i], countries[i], prices[i], years[i]])

def cd_catalog_stats(filename):
    _, _, _, prices, _ = parse_xml(filename)
    num_items = len(prices)
    avg_price = sum(prices) / num_items

    return [num_items, avg_price]

stats = cd_catalog_stats('cd_catalog.xml')
print('Number of items:', stats[0])
print('Average price:', stats[1])
