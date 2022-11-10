input_filename = 'country_info.txt'

countries = {}
with open(input_filename) as country_file:
    country_file.readline()  # 读取第一行，后面该文件读取（遍历）的时候，就从下一行开始读起。
    for row in country_file:
        data = row.strip('\n').split('|')
        country, capital, code, code3, dialing, timezone, currency = data
        # print(country, capital, code, code3, dialing, timezone, currency, sep='\n\t')
        country_dict = {
            'name': country,
            'capital': capital,
            'country_code': code,
            'cc3': code3,
            'dialing_code': dialing,
            'timezone': timezone,
            'currency': currency
        }
        # print(country_dict)
        countries[country.casefold()] = country_dict
        # code_lookup[code.casefold()] = country
        countries[code.casefold()] = country_dict
        # countries is storing references to the individual dictionaries.

# print(countries)

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
    elif chosen_country == 'exit':
        break
    else:
        print(f"There is no country called{chosen_country}")
