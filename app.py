#!/usr/bin/env python3

from aws_cdk import core

from my_artifact_bucket_stack.my_artifact_bucket_stack_stack import MyArtifactBucketStackStack

app = core.App()

env_uat = core.Environment(account=app.node.try_get_context('uat')['account'],
                           region=app.node.try_get_context('uat')['region'])
env_prd = core.Environment(account=app.node.try_get_context('prd')['account'],
                             region=app.node.try_get_context('prd')['region'])

MyArtifactBucketStackStack(app, "my-artifact-bucket-stack-Uat", env=env_uat)
MyArtifactBucketStackStack(app, "my-artifact-bucket-stack-Prd",is_prod=True, env=env_prd)

app.synth()
