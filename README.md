# CDK Python 실습

```bash
cdk init sample-app --language python
source .venv/bin/activate
pip install -r requirements.txt
```

## 버킷 만들어 보기

```python
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
```

## Lambda와 REST API 만들어 보기

**람다 코드**

`프로젝트 폴더/handlers/hello.py` 에 `handler` 라는 메서드를 정의한다.

```python
import json

def handler(event, context):
    print("request: {}".format(json.dumps(event)))
    params = event['pathParameters']
    name = event['pathParameters'].get('name', 'CDK') if params is not None else 'CDK'
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain'
        },
        'body': "Hello, {}! You've hit {}\n".format(name, event['path'])
    }
```

해당 핸들러 메서드의 위치는

- **CodeUri** - ****`handlers` (소스파일 위치)
- **Handler** - `hello.handler`  (⇒ hello.py의 handler라는 메서드)

로 표현된다. 따라서 아래 람다 컨스트럭트를 만들 때 두 값을 쓰는 걸 보게 될 것이다.

**스택 코드**

람다·REST API·리소스·두 자원 사이의 연결을 정의하고 있다.

```python
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
```