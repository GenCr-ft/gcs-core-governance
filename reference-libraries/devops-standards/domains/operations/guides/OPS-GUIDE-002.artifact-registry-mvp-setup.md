---
docId: OPS-GUIDE-002
title: Artifact Registry MVP Initial Setup Guide
version: 1.0.0
date: '2025-07-17'
authors:
  - EE (GCT-DVO-DVSST-001)
knowledgeGuardian: Édouard (GCT-DVO-DVSST-001)
metadata:
  scope: studio
  domain: devops
  doc-type: guide
  lifecycle-stage: approved

ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/devops-standards/domains/operations/guides/OPS-GUIDE-002.artifact-registry-mvp-setup.md
---

# Artifact Registry MVP Initial Setup Guide

This guide outlines the one-time manual setup procedures required after the infrastructure for the Artifact Registry MVP has been provisioned via Terraform.

## 1. Initial GraphDB Repository Creation

1. Access the GraphDB Workbench in your browser at `http://<INSTANCE_PUBLIC_IP>:7200`.
2. Navigate to `Setup -> Repositories`.
3. Click "Create new repository".
    * **Repository ID**: `gencraft_ssot_registry`
    * **Repository title**: `Gencraft SSoT Registry`
4. Leave all other settings as default and click "Create".

## 2. Service User and Security Configuration

1. In the GraphDB Workbench, navigate to `Admin -> Users and Access`.
2. Enable security by toggling the switch to **ON**. You will be prompted to set a password for the default `admin` user. **Store this password securely.**
3. Log in as the `admin` user.
4. Click "Create new user".
    * **Username**: `gft-service-user`
    * **Password**: Generate a strong, random password.
    * **Grant Permissions**: Assign the `read-write` role to this user for the `gencraft_ssot_registry` repository.
5. Click "Save".

## 3. Storing the Service User Password in AWS SSM

The password for `gft-service-user` must be stored securely in AWS Systems Manager Parameter Store.

1. Navigate to AWS Console: Go to `Systems Manager > Parameter Store`.
2. Create Parameter:
    * **Name**: `/gencraft/graphdb/service_user_password`
    * **Description**: Password for the GraphDB service account used by CI/CD and tools.
    * **Tier**: `Standard`
    * **Type**: `SecureString`
    * **KMS key source**: `My current account` (uses the default `alias/aws/ssm` key).
    * **Value**: Paste the strong password generated in the previous step.
3. Click "Create parameter".

## 4. Minimum IAM Policy for GitHub Actions

A GitHub Action workflow that needs to retrieve this password requires the following IAM policy attached to its role:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "ssm:GetParameter",
            "Resource": "arn:aws:ssm:<REGION>:<ACCOUNT_ID>:parameter/gencraft/graphdb/service_user_password"
        }
    ]
}
```

Replace `<REGION>` and `<ACCOUNT_ID>`  with the appropriate values for our AWS account.

## 5. Future Migration Path to AWS Secrets Manager

For production environments, AWS Systems Manager (SSM) Parameter Store provides a secure and adequate solution for the initial MVP. However, our long-term strategy for secret management, as defined by security protocol S8, designates AWS Secrets Manager as the definitive SSoT. This is due to its advanced features which are critical for a mature security posture.

**Future Action**: A formal task will be created to migrate this service password to Secrets Manager. This migration will unlock several key benefits:

* **Automatic Secret Rotation**: This is the primary driver for the migration. Secrets Manager can be configured to automatically rotate credentials on a defined schedule (e.g., every 90 days) using AWS Lambda functions. This practice significantly reduces the attack surface by ensuring that even if a credential is compromised, its valid lifetime is minimal, aligning with a proactive security posture.
* **Fine-grained Access Policies**: While SSM allows for IAM policies on a per-parameter basis, Secrets Manager provides more granular control. It integrates more deeply with AWS IAM, allowing for complex policies based on resource tags and identity, which enables us to enforce the principle of least privilege with greater precision across different services and roles.
* **Cross-Account Access**: This feature streamlines our multi-account architecture. For instance, if a future analytics service resides in a separate, dedicated AWS account, Secrets Manager makes it straightforward to share a specific secret with an IAM role in that account without building complex and difficult-to-maintain cross-account role assumption policies.

The migration process will be carefully planned to ensure zero downtime. It will involve updating the client code (e.g., in `gft-cli` or CI/CD scripts) to be capable of reading from both SSM and Secrets Manager, performing the secret migration, updating the IAM policies to point to the new secret, and finally, after a validation period, decommissioning the old SSM parameter. This phased approach ensures a seamless and secure transition.
