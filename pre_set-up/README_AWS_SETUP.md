# AWS Data Pipeline Project - Setup Instructions

This document records the initial AWS IAM and AWS CLI setup steps for the **AWS Data Pipeline for E-commerce Transactions & User Profiles** project.  
Use this as a reference if you ever need to reconfigure your environment.

---

## 1. Create an AWS Account
- Go to [https://aws.amazon.com](https://aws.amazon.com)
- Click **Create an AWS Account** and follow instructions.
- You will need a valid credit/debit card (for Free Tier validation).
- Once done, log into the **AWS Management Console**.

---

## 2. Create an IAM User
We do not use the AWS root user for development. Instead, create a dedicated IAM user.

1. In AWS Console → search for **IAM** → click **IAM** service.
2. In left menu → **Users** → **Add users**.
3. Username: `data-engineer-dev`
4. Access type:
   - ✅ Programmatic access (for CLI)
   - ❌ Console access (not required)
5. Permissions:
   - Attach policy: **AdministratorAccess** (for learning only).  
     ⚠️ In production, replace with least-privilege policies (S3, Glue, Lambda, Step Functions, Athena, Quicksight, CloudWatch).
6. Create the user and save the **Access Key ID** and **Secret Access Key** securely.

> ⚠️ **Never commit your AWS access keys to GitHub or any repo!**

---

## 3. Install AWS CLI
### Windows
- Download installer: [AWS CLI MSI](https://awscli.amazonaws.com/AWSCLIV2.msi)

### Mac/Linux (via pip)
```bash
pip install awscli --upgrade --user
aws --version
```

Expected output:  
`aws-cli/2.x.x Python/3.x.x ...`

---

## 4. Configure AWS CLI
Run:
```bash
aws configure
```

Enter values:
```
AWS Access Key ID [None]: <your Access Key ID>
AWS Secret Access Key [None]: <your Secret Access Key>
Default region name [None]: us-east-1
Default output format [None]: json
```

---

## 5. Tips on Using Multiple Profiles (for AWS CLI configuration)
Run:
```bash
aws configure --profile dev
aws configure --profile prod
```

Switching Profiles: 
Use --profile in each command:
```
aws sts get-caller-identity --profile dev
aws sts get-caller-identity --profile prod
```


---

## 6. Verify Configuration
Test your setup:
```bash
aws sts get-caller-identity
```

Example output:
```json
{
    "UserId": "AIDA...XYZ",
    "Account": "123456789012",
    "Arn": "arn:aws:iam::123456789012:user/data-engineer-dev"
}
```

If you see this → ✅ AWS CLI is working correctly.

---

## Next Steps
- Create an S3 bucket for raw and processed data.
- Upload CSV and JSON datasets to S3.
- Proceed with building the PySpark ETL pipeline in AWS Glue.

---

## Safety & Cost Notes
- Stay within Free Tier where possible.
- Delete unused resources to avoid charges.
- Rotate and secure IAM credentials.
