import requests


site = 'http://rmerces.com'

try:
    requests.get(site, timeout=5)
    print('Site OK!')
except Exception:
    print('Houston, we have a problem!')