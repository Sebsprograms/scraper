from lead import Lead
from search_interface import get_google_urls

number_of_results = int(input("Enter the number of results you want to fetch: "))
search_query = input("Enter your search query: ")
urls = get_google_urls(search_query, num_results=number_of_results)

print("First '{}' URLs for the search query '{}':".format(number_of_results ,search_query))
leads = []
for url in urls:
    leads.append(Lead(url.url, url.title, url.description))

count = 1
for lead in leads:
    print('-------------------Result #', count)
    lead.parse_url()
    print(lead.get_data())
    count += 1