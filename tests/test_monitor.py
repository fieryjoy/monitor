#!/usr/bin/env python

"""Tests for `monitor` package."""


import unittest

from monitor import consumer_example, producer_example


class TestMonitor(unittest.TestCase):
    """Tests for `monitor` package."""

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

    def test_002_site_checker(self):
        """Test site checker."""
        result = producer_example.get_result()
        self.assertEqual(result['status_code'], 200)
