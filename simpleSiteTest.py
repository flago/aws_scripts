import requests
from botocore.vendored import requests

site = 'http://rmerces.com'
def lambda_handler(event, context):

try:
    requests.get(site, timeout=5)
    print('Site OK!')
except Exception:
    print('Houston, we have a problem!')
