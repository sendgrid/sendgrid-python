Use Docker to easily try out or contribute to the sendgrid-python library. 

This Docker image contains:
 - Python 3.6
 - A running instance of [Stoplight.io's Prism](https://stoplight.io/platform/prism/), which lets you try out the SendGrid API without actually sending email
 - A mirrored copy of sendgrid-php so that you may develop locally and then run the tests within the Docker container.

# Table of Contents

* [Quick Start](#quick-start)
* [Testing](#testing)
* [Contributing](#contributing)

<a name="quick-start"></a>
# Quick Start

1. Clone the sendgrid-python repo
  - `git clone https://github.com/sendgrid/sendgrid-python.git`
  - `cd sendgrid-python`
  - `python setup.py install`
2. [Install Docker](https://docs.docker.com/install/)
3. [Setup local environment variable SENDGRID_API_KEY](https://github.com/sendgrid/sendgrid-php#setup-environment-variables)
4. Build Docker image, run Docker container, login to the Docker container
  - `docker image build --tag="sendgrid/python3.6" ./docker-test`
  - `docker run -itd --name="sendgrid_python3.6" -v $(pwd):/root/sendgrid-python sendgrid/python3.6 /bin/bash`
5. Run the tests within the Docker container
  - `sudo docker exec -it sendgrid_python3.6 /bin/bash -c 'cd sendgrid-python; python3.6 -m unittest discover -v; exec "${SHELL:-sh}"'`

Now you can continue development locally, and run `python3.6 -m unittest discover -v` inside of the container to test.

To clean up the container: `docker stop sendgrid_python3.6 && docker rm sendgrid_python3.6`.

Happy Hacking! 

<a name="testing"></a>
# For Testing the Library (Kick the Tires)

- After step 5 in the QuickStart, within the Docker container: 
  - `cd ../`
  - `python sendmail.py` 

<a name="contributing"></a>
# For Contributors

- Develop per usual locally, but before pushing up to GitHub, you can run the tests locally in the Docker container per step 5 of the quickstart.
- To run all the tests: `python3.6 -m unittest discover -v`
- To run an individual test: `python3.6 -m unittest [Filename].[Class].[TestName]`
