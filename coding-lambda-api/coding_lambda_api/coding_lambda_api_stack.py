from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigateway
)
import os.path as path


class CodingLambdaApiStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        func = _lambda.Function(self, id='HelloWorldFunction',
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.from_asset('handlers'),
            handler='hello.handler') # it means 'handlers> hello.py> handler' function

        api = apigateway.LambdaRestApi(self, "MyApi", handler=func, proxy=False)
        root = api.root 

        hello = root.add_resource('hello')
        hello.add_method('GET')

        helloname = hello.add_resource('{name}')
        helloname.add_method('GET')
