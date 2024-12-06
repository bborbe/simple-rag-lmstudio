from scraper import scrape
from embedder import embed
from server import startChat

# Starting URL
start_url = "https://docs.solace.com/Cloud/Event-Portal/event-portal-lp.htm"
# Starting depth
start_depth = 3

scrape(start_url, start_depth)
print("scrape done")

embed()
print("embed done")

startChat()
print("startChat done")
