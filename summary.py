import pandas as pd
import boto3
from botocore.exceptions import ClientError

s3 = boto3.resource('s3')

def create_summary(event, context):
    file_key = event['Records'][0]['s3']['object']['key']
    bucket = event['Records'][0]['s3']['bucket']['name']

    # get the file so we can use data frames
    obj = s3.Object(bucket, file_key).download_file('/tmp/working_file.csv')  
    df = pd.read_csv('/tmp/working_file.csv')
    

    tax_percentage = 0.14975  
    #Sum of columns
    sub_total_sales = df[["'Sale'"]].sum()[0]
    taxes = df [["'Tax'"]].sum()[0]
    total = df[["'Total'"]].sum()[0]
    uber_fee = df[["'Uber Fee'"]].sum()[0]

    tax_uber_fee = uber_fee*tax_percentage

    print("Subtotal:    " + str(sub_total_sales))
    print("Taxes:       " + str(taxes))
    print("Total:       " + str(total))
    print("Fee:         " + str(uber_fee))
    print("Service tax: "+ str(tax_uber_fee))

    # Check that file exists and get a StreamingBody if it does exist
    # If it doesn't exist,
    header = []
    
    try:
        obj = s3.Object(BUCKET_NAME, FILE).get()['Body']
        print('Exists')
        char = ''
        str = ''
        
        while char != '\n'
            char = obj.read(1).decode("utd-8")
            if char != ',':
                str+=char
            else:
                header.append(str)

    except ClientError as e:
        print("Not Exists")


