import csv

input_filename = 'country_info.txt'

dialect = csv.excel
dialect.delimiter = '|'

countries = {}
with open(input_filename, encoding='utf-8', newline='') as country_file:
    # Get the column heading from the first line of the file
    headings = country_file.readline().strip("\n").split(dialect.delimiter)
    for index, heading in enumerate(headings):
        headings[index] = heading.casefold()
    # dict_reader = csv.DictReader(country_file, delimiter='|')
    dict_reader = csv.DictReader(country_file, dialect=dialect, fieldnames=headings)
    for row in dict_reader:
        countries[row['country'].casefold()] = row
        countries[row['cc'].casefold()] = row

print(countries)


while True:
    chosen_country = input("Please enter the name of a country: ")
    country_key = chosen_country.casefold()
    if country_key in countries:
        country_data = countries[country_key]
        capital_chosen = country_data['capital']
        if capital_chosen:
            print(f"The capital of {chosen_country} is {capital_chosen}")
        else:
            print(f"{chosen_country} does not have a capital~")
    elif country_key == 'exit':
        break
    else:
        print(f"There is no country called {chosen_country}")
