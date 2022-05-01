import boto3

dynamodbTableName = "heroes-db"
dynamodb = boto3.resource('dynamodb')#,
#aws_access_key_id="",
#aws_secret_access_key="",
#region_name="us-east-1")
#Descomentar las líneas de arriba y poner los datos correspondientes para deployment por fuera de AWS
heroes_table = dynamodb.Table(dynamodbTableName)
