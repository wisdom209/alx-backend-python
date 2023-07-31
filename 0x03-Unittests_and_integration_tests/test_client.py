#!/usr/bin/env python3
"""TestClient test module"""
import unittest
from unittest import mock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """test github client classs"""

    @parameterized.expand([
        ('google'),
        ('abc')

    ])
    def test_org(self, x):
        """Test the organization"""
        with mock.patch('client.GithubOrgClient.org') as mock_method:
            GithubOrgClient.org(x)
            mock_method.assert_called_once_with(x)
