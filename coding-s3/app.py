#!/usr/bin/env python3

import aws_cdk as cdk

from coding_s3.coding_s3_stack import CodingS3Stack


app = cdk.App()
CodingS3Stack(app, "coding-s3")

app.synth()
