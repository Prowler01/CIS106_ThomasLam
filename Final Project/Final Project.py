# This program reads data from a CD catalog data set
# and builds arrays for the catalog items
# Each array contains the title, artist, country, prie, and year
# At the bottom, the total number of items and average price is 
# displayed
# References: datacamp.com, stackoverflow.com

import xml.etree.ElementTree as ET

def parse_xml(file_name):
    try:
        tree = ET.parse(file_name)
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
        
        return [titles, artists, countries, prices, years]
    
    except ET.ParseError:
        print(f"Error: {file_name} is not a well-formed XML document.")
        return None
    except FileNotFoundError:
        print(f"Error: {file_name} file not found.")
        return None
    except:
        print(f"Error: Failed to parse {file_name}")
        return None


def print_catalog(file_name):
    catalog = parse_xml(file_name)
    
    if catalog is None:
        print("Error: Missing or bad data")
        return
    
    titles, artists, countries, prices, years = catalog
    
    count = 0
    while count < len(titles):
        print([titles[count], artists[count], countries[count], prices[count], years[count]])
        count += 1
    
    
def get_catalog_stats(file_name):
    catalog = parse_xml(file_name)
    
    if catalog is None:
        print("Error: Missing or bad data")
        return None
    
    titles, artists, countries, prices, years = catalog
    total_items = len(titles)
    average_price = sum(float(price) for price in prices) / total_items
    
    return [total_items, average_price]


# Test the program
print_catalog('cd_catalog.xml')
print(get_catalog_stats('cd_catalog.xml'))

