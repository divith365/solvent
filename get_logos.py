import requests
import json
import urllib.parse

companies = ["NetApp", "Dell EMC", "Hitachi Vantara", "Juniper Networks", "Aruba Networks", "Arista Networks", "Sophos", "SonicWall"]
headers = {"User-Agent": "Bot (test@example.com)"}

for c in companies:
    # 1. Search Wikipedia for the article
    url = f"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={urllib.parse.quote(c)}&utf8=&format=json"
    try:
        res = requests.get(url, headers=headers).json()
        if not res['query']['search']:
            print(f"Not found: {c}")
            continue
        title = res['query']['search'][0]['title']
        
        # 2. Get the images for the page
        url = f"https://en.wikipedia.org/w/api.php?action=query&titles={urllib.parse.quote(title)}&prop=images&format=json"
        res = requests.get(url, headers=headers).json()
        pages = res['query']['pages']
        page = list(pages.values())[0]
        images = page.get('images', [])
        
        logo_file = None
        for img in images:
            if 'logo' in img['title'].lower() or 'wordmark' in img['title'].lower():
                logo_file = img['title']
                break
                
        if not logo_file:
            print(f"No logo found for {c}")
            continue
            
        # 3. Get imageinfo for URL
        url = f"https://en.wikipedia.org/w/api.php?action=query&titles={urllib.parse.quote(logo_file)}&prop=imageinfo&iiprop=url&format=json"
        res = requests.get(url, headers=headers).json()
        pages = res['query']['pages']
        page = list(pages.values())[0]
        img_url = page['imageinfo'][0]['url']
        print(f"{c}: {img_url}")
    except Exception as e:
        print(f"Error for {c}: {e}")

