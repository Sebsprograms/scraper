from lead import Lead

# Remove trailing slash from the URL for now
testUrl = "https://reggin.ca"
lead = Lead(testUrl)
lead.parse_url()

print(lead.get_data())