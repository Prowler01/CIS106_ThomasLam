# This program reads data from a CD catalog data set
# and builds arrays for the catalog items
# Each array contains the title, artist, country, prie, and year
# At the bottom, the total number of items and average price is 
# displayed
# References: datacamp.com, stackoverflow.com
# References: educba.com, guru99.com, nanonets.com
# References: realpython.com, edureka.co, stackabuse.com
# References: superfastpython.com

import sys

# Need a function to read the XML file and return arrays
# of all the titles, artists, countries, prices, and years
def read_file(xml_file):
    with open(xml_file, 'r') as file:
        data = file.read()
    title1 = "<TITLE>"
    title2 = "</TITLE2"
    artist1 = "<ARTIST>"
    artist2 = "</ARTIST>"
    country1 = "<COUNTRY>"
    country2 = "</COUNTRY>"
    price1 = "<PRICE>"
    price2 = "</PRICE>"
    year1 = "<YEAR>"
    year2 = "</YEAR>"
    
    title_array = []
    artist_array = []
    country_array = []
    price_array = []
    year_array = []
    
    while True:
        start = data.find("<CD>")
        end = data.find("</CD>")
        if start == -1 or end == -1:
            break
        catalog = data[start:end]
        
        title_count = catalog.find(title1)
        title = catalog[title_count + len(title1): catalog.find(title2)]
        title_array = title_array.append(title)
        
        artist_count = catalog.find(artist1)
        artist = catalog[artist_count + len(artist1): catalog.find(artist2)]
        artist_array = artist_array.append(artist)
        
        country_count = catalog.find(country1)
        country = catalog[country_count + len(country1): catalog.find(country2)]
        country_array = country_array.append(country)
        
        price_count = catalog.find(price1)
        price = catalog[price_count + len(price1): catalog.find(price2)]
        price_array = price_array.append(price)
        
        year_count = catalog.find(year1)
        year = catalog[year_count + len(year1): catalog.find(year2)]
        year_array = year_array.append(year)
        
        data = data[end + len("</CD>"):]
        # check for empty file
        #if len(title_array) == 0:
            #print("Error: Missing or bad data.")
            #sys.exit()
        
        return title_array, artist_array, country_array, price_array, year_array
        


# Count up all items in the CD catalog
def count_titles(xml_file):
    with open(xml_file, 'r') as file:
        data = file.read()

    total_titles = 0
    while data:
        start_title = data.find('<title>')
        end_title = data.find('</title>')
        if start_title == -1 or end_title == -1:
            break
        else:
            total_titles += 1
            data = data[end_title+8:]

    return total_titles


# Find the average price
def calculate_average(xml_file):
    title_array = read_file(xml_file)
    price_array = read_file(xml_file)
    items = len(title_array)
    average = sum([float(price) for price in price_array]) / items
    return average

# Calculate total number of items
def calculate_total(xml_file):
    title_array = read_file(xml_file)
    total = len(title_array)
    return total

# Display arrays
def display_result(xml_file):
    title_array = read_file(xml_file)
    artist_array = read_file(xml_file)
    country_array = read_file(xml_file)
    price_array = read_file(xml_file)
    year_array = read_file(xml_file)
    
    for i in range(len(title_array)):
        print(f"{title_array[i]} - {artist_array[i]} - {country_array[i]} - {price_array[i]} - {year_array[i]}")
        
def display_stats(average, total):
    print("Total number of items: " + str(total))
    print("Average price: " + str(average))
    


# Main function and call
def main():
    xml_file = "cd_catalog.xml"
    read = read_file(xml_file)
    average = calculate_average(xml_file)
    total = calculate_total(xml_file)
    display_result(xml_file)
    
    
    
main()
        
    
    
    
