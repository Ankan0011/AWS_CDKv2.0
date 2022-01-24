#!/usr/bin/env python3

import aws_cdk as cdk

from awscdk_toolkit.awscdk_toolkit_stack import AwscdkToolkitStack

ENV_ARG = cdk.Environment(account="773124578159", region="ap-south-1")

app = cdk.App()
AwscdkToolkitStack(app, "awscdk-toolkit", env=ENV_ARG)

app.synth()
