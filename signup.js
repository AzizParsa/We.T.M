var AWS = require('aws-sdk');
var dynamodb = new AWS.DynamoDB({apiVersion: '2012-08-10'});

exports.handler = function(event, context,callback) {
  
    var tableName = "customer";
    var tempCode=  Math.floor(Math.random() * Math.floor(1000));
   var params = {
  Message:'Your We.T.M verification code is '+ tempCode.toString(), /* required */
  PhoneNumber: event['pathParameters']['phone'],
    
};

// Create promise and SNS service object
var publishTextPromise = new AWS.SNS({apiVersion: '2010-03-31'}).publish(params).promise();
publishTextPromise.then(
  function(data) {
    console.log("MessageID is " + data.MessageId);
  }).catch(
    function(err) {
    console.error(err, err.stack);
  });


    dynamodb.putItem({
        "TableName": tableName,
        "Item" : {
            "phone": {"S": event['pathParameters']['phone']},
            "password": {"S": event['pathParameters']['password']},
            "code": {"S":tempCode.toString()},
            "balance": {"S":"0"},
            "varified":{"S":"false"},
        }
    }, function(err, data) {
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
            "x-custom-header" : "created"
        },
        body: JSON.stringify("customer registered with Code "+tempCode)
    };
        callback(null, response);
        }
    });
};


