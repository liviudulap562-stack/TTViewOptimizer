import requests
import re

def scrape_fresh_proxies():
    proxy_sources = [
        'https://www.sslproxies.org/',
        'https://free-proxy-list.net/'
    ]
    
    fresh_proxies = []
    for source in proxy_sources:
        try:
            response = requests.get(source, timeout=10)
            proxies = re.findall(r'[0-9]+(?:\.[0-9]+){3}:[0-9]+', response.text)
            fresh_proxies.extend(proxies)
            print(f"🎯 Scraped {len(proxies)} proxies from {source}")
        except Exception as e:
            print(f"💀 Failed to scrape {source}: {e}")
    
    return fresh_proxies

if __name__ == "__main__":
    fresh = scrape_fresh_proxies()
    with open('proxies.txt', 'w') as f:
        f.write('\n'.join(fresh))
    print(f"🔥 Updated with {len(fresh)} fresh proxies!")
