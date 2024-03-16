import requests
import pprint
import xml.etree.ElementTree as ET

# Parse the XML file
tree = ET.parse('linkedin_api_calls/logged_in_job_search_unencoded.xml')  
root = tree.getroot()
req_list = root[0][8].text.split('\n')
req_list = list(filter(lambda x: x != '', req_list))

# Parse request from XML
headers_dict = {}
for i in req_list[1:]:
    header_name, header_value = i.split(": ", 1)
    headers_dict[header_name] = header_value
url = 'https://' + headers_dict['Host'] + req_list[0].split(' ')[1]

try:
    with open('urns.txt', 'r') as file:
         collected_urns = [line.strip() for line in file]
except FileNotFoundError:
    collected_urns = set()


with open('urns.txt', 'a') as file:
    for i in range(10):
        count = 0
        cur_url = url.replace('<PAGE_NUM>', str(i*100))
        #print(cur_url)
        print('checking page', i)
        res = requests.get(cur_url, headers=headers_dict)
        urns = res.json()['data']['metadata']['jobCardPrefetchQueries'][-1]['prefetchJobPostingCardUrns']
        urns = [n.split('(')[-1].split(',')[0] for n in urns if n not in collected_urns]
    
        for urn in urns:
            if urn not in collected_urns:
                count+=1
                file.write(urn+ '\n')   

        if count>0:
            print(f'added {count} urns')
