'''
 device_lambda.py - not the code for 'publishDeviceStatus' AWS lambda

 This lambda used for 'Demo' notebook (bash) with payload.json input. IoT sends diffirent
 format message, so device_mqtt_lambda.py is created and used at 'publishDeviceStatus' AWS lambda.
'''

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

def findKey(recdict, possibleKeys):
    for tt in possibleKeys:
        if tt in recdict:
            print('*** found tag', tt)
            return recdict[tt]
    return None

def lambda_handler(event, context):
    print(event)
    for record in event['Records']:
        # print('Stream record: ', json.dumps(record, indent=2))
        if record['eventName'] == 'INSERT':
            deviceId = record['dynamodb']['NewImage']['DeviceId']['S']
            when = record['dynamodb']['NewImage']['Timestamp']['S']
            rr = findKey(record['dynamodb']['NewImage'], ["Payload", "OK", "Status"])
            if rr:
                status = rr['M']['status']['S']
                sequenceNo = rr["M"]['Sequence']['N'] if 'Sequence' in rr["M"] else rr["M"]['sequence']['N']
                subject = "Device Status"
                msg = "seqNo {}) device {} @ {} is {}, ".format(sequenceNo, deviceId, when, status)
                sns.publish(Subject=subject, TopicArn='arn:aws:sns:us-west-2:408575476948:deviceStatusTopic',Message=msg)
            else:
                print("Unknown tag")

    return respond(None, "Processed {} records".format(len(event['Records'])))
