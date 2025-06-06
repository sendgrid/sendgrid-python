```mermaid
graph LR
    IP_Unassigned_Processor["IP Unassigned Processor"]
    Return_Data_Formatter["Return Data Formatter"]
    IP_Unassigned_Processor -- "invokes" --> Return_Data_Formatter
```
[![CodeBoarding](https://img.shields.io/badge/Generated%20by-CodeBoarding-9cf?style=flat-square)](https://github.com/CodeBoarding/GeneratedOnBoardings)[![Demo](https://img.shields.io/badge/Try%20our-Demo-blue?style=flat-square)](https://www.codeboarding.org/demo)[![Contact](https://img.shields.io/badge/Contact%20us%20-%20contact@codeboarding.org-lightgrey?style=flat-square)](mailto:contact@codeboarding.org)

## Component Details

This subsystem is responsible for identifying and formatting unassigned IP addresses from a given dataset. The main flow involves processing IP data to find IPs without subusers, and then formatting these unassigned IPs into a structured output, either as a list of dictionaries or a JSON object.

### IP Unassigned Processor
This component is responsible for processing a list of IP addresses and identifying those that have no subusers assigned. It takes raw IP data as input and prepares a set of unassigned IPs for further formatting.


**Related Classes/Methods**:

- <a href="https://github.com/sendgrid/sendgrid-python/blob/master/sendgrid/helpers/endpoints/ip/unassigned.py#L18-L59" target="_blank" rel="noopener noreferrer">`sendgrid.helpers.endpoints.ip.unassigned:unassigned` (18:59)</a>


### Return Data Formatter
This component handles the formatting of a set of IP addresses into a structured output, either as a list of dictionaries or a JSON object. It serves as a utility to standardize the return type for IP-related data.


**Related Classes/Methods**:

- <a href="https://github.com/sendgrid/sendgrid-python/blob/master/sendgrid/helpers/endpoints/ip/unassigned.py#L4-L15" target="_blank" rel="noopener noreferrer">`sendgrid.helpers.endpoints.ip.unassigned:format_ret` (4:15)</a>




### [FAQ](https://github.com/CodeBoarding/GeneratedOnBoardings/tree/main?tab=readme-ov-file#faq)