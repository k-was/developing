import boto3, botostubs

# List Objects in Bucket using the Client API
def listClient():
    s3client = boto3.client('s3')  # type: botostubs.S3
    
    response = s3client.list_objects_v2(Bucket='angus-pictures')
    for content in response['Contents']:
        print(content['Key'],content['LastModified'])

        # s3client.download_file(
        #     Bucket='angus-pictures',
        #     Key= content['Key'],
        #     Filename= 'anguspic.png'
        # )
    return 


# List Objects in Bucket using the Resource API
# Resources represent an object-oriented interface to AWS
def listResource():
    s3resource = boto3.resource('s3')    
    
    bucket = s3resource.Bucket('angus-pictures')
    
    for object in bucket.objects.all():
        print(object.key, object.last_modified)

        # bucket.download_file(
        #     Key= object.key,
        #     Filename= 'anguspic2.png'
        # )
    return 

if __name__ == '__main__':
    listClient()
    listResource()



