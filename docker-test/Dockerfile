FROM python:3.6-alpine

ENV OAI_SPEC_URL="https://raw.githubusercontent.com/sendgrid/sendgrid-oai/master/oai_stoplight.json"
ENV SENDGRID_API_KEY $SENDGRID_API_KEY

RUN apk add --no-cache curl
RUN apk add --update bash && rm -rf /var/cache/apk/*

# install Prism
WORKDIR /root
ADD https://raw.githubusercontent.com/stoplightio/prism/master/install.sh install.sh
RUN chmod +x ./install.sh && sync && \
    ./install.sh && \
    rm ./install.sh

# set up default sendgrid env
WORKDIR /root

RUN mkdir sendgrid-python
COPY entrypoint.sh entrypoint.sh
RUN chmod +x entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]
CMD ["--mock"]
