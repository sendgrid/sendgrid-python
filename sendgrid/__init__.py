try:
  from .sendgrid import SendGridClient
  from .message import Mail
except Exception as e:
  from sendgrid import SendGridClient
  from message import Mail