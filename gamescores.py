import boto3

def create_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.client('dynamodb')

    table = client.create_table(
        AttributeDefinitions=[{
            'AttributeName': 'event', 
            'AttributeType': 'S'
        }, 
        {
            'AttributeName': 'timestamp', 
            'AttributeType': 'S'
        }], 
        TableName='gamescores', 
        KeySchema=[{
            'AttributeName': 'event', 
            'KeyType': 'HASH'
        }, 
        {
            'AttributeName': 'timestamp', 
            'KeyType': 'RANGE' 
        }], 
        ProvisionedThroughput={
            'ReadCapacityUnits': 5, 
            'WriteCapacityUnits': 5
        }
    )
    return table

def add_gsi(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.client('dynamodb')

    response = dynamodb.update_table(
        TableName='gamescores', 
        AttributeDefinitions=[
            {'AttributeName': 'event', 'AttributeType': 'S'}, 
            {'AttributeName': 'timestamp', 'AttributeType': 'S'}, 
            {'AttributeName': 'gamerid', 'AttributeType': 'S'}, 
            {'AttributeName': 'score', 'AttributeType': 'N'}
        ], 
        GlobalSecondaryIndexUpdates=[{
            'Create': {
                'IndexName': 'game_scores', 
                'KeySchema': [{
                    'AttributeName': 'gamerid', 
                    'KeyType': 'HASH'
                }, 
                {
                    'AttributeName': 'score', 
                    'KeyType': 'RANGE'
                }
            ], 
           'Projection': {
                'ProjectionType': 'INCLUDE',
                'NonKeyAttributes': [
                    'gamerid',
                ]
            },
            'ProvisionedThroughput': {
                'ReadCapacityUnits': 1, 
                'WriteCapacityUnits': 1
            }}
        }]
    )
    return response

    

if __name__ == '__main__':
    client = boto3.client('dynamodb')

    try:
        gamescores_table = create_table(client)
        print("Gamescores Table has been created")
    except:
        print("Table already exists")

    #add_gsi(client)
    

