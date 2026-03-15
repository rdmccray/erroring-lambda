import boto3
import random

cloudwatch = boto3.client("cloudwatch")


def lambda_handler(event, context):

    x = random.random()
    y = 0
    status_code = 200

    if x < 0.5:
        y = 1
        status_code = 500

    cloudwatch.put_metric_data(
        Namespace="Custom/Lambda",
        MetricData=[{"MetricName": "HTTP500Count", "Value": y, "Unit": "Count"}],
    )

    return {
        "statusCode": status_code,
        "number": x,
        "value": y,
        "body": "Done",
    }
