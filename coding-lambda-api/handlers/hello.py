import json

def handler(event, context):
    print("request: {}".format(json.dumps(event)))
    params = event['pathParameters']
    name = event['pathParameters'].get('name', 'CDK') if params is not None else 'CDK'
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain'
        },
        'body': "Hello, {}! You've hit {}\n".format(name, event['path'])
    }
    