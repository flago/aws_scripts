from requests import get

site = 'http://rmerces.com'

response = get(site, timeout=5)

try:
    response = response.raise_for_status()
    print('Site OK!')
except:
    print('Houston, we have a problem!')