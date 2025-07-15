# Multi-Site Telugu News Scraper Configuration

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
    "Rashmika Mandanna",
    "Pooja Hegde"
]

# Multiple news sites configuration
NEWS_SITES = {
    "eenadu": {
        "name": "Eenadu",
        "base_url": "https://www.eenadu.net",
        "sections": [
            "https://www.eenadu.net/movies",
            "https://www.eenadu.net/telangana",
            "https://www.eenadu.net/andhra-pradesh",
            "https://www.eenadu.net/latest-news",
            "https://www.eenadu.net/trending-news"
        ],
        "url_pattern": "telugu-news",
        "active": True
    },
    "sakshi": {
        "name": "Sakshi",
        "base_url": "https://www.sakshi.com",
        "sections": [
            "https://www.sakshi.com/movies",
            "https://www.sakshi.com/telangana",
            "https://www.sakshi.com/andhra-pradesh",
            "https://www.sakshi.com/latest-news"
        ],
        "url_pattern": "telugu-news",
        "active": True
    },
    "tv9": {
        "name": "TV9 Telugu",
        "base_url": "https://www.tv9telugu.com",
        "sections": [
            "https://www.tv9telugu.com/entertainment",
            "https://www.tv9telugu.com/telangana",
            "https://www.tv9telugu.com/andhra-pradesh"
        ],
        "url_pattern": "news",
        "active": False  # Temporarily disabled due to 404 errors
    },
    "ntv": {
        "name": "NTV Telugu",
        "base_url": "https://www.ntvtelugu.com",
        "sections": [
            "https://www.ntvtelugu.com/entertainment",
            "https://www.ntvtelugu.com/telangana",
            "https://www.ntvtelugu.com/andhra-pradesh"
        ],
        "url_pattern": "news",
        "active": False  # Temporarily disabled due to 404 errors
    },
    "123telugu": {
        "name": "123Telugu",
        "base_url": "https://www.123telugu.com",
        "sections": [
            "https://www.123telugu.com/mnews",
            "https://www.123telugu.com/reviews",
            "https://www.123telugu.com/interviews"
        ],
        "url_pattern": "mnews",
        "active": True
    },
    "greatandhra": {
        "name": "Great Andhra",
        "base_url": "https://www.greatandhra.com",
        "sections": [
            "https://www.greatandhra.com/movies",
            "https://www.greatandhra.com/andhra",
            "https://www.greatandhra.com/telangana"
        ],
        "url_pattern": "news",
        "active": True
    }
}

# Request settings
REQUEST_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1"
}

# Scraping settings
DELAY_BETWEEN_SITES = 2  # seconds
DELAY_BETWEEN_CELEBRITIES = 3  # seconds
REQUEST_TIMEOUT = 10  # seconds
MAX_ARTICLES_PER_CELEBRITY = 10
MIN_ARTICLE_LENGTH = 20

# Output settings
CSV_FILENAME = "multi_site_scraping_results.csv"
ENABLE_DETAILED_LOGGING = True
