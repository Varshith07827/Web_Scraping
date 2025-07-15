import requests
from bs4 import BeautifulSoup
import time
import csv
from datetime import datetime

# ✅ 1. Your list of influencer names
influencers = [
    "Ram Charan",
    "Samantha Ruth Prabhu",  
    "Pawan Kalyan",
    "Mahesh Babu",
    "Allu Arjun",
    "Jr NTR"
]

# ✅ 2. Multiple news sites configuration
news_sites = {
    "eenadu": {
        "base_url": "https://www.eenadu.net",
        "sections": [
            "https://www.eenadu.net/movies",
            "https://www.eenadu.net/telangana",
            "https://www.eenadu.net/andhra-pradesh",
            "https://www.eenadu.net/latest-news",
            "https://www.eenadu.net/trending-news"
        ],
        "url_pattern": "telugu-news"
    },
    "sakshi": {
        "base_url": "https://www.sakshi.com",
        "sections": [
            "https://www.sakshi.com/movies",
            "https://www.sakshi.com/telangana",
            "https://www.sakshi.com/andhra-pradesh",
            "https://www.sakshi.com/latest-news"
        ],
        "url_pattern": "news"
    },
    "tv9": {
        "base_url": "https://www.tv9telugu.com",
        "sections": [
            "https://www.tv9telugu.com/entertainment",
            "https://www.tv9telugu.com/telangana",
            "https://www.tv9telugu.com/andhra-pradesh",
            "https://www.tv9telugu.com/latest"
        ],
        "url_pattern": "news"
    },
    "ntv": {
        "base_url": "https://www.ntvtelugu.com",
        "sections": [
            "https://www.ntvtelugu.com/entertainment",
            "https://www.ntvtelugu.com/telangana",
            "https://www.ntvtelugu.com/andhra-pradesh"
        ],
        "url_pattern": "news"
    }
}

# ✅ 3. Function to scrape multiple sites
def scrape_multiple_sites(name):
    print(f"\n🔍 Searching for: {name}")
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    all_found_articles = []
    
    for site_name, site_config in news_sites.items():
        print(f"  🌐 Checking site: {site_name.upper()}")
        
        site_articles = scrape_single_site(name, site_name, site_config, headers)
        all_found_articles.extend(site_articles)
        
        time.sleep(2)  # Delay between sites
    
    # Remove duplicates across all sites
    unique_articles = []
    seen_urls = set()
    seen_titles = set()
    
    for article in all_found_articles:
        # Check for duplicate URLs or very similar titles
        title_short = article['title'][:50].lower()
        if (article['url'] not in seen_urls and 
            title_short not in seen_titles):
            unique_articles.append(article)
            seen_urls.add(article['url'])
            seen_titles.add(title_short)
    
    # Display results
    if unique_articles:
        print(f"  ✅ Found {len(unique_articles)} unique articles across all sites:")
        for i, article in enumerate(unique_articles[:10], 1):  # Show first 10
            print(f"  {i}. 📰 {article['title'][:80]}...")
            print(f"     🔗 {article['url']}")
            print(f"     📂 From: {article['site']} - {article['section']}")
            print()
    else:
        print("  ❌ No relevant articles found across all sites.")
    
    return unique_articles

def scrape_single_site(name, site_name, site_config, headers):
    found_articles = []
    
    for section_url in site_config['sections']:
        try:
            print(f"    📂 Checking section: {section_url.split('/')[-1]}")
            response = requests.get(section_url, headers=headers, timeout=10)
            
            if response.status_code != 200:
                print(f"      ⚠️  Status code: {response.status_code}")
                continue
                
            soup = BeautifulSoup(response.text, "html.parser")
            
            # Find all links in the page
            all_links = soup.find_all('a', href=True)
            
            for link in all_links:
                link_text = link.get_text(strip=True)
                href = link.get('href', '')
                
                # Check if the link text contains the person's name
                name_parts = name.lower().split()
                if (link_text and len(link_text) > 15 and 
                    any(part in link_text.lower() for part in name_parts) and
                    site_config['url_pattern'] in href):
                    
                    # Make sure it's a full URL
                    if not href.startswith('http'):
                        href = site_config['base_url'] + href
                    
                    found_articles.append({
                        'title': link_text,
                        'url': href,
                        'site': site_name,
                        'section': section_url.split('/')[-1],
                        'celebrity': name
                    })
                    
        except Exception as e:
            print(f"      ❌ Error checking {section_url}: {e}")
            continue
    
    if found_articles:
        print(f"    ✅ Found {len(found_articles)} articles from {site_name}")
    else:
        print(f"    ❌ No articles found from {site_name}")
    
    return found_articles

# ✅ 4. Function to save results to CSV
def save_to_csv(all_results, filename="multi_site_scraping_results.csv"):
    if not all_results:
        print("No results to save.")
        return
    
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['celebrity', 'title', 'url', 'site', 'section', 'scraped_at']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for result in all_results:
            result['scraped_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            writer.writerow(result)
    
    print(f"\n💾 Results saved to {filename}")

# ✅ 5. Main execution
def main():
    print("🚀 Starting Multi-Site Telugu News Scraping...")
    print("=" * 70)
    print(f"📊 Configured Sites: {', '.join(news_sites.keys()).upper()}")
    print("=" * 70)
    
    all_results = []
    
    for influencer in influencers:
        results = scrape_multiple_sites(influencer)
        all_results.extend(results)
        time.sleep(3)  # be nice to the servers
    
    # Summary
    print("\n" + "=" * 70)
    print("📊 MULTI-SITE SCRAPING SUMMARY")
    print("=" * 70)
    
    total_articles = len(all_results)
    print(f"Total unique articles found: {total_articles}")
    
    if total_articles > 0:
        # Group by celebrity
        celebrity_counts = {}
        for result in all_results:
            celebrity = result['celebrity']
            celebrity_counts[celebrity] = celebrity_counts.get(celebrity, 0) + 1
        
        print("\nArticles per celebrity:")
        for celebrity, count in celebrity_counts.items():
            print(f"  • {celebrity}: {count} articles")
        
        # Group by site
        site_counts = {}
        for result in all_results:
            site = result['site']
            site_counts[site] = site_counts.get(site, 0) + 1
        
        print("\nArticles per site:")
        for site, count in site_counts.items():
            print(f"  • {site.upper()}: {count} articles")
        
        # Group by section
        section_counts = {}
        for result in all_results:
            section = result['section']
            section_counts[section] = section_counts.get(section, 0) + 1
        
        print("\nTop sections:")
        sorted_sections = sorted(section_counts.items(), key=lambda x: x[1], reverse=True)
        for section, count in sorted_sections[:5]:
            print(f"  • {section}: {count} articles")
        
        # Save to CSV
        save_to_csv(all_results)
    
    print(f"\n📈 Sites monitored: {len(news_sites)}")
    print(f"🎯 Celebrities tracked: {len(influencers)}")
    print("\n✅ Multi-site scraping completed!")

if __name__ == "__main__":
    main()
