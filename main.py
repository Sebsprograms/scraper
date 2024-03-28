from lead import Lead
from search_interface import get_google_urls

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