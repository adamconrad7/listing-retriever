import xml.etree.ElementTree as ET
import requests
import pprint
from utils import get_url

with open('urns.txt', 'r') as file:
     urns= [line.strip() for line in file]

#
for id in urns:
    url, headers = get_url('linkedin_api/listing_description.xml', '<POSTING_URN>', id)
    res = requests.get(url, headers=headers).json()
    description = res['included'][0]['descriptionText']['text']
    pprint.pprint(description )
    break
