import requests
import pprint
import xml.etree.ElementTree as ET

# Parse the XML file
tree = ET.parse('linkedin_api_calls/logged_in_job_search_unencoded.xml')  # Replace 'file.xml' with your XML file path
# Get the root element
root = tree.getroot()
req_list = root[0][8].text.split('\n')
# Remove blank lines
req_list = list(filter(lambda x: x != '', req_list))
#print(req_list) 
headers_dict = {}
for i in req_list[1:]:
    #print(i)
#for header in headers_list:
    header_name, header_value = i.split(": ", 1)
    headers_dict[header_name] = header_value
#print(headers_dict)
url = 'https://' + headers_dict['Host'] + req_list[0].split(' ')[1]
print(url)

res = requests.get(url, headers=headers_dict)
#pprint.pprint(vars(res))
