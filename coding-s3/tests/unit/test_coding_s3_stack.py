import aws_cdk as core
import aws_cdk.assertions as assertions
from coding_s3.coding_s3_stack import CodingS3Stack


def test_sqs_queue_created():
    app = core.App()
    stack = CodingS3Stack(app, "coding-s3")
    template = assertions.Template.from_stack(stack)

    template.has_resource_properties("AWS::SQS::Queue", {
        "VisibilityTimeout": 300
    })


def test_sns_topic_created():
    app = core.App()
    stack = CodingS3Stack(app, "coding-s3")
    template = assertions.Template.from_stack(stack)

    template.resource_count_is("AWS::SNS::Topic", 1)
