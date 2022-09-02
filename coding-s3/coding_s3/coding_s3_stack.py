from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,
    RemovalPolicy,
    aws_s3 as s3,
)


class CodingS3Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket = s3.Bucket(self, 'MyBucket', 
            versioned=True, 
            removal_policy=RemovalPolicy.DESTROY, 
            bucket_name=self.stack_name.lower() + '-cdk-generated-' + self.region)
