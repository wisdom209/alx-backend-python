#!/usr/bin/env python3
"Test module for utils.py"
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Testing class"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, x, y, expected_result):
        """Test the function"""
        self.assertEquals(access_nested_map(x, y), expected_result)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, x, y, expected):
        """test the function exceptions"""
        with self.assertRaises(expected):
            access_nested_map(x, y)
