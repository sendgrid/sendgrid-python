Hello! Thank you for choosing to help contribute to one of the SendGrid open source libraries. There are many ways you can contribute and help is always welcome.  We simply ask that you follow the following contribution policies.

- [CLAs and CCLAs](#cla)
- [Roadmap & Milestones](#roadmap)
- [Feature Request](#feature-request)
- [Submit a Bug Report](#submit-a-bug-report)
- [Improvements to the Codebase](#improvements-to-the-codebase)
- [Understanding the Code Base](#understanding-the-codebase)
- [Testing](#testing)
- [Style Guidelines & Naming Conventions](#style-guidelines-and-naming-conventions)
- [Creating a Pull Request](#creating-a-pull-request)
- [Code Reviews](#code-reviews)

<a name="roadmap"></a>
We use [Milestones](https://github.com/sendgrid/sendgrid-python/milestones) to help define current roadmaps, please feel free to grab an issue from the current milestone. Please indicate that you have begun work on it to avoid collisions. Once a PR is made, community reviews, comments, suggestions and additional PRs are welcomed and encouraged.

<a name="cla"></a>
## CLAs and CCLAs

Before you get started, SendGrid requires that a SendGrid Contributor License Agreement (CLA) be filled out by every contributor to a SendGrid open source project.

Our goal with the CLA is to clarify the rights of our contributors and reduce other risks arising from inappropriate contributions.  The CLA also clarifies the rights SendGrid holds in each contribution and helps to avoid misunderstandings over what rights each contributor is required to grant to SendGrid when making a contribution.  In this way the CLA encourages broad participation by our open source community and helps us build strong open source projects, free from any individual contributor withholding or revoking rights to any contribution.

SendGrid does not merge a pull request made against a SendGrid open source project until that pull request is associated with a signed CLA. Copies of the CLA are available [here](https://gist.github.com/SendGridDX/98b42c0a5d500058357b80278fde3be8#file-sendgrid_cla).

When you create a Pull Request, after a few seconds, a comment will appear with a link to the CLA. Click the link and fill out the brief form and then click the "I agree" button and you are all set. You will not be asked to re-sign the CLA unless we make a change.

There are a few ways to contribute, which we'll enumerate below:

<a name="feature-request"></a>
## Feature Request

If you'd like to make a feature request, please read this section.

The GitHub issue tracker is the preferred channel for library feature requests, but please respect the following restrictions:

- Please **search for existing issues** in order to ensure we don't have duplicate bugs/feature requests.
- Please be respectful and considerate of others when commenting on issues

<a name="submit-a-bug-report"></a>
## Submit a Bug Report

Note: DO NOT include your credentials in ANY code examples, descriptions, or media you make public.

A software bug is a demonstrable issue in the code base. In order for us to diagnose the issue and respond as quickly as possible, please add as much detail as possible into your bug report.

Before you decide to create a new issue, please try the following:

1. Check the Github issues tab if the identified issue has already been reported, if so, please add a +1 to the existing post.
2. Update to the latest version of this code and check if issue has already been fixed
3. Copy and fill in the Bug Report Template we have provided below

### Please use our Bug Report Template

In order to make the process easier, we've included a [sample bug report template]((https://github.com/sendgrid/sendgrid-python/.github/ISSUE_TEMPLATE)) (borrowed from [Ghost](https://github.com/TryGhost/Ghost/)). The template uses [GitHub flavored markdown](https://help.github.com/articles/github-flavored-markdown/) for formatting.

<a name="improvements-to-the-codebase"></a>
## Improvements to the Codebase

We welcome direct contributions to the sendgrid-python code base. Thank you!

### Development Environment ###
#### There are two ways to get set up: ####
#### 1. Using Docker ####
This is usually the easiest and fastest way to get set up.
You can use our Docker image to avoid setting up the development environment yourself.  See [USAGE.md](https://github.com/sendgrid/sendgrid-python/blob/master/docker/USAGE.md).

#### - OR - ####
#### 2. Install and Run Locally ####

##### Prerequisites #####

- Python 2.7 and 3.4+
- [python_http_client](https://github.com/sendgrid/python-http-client)

##### Initial setup: #####

```bash
git clone https://github.com/sendgrid/sendgrid-python.git
cd sendgrid-python
```

### Environment Variables

First, get your free SendGrid account [here](https://sendgrid.com/free?source=sendgrid-python).

Next, update your environment with your [SENDGRID_API_KEY](https://app.sendgrid.com/settings/api_keys).

```bash
cp .env_sample .env
```

Then edit `.env` and insert your API key.

```bash
# You do not need to do this when using Docker Compose
source .env
```

##### Execute: #####

See the [examples folder](https://github.com/sendgrid/sendgrid-python/tree/master/examples) to get started quickly.

If testing from the root directory of this repo, create a new file (e.g. test.py) and replace `import sendgrid` with `from sendgrid import *`

<a name="understanding-the-codebase"></a>
## Understanding the Code Base

**/examples**

Working examples that demonstrate usage.

**/tests**

Currently we have unit and profiling tests.

**/sendgrid**

The Web API v3 client is `sendgrid.py`, the other files are legacy code for our mail send v2 endpoint.

<a name="testing"></a>
## Testing

The PR must pass all the tests before it is reviewed.

All test files are in the [`test`](https://github.com/sendgrid/sendgrid-python/test) directory.

For the purposes of contributing to this repo, please update the [`test_sendgrid.py`](https://github.com/sendgrid/sendgrid-python/tree/master/test/test_sendgrid.py) file with unit tests as you modify the code.

`python -m unittest discover -v`

### Testing Multiple Versions of Python

The PR must pass all the tests before it is reviewed.

#### Prerequisites: ####

The above local "Initial setup" is complete

* [pyenv](https://github.com/yyuu/pyenv)
* [tox](https://pypi.python.org/pypi/tox)
* [prism](https://github.com/stoplightio/prism) v0.6 - It should be available in your PATH, but unittest script
will try to install it locally if not found. Apart from PATH env variable it will check in `~/bin` and `/usr/local/bin`.
You can install it by yourself in user dir by calling `source test/prism.sh`.

#### Initial setup: ####

Add ```eval "$(pyenv init -)"``` to your shell environment (.profile, .bashrc, etc) after installing tox, you only need to do this once.

```
pyenv install 2.7.11
pyenv install 3.4.3
pyenv install 3.5.0
```
Make sure to change the current working directory to your local version of the repo before running the following command:
```
python setup.py install
```
```
pyenv local 3.5.0 3.4.3 2.7.11
pyenv rehash
```

#### Execute: ####

```
source venv/bin/activate
tox
```

<a name="style-guidelines-and-naming-conventions"></a>
## Style Guidelines & Naming Conventions

Generally, we follow the style guidelines as suggested by the official language. However, we ask that you conform to the styles that already exist in the library. If you wish to deviate, please explain your reasoning.

- [PEP8](https://www.python.org/dev/peps/pep-0008/)

Please run your code through:

- [pyflakes](https://pypi.python.org/pypi/pyflakes)
- [pylint](https://www.pylint.org/)
- [pep8](https://pypi.python.org/pypi/pep8)

## Creating a Pull Request<a name="creating-a-pull-request"></a>

1. [Fork](https://help.github.com/fork-a-repo/) the project, clone your fork,
   and configure the remotes:

   ```bash
   # Clone your fork of the repo into the current directory
   git clone https://github.com/sendgrid/sendgrid-python

   # Navigate to the newly cloned directory
   cd sendgrid-python

   # Assign the original repo to a remote called "upstream"
   git remote add upstream https://github.com/sendgrid/sendgrid-python
   ```

2. If you cloned a while ago, get the latest changes from upstream:

   ```bash
   git checkout <dev-branch>
   git pull upstream <dev-branch>
   ```

3. Create a new topic branch (off the main project development branch) to
   contain your feature, change, or fix:

   ```bash
   git checkout -b <topic-branch-name>
   ```

4. Commit your changes in logical chunks. Please adhere to these [git commit
   message guidelines](http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html)
   or your code is unlikely to be merged into the main project. Use Git's
   [interactive rebase](https://help.github.com/articles/interactive-rebase)
   feature to tidy up your commits before making them public.

4a. Create tests.

4b. Create or update the example code that demonstrates the functionality of this change to the code.

5. Locally merge (or rebase) the upstream development branch into your topic branch:

   ```bash
   git pull [--rebase] upstream master
   ```

6. Push your topic branch up to your fork:

   ```bash
   git push origin <topic-branch-name>
   ```

7. [Open a Pull Request](https://help.github.com/articles/using-pull-requests/)
    with a clear title and description against the `master` branch. All tests must be passing before we will review the PR.

If you have any additional questions, please feel free to [email](mailto:dx@sendgrid.com) us or create an issue in this repo.

<a name="code-reviews"></a>
## Code Reviews
If you can, please look at open PRs and review them. Give feedback and help us merge these PRs much faster! If you don't know how, Github has some great [information on how to review a Pull Request](https://help.github.com/articles/about-pull-request-reviews/).
