#!/usr/bin/env python3

from aws_cdk import core

from my_artifact_bucket_stack.my_artifact_bucket_stack_stack import MyArtifactBucketStackStack


app = core.App()
MyArtifactBucketStackStack(app, "my-artifact-bucket-stack")

app.synth()
