FROM ubuntu:xenial
ENV PYTHON_VERSIONS='python2.6 python2.7 python3.4 python3.5 python3.6' \
    OAI_SPEC_URL="https://raw.githubusercontent.com/sendgrid/sendgrid-oai/master/oai_stoplight.json"

ARG SENDGRID-PYTHON_VERSION
ARG BRANCH_HTTP_CLIENT

# install testing versions of python, including old versions, from deadsnakes
RUN set -x \
    && apt-get update \
    && apt-get install -y --no-install-recommends software-properties-common \
    && apt-add-repository -y ppa:fkrull/deadsnakes \
    && apt-get update \
    && apt-get install -y --no-install-recommends $PYTHON_VERSIONS \
        git \
        curl \
    && apt-get purge -y --auto-remove software-properties-common \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /root

# install Prism
ADD https://raw.githubusercontent.com/stoplightio/prism/master/install.sh install.sh
RUN chmod +x ./install.sh && sync && \
    ./install.sh && \
    rm ./install.sh

# install pip, tox
ADD https://bootstrap.pypa.io/get-pip.py get-pip.py
RUN python2.7 get-pip.py && \
    python3.6 get-pip.py && \
    pip install tox && \
    rm get-pip.py

#install pyyaml, six, werkzeug
RUN python3.6 -m pip install pyyaml
RUN python3.6 -m pip install six
RUN python3.6 -m pip install werkzeug
RUN python3.6 -m pip install flask

# set up default sendgrid env
WORKDIR /root/sources
RUN git clone https://github.com/sendgrid/sendgrid-python.git --branch $SENDGRID-PYTHON_VERSION && \
    git clone https://github.com/sendgrid/python-http-client.git --branch $HTTP-CLIENT_VERSION
WORKDIR /root
RUN ln -s /root/sources/sendgrid-python/sendgrid && \
    ln -s /root/sources/python-http-client/python_http_client

COPY entrypoint.sh entrypoint.sh
RUN chmod +x entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]
CMD ["--mock"]
