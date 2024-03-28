from googlesearch import search
from blocklist import blocklist

def get_google_urls(query, num_results=100):
    sleep_interval = 7 if num_results > 100  else  0
    urls = []
    for url in search(query, num_results=num_results, lang='en' ,advanced=False, sleep_interval=sleep_interval):
        if(not any((domain + '.') in url for domain in blocklist)):
            urls.append(url)
        else:
            print(f"Blocked URL: {url}")
    return urls