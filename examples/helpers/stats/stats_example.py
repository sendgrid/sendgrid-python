import json
import os
from sendgrid.helpers.stats import *
from sendgrid import *

# NOTE: you will need move this file to the root directory of this project to execute properly.

# Assumes you set your environment variable:
# https://github.com/sendgrid/sendgrid-python/blob/master/TROUBLESHOOTING.md#environment-variables-and-your-sendgrid-api-key
sg = SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))


def build_global_stats():
    global_stats = Stats()
    global_stats.start_date = '2017-10-14'
    global_stats.end_date = '2017-10-20'
    global_stats.aggregated_by = 'day'
    return global_stats.get()


def build_category_stats():
    category_stats = CategoryStats()
    category_stats.start_date = '2017-10-15'
    category_stats.add_category(Category("foo"))
    category_stats.add_category(Category("bar"))
    return category_stats.get()


def build_category_stats_sums():
    category_stats = CategoryStats()
    category_stats.start_date = '2017-10-15'
    category_stats.limit = 5
    category_stats.offset = 1
    return category_stats.get()


def get_global_stats():
    stats_params = build_global_stats()
    response = sg.client.stats.get(query_params=stats_params)
    print(response.status_code)
    print(response.headers)
    print(json.dumps(json.loads(response.body), indent=4, sort_keys=True))


def get_category_stats():
    stats_params = build_category_stats()
    response = sg.client.categories.stats.get(query_params=stats_params)
    print(response.status_code)
    print(response.headers)
    print(json.dumps(json.loads(response.body), indent=4, sort_keys=True))


def get_category_stats_sums():
    stats_params = build_category_stats_sums()
    response = sg.client.categories.stats.sums.get(query_params=stats_params)
    print(response.status_code)
    print(response.headers)
    print(json.dumps(json.loads(response.body), indent=4, sort_keys=True))

get_global_stats()
get_category_stats()
get_category_stats_sums()
