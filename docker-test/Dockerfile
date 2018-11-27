FROM python:3.6-alpine

WORKDIR /root

ENV OAI_SPEC_URL="https://raw.githubusercontent.com/sendgrid/sendgrid-oai/master/oai_stoplight.json"
ENV SENDGRID_API_KEY $SENDGRID_API_KEY

RUN apk add --update --no-cache bash curl

# Install Prism
ADD prism.sh install.sh
RUN sync && bash install.sh

# Set up default SendGrid env
RUN mkdir sendgrid-python
COPY entrypoint.sh entrypoint.sh
RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]
CMD ["--mock"]
