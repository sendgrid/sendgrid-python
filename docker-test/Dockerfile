FROM python:3.6-alpine

WORKDIR /root

ENV OAI_SPEC_URL="https://raw.githubusercontent.com/sendgrid/sendgrid-oai/master/oai_stoplight.json"
ENV SENDGRID_API_KEY $SENDGRID_API_KEY

RUN apk add --update --no-cache bash curl

# install Prism
WORKDIR /root
ADD https://raw.githubusercontent.com/stoplightio/prism/2.x/install.sh install.sh
RUN sync && bash install.sh

# set up default sendgrid env
RUN mkdir sendgrid-python
COPY entrypoint.sh entrypoint.sh

ENTRYPOINT ["entrypoint.sh"]
CMD ["--mock"]
