# This program reads data from a CD catalog data set
# and builds arrays for the catalog items
# Each array contains the title, artist, country, prie, and year
# At the bottom, the total number of items and average price is 
# displayed
# References: datacamp.com, stackoverflow.com

import xml.etree.ElementTree as ET

def get_cd_data(filename):
    try:
        tree = ET.parse(filename)
    except:
        print("Error: Missing or bad data")
        return None
    
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

    cd_data = []

    for i in range(len(titles)):
        cd_info = titles[i] + " - " + artists[i] + " - " + countries[i] + " - " + prices[i] + " - " + years[i]
        cd_data.append(cd_info)

    return cd_data

def get_cd_stats(cd_data):
    num_cds = len(cd_data)
    total_price = 0

    for cd in cd_data:
        price = float(cd.split(" - ")[3])
        total_price += price

    avg_price = total_price / num_cds

    return [num_cds, avg_price]

filename = 'cd_catalog.xml'
cd_data = get_cd_data(filename)

if cd_data:
    for cd_info in cd_data:
        print(cd_info)

    cd_stats = get_cd_stats(cd_data)
    print("\nTotal CDs: " + str(cd_stats[0]))
    print("Average price: " + "{:.2f}".format(cd_stats[1]))
