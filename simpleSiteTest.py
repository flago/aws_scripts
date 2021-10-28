from botocore.vendored import requests
import boto3
site = 'http://rmerces.com'
def lambda_handler(event, context):

try:
    requests.get(site, timeout=5)
    print('Site OK!')
except Exception:
    print('Houston, we have a problem!')
    envia_notificacao()
    
def envia_notificacao():
    client.publish(
        TopicArn='Colocar o arn do topico aqui!',
        Message='Houston, we have a problem',
        Subject='ALERTA')
