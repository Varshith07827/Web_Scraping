## 🔍 Telugu Influencer News Scraper - Project Summary

### Project Overview
This web scraping project monitors news articles about Telugu cinema influencers from Eenadu.net, one of the leading Telugu news websites.

### 🎯 Key Features
1. **Multi-Celebrity Monitoring**: Tracks news for multiple Telugu influencers
2. **Section-wise Search**: Searches across different news sections (movies, politics, general news)
3. **Data Export**: Saves results to CSV format for further analysis
4. **Duplicate Removal**: Eliminates duplicate articles
5. **Error Handling**: Robust error handling for network issues
6. **Rate Limiting**: Respectful scraping with delays between requests

### 📊 Current Results
- **Total Articles Found**: 2
- **Celebrities with Coverage**: 
  - Ram Charan: 1 article
  - Mahesh Babu: 1 article
- **Sources**: Movies section, Andhra Pradesh news section

### 🚀 How It Works
1. **Target Sections**: Searches through key sections of Eenadu.net
2. **Name Matching**: Uses intelligent name matching to find relevant articles
3. **Content Filtering**: Filters out short snippets and focuses on full articles
4. **Data Structure**: Organizes results with celebrity, title, URL, and section info

### 🔧 Technical Stack
- **Python**: Main programming language
- **BeautifulSoup**: HTML parsing
- **Requests**: HTTP requests
- **CSV**: Data export
- **Time**: Rate limiting

### 📈 Potential Improvements
1. **Enhanced Search**: Implement more sophisticated name matching
2. **Content Analysis**: Add sentiment analysis of articles
3. **Scheduling**: Add automated daily/weekly scraping
4. **Database Integration**: Store results in a database instead of CSV
5. **Email Alerts**: Send notifications for new articles
6. **Image Extraction**: Extract article images
7. **Full Content**: Scrape full article content, not just headlines

### 📝 Usage Instructions
1. Install dependencies: `pip install requests beautifulsoup4`
2. Run the script: `python app.py`
3. Check results in `eenadu_scraping_results.csv`

### ⚠️ Important Notes
- The script respects the website's robots.txt and includes delays
- Results may vary based on current news coverage
- The script searches for articles containing the celebrity names
- Some names might not have recent coverage on the day of scraping

### 📁 Project Files
- `app.py`: Main scraping script
- `eenadu_scraping_results.csv`: Results data
- `README.md`: This documentation

Last updated: July 14, 2025
