import json
import os


from botocore.vendored import requests

def lambda_handler(event, context):



    headers = {
         'Accept': 'application/json',
    }


    payload =  {
"messageId": "1526327698270",
"clientId": "B2BWS_1_1_9999",
"buyerId": "9999",
"actionType": "1",
"payment": {
"accountNumber": "411111111111111",
"accountType": "2",
"accountLimit": "100",
"cardAccountExpiryDate": "02/2021",
"paymentGrossAmount": "2.50",
"currencyCode": "USD",
"paymentExpiryDate": "2018-05-30",
"paymentRequestDate": "2018-05-14",
"paymentType": "CCC",
"supplier": {
"supplierId": "RESTAPISupp-007",
"supplierName": "RESTAPISupp-007",
"supplierType": "VPA",
"stpId": "",
"supplierAddressLine1": "Address1",
"supplierAddressLine2": "Address2",
"supplierCity": "FC",
"supplierState": "CA",
"supplierPostalCode": "94404",
"supplierCountryCode": "USA",
"supplierLanguage": "en_US",
"defaultCurrencyCode": "USD",
"supplierGLCode": "12345",
"enablePin": "N",
"supplierDate": "MMDDYYYY",
"primaryEmailAddress": "abc@company.com",
"alternateEmailAddresses": [
{
"alternateEmailAddress": "abc@company.com"
}
],
"emailNotes": "B2B WS CVV2 Payment for FXD Account"
},
"invoices": [
{
"invoiceNumber": "INV01",
"invoiceDate": "2018-04-24",
"invoiceAmount": "3.75",
"PurchaseOrderNumber": "PO1234",
"PurchaseOrderDate": "2018-02-01"
},
{
"invoiceNumber": "INV02",
"invoiceDate": "2018-04-24",
"invoiceAmount": "1.25",
"PurchaseOrderNumber": "PO1234",
"PurchaseOrderDate": "2018-02-01"
}
],
"ReferenceFields": [
"1234",
"12356"
],
"PartialPaymentIndicator": "y"
}
}



    url = 'https://sandbox.api.visa.com/vpa/v1/payment/ProcessPayments'
    response = requests.post(url, headers=headers, auth=('ZIJASRFP33KM0M1S4HYE21KGWEAxPDb5D_8WwvmFLBJPzPe6k','B4IKZ0AEBN3Bewse6W0l2YTLhR'),
                             json=json.dumps(payload)
                             ,cert=( os.environ['LAMBDA_TASK_ROOT']+'/cert.pem', os.environ['LAMBDA_TASK_ROOT']+'/key_d7424101-8fa6-4e00-b4a6-7aa4c4c535f9.pem')
                             )
    response.raise_for_status()
    
    return {
        "statusCode": 200,
        "body": "payment completed"}


