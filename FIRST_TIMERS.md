## Welcome to the SendGrid Open Source Community
 If you are new to Open Source, you are at the right place to start with. Contributions are always encouraged & appreciated. Just follow the organisation's Contribution Policies & you are good to go.
 ## How to get Started?
 - [Explore SendGrid](#explore)
 - [Raise Issues(If Found Any)](#issues)
 - [Setting up the Development Environment](#setup)
 - [Proposing Change through a Pull Request](#pr)
 - [Be Patient & Wait for reviews](#reviews)
 
 <a name="explore"></a>
 ### Explore SendGrid
Step 1: Get yourself Access to SendGrid API Service absolutely free from [here](https://sendgrid.com/free/?source=sendgrid-python)\
Step 2: Get familiar with SendGrid Service
 - Prerequisites are Python version 2.6, 2.7, 3.4, 3.5 or 3.6
 - Set up your [SendGrid API Key](https://app.sendgrid.com/settings/api_keys) to your local workspace [using](https://github.com/sendgrid/sendgrid-python#setup-environment-variables)
 - Install SendGrid to your workspace using `pip install sendgrid`
 - Copy & Run few sample programs from [here](https://github.com/sendgrid/sendgrid-python#hello-email)
 
 
 <a name="issues"></a>
 ### Raise Issues
 SendGrid uses GitHub as the content management service so, all the issues related to the project be it some feature request or a bug report, all are reported at the [GitHub Issue Tracker](https://github.com/sendgrid/sendgrid-python/issues)\
 Kindly make sure, to check for any duplicate issues raised by fellow contributors before opening a new issue. Be humble & polite while commenting on issues
  - Feature Request\
  In case you feel like something is missing or lacking in the API Service, feel free to share your views & opinions with the community
  - Bug Report\
  If you encounter any sort of bug or abnormal behavior, feel free to inform the community after performing the following checks:
    - Update to the latest version & check if the bug persists
    - Check the Issue Tracker for any similar bug report
    
  Finally fill up the Bug Report Template & Open the Issue highlighting your encountered bug & detailed steps to regenerate the bug.
  
  <a name="setup"></a>
  ### Setting up the Development Environment
   - **Using Docker**\
   Use our Docker image to avoid setting up the development environment yourself. See [USAGE.md](https://github.com/sendgrid/sendgrid-python/blob/master/docker/USAGE.md)
   
   - **Setting up Locally**\
   Step 1: Install the Prerequistes: Any Version of Python(2.6 through 3.6) & [python_http_client](https://github.com/sendgrid/python-http-client)\
   Step 2: Get a local copy of repository using `git clone https://github.com/sendgrid/sendgrid-python.git`\
   Step 3: Set your [SendGrid API Key](https://app.sendgrid.com/settings/api_keys) to your local workspace using\
    `echo "export SENDGRID_API_KEY='YOUR_API_KEY'" > sendgrid.env`\
    `echo "sendgrid.env" >> .gitignore`\
    `source ./sendgrid.env`\
   Step 4: The entire codebase consist of 3 major divisions
   - **/examples** contains *Working examples that demonstrate usage*
   - **/tests** contains *the unit and profiling tests*
   - **/sendgrid** contains *the Web API v3 client ie sendgrid.py and other files*.
   
   
  <a name="pr"></a>
  ## Proposing Change through a Pull Request
  **Step 1:** Fork the project & Clone your fork using `git clone https://github.com/<USERNAME>/sendgrid-python.git`
  
  **Step 2:** Reconfigure the remotes using `cd sendgrid-python` and `git remote add upstream https://github.com/sendgrid/sendgrid-python.git`
  
  **Step 3:** Create a new branch for your modifications using `git checkout -b <topic-branch-name>`
  
  **Step 4:** Commit the changes in logical chunks & add commit messages strictly following [this](http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html)
  
  **Step 5:** Run all test locally, [for more info](https://github.com/sendgrid/sendgrid-python/blob/master/CONTRIBUTING.md#testing)
  
  **Step 6:** Locally merge your the upstream development branch into your topic-branch using `git pull [--rebase] upstream master`
  
  **Step 7:** Push the topic branch up to your fork using `git push origin <topic-branch-name>`
  
  **Step 8:** Open a Pull Request with clear title and description against the master branch.
  
  In case, you have additional questions, feel free to drop a [mail](dx@sendgrid.com) or open an issue.
  
  <a name="reviews"></a>
  ## Be Patient & Wait for Reviews
  Kindly be patient & follow the suggestions as provided by the peer reviewers. Make required ammendments & changes to the PR as asked.
  
## [Explore New Issues to work upon](https://github.com/sendgrid/sendgrid-python/labels/difficulty%3A%20easy)