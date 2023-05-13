# This program reads data from a CD catalog data set
# and builds arrays for the catalog items
# Each array contains the title, artist, country, prie, and year
# At the bottom, the total number of items and average price is 
# displayed
# References: datacamp.com, stackoverflow.com

def parse_xml_file(xml_file):
    with open(xml_file, 'r') as file:
        xml_data = file.read()
    start_tag = '<CD>'
    end_tag = '</CD>'
    cd_list = xml_data.split(start_tag)[1:]
    titles = []
    artists = []
    countries = []
    prices = []
    years = []
    for cd in cd_list:
        title_start = cd.find('<TITLE>') + 7
        title_end = cd.find('</TITLE>')
        titles.append(cd[title_start:title_end])
        artist_start = cd.find('<ARTIST>') + 8
        artist_end = cd.find('</ARTIST>')
        artists.append(cd[artist_start:artist_end])
        country_start = cd.find('<COUNTRY>') + 9
        country_end = cd.find('</COUNTRY>')
        countries.append(cd[country_start:country_end])
        price_start = cd.find('<PRICE>') + 7
        price_end = cd.find('</PRICE>')
        prices.append(cd[price_start:price_end])
        year_start = cd.find('<YEAR>') + 6
        year_end = cd.find('</YEAR>')
        years.append(cd[year_start:year_end])
    return titles, artists, countries, prices, years


def display_result(xml_file):
    titles, artists, countries, prices, years = parse_xml_file(xml_file)
    if len(titles) == 0:
        print("Error: Missing or bad data")
        return
    for i in range(len(titles)):
        print(f"{titles[i]} - {artists[i]} - {countries[i]} - {prices[i]} - {years[i]}")


def display_result2(xml_file):
    titles, artists, countries, prices, years = parse_xml_file(xml_file)
    if len(titles) == 0:
        print("Error: Missing or bad data")
        return
    num_items = len(titles)
    avg_price = sum([float(price) for price in prices]) / num_items
    print(f"Number of items: {num_items}")
    print(f"Average price: {avg_price:.2f}")


if __name__ == "__main__":
    xml_file = "cd_catalog.xml"
    display_result(xml_file)
    display_result2(xml_file)
