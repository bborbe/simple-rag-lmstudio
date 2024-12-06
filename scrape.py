from scraper import scrape

# Starting URL
start_url = "https://www.tagesschau.de"
# Starting depth
start_depth = 3

scrape(start_url, start_depth)
print("scrape done")
