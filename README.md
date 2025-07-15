# � Telugu News Multi-Site Scraper

A comprehensive web scraping solution for monitoring Telugu cinema news across multiple news websites simultaneously.

## � Features

### 🎯 Multi-Site Support
- **4+ Active News Websites**: Eenadu, Sakshi, 123Telugu, Great Andhra
- **Intelligent Site Adaptation**: Custom patterns for each site
- **Expandable Architecture**: Easy to add new sites

### 📊 Smart Data Processing
- **Duplicate Removal**: Eliminates duplicate articles across all sites
- **Celebrity Tracking**: Monitors 10+ Telugu cinema influencers
- **Section Coverage**: Movies, regional news, trending topics

### 🔧 Technical Excellence
- **Robust Error Handling**: Continues working even if some sites fail
- **Rate Limiting**: Respectful scraping with configurable delays
- **CSV Export**: Structured data output for analysis
- **Rich Logging**: Detailed console output and progress tracking

## � Latest Results
- **Total Articles**: 48+ unique articles found
- **Top Celebrities**: Ram Charan (28 articles), Jr NTR (5), Allu Arjun (5)
- **Most Active Site**: Sakshi (31 articles)
- **Coverage**: Movies section dominates (68% of articles)

## 🚀 Quick Start

### Prerequisites
```bash
pip install -r requirements.txt
```

### Run Multi-Site Scraper
```bash
python multi_site_scraper.py
```

### Run Single-Site Scraper
```bash
python app.py
```

## 📁 Project Structure
```
├── multi_site_scraper.py     # Main multi-site scraper
├── multi_site_config.py      # Configuration for all sites
├── app.py                    # Enhanced single-site version
├── scraper.py               # Basic single-site version
├── config.py                # Single-site configuration
├── requirements.txt         # Python dependencies
├── .gitignore              # Git ignore patterns
└── docs/
    ├── README.md           # This file
    └── MULTI_SITE_OVERVIEW.md  # Detailed overview
```

## 🔧 Configuration

### Adding New Sites
Edit `multi_site_config.py`:
```python
NEWS_SITES = {
    "new_site": {
        "name": "New Site Name",
        "base_url": "https://example.com",
        "sections": ["movies", "news"],
        "url_pattern": "news",
        "active": True
    }
}
```

### Adding Celebrities
```python
INFLUENCERS = [
    "Ram Charan",
    "Mahesh Babu",
    "Your New Celebrity"
]
```

## � Sample Output
```
🚀 Starting Multi-Site Telugu News Scraping...
📊 Active Sites: Eenadu, Sakshi, 123Telugu, Great Andhra

🔍 Searching for: Ram Charan
  🌐 Checking site: Eenadu
    ✅ Found 1 articles from Eenadu
  🌐 Checking site: Sakshi
    ✅ Found 21 articles from Sakshi
```

## 🎯 Use Cases
- **Media Monitoring**: Track celebrity coverage across sites
- **Trend Analysis**: Identify popular topics and celebrities
- **Research**: Analyze Telugu cinema news patterns
- **Automation**: Schedule regular news collection

## � Roadmap
- [ ] Add more news sites
- [ ] Implement sentiment analysis
- [ ] Add image extraction
- [ ] Database integration
- [ ] Email notifications
- [ ] Web dashboard

## ⚠️ Important Notes
- Respects robots.txt and implements rate limiting
- Results vary based on current news coverage
- Some sites may occasionally return 404 errors
- CSV files are gitignored to prevent large file commits

## � License
This project is for educational and research purposes.

## 🤝 Contributing
1. Fork the repository
2. Create a feature branch
3. Add your improvements
4. Submit a pull request

---

**Last Updated**: July 15, 2025  
**Sites Monitored**: 4 active  
**Success Rate**: 100% for active sites
