# this is just an example of how to use data from a url
# this should not be used as production quality code
import json
import urllib.request

json_data_source = 'https://www.ncdc.noaa.gov/cag/time-series/global/globe/land_ocean/ytd/12/1880-2021/data.json'

# with open(json_data_source, encoding='utf-8') as data:
with urllib.request.urlopen(json_data_source) as json_stream:
    data = json_stream.read().decode('utf-8')
    # anomalies = json.load(data)  # read JSON document from file and returns data in the form of a python dictionary
    anomalies = json.loads(data)   # convert JSON string to a dictionary

print(anomalies['description'])

for year, value in anomalies['data'].items():
    year, value = int(year), float(value)
    print(f"{year} ...{value:6.2f}")
print("*" * 80)

# print(anomalies['citation'])   # url下载的文件没有这一个键值对。
