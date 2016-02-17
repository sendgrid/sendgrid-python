import sendgrid
import json
from sendgrid.client import SendGridAPIClient
from sendgrid.version import __version__
from sendgrid.config import Config
try:
    import unittest2 as unittest
except ImportError:
    import unittest
import os
config = Config()

class UnitTests(unittest.TestCase):
    def setUp(self):
        self.sendgrid_api_key = os.environ.get('SENDGRID_API_KEY')
        self.host = "https://e9sk3d3bfaikbpdq7.stoplight-proxy.io/v3"
        self.sg = sendgrid.SendGridAPIClient(self.sendgrid_api_key, host=self.host)
        self.api_keys = self.sg.client.api_keys

    def test_apikey_init(self):
        self.assertEqual(self.sg.apikey, self.sendgrid_api_key)

    def test_useragent(self):
        useragent = 'sendgrid/' + __version__ + ';python_v3'
        self.assertEqual(self.sg.useragent, useragent)

    def test_host(self):
        host = 'https://api.sendgrid.com/v3'
        self.assertEqual(self.sg.host, self.host)

    def test_api_keys_post(self):
        data = {'sample': 'data'}
        params = {'mock': 201}
        response = self.sg.client.api_keys.post(data=data, params=params)
        self.assertEqual(response.status_code, 201)

    def test_api_keys_get(self):
        params = {'mock': 200}
        response = self.sg.client.api_keys.get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_api_keys__api_key_id__put(self):
        data = {'sample': 'data'}
        params = {'mock': 200}
        api_key_id = "test_url_param"
        response = self.sg.client.api_keys._(api_key_id).put(data=data, params=params)
        self.assertEqual(response.status_code, 200)

    def test_api_keys__api_key_id__patch(self):
        data = {'sample': 'data'}
        params = {'mock': 200}
        api_key_id = "test_url_param"
        response = self.sg.client.api_keys._(api_key_id).patch(data=data, params=params)
        self.assertEqual(response.status_code, 200)

    def test_api_keys__api_key_id__get(self):
        params = {'mock': 200}
        api_key_id = "test_url_param"
        response = self.sg.client.api_keys._(api_key_id).get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_api_keys__api_key_id__delete(self):
        params = {'mock': 204}
        api_key_id = "test_url_param"
        response = self.sg.client.api_keys._(api_key_id).delete(params=params)
        self.assertEqual(response.status_code, 204)

    def test_asm_groups_post(self):
        data = {'sample': 'data'}
        params = {'mock': 200}
        response = self.sg.client.asm.groups.post(data=data, params=params)
        self.assertEqual(response.status_code, 200)

    def test_asm_groups_get(self):
        params = {'mock': 200}
        response = self.sg.client.asm.groups.get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_asm_groups__group_id__get(self):
        params = {'mock': 200}
        group_id = "test_url_param"
        response = self.sg.client.asm.groups._(group_id).get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_asm_groups__group_id__delete(self):
        params = {'mock': 204}
        group_id = "test_url_param"
        response = self.sg.client.asm.groups._(group_id).delete(params=params)
        self.assertEqual(response.status_code, 204)

    def test_asm_groups__group_id__suppressions_post(self):
        data = {'sample': 'data'}
        params = {'mock': 201}
        group_id = "test_url_param"
        response = self.sg.client.asm.groups._(group_id).suppressions.post(data=data, params=params)
        self.assertEqual(response.status_code, 201)

    def test_asm_groups__group_id__suppressions_get(self):
        params = {'mock': 200}
        group_id = "test_url_param"
        response = self.sg.client.asm.groups._(group_id).suppressions.get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_asm_groups__group_id__suppressions__email__delete(self):
        params = {'mock': 204}
        group_id = "test_url_param"
        email = "test_url_param"
        response = self.sg.client.asm.groups._(group_id).suppressions._(email).delete(params=params)
        self.assertEqual(response.status_code, 204)

    def test_asm_groups__unsubscribe_group_id__patch(self):
        data = {'sample': 'data'}
        params = {'mock': 200}
        unsubscribe_group_id = "test_url_param"
        response = self.sg.client.asm.groups._(unsubscribe_group_id).patch(data=data, params=params)
        self.assertEqual(response.status_code, 200)

    def test_asm_suppressions_global_post(self):
        data = {'sample': 'data'}
        params = {'mock': 200}
        response = self.sg.client.asm.suppressions.global_.post(data=data, params=params)
        self.assertEqual(response.status_code, 200)

    def test_asm_suppressions_global__email_address__get(self):
        params = {'mock': 200}
        email_address = "test_url_param"
        response = self.sg.client.asm.suppressions.global_._(email_address).get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_asm_suppressions__email__get(self):
        params = {'mock': 200}
        email = "test_url_param"
        response = self.sg.client.asm.suppressions._(email).get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_asm_suppressions__email__delete(self):
        params = {'mock': 200}
        email = "test_url_param"
        response = self.sg.client.asm.suppressions._(email).delete(params=params)
        self.assertEqual(response.status_code, 200)

    def test_browsers_stats_get(self):
        params = {'mock': 200}
        response = self.sg.client.browsers.stats.get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_campaigns_post(self):
        data = {'sample': 'data'}
        params = {'mock': 201}
        response = self.sg.client.campaigns.post(data=data, params=params)
        self.assertEqual(response.status_code, 201)

    def test_campaigns_get(self):
        params = {'mock': 200}
        response = self.sg.client.campaigns.get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_campaigns__campaign_id__patch(self):
        data = {'sample': 'data'}
        params = {'mock': 200}
        campaign_id = "test_url_param"
        response = self.sg.client.campaigns._(campaign_id).patch(data=data, params=params)
        self.assertEqual(response.status_code, 200)

    def test_campaigns__campaign_id__get(self):
        params = {'mock': 200}
        campaign_id = "test_url_param"
        response = self.sg.client.campaigns._(campaign_id).get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_campaigns__campaign_id__delete(self):
        params = {'mock': 204}
        campaign_id = "test_url_param"
        response = self.sg.client.campaigns._(campaign_id).delete(params=params)
        self.assertEqual(response.status_code, 204)

    def test_campaigns__campaign_id__schedules_patch(self):
        data = {'sample': 'data'}
        params = {'mock': 200}
        campaign_id = "test_url_param"
        response = self.sg.client.campaigns._(campaign_id).schedules.patch(data=data, params=params)
        self.assertEqual(response.status_code, 200)

    def test_campaigns__campaign_id__schedules_post(self):
        data = {'sample': 'data'}
        params = {'mock': 201}
        campaign_id = "test_url_param"
        response = self.sg.client.campaigns._(campaign_id).schedules.post(data=data, params=params)
        self.assertEqual(response.status_code, 201)

    def test_campaigns__campaign_id__schedules_get(self):
        params = {'mock': 200}
        campaign_id = "test_url_param"
        response = self.sg.client.campaigns._(campaign_id).schedules.get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_campaigns__campaign_id__schedules_delete(self):
        params = {'mock': 204}
        campaign_id = "test_url_param"
        response = self.sg.client.campaigns._(campaign_id).schedules.delete(params=params)
        self.assertEqual(response.status_code, 204)

    def test_campaigns__campaign_id__schedules_now_post(self):
        data = {'sample': 'data'}
        params = {'mock': 201}
        campaign_id = "test_url_param"
        response = self.sg.client.campaigns._(campaign_id).schedules.now.post(data=data, params=params)
        self.assertEqual(response.status_code, 201)

    def test_campaigns__campaign_id__schedules_test_post(self):
        data = {'sample': 'data'}
        params = {'mock': 200}
        campaign_id = "test_url_param"
        response = self.sg.client.campaigns._(campaign_id).schedules.test.post(data=data, params=params)
        self.assertEqual(response.status_code, 200)

    def test_categories_get(self):
        params = {'mock': 200}
        response = self.sg.client.categories.get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_categories_stats_get(self):
        params = {'mock': 200}
        response = self.sg.client.categories.stats.get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_categories_stats_sums_get(self):
        params = {'mock': 200}
        response = self.sg.client.categories.stats.sums.get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_clients_stats_get(self):
        params = {'mock': 200}
        response = self.sg.client.clients.stats.get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_clients__client_type__stats_get(self):
        params = {'mock': 200}
        client_type = "test_url_param"
        response = self.sg.client.clients._(client_type).stats.get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_contactdb_custom_fields_post(self):
        data = {'sample': 'data'}
        params = {'mock': 201}
        response = self.sg.client.contactdb.custom_fields.post(data=data, params=params)
        self.assertEqual(response.status_code, 201)

    def test_contactdb_custom_fields_get(self):
        params = {'mock': 200}
        response = self.sg.client.contactdb.custom_fields.get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_contactdb_custom_fields__custom_field_id__get(self):
        params = {'mock': 200}
        custom_field_id = "test_url_param"
        response = self.sg.client.contactdb.custom_fields._(custom_field_id).get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_contactdb_custom_fields__custom_field_id__delete(self):
        params = {'mock': 202}
        custom_field_id = "test_url_param"
        response = self.sg.client.contactdb.custom_fields._(custom_field_id).delete(params=params)
        self.assertEqual(response.status_code, 202)

    def test_contactdb_lists_post(self):
        data = {'sample': 'data'}
        params = {'mock': 201}
        response = self.sg.client.contactdb.lists.post(data=data, params=params)
        self.assertEqual(response.status_code, 201)

    def test_contactdb_lists_get(self):
        params = {'mock': 200}
        response = self.sg.client.contactdb.lists.get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_contactdb_lists_delete(self):
        params = {'mock': 204}
        response = self.sg.client.contactdb.lists.delete(params=params)
        self.assertEqual(response.status_code, 204)

    def test_contactdb_lists__list_id__patch(self):
        data = {'sample': 'data'}
        params = {'mock': 200}
        list_id = "test_url_param"
        response = self.sg.client.contactdb.lists._(list_id).patch(data=data, params=params)
        self.assertEqual(response.status_code, 200)

    def test_contactdb_lists__list_id__get(self):
        params = {'mock': 200}
        list_id = "test_url_param"
        response = self.sg.client.contactdb.lists._(list_id).get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_contactdb_lists__list_id__delete(self):
        params = {'mock': 202}
        list_id = "test_url_param"
        response = self.sg.client.contactdb.lists._(list_id).delete(params=params)
        self.assertEqual(response.status_code, 202)

    def test_contactdb_lists__list_id__recipients_post(self):
        data = {'sample': 'data'}
        params = {'mock': 201}
        list_id = "test_url_param"
        response = self.sg.client.contactdb.lists._(list_id).recipients.post(data=data, params=params)
        self.assertEqual(response.status_code, 201)

    def test_contactdb_lists__list_id__recipients_get(self):
        params = {'mock': 200}
        list_id = "test_url_param"
        response = self.sg.client.contactdb.lists._(list_id).recipients.get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_contactdb_lists__list_id__recipients__recipient_id__post(self):
        data = {'sample': 'data'}
        params = {'mock': 201}
        list_id = "test_url_param"
        recipient_id = "test_url_param"
        response = self.sg.client.contactdb.lists._(list_id).recipients._(recipient_id).post(data=data, params=params)
        self.assertEqual(response.status_code, 201)

    def test_contactdb_lists__list_id__recipients__recipient_id__delete(self):
        params = {'mock': 204}
        list_id = "test_url_param"
        recipient_id = "test_url_param"
        response = self.sg.client.contactdb.lists._(list_id).recipients._(recipient_id).delete(params=params)
        self.assertEqual(response.status_code, 204)

    def test_contactdb_recipients_patch(self):
        data = {'sample': 'data'}
        params = {'mock': 201}
        response = self.sg.client.contactdb.recipients.patch(data=data, params=params)
        self.assertEqual(response.status_code, 201)

    def test_contactdb_recipients_post(self):
        data = {'sample': 'data'}
        params = {'mock': 201}
        response = self.sg.client.contactdb.recipients.post(data=data, params=params)
        self.assertEqual(response.status_code, 201)

    def test_contactdb_recipients_get(self):
        params = {'mock': 200}
        response = self.sg.client.contactdb.recipients.get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_contactdb_recipients_delete(self):
        params = {'mock': 200}
        response = self.sg.client.contactdb.recipients.delete(params=params)
        self.assertEqual(response.status_code, 200)

    def test_contactdb_recipients_billable_count_get(self):
        params = {'mock': 200}
        response = self.sg.client.contactdb.recipients.billable_count.get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_contactdb_recipients_count_get(self):
        params = {'mock': 200}
        response = self.sg.client.contactdb.recipients.count.get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_contactdb_recipients_search_get(self):
        params = {'mock': 200}
        response = self.sg.client.contactdb.recipients.search.get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_contactdb_recipients__recipient_id__get(self):
        params = {'mock': 200}
        recipient_id = "test_url_param"
        response = self.sg.client.contactdb.recipients._(recipient_id).get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_contactdb_recipients__recipient_id__delete(self):
        params = {'mock': 204}
        recipient_id = "test_url_param"
        response = self.sg.client.contactdb.recipients._(recipient_id).delete(params=params)
        self.assertEqual(response.status_code, 204)

    def test_contactdb_recipients__recipient_id__lists_get(self):
        params = {'mock': 200}
        recipient_id = "test_url_param"
        response = self.sg.client.contactdb.recipients._(recipient_id).lists.get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_contactdb_reserved_fields_get(self):
        params = {'mock': 200}
        response = self.sg.client.contactdb.reserved_fields.get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_contactdb_segments_post(self):
        data = {'sample': 'data'}
        params = {'mock': 200}
        response = self.sg.client.contactdb.segments.post(data=data, params=params)
        self.assertEqual(response.status_code, 200)

    def test_contactdb_segments_get(self):
        params = {'mock': 200}
        response = self.sg.client.contactdb.segments.get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_contactdb_segments__segment_id__patch(self):
        data = {'sample': 'data'}
        params = {'mock': 200}
        segment_id = "test_url_param"
        response = self.sg.client.contactdb.segments._(segment_id).patch(data=data, params=params)
        self.assertEqual(response.status_code, 200)

    def test_contactdb_segments__segment_id__get(self):
        params = {'mock': 200}
        segment_id = "test_url_param"
        response = self.sg.client.contactdb.segments._(segment_id).get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_contactdb_segments__segment_id__delete(self):
        params = {'mock': 204}
        segment_id = "test_url_param"
        response = self.sg.client.contactdb.segments._(segment_id).delete(params=params)
        self.assertEqual(response.status_code, 204)

    def test_contactdb_segments__segment_id__recipients_get(self):
        params = {'mock': 200}
        segment_id = "test_url_param"
        response = self.sg.client.contactdb.segments._(segment_id).recipients.get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_devices_stats_get(self):
        params = {'mock': 200}
        response = self.sg.client.devices.stats.get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_geo_stats_get(self):
        params = {'mock': 200}
        response = self.sg.client.geo.stats.get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_ips_get(self):
        params = {'mock': 200}
        response = self.sg.client.ips.get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_ips_assigned_get(self):
        params = {'mock': 200}
        response = self.sg.client.ips.assigned.get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_ips_pools_post(self):
        data = {'sample': 'data'}
        params = {'mock': 200}
        response = self.sg.client.ips.pools.post(data=data, params=params)
        self.assertEqual(response.status_code, 200)

    def test_ips_pools__pool_name__get(self):
        params = {'mock': 200}
        pool_name = "test_url_param"
        response = self.sg.client.ips.pools._(pool_name).get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_ips_pools__pool_name__delete(self):
        params = {'mock': 204}
        pool_name = "test_url_param"
        response = self.sg.client.ips.pools._(pool_name).delete(params=params)
        self.assertEqual(response.status_code, 204)

    def test_ips_warmup_post(self):
        data = {'sample': 'data'}
        params = {'mock': 200}
        response = self.sg.client.ips.warmup.post(data=data, params=params)
        self.assertEqual(response.status_code, 200)

    def test_ips_warmup__ip_address__delete(self):
        params = {'mock': 204}
        ip_address = "test_url_param"
        response = self.sg.client.ips.warmup._(ip_address).delete(params=params)
        self.assertEqual(response.status_code, 204)

    def test_mail_batch_post(self):
        data = {'sample': 'data'}
        params = {'mock': 201}
        response = self.sg.client.mail.batch.post(data=data, params=params)
        self.assertEqual(response.status_code, 201)

    def test_mail_batch__batch_id__get(self):
        params = {'mock': 200}
        batch_id = "test_url_param"
        response = self.sg.client.mail.batch._(batch_id).get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_mail_settings_get(self):
        params = {'mock': 200}
        response = self.sg.client.mail_settings.get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_mail_settings_address_whitelist_patch(self):
        data = {'sample': 'data'}
        params = {'mock': 200}
        response = self.sg.client.mail_settings.address_whitelist.patch(data=data, params=params)
        self.assertEqual(response.status_code, 200)

    def test_mail_settings_address_whitelist_get(self):
        params = {'mock': 200}
        response = self.sg.client.mail_settings.address_whitelist.get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_mail_settings_bcc_patch(self):
        data = {'sample': 'data'}
        params = {'mock': 200}
        response = self.sg.client.mail_settings.bcc.patch(data=data, params=params)
        self.assertEqual(response.status_code, 200)

    def test_mail_settings_bcc_get(self):
        params = {'mock': 200}
        response = self.sg.client.mail_settings.bcc.get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_mail_settings_bounce_purge_patch(self):
        data = {'sample': 'data'}
        params = {'mock': 200}
        response = self.sg.client.mail_settings.bounce_purge.patch(data=data, params=params)
        self.assertEqual(response.status_code, 200)

    def test_mail_settings_bounce_purge_get(self):
        params = {'mock': 200}
        response = self.sg.client.mail_settings.bounce_purge.get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_mail_settings_footer_patch(self):
        data = {'sample': 'data'}
        params = {'mock': 200}
        response = self.sg.client.mail_settings.footer.patch(data=data, params=params)
        self.assertEqual(response.status_code, 200)

    def test_mail_settings_footer_get(self):
        params = {'mock': 200}
        response = self.sg.client.mail_settings.footer.get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_mail_settings_forward_bounce_patch(self):
        data = {'sample': 'data'}
        params = {'mock': 200}
        response = self.sg.client.mail_settings.forward_bounce.patch(data=data, params=params)
        self.assertEqual(response.status_code, 200)

    def test_mail_settings_forward_bounce_get(self):
        params = {'mock': 200}
        response = self.sg.client.mail_settings.forward_bounce.get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_mail_settings_forward_spam_patch(self):
        data = {'sample': 'data'}
        params = {'mock': 200}
        response = self.sg.client.mail_settings.forward_spam.patch(data=data, params=params)
        self.assertEqual(response.status_code, 200)

    def test_mail_settings_forward_spam_get(self):
        params = {'mock': 200}
        response = self.sg.client.mail_settings.forward_spam.get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_mail_settings_plain_content_patch(self):
        data = {'sample': 'data'}
        params = {'mock': 200}
        response = self.sg.client.mail_settings.plain_content.patch(data=data, params=params)
        self.assertEqual(response.status_code, 200)

    def test_mail_settings_plain_content_get(self):
        params = {'mock': 200}
        response = self.sg.client.mail_settings.plain_content.get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_mail_settings_spam_check_patch(self):
        data = {'sample': 'data'}
        params = {'mock': 200}
        response = self.sg.client.mail_settings.spam_check.patch(data=data, params=params)
        self.assertEqual(response.status_code, 200)

    def test_mail_settings_spam_check_get(self):
        params = {'mock': 200}
        response = self.sg.client.mail_settings.spam_check.get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_mail_settings_template_patch(self):
        data = {'sample': 'data'}
        params = {'mock': 200}
        response = self.sg.client.mail_settings.template.patch(data=data, params=params)
        self.assertEqual(response.status_code, 200)

    def test_mail_settings_template_get(self):
        params = {'mock': 200}
        response = self.sg.client.mail_settings.template.get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_mailbox_providers_stats_get(self):
        params = {'mock': 200}
        response = self.sg.client.mailbox_providers.stats.get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_partner_settings_get(self):
        params = {'mock': 200}
        response = self.sg.client.partner_settings.get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_partner_settings_new_relic_patch(self):
        data = {'sample': 'data'}
        params = {'mock': 200}
        response = self.sg.client.partner_settings.new_relic.patch(data=data, params=params)
        self.assertEqual(response.status_code, 200)

    def test_partner_settings_new_relic_get(self):
        params = {'mock': 200}
        response = self.sg.client.partner_settings.new_relic.get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_partner_settings_sendwithus_patch(self):
        data = {'sample': 'data'}
        params = {'mock': 200}
        response = self.sg.client.partner_settings.sendwithus.patch(data=data, params=params)
        self.assertEqual(response.status_code, 200)

    def test_partner_settings_sendwithus_get(self):
        params = {'mock': 200}
        response = self.sg.client.partner_settings.sendwithus.get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_scopes_get(self):
        params = {'mock': 200}
        response = self.sg.client.scopes.get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_stats_get(self):
        params = {'mock': 200}
        response = self.sg.client.stats.get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_subusers_post(self):
        data = {'sample': 'data'}
        params = {'mock': 200}
        response = self.sg.client.subusers.post(data=data, params=params)
        self.assertEqual(response.status_code, 200)

    def test_subusers_get(self):
        params = {'mock': 200}
        response = self.sg.client.subusers.get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_subusers_reputations_get(self):
        params = {'mock': 200}
        response = self.sg.client.subusers.reputations.get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_subusers_stats_get(self):
        params = {'mock': 200}
        response = self.sg.client.subusers.stats.get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_subusers_stats_sums_get(self):
        params = {'mock': 200}
        response = self.sg.client.subusers.stats.sums.get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_subusers__subuser_name__patch(self):
        data = {'sample': 'data'}
        params = {'mock': 204}
        subuser_name = "test_url_param"
        response = self.sg.client.subusers._(subuser_name).patch(data=data, params=params)
        self.assertEqual(response.status_code, 204)

    def test_subusers__subuser_name__delete(self):
        params = {'mock': 204}
        subuser_name = "test_url_param"
        response = self.sg.client.subusers._(subuser_name).delete(params=params)
        self.assertEqual(response.status_code, 204)

    def test_subusers__subuser_name__ips_put(self):
        data = {'sample': 'data'}
        params = {'mock': 200}
        subuser_name = "test_url_param"
        response = self.sg.client.subusers._(subuser_name).ips.put(data=data, params=params)
        self.assertEqual(response.status_code, 200)

    def test_subusers__subuser_name__monitor_put(self):
        data = {'sample': 'data'}
        params = {'mock': 200}
        subuser_name = "test_url_param"
        response = self.sg.client.subusers._(subuser_name).monitor.put(data=data, params=params)
        self.assertEqual(response.status_code, 200)

    def test_subusers__subuser_name__monitor_post(self):
        data = {'sample': 'data'}
        params = {'mock': 200}
        subuser_name = "test_url_param"
        response = self.sg.client.subusers._(subuser_name).monitor.post(data=data, params=params)
        self.assertEqual(response.status_code, 200)

    def test_subusers__subuser_name__monitor_get(self):
        params = {'mock': 200}
        subuser_name = "test_url_param"
        response = self.sg.client.subusers._(subuser_name).monitor.get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_subusers__subuser_name__monitor_delete(self):
        params = {'mock': 204}
        subuser_name = "test_url_param"
        response = self.sg.client.subusers._(subuser_name).monitor.delete(params=params)
        self.assertEqual(response.status_code, 204)

    def test_suppression_bounces_get(self):
        params = {'mock': 200}
        response = self.sg.client.suppression.bounces.get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_suppression_bounces_delete(self):
        params = {'mock': 204}
        response = self.sg.client.suppression.bounces.delete(params=params)
        self.assertEqual(response.status_code, 204)

    def test_suppression_bounces__email__get(self):
        params = {'mock': 200}
        email = "test_url_param"
        response = self.sg.client.suppression.bounces._(email).get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_suppression_bounces__email__delete(self):
        params = {'mock': 204}
        email = "test_url_param"
        response = self.sg.client.suppression.bounces._(email).delete(params=params)
        self.assertEqual(response.status_code, 204)

    def test_templates_post(self):
        data = {'sample': 'data'}
        params = {'mock': 201}
        response = self.sg.client.templates.post(data=data, params=params)
        self.assertEqual(response.status_code, 201)

    def test_templates_get(self):
        params = {'mock': 200}
        response = self.sg.client.templates.get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_templates__template_id__patch(self):
        data = {'sample': 'data'}
        params = {'mock': 200}
        template_id = "test_url_param"
        response = self.sg.client.templates._(template_id).patch(data=data, params=params)
        self.assertEqual(response.status_code, 200)

    def test_templates__template_id__get(self):
        params = {'mock': 200}
        template_id = "test_url_param"
        response = self.sg.client.templates._(template_id).get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_templates__template_id__delete(self):
        params = {'mock': 204}
        template_id = "test_url_param"
        response = self.sg.client.templates._(template_id).delete(params=params)
        self.assertEqual(response.status_code, 204)

    def test_templates__template_id__versions_post(self):
        data = {'sample': 'data'}
        params = {'mock': 201}
        template_id = "test_url_param"
        response = self.sg.client.templates._(template_id).versions.post(data=data, params=params)
        self.assertEqual(response.status_code, 201)

    def test_templates__template_id__versions__version_id__patch(self):
        data = {'sample': 'data'}
        params = {'mock': 200}
        template_id = "test_url_param"
        version_id = "test_url_param"
        response = self.sg.client.templates._(template_id).versions._(version_id).patch(data=data, params=params)
        self.assertEqual(response.status_code, 200)

    def test_templates__template_id__versions__version_id__get(self):
        params = {'mock': 200}
        template_id = "test_url_param"
        version_id = "test_url_param"
        response = self.sg.client.templates._(template_id).versions._(version_id).get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_templates__template_id__versions__version_id__delete(self):
        params = {'mock': 204}
        template_id = "test_url_param"
        version_id = "test_url_param"
        response = self.sg.client.templates._(template_id).versions._(version_id).delete(params=params)
        self.assertEqual(response.status_code, 204)

    def test_templates__template_id__versions__version_id__activate_post(self):
        data = {'sample': 'data'}
        params = {'mock': 200}
        template_id = "test_url_param"
        version_id = "test_url_param"
        response = self.sg.client.templates._(template_id).versions._(version_id).activate.post(data=data, params=params)
        self.assertEqual(response.status_code, 200)

    def test_tracking_settings_get(self):
        params = {'mock': 200}
        response = self.sg.client.tracking_settings.get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_tracking_settings_click_patch(self):
        data = {'sample': 'data'}
        params = {'mock': 200}
        response = self.sg.client.tracking_settings.click.patch(data=data, params=params)
        self.assertEqual(response.status_code, 200)

    def test_tracking_settings_click_get(self):
        params = {'mock': 200}
        response = self.sg.client.tracking_settings.click.get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_tracking_settings_google_analytics_patch(self):
        data = {'sample': 'data'}
        params = {'mock': 200}
        response = self.sg.client.tracking_settings.google_analytics.patch(data=data, params=params)
        self.assertEqual(response.status_code, 200)

    def test_tracking_settings_google_analytics_get(self):
        params = {'mock': 200}
        response = self.sg.client.tracking_settings.google_analytics.get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_tracking_settings_open_patch(self):
        data = {'sample': 'data'}
        params = {'mock': 200}
        response = self.sg.client.tracking_settings.open.patch(data=data, params=params)
        self.assertEqual(response.status_code, 200)

    def test_tracking_settings_open_get(self):
        params = {'mock': 200}
        response = self.sg.client.tracking_settings.open.get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_tracking_settings_subscription_patch(self):
        data = {'sample': 'data'}
        params = {'mock': 200}
        response = self.sg.client.tracking_settings.subscription.patch(data=data, params=params)
        self.assertEqual(response.status_code, 200)

    def test_tracking_settings_subscription_get(self):
        params = {'mock': 200}
        response = self.sg.client.tracking_settings.subscription.get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_user_account_get(self):
        params = {'mock': 200}
        response = self.sg.client.user.account.get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_user_profile_patch(self):
        data = {'sample': 'data'}
        params = {'mock': 200}
        response = self.sg.client.user.profile.patch(data=data, params=params)
        self.assertEqual(response.status_code, 200)

    def test_user_profile_get(self):
        params = {'mock': 200}
        response = self.sg.client.user.profile.get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_user_scheduled_sends_post(self):
        data = {'sample': 'data'}
        params = {'mock': 201}
        response = self.sg.client.user.scheduled_sends.post(data=data, params=params)
        self.assertEqual(response.status_code, 201)

    def test_user_scheduled_sends_get(self):
        params = {'mock': 200}
        response = self.sg.client.user.scheduled_sends.get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_user_scheduled_sends__batch_id__patch(self):
        data = {'sample': 'data'}
        params = {'mock': 204}
        batch_id = "test_url_param"
        response = self.sg.client.user.scheduled_sends._(batch_id).patch(data=data, params=params)
        self.assertEqual(response.status_code, 204)

    def test_user_scheduled_sends__batch_id__get(self):
        params = {'mock': 200}
        batch_id = "test_url_param"
        response = self.sg.client.user.scheduled_sends._(batch_id).get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_user_scheduled_sends__batch_id__delete(self):
        params = {'mock': 204}
        batch_id = "test_url_param"
        response = self.sg.client.user.scheduled_sends._(batch_id).delete(params=params)
        self.assertEqual(response.status_code, 204)

    def test_user_webhooks_parse_stats_get(self):
        params = {'mock': 200}
        response = self.sg.client.user.webhooks.parse.stats.get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_whitelabel_domains_post(self):
        data = {'sample': 'data'}
        params = {'mock': 201}
        response = self.sg.client.whitelabel.domains.post(data=data, params=params)
        self.assertEqual(response.status_code, 201)

    def test_whitelabel_domains_get(self):
        params = {'mock': 200}
        response = self.sg.client.whitelabel.domains.get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_whitelabel_domains_default_get(self):
        params = {'mock': 200}
        response = self.sg.client.whitelabel.domains.default.get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_whitelabel_domains_subuser_get(self):
        params = {'mock': 200}
        response = self.sg.client.whitelabel.domains.subuser.get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_whitelabel_domains_subuser_delete(self):
        params = {'mock': 204}
        response = self.sg.client.whitelabel.domains.subuser.delete(params=params)
        self.assertEqual(response.status_code, 204)

    def test_whitelabel_domains__domain_id__patch(self):
        data = {'sample': 'data'}
        params = {'mock': 200}
        domain_id = "test_url_param"
        response = self.sg.client.whitelabel.domains._(domain_id).patch(data=data, params=params)
        self.assertEqual(response.status_code, 200)

    def test_whitelabel_domains__domain_id__get(self):
        params = {'mock': 200}
        domain_id = "test_url_param"
        response = self.sg.client.whitelabel.domains._(domain_id).get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_whitelabel_domains__domain_id__delete(self):
        params = {'mock': 204}
        domain_id = "test_url_param"
        response = self.sg.client.whitelabel.domains._(domain_id).delete(params=params)
        self.assertEqual(response.status_code, 204)

    def test_whitelabel_domains__domain_id__subuser_post(self):
        data = {'sample': 'data'}
        params = {'mock': 201}
        domain_id = "test_url_param"
        response = self.sg.client.whitelabel.domains._(domain_id).subuser.post(data=data, params=params)
        self.assertEqual(response.status_code, 201)

    def test_whitelabel_domains__id__ips_post(self):
        data = {'sample': 'data'}
        params = {'mock': 200}
        id = "test_url_param"
        response = self.sg.client.whitelabel.domains._(id).ips.post(data=data, params=params)
        self.assertEqual(response.status_code, 200)

    def test_whitelabel_domains__id__ips__ip__delete(self):
        params = {'mock': 200}
        id = "test_url_param"
        ip = "test_url_param"
        response = self.sg.client.whitelabel.domains._(id).ips._(ip).delete(params=params)
        self.assertEqual(response.status_code, 200)

    def test_whitelabel_domains__id__validate_post(self):
        data = {'sample': 'data'}
        params = {'mock': 200}
        id = "test_url_param"
        response = self.sg.client.whitelabel.domains._(id).validate.post(data=data, params=params)
        self.assertEqual(response.status_code, 200)

    def test_whitelabel_ips_post(self):
        data = {'sample': 'data'}
        params = {'mock': 201}
        response = self.sg.client.whitelabel.ips.post(data=data, params=params)
        self.assertEqual(response.status_code, 201)

    def test_whitelabel_ips_get(self):
        params = {'mock': 200}
        response = self.sg.client.whitelabel.ips.get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_whitelabel_ips__id__get(self):
        params = {'mock': 200}
        id = "test_url_param"
        response = self.sg.client.whitelabel.ips._(id).get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_whitelabel_ips__id__delete(self):
        params = {'mock': 204}
        id = "test_url_param"
        response = self.sg.client.whitelabel.ips._(id).delete(params=params)
        self.assertEqual(response.status_code, 204)

    def test_whitelabel_ips__id__validate_post(self):
        data = {'sample': 'data'}
        params = {'mock': 200}
        id = "test_url_param"
        response = self.sg.client.whitelabel.ips._(id).validate.post(data=data, params=params)
        self.assertEqual(response.status_code, 200)

    def test_whitelabel_links_post(self):
        data = {'sample': 'data'}
        params = {'mock': 201}
        response = self.sg.client.whitelabel.links.post(data=data, params=params)
        self.assertEqual(response.status_code, 201)

    def test_whitelabel_links_get(self):
        params = {'mock': 200}
        response = self.sg.client.whitelabel.links.get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_whitelabel_links_default_get(self):
        params = {'mock': 200}
        response = self.sg.client.whitelabel.links.default.get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_whitelabel_links_subuser_get(self):
        params = {'mock': 200}
        response = self.sg.client.whitelabel.links.subuser.get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_whitelabel_links_subuser_delete(self):
        params = {'mock': 204}
        response = self.sg.client.whitelabel.links.subuser.delete(params=params)
        self.assertEqual(response.status_code, 204)

    def test_whitelabel_links__id__patch(self):
        data = {'sample': 'data'}
        params = {'mock': 200}
        id = "test_url_param"
        response = self.sg.client.whitelabel.links._(id).patch(data=data, params=params)
        self.assertEqual(response.status_code, 200)

    def test_whitelabel_links__id__get(self):
        params = {'mock': 200}
        id = "test_url_param"
        response = self.sg.client.whitelabel.links._(id).get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_whitelabel_links__id__delete(self):
        params = {'mock': 204}
        id = "test_url_param"
        response = self.sg.client.whitelabel.links._(id).delete(params=params)
        self.assertEqual(response.status_code, 204)

    def test_whitelabel_links__id__validate_post(self):
        data = {'sample': 'data'}
        params = {'mock': 200}
        id = "test_url_param"
        response = self.sg.client.whitelabel.links._(id).validate.post(data=data, params=params)
        self.assertEqual(response.status_code, 200)

    def test_whitelabel_links__link_id__subuser_post(self):
        data = {'sample': 'data'}
        params = {'mock': 200}
        link_id = "test_url_param"
        response = self.sg.client.whitelabel.links._(link_id).subuser.post(data=data, params=params)
        self.assertEqual(response.status_code, 200)

