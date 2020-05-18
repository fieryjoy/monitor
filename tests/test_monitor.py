#!/usr/bin/env python

"""Tests for `monitor` package."""


import unittest
from unittest import mock
import datetime

from monitor import consumer_example, producer_example
from monitor.database import prepare_command


# This method will be used by the mock to replace requests.get
def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, reason, status_code, elapsed):
            self.reason = reason
            self.status_code = status_code
            self.elapsed = elapsed

        def json(self):
            return self.json_data

    delta = datetime.timedelta(0, 0, 97321)
    if args[0] == 'http://someurl.com':
        return MockResponse("OK", 200, delta)
    elif args[0] == 'http://someotherurl.com':
        return MockResponse("Bad Request", 400, delta)

    return MockResponse(None, 404)


class TestMonitor(unittest.TestCase):
    """Tests for monitor package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_consumer(self):
        """Test consumer."""
        with self.assertRaises(TypeError):
            consumer_example.consumer_example()

    def test_001_producer(self):
        """Test producer."""
        with self.assertRaises(TypeError):
            producer_example.producer_example()

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_002_site_checker(self, mock_get):
        """Test site checker."""
        result = producer_example.get_result('http://someurl.com')
        self.assertEqual(result['status_code'], 200)
        self.assertEqual(result['reason'], 'OK')
        self.assertEqual(result['response_time'], 0.097321)
        result = producer_example.get_result('http://someotherurl.com')
        self.assertEqual(result['status_code'], 400)
        self.assertEqual(result['reason'], 'Bad Request')

    def test_003_prepare_command(self):
        """Tests command and values for insert in DB"""
        values = [{'status_code': 200, 'reason': 'ok', 'response_time': 333}]
        command, values = prepare_command(values)
        x = "INSERT INTO stats (status_code', reason, response_time) VALUES %s"
        self.assertEqual(command, x)
        self.assertEqual(values, [(200, 'ok', 333)])
