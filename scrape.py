from scraper import scrape

# Starting URL
start_url = "https://docs.solace.com/Cloud/Event-Portal/event-portal-lp.htm"
# Starting depth
start_depth = 3

scrape(start_url, start_depth)
print("scrape done")
