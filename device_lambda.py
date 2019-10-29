import json
import boto3

print('Loading function')
sns = boto3.client('sns')

def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err.message if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
        },
    }

def lambda_handler(event, context):
    # print(event)
    for record in event['Records']:
        # print('Stream record: ', json.dumps(record, indent=2))
        if record['eventName'] == 'INSERT':
            deviceId = record['dynamodb']['NewImage']['DeviceId']['S']
            when = record['dynamodb']['NewImage']['Timestamp']['S']
            status = record['dynamodb']['NewImage']['Status']['S']
            subject = "Device Status"
            msg = "device {} @ {} is {}".format(deviceId, when, status)
            sns.publish(Subject=subject, TopicArn='arn:aws:sns:us-west-2:408575476948:deviceStatusTopic',Message=msg)
    return respond(None, "Processed {} records".format(len(event['Records'])))
