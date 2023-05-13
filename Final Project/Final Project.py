import xml.etree.ElementTree as ET

def parse_xml_file(xml_file):
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
        prices.append(float(cd.find('PRICE').text))
        years.append(cd.find('YEAR').text)

    return titles, artists, countries, prices, years

def print_cd_catalog(xml_file):
    try:
        titles, artists, countries, prices, years = parse_xml_file(xml_file)
        count =  0
        while count < len(titles):
            print([titles[count], artists[count], countries[count], prices[count], years[count]])
            count += 1
    except ET.ParseError:
        print("Error: Invalid XML file.")

def print_catalog_stats(xml_file):
    try:
        titles, artists, countries, prices, years = parse_xml_file(xml_file)
        num_items = len(titles)
        avg_price = sum(prices) / num_items
        print(f"Number of items: {num_items}")
        print(f"Average price: {avg_price:.2f}")
    except ET.ParseError:
        print("Error: Invalid XML file.")

# Example usage
print_cd_catalog('cd_catalog.xml')
print_catalog_stats('cd_catalog.xml')
