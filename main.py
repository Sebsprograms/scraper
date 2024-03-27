from lead import Lead
from googlesearch import search

def get_google_urls(query, num_results=100):
    urls = []
    for url in search(query, num_results=num_results, lang='en' ,advanced=False):
        urls.append(url)
    return urls

search_query = input("Enter your search query: ")
urls = get_google_urls(search_query, num_results=100)

print("First 100 URLs for the search query '{}':".format(search_query))
for i, url in enumerate(urls, start=1):
    print(f"{i}. {url}")






# testUrl = "https://reggin.ca/"
# lead = Lead(testUrl)
# lead.parse_url()

# print(lead.get_data())
# print(lead.internal_links)