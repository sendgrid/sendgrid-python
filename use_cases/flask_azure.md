## Deploying a simple SendGrid Hello Mail App on Microsoft Azure

### Setting Up SendGrid & Azure Accounts

**Step 1:** Create a SendGrid Free Account from [here](https://sendgrid.com/free?source=sendgrid-python)

**Step 2:** Create a Microsoft Azure Account: [Free-Tier](https://azure.microsoft.com/en-in/free/) | [Student-Pack](https://azure.microsoft.com/en-in/free/students/)

**Step 3:** Create your SendGrid API Key from [here](https://app.sendgrid.com/settings/api_keys)

**Step 4:** Validate your Generated SendGrid API Key using
```bash
curl -i --request POST \
--url https://api.sendgrid.com/v3/mail/send \
--header 'Authorization: Bearer <YOUR_SENDGRID_API_KEY>' \
--header 'Content-Type: application/json' \
--data '{"personalizations": [{"to": [{"email": "<RECEIPENT_MAIL>"}]}],"from": {"email": "<SENDER_MAIL>"},"subject": "Is API Key Working","content": [{"type": "text/plain", "value": "Yes, It is!"}]}'
```

> **If Result gives *HTTP/1.1 202 Accepted*, You're good to move forward.**


### Setting up the App

**Step 1:** Get local copy of the project using `git clone https://github.com/jaykay12/demo-sendgrid-azure.git`

**Step 2:** Create a virtualenv for the web app using `virtualenv venv`

**Step 3:** Activate the virtualenv using `source venv/bin/activate`

**Step 4:** Update your environment with SendGrid-API Key generated in Step 3 of Phase 1 using,
```bash
echo "export SENDGRID_API_KEY=<YOUR_API_KEY>" > sendgrid.env
source ./sendgrid.env
```

**Step 5:** Install all the dependencies of the web-app using `pip install -r requirements.txt`

**Step 6:** Check if the app is running locally using `FLASK_APP=application.py flask run`

**Step 7:** Hit: `127.0.0.1:5000/` from browser & check if the simple mail sending is working or not.

> **If the Mail is Sent suceesfully with *Response.code 202*, You're good to move ahead.**


### Deploying the App on Microsoft Azure

**Step 1:** Open Azure CLI using bash(preferabbly) or PowerShell

![azure-cli](https://user-images.githubusercontent.com/13948542/46796235-cb3f8d00-cd69-11e8-9eed-120671532b9d.png)

**Step 2:** Create a deployment user using 
```bash
az webapp deployment user set --user-name <USERNAME> --password <PASSWORD>
```
*Note the Password created at this step, as it is used for further deploys*

**Step 3:** Create a Resource-group using 
```bash 
az group create --name <YOUR_RESOURCE_GROUP_NAME> --location "Central India"
```
```json
{
  "id": "/subscriptions/<SOME_UNIQUE_HASH>/resourceGroups/<YOUR_RESOURCE_GROUP_NAME>",
  "location": "centralindia",
  "managedBy": null,
  "name": "<YOUR_RESOURCE_GROUP_NAME>",
  "properties": {
    "provisioningState": "Succeeded"
  },
  "tags": null
}
```

You can select the best location for the resource-group using 
```bash
az appservice list-locations --sku B1 --linux-workers-enabled
```

**Step 4:** Create Azure App Service Plan for the deploy using 
```bash
az appservice plan create --name <YOUR_SERVICE_PLAN_NAME> --resource-group <YOUR_RESOURCE_GROUP_NAME> --sku B1 --is-linux
```
```json
{
  "adminSiteName": null,
  "freeOfferExpirationTime": "2019-04-10T21:25:41.010000",
  "geoRegion": "Central India",
  "...": "...",
  "name": "<YOUR_SERVICE_PLAN_NAME>",  
  "status": "Ready",
  "...": "...",
  "type": "Microsoft.Web/serverfarms",
  "workerTierName": null
}
```

**Step 5:** Create your web-app on Azure Portal using 
```bash
az webapp create --resource-group <YOUR_RESOURCE_GROUP_NAME> --plan <YOUR_SERVICE_PLAN_NAME> --name <YOUR_WEBAPP_NAME> --runtime "PYTHON|3.7" --deployment-local-git
```
```json
Local git is configured with url of '<LOCAL_GIT_URL>'
{
  "availabilityState": "Normal",
  "deploymentLocalGitUrl": "<LOCAL_GIT_URL>",
  "...": "...",
  "hostNames": [
    "<YOUR_WEBAPP_NAME>.azurewebsites.net"
  ],
  "...": "...",
  "type": "Microsoft.Web/sites",
  "usageState": "Normal"
}
```

Copy the <LOCAL_GIT_URL> obtained in the above step.

**Step 6:** In Local Terminal, Add a new remote to the git repo using `git remote add azure <LOCAL_GIT_URL>`

**Step 7:** Push the local webapp to the deployment using `git push azure master`
```bash
Counting objects: 24, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (20/20), done.
Writing objects: 100% (24/24), 26.53 KiB | 0 bytes/s, done.
Total 24 (delta 5), reused 0 (delta 0)
remote: Updating branch 'master'.
remote: Updating submodules.
remote: Preparing deployment for commit id '704c54e999'.
remote: Generating deployment script.
remote: Generating deployment script for python Web Site
remote: Generated deployment script files
remote: Running deployment command...
remote: Python deployment.
remote: Kudu sync from: '/home/site/repository' to: '/home/site/wwwroot'
remote: Copying file: '.gitignore'
remote: Copying file: 'README.md'
remote: Copying file: 'application.py'
remote: Copying file: 'requirements.txt'
remote: Deleting file: 'hostingstart.html'
remote: Ignoring: .git
remote: Copying file: 'static/sendgrid.ico'
remote: Copying file: 'templates/index.html'
remote: /home/site/repository
remote: /home/site/wwwroot
remote: Found requirements.txt
remote: Create virtual environment
remote: Activate virtual environment
remote: Collecting Flask==1.0.2 (from -r requirements.txt (line 2))
...
remote: Collecting sendgrid==5.6.0 (from -r requirements.txt (line 7))
...
remote: Successfully installed Click-7.0 Flask-1.0.2 Jinja2-2.10 MarkupSafe-1.0 Werkzeug-0.14.1 itsdangerous-0.24 python-http-client-3.1.0 sendgrid-5.6.0
remote: pip install finished
remote: Finished successfully.
remote: Deployment successful.
remote: App container will begin restart within 10 seconds.
To <LOCAL_GIT_URL>
 * [new branch]      master -> master
```

**Step 8:** Set the SENDGRID_API_KEY as the Environment variable in Azure Portal. Open the Application Settings of the Web-App.

![api_key](https://user-images.githubusercontent.com/13948542/46796244-d2669b00-cd69-11e8-93bb-d7d0ddcb4081.png)


**Step 9:** Browse to the deployed application using your web browser and Hit `http://<YOUR_WEBAPP_NAME>.azurewebsites.net`

Check if the Web-App loads & Mail Sending is Success!

> **Woohoo! Congratulations. You just got your SendGrid app deployed on Microsoft Azure!.**
