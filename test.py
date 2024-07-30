import json
import boto3


def lambda_handler(event, context):
    # print(event['queryStringParameter'])
    
   
    event_has_user = 'user' in event['queryStringParameter']
    # print(event_has_user)
    x=5
    y=4
   
    if event_has_user :
        print("False")
    
    
    client = boto3.client('dynamodb')
    
    response = client.query(
        
    if event_has_user:
        user_name = event['user']
        TableName='TestTodo',
        KeyConditionExpression='#PK = :PK',
        ExpressionAttributeNames={
         '#PK' : 'PK'
            '#SK' : 'SK'
         },
        ExpressionAttributeValues={
            ':PK' :{'S': 'Task#'}
            ':SK' :{'S': f'Task#User#{user_name}'}
                
        }
            
    else:
        TableName='TestTodo',
        KeyConditionExpression='#PK = :PK',
        ExpressionAttributeNames={
            '#PK' : 'PK'
        },
        ExpressionAttributeValues={
            ':PK' :{'S': 'Task#'}
        }
            
    )
            
        
        

    return response