var AWS = require('aws-sdk');
var dynamodb = new AWS.DynamoDB({apiVersion: '2012-08-10'});

exports.handler = function(event, context,callback) {

var tableName="customer";
var params = {
    TableName:tableName,
    Key:{
        "phone": {"S":event['pathParameters']['phone'],}
    },
    UpdateExpression: "set varified = :v",
    ExpressionAttributeValues:{
        ":v":{"S":"true"}
    },
    ReturnValues:"UPDATED_NEW"
};


    dynamodb.updateItem(params, function(err, data) {
        if (err) {
              var response = {
        statusCode: 500,
        headers: {
            "x-custom-header" : "verification failed"
        },
        body: JSON.stringify(err)
    };
        callback(null, response);
        }
        else {
              var response = {
        statusCode: 200,
        headers: {
            "x-custom-header" : "verified"
        },
        body: JSON.stringify("customer verified")
    };
        callback(null, response);
        }
    });
};


