import json
import boto3

headers = {
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': '*',
    'Access-Control-Allow-Headers': '*',
    'Accept': '*/*'
}

def lambda_handler(event, context):
    body = json.loads(event['body'])
    name = body['name']
    phone_number = body['phone_number']
    
    dynamodb = boto3.client('dynamodb')
    
    table_name = 'ra-api-demo'
    
    item = {
        'Name': {'S': name},
        'PhoneNumber': {'S': phone_number}
    }
    
    try:
        response = dynamodb.put_item(
            TableName=table_name,
            Item=item
        )
        
        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps('Item added to DynamoDB')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': headers,
            'body': json.dumps(str(e))
        }





{
    "name": "Ravi",
    "phone_number": 9532563563
}