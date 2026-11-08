import urllib.request
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

req = urllib.request.Request(
    'https://tunasalamanca.com/',
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
)
try:
    with urllib.request.urlopen(req, context=ctx, timeout=10) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
        print('Status: 200, Length:', len(html))
        with open('tuna_salamanca_sample.html', 'w', encoding='utf-8') as f:
            f.write(html)
        print('Saved sample HTML')
        
        # Analizar elementos clave
        title = re.findall(r'<title>(.*?)</title>', html, re.I)
        print('Title:', title)
        
        # Enlaces del menu
        navs = re.findall(r'<nav.*?</nav>', html, re.I | re.S)
        if navs:
            print('Nav text sample:', re.sub(r'<[^>]+>', ' ', navs[0])[:500])
        else:
            links = re.findall(r'<a[^>]+>(.*?)</a>', html, re.I | re.S)
            clean_links = [re.sub(r'<[^>]+>', '', l).strip() for l in links if re.sub(r'<[^>]+>', '', l).strip()]
            print('Links sample:', clean_links[:20])

        # Secciones principales o H1, H2, H3
        headings = re.findall(r'<(h[1-3])[^>]*>(.*?)</\1>', html, re.I | re.S)
        print('Headings:')
        for h, text in headings[:15]:
            print(f'  {h}: {re.sub(r"<[^>]+>", "", text).strip()}')

except Exception as e:
    print('Error:', e)
