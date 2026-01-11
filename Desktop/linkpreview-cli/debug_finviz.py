#!/usr/bin/env python3
"""Debug script for finviz URL"""

import requests
from bs4 import BeautifulSoup
import sys

def test_finviz_url():
    url = "https://finviz.com/news/268350/durin-debuts-magickey-the-first-multi-factor-authentication-for-home-entry"
    
    print(f"Testing URL: {url}")
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }
    
    try:
        print("Making request...")
        response = requests.get(url, headers=headers, timeout=10)
        print(f"Status code: {response.status_code}")
        print(f"Final URL: {response.url}")
        print(f"Content length: {len(response.text)}")
        print(f"Content type: {response.headers.get('Content-Type', 'Unknown')}")
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Look for title
            title_tag = soup.find('title')
            title = title_tag.text.strip() if title_tag else "No title"
            print(f"Page title: {title}")
            
            # Look for OG tags
            og_title = soup.find('meta', property='og:title')
            og_desc = soup.find('meta', property='og:description')
            og_image = soup.find('meta', property='og:image')
            
            print(f"OG title: {og_title.get('content') if og_title else 'Not found'}")
            print(f"OG description: {og_desc.get('content') if og_desc else 'Not found'}")
            print(f"OG image: {og_image.get('content') if og_image else 'Not found'}")
            
            # Check if page content suggests it needs JS
            if len(response.text) < 1000 or "javascript" in response.text.lower():
                print("WARNING: Page may require JavaScript")
                
        else:
            print(f"HTTP Error: {response.status_code}")
            print(f"Response text: {response.text[:500]}...")
            
    except requests.exceptions.Timeout:
        print("Request timed out!")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    test_finviz_url()