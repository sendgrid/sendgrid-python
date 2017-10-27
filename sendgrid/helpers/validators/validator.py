import re

try:
    from exceptions import exception
except ImportError:
    # Python 3+, Travis
    from sendgrid.helpers.exceptions import exception


#Default Regex to find SendGrid API key in format: `SG.[a-zA-Z0-9_].[a-zA-Z0-9-]`
sendgrid_api_regex_string = 'SG\.[0-9a-zA-Z]+\.[0-9a-zA-Z]+'


def validate_for_api_key(request_body, 
                         regex_strings=[sendgrid_api_regex_string]):
    """Given the JSON dict that will be sent to SendGrid's API, check the content
            for SendGrid API keys and if found, throw an exception

        Args:
            request_body (:obj:`dict`): message parameter that's an argument to: mail.send.post()
            regex_strings (list<str>): list of regex strings that will be turned into patterns

        Raises:
            APIKeyIncludedException: If message_text matches a regex_string
    """

    message_texts = list()
    regex_patterns = set()

    #Compile the regex strings into patterns, add them to our set
    if regex_strings is not None:
        for regex_string in regex_strings:
            regex_patterns.add(re.compile(regex_string))


    #In-case we're given a string
    if isinstance(request_body, str):
        message_texts.append(request_body)

    #If we're given the `request_body` dictionary, extract the message_text
    elif isinstance(request_body, dict):
        if "content" in request_body:
            contents = request_body["content"]

            for content in contents:
                if "value" in content and "type" in content:
                    if content["type"] == "text/html" or isinstance(content["value"], str):
                        message_texts.append(content["value"])


    for regex_pattern in regex_patterns:
        for message_text in message_texts:
            if regex_pattern.match(message_text) is not None:
                raise APIKeyIncludedException()


