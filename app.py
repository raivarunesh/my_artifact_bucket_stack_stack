#!/usr/bin/env python3

from aws_cdk import core

from my_artifact_bucket_stack.my_artifact_bucket_stack_stack import MyArtifactBucketStackStack

env_uat = core.Environment(account="264444055481", region="ap-southeast-2")
env_prd = core.Environment(account="880496541732", region="ap-southeast-2")

app = core.App()

MyArtifactBucketStackStack(app, "my-artifact-bucket-stack-Uat", env=env_uat)
MyArtifactBucketStackStack(app, "my-artifact-bucket-stack-Prd",is_prod=True, env=env_prd)

app.synth()
