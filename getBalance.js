var AWS = require('aws-sdk');
var dynamodb = new AWS.DynamoDB({apiVersion: '2012-08-10'});

exports.handler = function(event, context,callback) {
  
    var tableName = "customer";
    var params = {
    AttributesToGet: [
      "balance"
    ],
    TableName : tableName,
    Key : { 
      "phone" : {
        "S" : event['pathParameters']['phone'],
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
              var response = {
        statusCode: 200,
        headers: {
            "x-custom-header" : ""
        },
        body: JSON.stringify(data.Item.balance.S)
    };
        callback(null, response);
        }
    });
};


