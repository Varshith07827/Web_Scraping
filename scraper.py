import requests
from bs4 import BeautifulSoup
import time
import csv
from datetime import datetime
from config import INFLUENCERS, SECTIONS, HEADERS, REQUEST_DELAY, MAX_ARTICLES_PER_CELEBRITY, MIN_ARTICLE_LENGTH, CSV_FILENAME

def scrape_eenadu(name):
    """
    Scrape Eenadu.net for articles about a specific celebrity
    """
    print(f"\n🔍 Searching for: {name}")
    
    found_articles = []
    
    for section_url in SECTIONS:
        try:
            print(f"  📂 Checking section: {section_url.split('/')[-1]}")
            response = requests.get(section_url, headers=HEADERS)
            
            if response.status_code != 200:
                print(f"    ⚠️  Status code: {response.status_code}")
                continue
                
            soup = BeautifulSoup(response.text, "html.parser")
            
            # Find all links in the page
            all_links = soup.find_all('a', href=True)
            
            for link in all_links:
                link_text = link.get_text(strip=True)
                href = link.get('href', '')
                
                # Check if the link text contains the person's name
                name_parts = name.lower().split()
                if (link_text and len(link_text) > MIN_ARTICLE_LENGTH and 
                    any(part in link_text.lower() for part in name_parts) and
                    'telugu-news' in href):
                    
                    # Make sure it's a full URL
                    if not href.startswith('http'):
                        href = 'https://www.eenadu.net' + href
                    
                    found_articles.append({
                        'title': link_text,
                        'url': href,
                        'section': section_url.split('/')[-1],
                        'celebrity': name
                    })
                    
        except Exception as e:
            print(f"    ❌ Error checking {section_url}: {e}")
            continue
    
    # Remove duplicates
    unique_articles = []
    seen_urls = set()
    for article in found_articles:
        if article['url'] not in seen_urls:
            unique_articles.append(article)
            seen_urls.add(article['url'])
    
    # Display results
    if unique_articles:
        print(f"  ✅ Found {len(unique_articles)} articles:")
        for i, article in enumerate(unique_articles[:MAX_ARTICLES_PER_CELEBRITY], 1):
            print(f"  {i}. 📰 {article['title'][:80]}...")
            print(f"     🔗 {article['url']}")
            print(f"     📂 From: {article['section']}")
            print()
    else:
        print("  ❌ No relevant articles found.")
    
    return unique_articles

def save_to_csv(all_results, filename=CSV_FILENAME):
    """
    Save scraping results to CSV file
    """
    if not all_results:
        print("No results to save.")
        return
    
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['celebrity', 'title', 'url', 'section', 'scraped_at']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for result in all_results:
            result['scraped_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            writer.writerow(result)
    
    print(f"\n💾 Results saved to {filename}")

def print_summary(all_results):
    """
    Print a summary of scraping results
    """
    print("\n" + "=" * 60)
    print("📊 SCRAPING SUMMARY")
    print("=" * 60)
    
    total_articles = len(all_results)
    print(f"Total articles found: {total_articles}")
    
    if total_articles > 0:
        # Group by celebrity
        celebrity_counts = {}
        for result in all_results:
            celebrity = result['celebrity']
            celebrity_counts[celebrity] = celebrity_counts.get(celebrity, 0) + 1
        
        print("\nArticles per celebrity:")
        for celebrity, count in sorted(celebrity_counts.items()):
            print(f"  • {celebrity}: {count} articles")
        
        # Group by section
        section_counts = {}
        for result in all_results:
            section = result['section']
            section_counts[section] = section_counts.get(section, 0) + 1
        
        print("\nArticles per section:")
        for section, count in sorted(section_counts.items()):
            print(f"  • {section}: {count} articles")
    
    print(f"\nConfiguration:")
    print(f"  • {len(INFLUENCERS)} influencers monitored")
    print(f"  • {len(SECTIONS)} sections searched")
    print(f"  • {REQUEST_DELAY}s delay between requests")

def main():
    """
    Main function to run the scraper
    """
    print("🚀 Starting Eenadu.net scraping for Telugu influencers...")
    print("=" * 60)
    
    all_results = []
    
    for influencer in INFLUENCERS:
        results = scrape_eenadu(influencer)
        all_results.extend(results)
        time.sleep(REQUEST_DELAY)  # be nice to the server
    
    print_summary(all_results)
    
    if all_results:
        save_to_csv(all_results)
    
    print("\n✅ Scraping completed!")

if __name__ == "__main__":
    main()
