# Copyright 2024 DataRobot, Inc. and its affiliates.
# All rights reserved.
# DataRobot, Inc.
# This is proprietary source code of DataRobot, Inc. and its
# affiliates.
# Released under the terms of DataRobot Tool and Utility Agreement.

from .common.schema import (
    CredentialArgs,
)
from pydantic import ValidationError
from .settings_main import project_name
from docsassist.credentials import AzureOpenAICredentials

try:
    credential = AzureOpenAICredentials()
    credential.test()
except ValidationError as e:
    raise ValueError(
        "Unable to load LLM credentials. "
        "Verify you have setup your environment variables as described in README.md."
    ) from e

credential_args = CredentialArgs(
    resource_name="llm-specific-credential",
    name=f"LLM Credential [{project_name}]",
)
