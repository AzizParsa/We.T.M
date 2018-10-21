import json
import os


from botocore.vendored import requests

def lambda_handler(event, context):

    amount = event.amount
    account = event.account
    invoice=event.invoce


    headers = {
         'Accept': 'application/json',
    }


    payload =  {
"messageId": "1526327698270",
"clientId": "B2BWS_1_1_9999",
"buyerId": "324323300993",
"actionType": "1",
"payment": {
"accountNumber": account,
"accountType": "2",
"accountLimit": "100",
"cardAccountExpiryDate": "02/2021",
"paymentGrossAmount": amount,
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
"primaryEmailAddress": "milisecond@gmail.com",
"alternateEmailAddresses": [
{
"alternateEmailAddress": "milisecond@gmail.com"
}
],
"emailNotes": "We.T.M payment on behalf of customer"
},
"invoices": [
{
"invoiceNumber": invoice,
"invoiceDate": "2018-04-24",
"invoiceAmount": amount,
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
    response = requests.post(url, headers=headers, auth=('user ID',' secrete key'),
                             json=json.dumps(payload)
                             ,cert=( os.environ['LAMBDA_TASK_ROOT']+'/cert.pem', os.environ['LAMBDA_TASK_ROOT']+'/key_d7424101-8fa6-4e00-b4a6-7aa4c4c535f9.pem')
                             )
    response.raise_for_status()
    
    return {
        "statusCode": 200,
        "body": "payment completed"}


