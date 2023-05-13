import xml.etree.ElementTree as ET

def parse_xml(xml_file):
    tree = ET.parse(xml_file)
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

    return titles, artists, countries, prices, years

def print_catalog(titles, artists, countries, prices, years):
    count =  0
    while count < len(titles):
        print([titles[count], artists[count], countries[count], prices[count], years[count]])
        count += 1

if __name__ == "__main__":
    xml_file = 'cd_catalog.xml'
    titles, artists, countries, prices, years = parse_xml(xml_file)
    print_catalog(titles, artists, countries, prices, years)
