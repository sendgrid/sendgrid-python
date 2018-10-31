# Table of Contents <!-- omit in toc -->
- [Introduction](#introduction)
- [Requirements](#requirements)
- [Deploying Locally](#deploying-locally)
- [Deploying to Google Kubernetes Engine](#deploying-to-google-kubernetes-engine)
    - [Deployment](#deployment)
    - [Cleaning Up](#cleaning-up)
- [Contributing](#contributing)
- [License](#license)


# Introduction
This is a sample application showcasing SendGrid's [inbound parse email webhooks](https://sendgrid.com/docs/for-developers/parsing-email/setting-up-the-inbound-parse-webhook/)
using Docker and Python 3.

# Requirements
 - Python 3.6 or higher
 - Docker Version 18 CE
 - Ngrok 2.2.8
 - SendGrid account with [inbound parse](https://sendgrid.com/docs/for-developers/parsing-email/setting-up-the-inbound-parse-webhook/) enabled
 - (Optional) A subscription to [Google Cloud Platform](https://cloud.google.com/)

# Deploying Locally
1. Clone the repo and find the example:
    ```bash
    git clone https://github.com/sendgrid/sendgrid-python.git
    cd sendgrid-python/examples/inbound-webhook-parsing
    ```
2. Build and run the Docker image:
   ```bash
   docker-compose build
   docker-compose up
   ```
3. Expose localhost:5000 using ngrok:
   ```bash
   ngrok http 5000
   ```
4. Add the `HTTPS` URL created by ngrok followed by `/parse_inbound` (so that
   the URL looks something like `https://XXXXXXX.ngrok.io/parse_inbound`) to SendGrid's
   [inbound parse settings](https://app.sendgrid.com/settings/parse) along with
   the host name you want as the recipient.

5. Send an email to the host. The parsed information should be visible in the
   output of the running Docker container.

# Deploying to Google Kubernetes Engine

## Deployment
1. Ensure you have an account on Google Cloud Platform for this section
2. Install the [Google Cloud SDK](https://cloud.google.com/sdk/)
3. Create a new project on Google Cloud Platform:
   ```bash
   gcloud projects create PROJECT_ID
   ```
   Keep note of the *PROJECT_ID* for future steps.

4. Build and upload the Docker image to Google Container Registry:
   ```bash
   docker build -t gcr.io/PROJECT_ID/inbound-webhook-parser .
   gcloud docker -- push gcr.io/PROJECT_ID/inbound-webhook-parser
   ```
   With *PROJECT_ID* being the same ID set in the previous step
5. Install `kubectl`:
   ```bash
   gcloud components install kubectl
   ```
6. Create the Kubernetes cluster:
   ```bash
   gcloud container clusters create PROJECT_ID \
    --scopes "cloud-platform" \ # GCE needs access to the Cloud API's
    --num-nodes 2 \
    --region GCP_ZONE
   ```
   Where *GCP_ZONE* can be any of Google's [supported server locations](https://cloud.google.com/compute/docs/regions-zones/)
7. Verify your access to the cluster:
   ```bash
   kubectl get nodes
   ```
8. Update the [app.yml](./gke/app.yml) file with your *PROJECT_ID*
9. Deploy the resources to the cluster:
   ```bash
   kubectl apply -f gke/app.yml
   ```
10. Get the External IP of the new service:
   ```bash
   kubectl describe service inbound-parser-svc
   ```
11. Add the IP + the endpoint `/parse_inbound` (such that the URL looks like
    `http://X.X.X.X:5000/parse_inbound`) to your SendGrid inbound parse settings and send a test email


## Cleaning Up
1. Delete the cluster:
   ```bash
   gcloud container clusters delete PROJECT_ID --zone GCP_ZONE
   ```   

# Contributing
If you would like to contribute to this project, please see the
[CONTRIBUTING](https://github.com/sendgrid/sendgrid-python/blob/master/CONTRIBUTING.md)
guide for more information

# License
See [LICENSE](https://github.com/sendgrid/sendgrid-python/blob/master/LICENSE.txt) for more information.
