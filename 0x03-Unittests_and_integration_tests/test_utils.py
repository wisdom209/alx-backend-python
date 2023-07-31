#!/usr/bin/env python3
"Test module for utils.py"
import unittest
from unittest import mock
from parameterized import parameterized
from utils import access_nested_map
from utils import get_json


class TestAccessNestedMap(unittest.TestCase):
    """Testing class"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, x, y, expected_result):
        """Test the function"""
        self.assertEqual(access_nested_map(x, y), expected_result)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, x, y, expected):
        """test the function exceptions"""
        with self.assertRaises(expected):
            access_nested_map(x, y)


class TestGetJson(unittest.TestCase):
    """Testing getJson class"""

    @parameterized.expand([
        ('http://example.com', {"payload": True}),
        ('http://holberton.io', {"payload": False})
    ])
    def test_get_json(self, input, expected_result):
        """test get_json function"""
        with mock.patch('utils.requests.get') as Mock_class:
            Mock_class.json.return_value = expected_result
            result = get_json(input)
            Mock_class.assert_called_once_with(input)
            # self.assertEqual(result, expected_result)
