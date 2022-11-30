import json
import boto3
import requests


IP_RANGE_URL = 'https://ip-ranges.amazonaws.com/ip-ranges.json'
REGION = 'ap-northeast-1'
SERVICE = 'S3'


def lambda_handler(event, context):
    res = requests.get(IP_RANGE_URL)
    ipranges = res.json()
    new_ip_ranges = []

    for prefix in ipranges['prefixes']:
        if prefix['region'] == REGION and prefix['service'] == SERVICE:
            new_ip_ranges.append(prefix['ip_prefix'])

    return {
        "statusCode": 200,
        "body": json.dumps({
            "ip_ranges": new_ip_ranges,
        }),
    }
