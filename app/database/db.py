import boto3

dynamodbTableName = "heroes-db"
dynamodb = boto3.resource('dynamodb')#,
#aws_access_key_id="AKIAU4ZGB244UHGG4K4V",
#aws_secret_access_key="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",
#region_name="us-east-1")
#Descomentar las líneas de arriba para deployment por fuera de AWS
heroes_table = dynamodb.Table(dynamodbTableName)