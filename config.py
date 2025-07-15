# Configuration for Telugu Influencer News Scraper

# List of influencers to monitor
INFLUENCERS = [
    "Ram Charan",
    "Samantha Ruth Prabhu",  
    "Pawan Kalyan",
    "Mahesh Babu",
    "Allu Arjun",
    "Jr NTR",
    "Chiranjeevi",
    "Nagarjuna",
    "Venkatesh",
    "Rashmika Mandanna",
    "Pooja Hegde",
    "Kajal Aggarwal"
]

# Website sections to search
SECTIONS = [
    "https://www.eenadu.net/movies",
    "https://www.eenadu.net/telangana",
    "https://www.eenadu.net/andhra-pradesh",
    "https://www.eenadu.net/latest-news",
    "https://www.eenadu.net/trending-news"
]

# Request headers
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Scraping settings
REQUEST_DELAY = 3  # seconds between requests
MAX_ARTICLES_PER_CELEBRITY = 7
MIN_ARTICLE_LENGTH = 15  # minimum characters for article title

# Output settings
CSV_FILENAME = "eenadu_scraping_results.csv"
