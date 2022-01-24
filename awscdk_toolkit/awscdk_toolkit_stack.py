from constructs import Construct
from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as gateway,
)


class AwscdkToolkitStack (Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        #Defining an AWS Lambda Resource
        my_lambda = _lambda.Function(
            self, 'HelloHandler', runtime=_lambda.Runtime.PYTHON_3_9,
            code= _lambda.Code.from_asset('lambda'),
            handler='hello.handle'
        )

        #Defining an API gateway to access the Lambda function
        Restapi =gateway.LambdaRestApi(
            self, 'Endpoint',
            handler=my_lambda,
        )