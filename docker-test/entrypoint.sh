#! /bin/bash
clear

if [ "$1" != "--no-mock" ]
then
	echo "Starting Prism in mock mode. Calls made to Prism will not actually send emails."
	echo "Disable this by running this container with --no-mock."
	/prism/bin/prism run --mock --spec $OAI_SPEC_URL 2> /dev/null &
else
	echo "Starting Prism in live (--no-mock) mode. Calls made to Prism will send emails."
	/prism/bin/prism run --spec $OAI_SPEC_URL 2> /dev/null  &
fi

cd sendgrid-python
python3.6 setup.py install
pip install pyyaml six werkzeug flask python_http_client
exec $SHELL
