import requests

page_size = 3000
url = f"https://api.sojobs.co/channels/stack-overflow-jobs/feed?page_size={page_size}&pagination_type=page&source=stack-overflow-jobs&search=python&es=true&location=&page=1"
res = requests.get(url)
data = res.json()['results']
print('n results:', len(data))
#for result in data: 
#    print(result['redirect'])
#    break

