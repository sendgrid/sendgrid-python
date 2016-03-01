import sendgrid
import json
from sendgrid.client import SendGridAPIClient
from sendgrid.version import __version__
try:
    import unittest2 as unittest
except ImportError:
    import unittest
import os

if os.environ.get('TRAVIS'):
    host = os.environ.get('MOCK_HOST')
else:
    host = "http://localhost:4010"

class UnitTests(unittest.TestCase):
    def setUp(self):
        self.host = host
        self.path = '{0}{1}'.format(os.path.abspath(os.path.dirname(__file__)), '/..')
        self.sg = sendgrid.SendGridAPIClient(host=host, path=self.path)

    def test_apikey_init(self):
        self.assertEqual(self.sg.apikey, os.environ.get('SENDGRID_API_KEY'))

    def test_useragent(self):
        useragent = '{0}{1}{2}'.format('sendgrid/', __version__, ';python_v3')
        self.assertEqual(self.sg.useragent, useragent)

    def test_host(self):
        self.assertEqual(self.sg.host, self.host)

    def test_api_key_post(self):
        data = {'sample': 'data'}
        headers = {'X-Mock': 201}
        response = self.sg.client.api_key.post(request_body=data, request_headers=headers)
        self.assertEqual(response.status_code, 201)

    def test_api_keys_get(self):
        headers = {'X-Mock': 200}
        response = self.sg.client.api_keys.get(request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_api_keys__api_key_id__put(self):
        data = {'sample': 'data'}
        api_key_id = "test_url_param"
        headers = {'X-Mock': 200}
        response = self.sg.client.api_keys._(api_key_id).put(request_body=data, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_api_keys__api_key_id__patch(self):
        data = {'sample': 'data'}
        api_key_id = "test_url_param"
        headers = {'X-Mock': 200}
        response = self.sg.client.api_keys._(api_key_id).patch(request_body=data, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_api_keys__api_key_id__get(self):
        api_key_id = "test_url_param"
        headers = {'X-Mock': 200}
        response = self.sg.client.api_keys._(api_key_id).get(request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_api_keys__api_key_id__delete(self):
        api_key_id = "test_url_param"
        headers = {'X-Mock': 204}
        response = self.sg.client.api_keys._(api_key_id).delete(request_headers=headers)
        self.assertEqual(response.status_code, 204)

    def test_asm_groups_post(self):
        data = {'sample': 'data'}
        headers = {'X-Mock': 200}
        response = self.sg.client.asm.groups.post(request_body=data, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_asm_groups_get(self):
        headers = {'X-Mock': 200}
        response = self.sg.client.asm.groups.get(request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_asm_groups__group_id__patch(self):
        data = {'sample': 'data'}
        group_id = "test_url_param"
        headers = {'X-Mock': 201}
        response = self.sg.client.asm.groups._(group_id).patch(request_body=data, request_headers=headers)
        self.assertEqual(response.status_code, 201)

    def test_asm_groups__group_id__get(self):
        group_id = "test_url_param"
        headers = {'X-Mock': 200}
        response = self.sg.client.asm.groups._(group_id).get(request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_asm_groups__group_id__delete(self):
        group_id = "test_url_param"
        headers = {'X-Mock': 204}
        response = self.sg.client.asm.groups._(group_id).delete(request_headers=headers)
        self.assertEqual(response.status_code, 204)

    def test_asm_groups__group_id__suppressions_post(self):
        data = {'sample': 'data'}
        group_id = "test_url_param"
        headers = {'X-Mock': 201}
        response = self.sg.client.asm.groups._(group_id).suppressions.post(request_body=data, request_headers=headers)
        self.assertEqual(response.status_code, 201)

    def test_asm_groups__group_id__suppressions_get(self):
        group_id = "test_url_param"
        headers = {'X-Mock': 200}
        response = self.sg.client.asm.groups._(group_id).suppressions.get(request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_asm_groups__group_id__suppressions__email__delete(self):
        group_id = "test_url_param"
        email = "test_url_param"
        headers = {'X-Mock': 204}
        response = self.sg.client.asm.groups._(group_id).suppressions._(email).delete(request_headers=headers)
        self.assertEqual(response.status_code, 204)

    def test_asm_suppressions_global_post(self):
        data = {'sample': 'data'}
        headers = {'X-Mock': 201}
        response = self.sg.client.asm.suppressions._("global").post(request_body=data, request_headers=headers)
        self.assertEqual(response.status_code, 201)

    def test_asm_suppressions_global__email_address__get(self):
        email_address = "test_url_param"
        headers = {'X-Mock': 200}
        response = self.sg.client.asm.suppressions._("global")._(email_address).get(request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_asm_suppressions_global__email__get(self):
        email = "test_url_param"
        headers = {'X-Mock': 200}
        response = self.sg.client.asm.suppressions._("global")._(email).get(request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_asm_suppressions_global__email__delete(self):
        email = "test_url_param"
        headers = {'X-Mock': 204}
        response = self.sg.client.asm.suppressions._("global")._(email).delete(request_headers=headers)
        self.assertEqual(response.status_code, 204)

    def test_browsers_stats_get(self):
        params = {'end_date': 'test_string', 'aggregated_by': 'test_string', 'browsers': 'test_string', 'limit': 'test_string', 'offset': 'test_string', 'start_date': 'test_string'}
        headers = {'X-Mock': 200}
        response = self.sg.client.browsers.stats.get(query_params=params, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_campaigns_post(self):
        data = {'sample': 'data'}
        headers = {'X-Mock': 201}
        response = self.sg.client.campaigns.post(request_body=data, request_headers=headers)
        self.assertEqual(response.status_code, 201)

    def test_campaigns_get(self):
        params = {'limit': 0, 'offset': 0}
        headers = {'X-Mock': 200}
        response = self.sg.client.campaigns.get(query_params=params, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_campaigns__campaign_id__patch(self):
        data = {'sample': 'data'}
        campaign_id = "test_url_param"
        headers = {'X-Mock': 200}
        response = self.sg.client.campaigns._(campaign_id).patch(request_body=data, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_campaigns__campaign_id__get(self):
        campaign_id = "test_url_param"
        headers = {'X-Mock': 200}
        response = self.sg.client.campaigns._(campaign_id).get(request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_campaigns__campaign_id__delete(self):
        campaign_id = "test_url_param"
        headers = {'X-Mock': 204}
        response = self.sg.client.campaigns._(campaign_id).delete(request_headers=headers)
        self.assertEqual(response.status_code, 204)

    def test_campaigns__campaign_id__schedules_patch(self):
        data = {'sample': 'data'}
        campaign_id = "test_url_param"
        headers = {'X-Mock': 200}
        response = self.sg.client.campaigns._(campaign_id).schedules.patch(request_body=data, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_campaigns__campaign_id__schedules_post(self):
        data = {'sample': 'data'}
        campaign_id = "test_url_param"
        headers = {'X-Mock': 201}
        response = self.sg.client.campaigns._(campaign_id).schedules.post(request_body=data, request_headers=headers)
        self.assertEqual(response.status_code, 201)

    def test_campaigns__campaign_id__schedules_get(self):
        campaign_id = "test_url_param"
        headers = {'X-Mock': 200}
        response = self.sg.client.campaigns._(campaign_id).schedules.get(request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_campaigns__campaign_id__schedules_delete(self):
        campaign_id = "test_url_param"
        headers = {'X-Mock': 204}
        response = self.sg.client.campaigns._(campaign_id).schedules.delete(request_headers=headers)
        self.assertEqual(response.status_code, 204)

    def test_campaigns__campaign_id__schedules_now_post(self):
        data = {'sample': 'data'}
        campaign_id = "test_url_param"
        headers = {'X-Mock': 201}
        response = self.sg.client.campaigns._(campaign_id).schedules.now.post(request_body=data, request_headers=headers)
        self.assertEqual(response.status_code, 201)

    def test_campaigns__campaign_id__schedules_test_post(self):
        data = {'sample': 'data'}
        campaign_id = "test_url_param"
        headers = {'X-Mock': 204}
        response = self.sg.client.campaigns._(campaign_id).schedules.test.post(request_body=data, request_headers=headers)
        self.assertEqual(response.status_code, 204)

    def test_categories_get(self):
        params = {'category': 'test_string', 'sort_by': 'test_string', 'limit': 0, 'order': 'test_string', 'offset': 0}
        headers = {'X-Mock': 200}
        response = self.sg.client.categories.get(query_params=params, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_categories_stats_get(self):
        params = {'end_date': 'test_string', 'aggregated_by': 'test_string', 'limit': 0, 'offset': 0, 'start_date': 'test_string', 'categories': 'test_string'}
        headers = {'X-Mock': 200}
        response = self.sg.client.categories.stats.get(query_params=params, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_categories_stats_sums_get(self):
        params = {'end_date': 'test_string', 'aggregated_by': 'test_string', 'limit': 0, 'sort_by_metric': 'test_string', 'offset': 0, 'start_date': 'test_string', 'sort_by_direction': 'test_string'}
        headers = {'X-Mock': 200}
        response = self.sg.client.categories.stats.sums.get(query_params=params, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_clients_stats_get(self):
        params = {'aggregated_by': 'test_string', 'start_date': 'test_string', 'end_date': 'test_string'}
        headers = {'X-Mock': 200}
        response = self.sg.client.clients.stats.get(query_params=params, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_clients__client_type__stats_get(self):
        params = {'aggregated_by': 'test_string', 'start_date': 'test_string', 'end_date': 'test_string'}
        client_type = "test_url_param"
        headers = {'X-Mock': 200}
        response = self.sg.client.clients._(client_type).stats.get(query_params=params, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_contactdb_custom_fields_post(self):
        data = {'sample': 'data'}
        headers = {'X-Mock': 201}
        response = self.sg.client.contactdb.custom_fields.post(request_body=data, request_headers=headers)
        self.assertEqual(response.status_code, 201)

    def test_contactdb_custom_fields_get(self):
        headers = {'X-Mock': 200}
        response = self.sg.client.contactdb.custom_fields.get(request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_contactdb_custom_fields__custom_field_id__get(self):
        params = {'custom_field_id': 0}
        custom_field_id = "test_url_param"
        headers = {'X-Mock': 200}
        response = self.sg.client.contactdb.custom_fields._(custom_field_id).get(query_params=params, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_contactdb_custom_fields__custom_field_id__delete(self):
        custom_field_id = "test_url_param"
        headers = {'X-Mock': 202}
        response = self.sg.client.contactdb.custom_fields._(custom_field_id).delete(request_headers=headers)
        self.assertEqual(response.status_code, 202)

    def test_contactdb_lists_post(self):
        data = {'sample': 'data'}
        headers = {'X-Mock': 201}
        response = self.sg.client.contactdb.lists.post(request_body=data, request_headers=headers)
        self.assertEqual(response.status_code, 201)

    def test_contactdb_lists_get(self):
        headers = {'X-Mock': 200}
        response = self.sg.client.contactdb.lists.get(request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_contactdb_lists_delete(self):
        headers = {'X-Mock': 204}
        response = self.sg.client.contactdb.lists.delete(request_headers=headers)
        self.assertEqual(response.status_code, 204)

    def test_contactdb_lists__list_id__patch(self):
        data = {'sample': 'data'}
        params = {'list_id': 0}
        list_id = "test_url_param"
        headers = {'X-Mock': 200}
        response = self.sg.client.contactdb.lists._(list_id).patch(request_body=data, query_params=params, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_contactdb_lists__list_id__get(self):
        params = {'list_id': 0}
        list_id = "test_url_param"
        headers = {'X-Mock': 200}
        response = self.sg.client.contactdb.lists._(list_id).get(query_params=params, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_contactdb_lists__list_id__delete(self):
        params = {'delete_contacts': 0}
        list_id = "test_url_param"
        headers = {'X-Mock': 202}
        response = self.sg.client.contactdb.lists._(list_id).delete(query_params=params, request_headers=headers)
        self.assertEqual(response.status_code, 202)

    def test_contactdb_lists__list_id__recipients_post(self):
        data = {'sample': 'data'}
        params = {'list_id': 0}
        list_id = "test_url_param"
        headers = {'X-Mock': 201}
        response = self.sg.client.contactdb.lists._(list_id).recipients.post(request_body=data, query_params=params, request_headers=headers)
        self.assertEqual(response.status_code, 201)

    def test_contactdb_lists__list_id__recipients_get(self):
        params = {'page': 0, 'page_size': 0, 'list_id': 0}
        list_id = "test_url_param"
        headers = {'X-Mock': 200}
        response = self.sg.client.contactdb.lists._(list_id).recipients.get(query_params=params, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_contactdb_lists__list_id__recipients__recipient_id__post(self):
        data = {'sample': 'data'}
        params = {'recipient_id': 'test_string', 'list_id': 0}
        list_id = "test_url_param"
        recipient_id = "test_url_param"
        headers = {'X-Mock': 201}
        response = self.sg.client.contactdb.lists._(list_id).recipients._(recipient_id).post(request_body=data, query_params=params, request_headers=headers)
        self.assertEqual(response.status_code, 201)

    def test_contactdb_lists__list_id__recipients__recipient_id__delete(self):
        params = {'recipient_id': 0, 'list_id': 0}
        list_id = "test_url_param"
        recipient_id = "test_url_param"
        headers = {'X-Mock': 204}
        response = self.sg.client.contactdb.lists._(list_id).recipients._(recipient_id).delete(query_params=params, request_headers=headers)
        self.assertEqual(response.status_code, 204)

    def test_contactdb_recipients_patch(self):
        data = {'sample': 'data'}
        headers = {'X-Mock': 201}
        response = self.sg.client.contactdb.recipients.patch(request_body=data, request_headers=headers)
        self.assertEqual(response.status_code, 201)

    def test_contactdb_recipients_post(self):
        data = {'sample': 'data'}
        headers = {'X-Mock': 201}
        response = self.sg.client.contactdb.recipients.post(request_body=data, request_headers=headers)
        self.assertEqual(response.status_code, 201)

    def test_contactdb_recipients_get(self):
        params = {'page': 0, 'page_size': 0}
        headers = {'X-Mock': 200}
        response = self.sg.client.contactdb.recipients.get(query_params=params, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_contactdb_recipients_delete(self):
        headers = {'X-Mock': 200}
        response = self.sg.client.contactdb.recipients.delete(request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_contactdb_recipients_billable_count_get(self):
        headers = {'X-Mock': 200}
        response = self.sg.client.contactdb.recipients.billable_count.get(request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_contactdb_recipients_count_get(self):
        headers = {'X-Mock': 200}
        response = self.sg.client.contactdb.recipients.count.get(request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_contactdb_recipients_search_get(self):
        params = {'{field_name}': 'test_string'}
        headers = {'X-Mock': 200}
        response = self.sg.client.contactdb.recipients.search.get(query_params=params, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_contactdb_recipients__recipient_id__get(self):
        params = {'recipient_id': 'test_string'}
        recipient_id = "test_url_param"
        headers = {'X-Mock': 200}
        response = self.sg.client.contactdb.recipients._(recipient_id).get(query_params=params, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_contactdb_recipients__recipient_id__delete(self):
        params = {'recipient_id': 'test_string'}
        recipient_id = "test_url_param"
        headers = {'X-Mock': 204}
        response = self.sg.client.contactdb.recipients._(recipient_id).delete(query_params=params, request_headers=headers)
        self.assertEqual(response.status_code, 204)

    def test_contactdb_recipients__recipient_id__lists_get(self):
        params = {'recipient_id': 'test_string'}
        recipient_id = "test_url_param"
        headers = {'X-Mock': 200}
        response = self.sg.client.contactdb.recipients._(recipient_id).lists.get(query_params=params, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_contactdb_reserved_fields_get(self):
        headers = {'X-Mock': 200}
        response = self.sg.client.contactdb.reserved_fields.get(request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_contactdb_segments_post(self):
        data = {'sample': 'data'}
        headers = {'X-Mock': 200}
        response = self.sg.client.contactdb.segments.post(request_body=data, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_contactdb_segments_get(self):
        headers = {'X-Mock': 200}
        response = self.sg.client.contactdb.segments.get(request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_contactdb_segments__segment_id__patch(self):
        data = {'sample': 'data'}
        params = {'segment_id': 'test_string'}
        segment_id = "test_url_param"
        headers = {'X-Mock': 200}
        response = self.sg.client.contactdb.segments._(segment_id).patch(request_body=data, query_params=params, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_contactdb_segments__segment_id__get(self):
        params = {'segment_id': 0}
        segment_id = "test_url_param"
        headers = {'X-Mock': 200}
        response = self.sg.client.contactdb.segments._(segment_id).get(query_params=params, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_contactdb_segments__segment_id__delete(self):
        params = {'delete_contacts': 0}
        segment_id = "test_url_param"
        headers = {'X-Mock': 204}
        response = self.sg.client.contactdb.segments._(segment_id).delete(query_params=params, request_headers=headers)
        self.assertEqual(response.status_code, 204)

    def test_contactdb_segments__segment_id__recipients_get(self):
        params = {'page': 0, 'page_size': 0}
        segment_id = "test_url_param"
        headers = {'X-Mock': 200}
        response = self.sg.client.contactdb.segments._(segment_id).recipients.get(query_params=params, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_devices_stats_get(self):
        params = {'aggregated_by': 'test_string', 'limit': 0, 'start_date': 'test_string', 'end_date': 'test_string', 'offset': 0}
        headers = {'X-Mock': 200}
        response = self.sg.client.devices.stats.get(query_params=params, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_geo_stats_get(self):
        params = {'end_date': 'test_string', 'country': 'test_string', 'aggregated_by': 'test_string', 'limit': 0, 'offset': 0, 'start_date': 'test_string'}
        headers = {'X-Mock': 200}
        response = self.sg.client.geo.stats.get(query_params=params, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_ips_get(self):
        params = {'subuser': 'test_string', 'ip': 'test_string', 'limit': 0, 'exclude_whitelabels': 0, 'offset': 0}
        headers = {'X-Mock': 200}
        response = self.sg.client.ips.get(query_params=params, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_ips_assigned_get(self):
        headers = {'X-Mock': 200}
        response = self.sg.client.ips.assigned.get(request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_ips_pools_post(self):
        data = {'sample': 'data'}
        headers = {'X-Mock': 200}
        response = self.sg.client.ips.pools.post(request_body=data, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_ips_pools_get(self):
        headers = {'X-Mock': 200}
        response = self.sg.client.ips.pools.get(request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_ips_pools__pool_name__put(self):
        data = {'sample': 'data'}
        pool_name = "test_url_param"
        headers = {'X-Mock': 200}
        response = self.sg.client.ips.pools._(pool_name).put(request_body=data, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_ips_pools__pool_name__get(self):
        pool_name = "test_url_param"
        headers = {'X-Mock': 200}
        response = self.sg.client.ips.pools._(pool_name).get(request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_ips_pools__pool_name__delete(self):
        pool_name = "test_url_param"
        headers = {'X-Mock': 204}
        response = self.sg.client.ips.pools._(pool_name).delete(request_headers=headers)
        self.assertEqual(response.status_code, 204)

    def test_ips_pools__pool_name__ips_post(self):
        data = {'sample': 'data'}
        pool_name = "test_url_param"
        headers = {'X-Mock': 201}
        response = self.sg.client.ips.pools._(pool_name).ips.post(request_body=data, request_headers=headers)
        self.assertEqual(response.status_code, 201)

    def test_ips_pools__pool_name__ips__ip__delete(self):
        pool_name = "test_url_param"
        ip = "test_url_param"
        headers = {'X-Mock': 204}
        response = self.sg.client.ips.pools._(pool_name).ips._(ip).delete(request_headers=headers)
        self.assertEqual(response.status_code, 204)

    def test_ips_warmup_post(self):
        data = {'sample': 'data'}
        headers = {'X-Mock': 200}
        response = self.sg.client.ips.warmup.post(request_body=data, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_ips_warmup_get(self):
        headers = {'X-Mock': 200}
        response = self.sg.client.ips.warmup.get(request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_ips_warmup__ip_address__get(self):
        ip_address = "test_url_param"
        headers = {'X-Mock': 200}
        response = self.sg.client.ips.warmup._(ip_address).get(request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_ips_warmup__ip_address__delete(self):
        ip_address = "test_url_param"
        headers = {'X-Mock': 204}
        response = self.sg.client.ips.warmup._(ip_address).delete(request_headers=headers)
        self.assertEqual(response.status_code, 204)

    def test_ips__ip_address__get(self):
        ip_address = "test_url_param"
        headers = {'X-Mock': 200}
        response = self.sg.client.ips._(ip_address).get(request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_mail_batch_post(self):
        data = {'sample': 'data'}
        headers = {'X-Mock': 201}
        response = self.sg.client.mail.batch.post(request_body=data, request_headers=headers)
        self.assertEqual(response.status_code, 201)

    def test_mail_batch__batch_id__get(self):
        batch_id = "test_url_param"
        headers = {'X-Mock': 200}
        response = self.sg.client.mail.batch._(batch_id).get(request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_mail_settings_get(self):
        params = {'limit': 0, 'offset': 0}
        headers = {'X-Mock': 200}
        response = self.sg.client.mail_settings.get(query_params=params, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_mail_settings_address_whitelist_patch(self):
        data = {'sample': 'data'}
        headers = {'X-Mock': 200}
        response = self.sg.client.mail_settings.address_whitelist.patch(request_body=data, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_mail_settings_address_whitelist_get(self):
        headers = {'X-Mock': 200}
        response = self.sg.client.mail_settings.address_whitelist.get(request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_mail_settings_bcc_patch(self):
        data = {'sample': 'data'}
        headers = {'X-Mock': 200}
        response = self.sg.client.mail_settings.bcc.patch(request_body=data, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_mail_settings_bcc_get(self):
        headers = {'X-Mock': 200}
        response = self.sg.client.mail_settings.bcc.get(request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_mail_settings_bounce_purge_patch(self):
        data = {'sample': 'data'}
        headers = {'X-Mock': 200}
        response = self.sg.client.mail_settings.bounce_purge.patch(request_body=data, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_mail_settings_bounce_purge_get(self):
        headers = {'X-Mock': 200}
        response = self.sg.client.mail_settings.bounce_purge.get(request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_mail_settings_footer_patch(self):
        data = {'sample': 'data'}
        headers = {'X-Mock': 200}
        response = self.sg.client.mail_settings.footer.patch(request_body=data, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_mail_settings_footer_get(self):
        headers = {'X-Mock': 200}
        response = self.sg.client.mail_settings.footer.get(request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_mail_settings_forward_bounce_patch(self):
        data = {'sample': 'data'}
        headers = {'X-Mock': 200}
        response = self.sg.client.mail_settings.forward_bounce.patch(request_body=data, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_mail_settings_forward_bounce_get(self):
        headers = {'X-Mock': 200}
        response = self.sg.client.mail_settings.forward_bounce.get(request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_mail_settings_forward_spam_patch(self):
        data = {'sample': 'data'}
        headers = {'X-Mock': 200}
        response = self.sg.client.mail_settings.forward_spam.patch(request_body=data, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_mail_settings_forward_spam_get(self):
        headers = {'X-Mock': 200}
        response = self.sg.client.mail_settings.forward_spam.get(request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_mail_settings_plain_content_patch(self):
        data = {'sample': 'data'}
        headers = {'X-Mock': 200}
        response = self.sg.client.mail_settings.plain_content.patch(request_body=data, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_mail_settings_plain_content_get(self):
        headers = {'X-Mock': 200}
        response = self.sg.client.mail_settings.plain_content.get(request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_mail_settings_spam_check_patch(self):
        data = {'sample': 'data'}
        headers = {'X-Mock': 200}
        response = self.sg.client.mail_settings.spam_check.patch(request_body=data, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_mail_settings_spam_check_get(self):
        headers = {'X-Mock': 200}
        response = self.sg.client.mail_settings.spam_check.get(request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_mail_settings_template_patch(self):
        data = {'sample': 'data'}
        headers = {'X-Mock': 200}
        response = self.sg.client.mail_settings.template.patch(request_body=data, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_mail_settings_template_get(self):
        headers = {'X-Mock': 200}
        response = self.sg.client.mail_settings.template.get(request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_mailbox_providers_stats_get(self):
        params = {'end_date': 'test_string', 'mailbox_providers': 'test_string', 'aggregated_by': 'test_string', 'limit': 0, 'offset': 0, 'start_date': 'test_string'}
        headers = {'X-Mock': 200}
        response = self.sg.client.mailbox_providers.stats.get(query_params=params, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_partner_settings_get(self):
        params = {'limit': 0, 'offset': 0}
        headers = {'X-Mock': 200}
        response = self.sg.client.partner_settings.get(query_params=params, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_partner_settings_new_relic_patch(self):
        data = {'sample': 'data'}
        headers = {'X-Mock': 200}
        response = self.sg.client.partner_settings.new_relic.patch(request_body=data, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_partner_settings_new_relic_get(self):
        headers = {'X-Mock': 200}
        response = self.sg.client.partner_settings.new_relic.get(request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_partner_settings_sendwithus_patch(self):
        data = {'sample': 'data'}
        headers = {'X-Mock': 200}
        response = self.sg.client.partner_settings.sendwithus.patch(request_body=data, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_partner_settings_sendwithus_get(self):
        headers = {'X-Mock': 200}
        response = self.sg.client.partner_settings.sendwithus.get(request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_scopes_get(self):
        headers = {'X-Mock': 200}
        response = self.sg.client.scopes.get(request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_stats_get(self):
        params = {'aggregated_by': 'test_string', 'limit': 0, 'start_date': 'test_string', 'end_date': 'test_string', 'offset': 0}
        headers = {'X-Mock': 200}
        response = self.sg.client.stats.get(query_params=params, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_subusers_post(self):
        data = {'sample': 'data'}
        headers = {'X-Mock': 200}
        response = self.sg.client.subusers.post(request_body=data, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_subusers_get(self):
        params = {'username': 'test_string', 'limit': 0, 'offset': 0}
        headers = {'X-Mock': 200}
        response = self.sg.client.subusers.get(query_params=params, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_subusers_reputations_get(self):
        params = {'usernames': 'test_string'}
        headers = {'X-Mock': 200}
        response = self.sg.client.subusers.reputations.get(query_params=params, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_subusers_stats_get(self):
        params = {'end_date': 'test_string', 'aggregated_by': 'test_string', 'limit': 0, 'offset': 0, 'start_date': 'test_string', 'subusers': 'test_string'}
        headers = {'X-Mock': 200}
        response = self.sg.client.subusers.stats.get(query_params=params, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_subusers_stats_sums_get(self):
        params = {'end_date': 'test_string', 'aggregated_by': 'test_string', 'limit': 0, 'sort_by_metric': 'test_string', 'offset': 0, 'start_date': 'test_string', 'sort_by_direction': 'test_string'}
        headers = {'X-Mock': 200}
        response = self.sg.client.subusers.stats.sums.get(query_params=params, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_subusers__subuser_name__patch(self):
        data = {'sample': 'data'}
        subuser_name = "test_url_param"
        headers = {'X-Mock': 204}
        response = self.sg.client.subusers._(subuser_name).patch(request_body=data, request_headers=headers)
        self.assertEqual(response.status_code, 204)

    def test_subusers__subuser_name__delete(self):
        subuser_name = "test_url_param"
        headers = {'X-Mock': 204}
        response = self.sg.client.subusers._(subuser_name).delete(request_headers=headers)
        self.assertEqual(response.status_code, 204)

    def test_subusers__subuser_name__ips_put(self):
        data = {'sample': 'data'}
        subuser_name = "test_url_param"
        headers = {'X-Mock': 200}
        response = self.sg.client.subusers._(subuser_name).ips.put(request_body=data, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_subusers__subuser_name__monitor_put(self):
        data = {'sample': 'data'}
        subuser_name = "test_url_param"
        headers = {'X-Mock': 200}
        response = self.sg.client.subusers._(subuser_name).monitor.put(request_body=data, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_subusers__subuser_name__monitor_post(self):
        data = {'sample': 'data'}
        subuser_name = "test_url_param"
        headers = {'X-Mock': 200}
        response = self.sg.client.subusers._(subuser_name).monitor.post(request_body=data, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_subusers__subuser_name__monitor_get(self):
        subuser_name = "test_url_param"
        headers = {'X-Mock': 200}
        response = self.sg.client.subusers._(subuser_name).monitor.get(request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_subusers__subuser_name__monitor_delete(self):
        subuser_name = "test_url_param"
        headers = {'X-Mock': 204}
        response = self.sg.client.subusers._(subuser_name).monitor.delete(request_headers=headers)
        self.assertEqual(response.status_code, 204)

    def test_suppression_bounces_get(self):
        params = {'start_time': 0, 'end_time': 0}
        headers = {'X-Mock': 200}
        response = self.sg.client.suppression.bounces.get(query_params=params, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_suppression_bounces_delete(self):
        headers = {'X-Mock': 204}
        response = self.sg.client.suppression.bounces.delete(request_headers=headers)
        self.assertEqual(response.status_code, 204)

    def test_suppression_bounces__email__get(self):
        email = "test_url_param"
        headers = {'X-Mock': 200}
        response = self.sg.client.suppression.bounces._(email).get(request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_suppression_bounces__email__delete(self):
        params = {'email_address': 'test_string'}
        email = "test_url_param"
        headers = {'X-Mock': 204}
        response = self.sg.client.suppression.bounces._(email).delete(query_params=params, request_headers=headers)
        self.assertEqual(response.status_code, 204)

    def test_templates_post(self):
        data = {'sample': 'data'}
        headers = {'X-Mock': 201}
        response = self.sg.client.templates.post(request_body=data, request_headers=headers)
        self.assertEqual(response.status_code, 201)

    def test_templates_get(self):
        headers = {'X-Mock': 200}
        response = self.sg.client.templates.get(request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_templates__template_id__patch(self):
        data = {'sample': 'data'}
        template_id = "test_url_param"
        headers = {'X-Mock': 200}
        response = self.sg.client.templates._(template_id).patch(request_body=data, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_templates__template_id__get(self):
        template_id = "test_url_param"
        headers = {'X-Mock': 200}
        response = self.sg.client.templates._(template_id).get(request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_templates__template_id__delete(self):
        template_id = "test_url_param"
        headers = {'X-Mock': 204}
        response = self.sg.client.templates._(template_id).delete(request_headers=headers)
        self.assertEqual(response.status_code, 204)

    def test_templates__template_id__versions_post(self):
        data = {'sample': 'data'}
        template_id = "test_url_param"
        headers = {'X-Mock': 201}
        response = self.sg.client.templates._(template_id).versions.post(request_body=data, request_headers=headers)
        self.assertEqual(response.status_code, 201)

    def test_templates__template_id__versions__version_id__patch(self):
        data = {'sample': 'data'}
        template_id = "test_url_param"
        version_id = "test_url_param"
        headers = {'X-Mock': 200}
        response = self.sg.client.templates._(template_id).versions._(version_id).patch(request_body=data, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_templates__template_id__versions__version_id__get(self):
        template_id = "test_url_param"
        version_id = "test_url_param"
        headers = {'X-Mock': 200}
        response = self.sg.client.templates._(template_id).versions._(version_id).get(request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_templates__template_id__versions__version_id__delete(self):
        template_id = "test_url_param"
        version_id = "test_url_param"
        headers = {'X-Mock': 204}
        response = self.sg.client.templates._(template_id).versions._(version_id).delete(request_headers=headers)
        self.assertEqual(response.status_code, 204)

    def test_templates__template_id__versions__version_id__activate_post(self):
        data = {'sample': 'data'}
        template_id = "test_url_param"
        version_id = "test_url_param"
        headers = {'X-Mock': 200}
        response = self.sg.client.templates._(template_id).versions._(version_id).activate.post(request_body=data, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_tracking_settings_get(self):
        params = {'limit': 0, 'offset': 0}
        headers = {'X-Mock': 200}
        response = self.sg.client.tracking_settings.get(query_params=params, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_tracking_settings_click_patch(self):
        data = {'sample': 'data'}
        headers = {'X-Mock': 200}
        response = self.sg.client.tracking_settings.click.patch(request_body=data, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_tracking_settings_click_get(self):
        headers = {'X-Mock': 200}
        response = self.sg.client.tracking_settings.click.get(request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_tracking_settings_google_analytics_patch(self):
        data = {'sample': 'data'}
        headers = {'X-Mock': 200}
        response = self.sg.client.tracking_settings.google_analytics.patch(request_body=data, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_tracking_settings_google_analytics_get(self):
        headers = {'X-Mock': 200}
        response = self.sg.client.tracking_settings.google_analytics.get(request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_tracking_settings_open_patch(self):
        data = {'sample': 'data'}
        headers = {'X-Mock': 200}
        response = self.sg.client.tracking_settings.open.patch(request_body=data, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_tracking_settings_open_get(self):
        headers = {'X-Mock': 200}
        response = self.sg.client.tracking_settings.open.get(request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_tracking_settings_subscription_patch(self):
        data = {'sample': 'data'}
        headers = {'X-Mock': 200}
        response = self.sg.client.tracking_settings.subscription.patch(request_body=data, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_tracking_settings_subscription_get(self):
        headers = {'X-Mock': 200}
        response = self.sg.client.tracking_settings.subscription.get(request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_user_account_get(self):
        headers = {'X-Mock': 200}
        response = self.sg.client.user.account.get(request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_user_profile_patch(self):
        data = {'sample': 'data'}
        headers = {'X-Mock': 200}
        response = self.sg.client.user.profile.patch(request_body=data, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_user_profile_get(self):
        headers = {'X-Mock': 200}
        response = self.sg.client.user.profile.get(request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_user_scheduled_sends_post(self):
        data = {'sample': 'data'}
        headers = {'X-Mock': 201}
        response = self.sg.client.user.scheduled_sends.post(request_body=data, request_headers=headers)
        self.assertEqual(response.status_code, 201)

    def test_user_scheduled_sends_get(self):
        headers = {'X-Mock': 200}
        response = self.sg.client.user.scheduled_sends.get(request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_user_scheduled_sends__batch_id__patch(self):
        data = {'sample': 'data'}
        batch_id = "test_url_param"
        headers = {'X-Mock': 204}
        response = self.sg.client.user.scheduled_sends._(batch_id).patch(request_body=data, request_headers=headers)
        self.assertEqual(response.status_code, 204)

    def test_user_scheduled_sends__batch_id__get(self):
        batch_id = "test_url_param"
        headers = {'X-Mock': 200}
        response = self.sg.client.user.scheduled_sends._(batch_id).get(request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_user_scheduled_sends__batch_id__delete(self):
        batch_id = "test_url_param"
        headers = {'X-Mock': 204}
        response = self.sg.client.user.scheduled_sends._(batch_id).delete(request_headers=headers)
        self.assertEqual(response.status_code, 204)

    def test_user_settings_enforced_tls_patch(self):
        data = {'sample': 'data'}
        headers = {'X-Mock': 200}
        response = self.sg.client.user.settings.enforced_tls.patch(request_body=data, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_user_settings_enforced_tls_get(self):
        headers = {'X-Mock': 200}
        response = self.sg.client.user.settings.enforced_tls.get(request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_user_webhooks_event_settings_patch(self):
        data = {'sample': 'data'}
        headers = {'X-Mock': 200}
        response = self.sg.client.user.webhooks.event.settings.patch(request_body=data, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_user_webhooks_event_settings_get(self):
        headers = {'X-Mock': 200}
        response = self.sg.client.user.webhooks.event.settings.get(request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_user_webhooks_event_test_post(self):
        data = {'sample': 'data'}
        headers = {'X-Mock': 204}
        response = self.sg.client.user.webhooks.event.test.post(request_body=data, request_headers=headers)
        self.assertEqual(response.status_code, 204)

    def test_user_webhooks_parse_settings_get(self):
        headers = {'X-Mock': 200}
        response = self.sg.client.user.webhooks.parse.settings.get(request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_user_webhooks_parse_stats_get(self):
        params = {'aggregated_by': 'test_string', 'limit': 'test_string', 'start_date': 'test_string', 'end_date': 'test_string', 'offset': 'test_string'}
        headers = {'X-Mock': 200}
        response = self.sg.client.user.webhooks.parse.stats.get(query_params=params, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_whitelabel_domains_post(self):
        data = {'sample': 'data'}
        headers = {'X-Mock': 201}
        response = self.sg.client.whitelabel.domains.post(request_body=data, request_headers=headers)
        self.assertEqual(response.status_code, 201)

    def test_whitelabel_domains_get(self):
        params = {'username': 'test_string', 'domain': 'test_string', 'exclude_subusers': 0, 'limit': 0, 'offset': 0}
        headers = {'X-Mock': 200}
        response = self.sg.client.whitelabel.domains.get(query_params=params, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_whitelabel_domains_default_get(self):
        headers = {'X-Mock': 200}
        response = self.sg.client.whitelabel.domains.default.get(request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_whitelabel_domains_subuser_get(self):
        headers = {'X-Mock': 200}
        response = self.sg.client.whitelabel.domains.subuser.get(request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_whitelabel_domains_subuser_delete(self):
        headers = {'X-Mock': 204}
        response = self.sg.client.whitelabel.domains.subuser.delete(request_headers=headers)
        self.assertEqual(response.status_code, 204)

    def test_whitelabel_domains__domain_id__patch(self):
        data = {'sample': 'data'}
        domain_id = "test_url_param"
        headers = {'X-Mock': 200}
        response = self.sg.client.whitelabel.domains._(domain_id).patch(request_body=data, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_whitelabel_domains__domain_id__get(self):
        domain_id = "test_url_param"
        headers = {'X-Mock': 200}
        response = self.sg.client.whitelabel.domains._(domain_id).get(request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_whitelabel_domains__domain_id__delete(self):
        domain_id = "test_url_param"
        headers = {'X-Mock': 204}
        response = self.sg.client.whitelabel.domains._(domain_id).delete(request_headers=headers)
        self.assertEqual(response.status_code, 204)

    def test_whitelabel_domains__domain_id__subuser_post(self):
        data = {'sample': 'data'}
        domain_id = "test_url_param"
        headers = {'X-Mock': 201}
        response = self.sg.client.whitelabel.domains._(domain_id).subuser.post(request_body=data, request_headers=headers)
        self.assertEqual(response.status_code, 201)

    def test_whitelabel_domains__id__ips_post(self):
        data = {'sample': 'data'}
        id = "test_url_param"
        headers = {'X-Mock': 200}
        response = self.sg.client.whitelabel.domains._(id).ips.post(request_body=data, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_whitelabel_domains__id__ips__ip__delete(self):
        id = "test_url_param"
        ip = "test_url_param"
        headers = {'X-Mock': 200}
        response = self.sg.client.whitelabel.domains._(id).ips._(ip).delete(request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_whitelabel_domains__id__validate_post(self):
        data = {'sample': 'data'}
        id = "test_url_param"
        headers = {'X-Mock': 200}
        response = self.sg.client.whitelabel.domains._(id).validate.post(request_body=data, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_whitelabel_ips_post(self):
        data = {'sample': 'data'}
        headers = {'X-Mock': 201}
        response = self.sg.client.whitelabel.ips.post(request_body=data, request_headers=headers)
        self.assertEqual(response.status_code, 201)

    def test_whitelabel_ips_get(self):
        params = {'ip': 'test_string', 'limit': 0, 'offset': 0}
        headers = {'X-Mock': 200}
        response = self.sg.client.whitelabel.ips.get(query_params=params, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_whitelabel_ips__id__get(self):
        id = "test_url_param"
        headers = {'X-Mock': 200}
        response = self.sg.client.whitelabel.ips._(id).get(request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_whitelabel_ips__id__delete(self):
        id = "test_url_param"
        headers = {'X-Mock': 204}
        response = self.sg.client.whitelabel.ips._(id).delete(request_headers=headers)
        self.assertEqual(response.status_code, 204)

    def test_whitelabel_ips__id__validate_post(self):
        data = {'sample': 'data'}
        id = "test_url_param"
        headers = {'X-Mock': 200}
        response = self.sg.client.whitelabel.ips._(id).validate.post(request_body=data, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_whitelabel_links_post(self):
        data = {'sample': 'data'}
        params = {'limit': 0, 'offset': 0}
        headers = {'X-Mock': 201}
        response = self.sg.client.whitelabel.links.post(request_body=data, query_params=params, request_headers=headers)
        self.assertEqual(response.status_code, 201)

    def test_whitelabel_links_get(self):
        params = {'limit': 0}
        headers = {'X-Mock': 200}
        response = self.sg.client.whitelabel.links.get(query_params=params, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_whitelabel_links_default_get(self):
        params = {'domain': 'test_string'}
        headers = {'X-Mock': 200}
        response = self.sg.client.whitelabel.links.default.get(query_params=params, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_whitelabel_links_subuser_get(self):
        params = {'username': 'test_string'}
        headers = {'X-Mock': 200}
        response = self.sg.client.whitelabel.links.subuser.get(query_params=params, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_whitelabel_links_subuser_delete(self):
        params = {'username': 'test_string'}
        headers = {'X-Mock': 204}
        response = self.sg.client.whitelabel.links.subuser.delete(query_params=params, request_headers=headers)
        self.assertEqual(response.status_code, 204)

    def test_whitelabel_links__id__patch(self):
        data = {'sample': 'data'}
        id = "test_url_param"
        headers = {'X-Mock': 200}
        response = self.sg.client.whitelabel.links._(id).patch(request_body=data, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_whitelabel_links__id__get(self):
        id = "test_url_param"
        headers = {'X-Mock': 200}
        response = self.sg.client.whitelabel.links._(id).get(request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_whitelabel_links__id__delete(self):
        id = "test_url_param"
        headers = {'X-Mock': 204}
        response = self.sg.client.whitelabel.links._(id).delete(request_headers=headers)
        self.assertEqual(response.status_code, 204)

    def test_whitelabel_links__id__validate_post(self):
        data = {'sample': 'data'}
        id = "test_url_param"
        headers = {'X-Mock': 200}
        response = self.sg.client.whitelabel.links._(id).validate.post(request_body=data, request_headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_whitelabel_links__link_id__subuser_post(self):
        data = {'sample': 'data'}
        link_id = "test_url_param"
        headers = {'X-Mock': 200}
        response = self.sg.client.whitelabel.links._(link_id).subuser.post(request_body=data, request_headers=headers)
        self.assertEqual(response.status_code, 200)

