import json
import pytest

from .unassigned import unassigned


def test_unassigned_ip():

    ret_json = '''[ {
        "ip": "167.89.21.3",
        "pools": [
          "pool1",
          "pool2"
        ],
        "whitelabeled": false,
        "start_date": 1409616000,
        "subusers": [
          "tim@sendgrid.net"
        ],
        "warmup": false,
        "assigned_at": 1482883200
      },
      {
        "ip": "192.168.1.1",
        "pools": [
          "pool1",
          "pool2"
        ],
        "whitelabeled": false,
        "start_date": 1409616000,
        "subusers": [
          "tim@sendgrid.net"
        ],
        "warmup": false,
        "assigned_at": 1482883200
      },
      {
        "ip": "208.115.214.22",
        "pools": [],
        "whitelabeled": true,
        "rdns": "o1.email.burgermail.com",
        "start_date": 1409616000,
        "subusers": [],
        "warmup": false,
        "assigned_at": 1482883200
      },
      {
        "ip": "208.115.214.23",
        "pools": [],
        "whitelabeled": true,
        "rdns": "o1.email.burgermail.com",
        "start_date": 1409616000,
        "subusers": [],
        "warmup": false,
        "assigned_at": 1482883200

      } ]
      '''

    def get_all_ip():
        ret_val = json.loads(ret_json)
        return ret_val

    data = {"208.115.214.23", "208.115.214.22"}

    as_json = True
    calculated = unassigned(get_all_ip(), as_json=as_json)
    calculated = json.loads(calculated)

    for item in calculated:
        assert item["ip"] in data

    as_json = False
    calculated = unassigned(get_all_ip(), as_json=as_json)

    for item in calculated:
        assert item["ip"] in data

    calculated = unassigned(dict(), as_json=as_json)
    assert calculated == []
