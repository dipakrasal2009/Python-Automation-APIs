import boto3


myec2 = boto3.resource(service_name = "ec2",
                        region_name = 'ap-south-1',
                        aws_access_key_id = "AKIAVRUVRDUTWFV5DG7Q",
                        aws_secret_access_key = "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"
                        )

def Launch_Instance():
    myec2.create_instances(
            InstanceType = "t2.micro",
            ImageId = "ami-0a4408457f9a03be3",
            MaxCount =1,
            MinCount=1
            )

Launch_Instance();
