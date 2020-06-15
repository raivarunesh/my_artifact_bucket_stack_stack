from aws_cdk import(
    aws_s3 as _s3,
    aws_kms as _kms,
     core)


class MyArtifactBucketStackStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str,is_prod=False, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here

        print(self.node.try_get_context('prd')['kms_arn'])

        my_key=_kms.Key.from_key_arn(self,
        "myKeyId",
        self.node.try_get_context('prd')['kms_arn']
        )

        if is_prod:
            artifactBucket = _s3.Bucket(self,
            "myProdArtifactBucketid",
            versioned=True,
            encryption=_s3.BucketEncryption.KMS,
            encryption_key=my_key,
            removal_policy=core.RemovalPolicy.RETAIN)

        else:
            artifactBucket = _s3.Bucket(self,
            "muDevArtifactBucketId",
            removal_policy=core.RemovalPolicy.DESTROY)

