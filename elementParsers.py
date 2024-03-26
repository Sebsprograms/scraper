# Takes a list of link elements and returns paths that are internal to the website
def extract_website_routes(links):
    cleaned_links = list(filter(lambda x: not x['href'].startswith('http'), links))
    cleaned_links = list(filter(lambda x: x['href'].startswith('/'), cleaned_links))
    final_links = []
    for link in cleaned_links:
        final_links.append(link['href'])
    final_links = list(set(final_links))
    return final_links
