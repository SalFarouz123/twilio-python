# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class PublicKeyTestCase(IntegrationTestCase):

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.accounts.v1.credentials \
                                   .public_key.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://accounts.twilio.com/v1/Credentials/PublicKeys',
        ))

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "credentials": [],
                "meta": {
                    "first_page_url": "https://accounts.twilio.com/v1/Credentials/PublicKeys?PageSize=50&Page=0",
                    "key": "credentials",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://accounts.twilio.com/v1/Credentials/PublicKeys?PageSize=50&Page=0"
                }
            }
            '''
        ))

        actual = self.client.accounts.v1.credentials \
                                        .public_key.list()

        self.assertIsNotNone(actual)

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "credentials": [
                    {
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "date_created": "2015-07-31T04:00:00Z",
                        "date_updated": "2015-07-31T04:00:00Z",
                        "friendly_name": "friendly_name",
                        "sid": "CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "url": "https://accounts.twilio.com/v1/Credentials/PublicKeys/CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    }
                ],
                "meta": {
                    "first_page_url": "https://accounts.twilio.com/v1/Credentials/PublicKeys?PageSize=50&Page=0",
                    "key": "credentials",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://accounts.twilio.com/v1/Credentials/PublicKeys?PageSize=50&Page=0"
                }
            }
            '''
        ))

        actual = self.client.accounts.v1.credentials \
                                        .public_key.list()

        self.assertIsNotNone(actual)

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.accounts.v1.credentials \
                                   .public_key.create(public_key="publickey")

        values = {'PublicKey': "publickey", }

        self.holodeck.assert_has_request(Request(
            'post',
            'https://accounts.twilio.com/v1/Credentials/PublicKeys',
            data=values,
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "2015-07-31T04:00:00Z",
                "date_updated": "2015-07-31T04:00:00Z",
                "friendly_name": "friendly_name",
                "sid": "CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "url": "https://accounts.twilio.com/v1/Credentials/PublicKeys/CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.accounts.v1.credentials \
                                        .public_key.create(public_key="publickey")

        self.assertIsNotNone(actual)

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.accounts.v1.credentials \
                                   .public_key(sid="CRXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://accounts.twilio.com/v1/Credentials/PublicKeys/CRXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "2015-07-31T04:00:00Z",
                "date_updated": "2015-07-31T04:00:00Z",
                "friendly_name": "friendly_name",
                "sid": "CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "url": "https://accounts.twilio.com/v1/Credentials/PublicKeys/CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.accounts.v1.credentials \
                                        .public_key(sid="CRXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.accounts.v1.credentials \
                                   .public_key(sid="CRXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.holodeck.assert_has_request(Request(
            'post',
            'https://accounts.twilio.com/v1/Credentials/PublicKeys/CRXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_update_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "2015-07-31T04:00:00Z",
                "date_updated": "2015-07-31T04:00:00Z",
                "friendly_name": "friendly_name",
                "sid": "CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "url": "https://accounts.twilio.com/v1/Credentials/PublicKeys/CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.accounts.v1.credentials \
                                        .public_key(sid="CRXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.accounts.v1.credentials \
                                   .public_key(sid="CRXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.holodeck.assert_has_request(Request(
            'delete',
            'https://accounts.twilio.com/v1/Credentials/PublicKeys/CRXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_delete_response(self):
        self.holodeck.mock(Response(
            204,
            None,
        ))

        actual = self.client.accounts.v1.credentials \
                                        .public_key(sid="CRXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.assertTrue(actual)
