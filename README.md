# Erroring Lambda

Just starting out learning Python and how to code in general. The cloud interests me so thought I would start with a little Lambda function that is supposed to error 50% of the time which triggers an alarm and sends me an email from SNS. This function is triggered on a schedule via EventBridge at a rate of once every minute.

```aws cli command to create custom metric

aws cloudwatch put-metric-alarm \
  --alarm-name "HighHTTP500Errors" \
  --metric-name HTTP500Count \
  --namespace MyAppMetrics \
  --statistic Sum \
  --period 300 \
  --threshold 5 \
  --comparison-operator GreaterThanThreshold \
  --evaluation-periods 1 \
  --alarm-actions arn:aws:sns:us-east-1:123456789012:MyAppAlerts \
  --treat-missing-data notBreaching
```
