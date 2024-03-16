import requests
import pprint
import xml.etree.ElementTree as ET
from utils import get_url

try:
    with open('urns.txt', 'r') as file:
         collected_urns = [line.strip() for line in file]
except FileNotFoundError:
    collected_urns = set()

with open('urns.txt', 'a') as file:
    for i in range(10):
        print('checking page', i)
        count = 0
        cur_url, headers = get_url('linkedin_api/logged_in_job_search_unencoded.xml', '<PAGE_NUM>', str(i*100))
        res = requests.get(cur_url, headers=headers)
        urns = res.json()['data']['metadata']['jobCardPrefetchQueries'][-1]['prefetchJobPostingCardUrns']
        urns = [n.split('(')[-1].split(',')[0] for n in urns if n not in collected_urns]
    
        for urn in urns:
            if urn not in collected_urns:
                count+=1
                file.write(urn+ '\n')   

        if count>0:
            print(f'added {count} urns')
