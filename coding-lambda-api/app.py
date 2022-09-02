#!/usr/bin/env python3

import aws_cdk as cdk

from coding_lambda_api.coding_lambda_api_stack import CodingLambdaApiStack


app = cdk.App()
CodingLambdaApiStack(app, "coding-lambda-api")

app.synth()
