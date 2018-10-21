var AWS = require('aws-sdk');
var dynamodb = new AWS.DynamoDB({apiVersion: '2012-08-10'});

exports.handler = function(event, context,callback) {

var tableName="customer";

   var params = {
    AttributesToGet: [
      "balance"
    ],
    TableName : tableName,
    Key : { 
      "phone" : {
        "S" :event['pathParameters']['phone'],
      }
    }
  }
 dynamodb.getItem(params, function(err, data) {
        if (err) {
              var response = {
                statusCode: 500,
                headers: {
                    "x-custom-header" : "failed"
                },
                body: JSON.stringify("failed!")
                 };
                callback(null, response);
        }
        else {
             var balance = data.Item.balance.S;
              var amount = event['pathParameters']['amount']
              var newBalance = parseInt(balance)+parseInt(amount);
             params = {
                TableName:tableName,
                Key:{
                    "phone": {"S":event['pathParameters']['phone'],}
                },
                UpdateExpression: "set balance = :v",
                ExpressionAttributeValues:{
                    ":v":{"S":newBalance.toString()}
                },
                ReturnValues:"UPDATED_NEW"
            };
            

        
        
            dynamodb.updateItem(params, function(err, data) {
                if (err) {
                      var response = {
                statusCode: 500,
                headers: {
                    "x-custom-header" : "balance update failed"
                },
                body: JSON.stringify(err)
            };
                callback(null, response);
                }
                else {
                      var response = {
                statusCode: 200,
                headers: {
                    "x-custom-header" : "balanced updated"
                },
                body: JSON.stringify("customer balance updated")
            };
                callback(null, response);
                }
            });
              
              
        }
    });


};


