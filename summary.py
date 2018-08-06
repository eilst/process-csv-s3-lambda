import pandas as pd
import boto3
from botocore.exceptions import ClientError

def get(event, context):

    s3 = boto3.resource('s3')

    tax_percentage = 0.14975
    #TODO: Change key from s3 PUT event
    df = pd.read_csv('e-statement-2018-07-14.csv')
    
    #Sum of columns
    sub_total_sales = df[["'Sale'"]].sum()[0]
    taxes = df [["'Tax'"]].sum()[0]
    total = df[["'Total'"]].sum()[0]
    uber_fee = df[["'Uber Fee'"]].sum()[0]

    tax_uber_fee = uber_fee*tax_percentage

    print("Subtotal: " + str(sub_total_sales))
    print("Taxes: "    + str(taxes))
    print("Total: "    + str(total))
    print("Fee: "      + str(uber_fee))
    print("Service tax: "+ str(tax_uber_fee))

    # Check that file exists and get a StreamingBody if it does exist
    # If it doesn't exist,
    header = []
    
    try:
        obj = s3.Object('reportesarriba', 'uberEatsData/hello.csv').get()['Body']
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


