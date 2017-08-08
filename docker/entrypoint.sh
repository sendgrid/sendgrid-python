#! /bin/bash
clear

# check for + link mounted libraries:
if [ -d /mnt/sendgrid-python ]
then
	rm /root/sendgrid
	ln -s /mnt/sendgrid-python/sendgrid
	echo "Linked mounted sendgrid-python's code to /root/sendgrid"
fi
if [ -d /mnt/python_http_client ]
then
	rm /root/python_http_client
	ln -s /mnt/python-http-client/python_http_client
	echo "Linked mounted python-http-client's code to /root/python_http_client"
fi

SENDGRID_PYTHON_VERSION=$(python2.7 -c 'import sendgrid; print(sendgrid.__version__)')
echo "Welcome to sendgrid-python docker v${SENDGRID_PYTHON_VERSION}."
echo

if [ "$1" != "--no-mock" ]
then
	echo "Starting Prism in mock mode. Calls made to Prism will not actually send emails."
	echo "Disable this by running this container with --no-mock."
	prism run --mock --spec $OAI_SPEC_URL 2> /dev/null &
else
	echo "Starting Prism in live (--no-mock) mode. Calls made to Prism will send emails."
	prism run --spec $OAI_SPEC_URL 2> /dev/null  &
fi
echo "To use Prism, make API calls to localhost:4010. For example,"
echo "    sg = sendgrid.SendGridAPIClient("
echo "        host='http://localhost:4010/',"
echo "        api_key=os.environ.get('SENDGRID_API_KEY_CAMPAIGNS'))"
echo "To stop Prism, run \"kill $!\" from the shell."

echo
echo "Starting Python. Type \"import sendgrid\" to get started; return to shell with exit()."
echo

python2.7

echo
echo "To get back into Python, run one of the installed versions:"
echo "    $PYTHON_VERSIONS"
echo "To test sendgrid-python, \"cd sendgrid\" and run \"tox\"."
echo
exec $SHELL