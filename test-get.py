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
    dynamodb = boto3.client('dynamodb')
    table_name = 'ra-api-demo'
    
    try:
        response = dynamodb.scan(TableName=table_name)
        
        items = response.get('Items', [])
        
        if items:
            formatted_items = []
            for item in items:
                formatted_item = {key: value.get('S') or value.get('N') for key, value in item.items()}
                formatted_items.append(formatted_item)
            
            return {
                'statusCode': 200,
                'headers': headers,
                'body': json.dumps(formatted_items)
            }
        else:
            return {
                'statusCode': 200,
                'headers': headers,
                'body': json.dumps([])
            }
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': headers,
            'body': json.dumps(str(e))
        }
