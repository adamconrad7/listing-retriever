import asyncio
import aiohttp

page_size = 100
base_url = "https://api.sojobs.co/channels/stack-overflow-jobs/feed"

async def fetch_page(session, page):
    url = f"{base_url}?page_size={page_size}&pagination_type=page&source=stack-overflow-jobs&search=python&es=true&location=&page={page}"
    async with session.get(url) as response:
        if response.status == 200:
            data = await response.json()
            return data.get('results', [])
        else:
            print(f"Failed to fetch page {page}: {response.status}")
            return []

async def fetch_all_pages(total_pages):
    results = []
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_page(session, page) for page in range(1, total_pages + 1)]
        pages = await asyncio.gather(*tasks)
        for page in pages:
            results.extend(page)
    return results

# Example usage:
async def main():
    total_pages = 30  # Change this to the actual number of pages you want to fetch
    all_results = await fetch_all_pages(total_pages)
    print(f'Total results fetched: {len(all_results)}')

   # # Print redirect URLs
   # for result in all_results:
   #     print(result['redirect'])

# Run the main function
asyncio.run(main())
