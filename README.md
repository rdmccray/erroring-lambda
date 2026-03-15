# Erroring Lambda

Just starting out learning Python and how to code in general. The cloud interests me so thought I would start with a little Lambda function that is supposed to error 50% of the time which triggers an alarm and sends me an email from SNS. This function is triggered on a schedule via EventBridge at a rate of once every minute.

You will have to create the Lambda function via the AWS console

aws cli command to create the SNS topic:
```
aws sns create-topic --name MyAppAlerts
aws sns subscribe \
  --topic-arn arn:aws:sns:us-east-1:123456789012:MyAppAlerts \
  --protocol email \
  --notification-endpoint you@example.com
```
aws cli command to create the custom metric:
```
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
aws cli command to create the EventBridge rule:
```
aws events put-rule \
    --name "EveryMinuteLambdaTrigger" \
    --schedule-expression "rate(1 minute)" \
    --state ENABLED
```
aws cli command to set the Lambda function as the target of the rule:
```
aws events put-targets \
    --rule "EveryMinuteLambdaTrigger" \
    --targets "Id"="1","Arn"="$(aws lambda get-function --function-name YOUR_LAMBDA_FUNCTION_NAME --query 'Configuration.FunctionArn' --output text)"
```
aws cli command to grant EventBridge permission to invoke the Lambda function:
```
aws lambda add-permission \
    --function-name YOUR_LAMBDA_FUNCTION_NAME \
    --statement-id "EveryMinuteLambdaTriggerPermission" \
    --action "lambda:InvokeFunction" \
    --principal events.amazonaws.com \
    --source-arn "$(aws events describe-rule --name EveryMinuteLambdaTrigger --query 'Arn' --output text)"
```
verification:
```
aws events list-rules --name-prefix "EveryMinuteLambdaTrigger"
aws events list-targets-by-rule --rule "EveryMinuteLambdaTrigger"
```

