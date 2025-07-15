import requests
from bs4 import BeautifulSoup
import time
import csv
from datetime import datetime
import logging
from multi_site_config import *

# Set up logging
logging.basicConfig(
    level=logging.INFO if ENABLE_DETAILED_LOGGING else logging.WARNING,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class MultiSiteNewsScraper:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update(REQUEST_HEADERS)
        self.results = []
        
    def scrape_all_sites(self, name):
        """Scrape all active news sites for a celebrity"""
        print(f"\n🔍 Searching for: {name}")
        
        all_articles = []
        active_sites = {k: v for k, v in NEWS_SITES.items() if v.get('active', True)}
        
        for site_id, site_config in active_sites.items():
            print(f"  🌐 Checking site: {site_config['name']}")
            
            try:
                site_articles = self.scrape_single_site(name, site_id, site_config)
                all_articles.extend(site_articles)
                
                if site_articles:
                    print(f"    ✅ Found {len(site_articles)} articles from {site_config['name']}")
                else:
                    print(f"    ❌ No articles found from {site_config['name']}")
                    
            except Exception as e:
                print(f"    ❌ Error scraping {site_config['name']}: {e}")
                logging.error(f"Error scraping {site_config['name']}: {e}")
                
            time.sleep(DELAY_BETWEEN_SITES)
        
        # Remove duplicates
        unique_articles = self.remove_duplicates(all_articles)
        
        # Display results
        if unique_articles:
            print(f"  ✅ Found {len(unique_articles)} unique articles across all sites:")
            for i, article in enumerate(unique_articles[:MAX_ARTICLES_PER_CELEBRITY], 1):
                print(f"  {i}. 📰 {article['title'][:70]}...")
                print(f"     🔗 {article['url']}")
                print(f"     📂 From: {article['site_name']} - {article['section']}")
                print()
        else:
            print("  ❌ No relevant articles found across all sites.")
        
        return unique_articles
    
    def scrape_single_site(self, name, site_id, site_config):
        """Scrape a single news site"""
        found_articles = []
        
        for section_url in site_config['sections']:
            try:
                section_name = section_url.split('/')[-1]
                print(f"    📂 Checking section: {section_name}")
                
                response = self.session.get(section_url, timeout=REQUEST_TIMEOUT)
                
                if response.status_code != 200:
                    print(f"      ⚠️  Status code: {response.status_code}")
                    continue
                
                soup = BeautifulSoup(response.text, "html.parser")
                articles = self.extract_articles(soup, name, site_id, site_config, section_name)
                found_articles.extend(articles)
                
            except requests.exceptions.RequestException as e:
                print(f"      ❌ Request error for {section_url}: {e}")
                continue
            except Exception as e:
                print(f"      ❌ Error processing {section_url}: {e}")
                continue
        
        return found_articles
    
    def extract_articles(self, soup, name, site_id, site_config, section_name):
        """Extract articles from a webpage"""
        articles = []
        
        # Find all links
        all_links = soup.find_all('a', href=True)
        
        for link in all_links:
            try:
                link_text = link.get_text(strip=True)
                href = link.get('href', '')
                
                # Check if article is relevant
                if self.is_relevant_article(link_text, href, name, site_config):
                    # Ensure full URL
                    if not href.startswith('http'):
                        href = site_config['base_url'] + href
                    
                    articles.append({
                        'title': link_text,
                        'url': href,
                        'site_id': site_id,
                        'site_name': site_config['name'],
                        'section': section_name,
                        'celebrity': name,
                        'scraped_at': datetime.now().isoformat()
                    })
                    
            except Exception as e:
                logging.debug(f"Error processing link: {e}")
                continue
        
        return articles
    
    def is_relevant_article(self, link_text, href, name, site_config):
        """Check if an article is relevant to the celebrity"""
        if not link_text or len(link_text) < MIN_ARTICLE_LENGTH:
            return False
        
        # Check if URL pattern matches
        if site_config['url_pattern'] not in href:
            return False
        
        # Check if celebrity name is mentioned
        name_parts = name.lower().split()
        link_text_lower = link_text.lower()
        
        # For exact matches or partial matches
        if len(name_parts) == 1:
            return name_parts[0] in link_text_lower
        else:
            # For multi-word names, check if any significant part is present
            return any(part in link_text_lower for part in name_parts if len(part) > 2)
    
    def remove_duplicates(self, articles):
        """Remove duplicate articles"""
        unique_articles = []
        seen_urls = set()
        seen_titles = set()
        
        for article in articles:
            url = article['url']
            title_short = article['title'][:50].lower()
            
            if url not in seen_urls and title_short not in seen_titles:
                unique_articles.append(article)
                seen_urls.add(url)
                seen_titles.add(title_short)
        
        return unique_articles
    
    def save_to_csv(self, filename=CSV_FILENAME):
        """Save results to CSV file"""
        if not self.results:
            print("No results to save.")
            return
        
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['celebrity', 'title', 'url', 'site_id', 'site_name', 'section', 'scraped_at']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for result in self.results:
                writer.writerow(result)
        
        print(f"\n💾 Results saved to {filename}")
    
    def print_summary(self):
        """Print scraping summary"""
        print("\n" + "=" * 70)
        print("📊 MULTI-SITE SCRAPING SUMMARY")
        print("=" * 70)
        
        total_articles = len(self.results)
        print(f"Total unique articles found: {total_articles}")
        
        if total_articles > 0:
            # Group by celebrity
            celebrity_counts = {}
            for result in self.results:
                celebrity = result['celebrity']
                celebrity_counts[celebrity] = celebrity_counts.get(celebrity, 0) + 1
            
            print("\\nArticles per celebrity:")
            for celebrity, count in sorted(celebrity_counts.items()):
                print(f"  • {celebrity}: {count} articles")
            
            # Group by site
            site_counts = {}
            for result in self.results:
                site = result['site_name']
                site_counts[site] = site_counts.get(site, 0) + 1
            
            print("\\nArticles per site:")
            for site, count in sorted(site_counts.items(), key=lambda x: x[1], reverse=True):
                print(f"  • {site}: {count} articles")
            
            # Group by section
            section_counts = {}
            for result in self.results:
                section = result['section']
                section_counts[section] = section_counts.get(section, 0) + 1
            
            print("\\nTop sections:")
            sorted_sections = sorted(section_counts.items(), key=lambda x: x[1], reverse=True)
            for section, count in sorted_sections[:7]:
                print(f"  • {section}: {count} articles")
        
        active_sites = len([s for s in NEWS_SITES.values() if s.get('active', True)])
        print(f"\\n📈 Active sites monitored: {active_sites}")
        print(f"🎯 Celebrities tracked: {len(INFLUENCERS)}")
    
    def run(self):
        """Main execution method"""
        print("🚀 Starting Multi-Site Telugu News Scraping...")
        print("=" * 70)
        
        active_sites = [s['name'] for s in NEWS_SITES.values() if s.get('active', True)]
        print(f"📊 Active Sites: {', '.join(active_sites)}")
        print("=" * 70)
        
        for influencer in INFLUENCERS:
            articles = self.scrape_all_sites(influencer)
            self.results.extend(articles)
            time.sleep(DELAY_BETWEEN_CELEBRITIES)
        
        self.print_summary()
        
        if self.results:
            self.save_to_csv()
        
        print("\\n✅ Multi-site scraping completed!")

def main():
    scraper = MultiSiteNewsScraper()
    scraper.run()

if __name__ == "__main__":
    main()
