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
    def test_org(self, input):
        """Test the organization"""
        with mock.patch('client.GithubOrgClient.org') as mock_method:
            GithubOrgClient.ORG_URL = input
            GithubOrgClient.org()
            mock_method.assert_called_once()

    def test_public_repos_url(self):
        """Test public repos url"""
        with mock.patch('client.GithubOrgClient._public_repos_url')\
                as mock_method:
            mock_method.return_value = 'github.com'
            self.assertEqual(GithubOrgClient._public_repos_url(), 'github.com')

    def test_public_repos(self):
        """Test public repos"""
        with mock.patch('client.GithubOrgClient.public_repos') as mock_method:
            mock_method.return_value = 'github.com'
            result = GithubOrgClient.public_repos()
            self.assertEqual(result, 'github.com')
            mock_method.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license"),
        ({"license": {"key": "other_license"}}, "my_license"),
    ])
    def test_has_license(self, x, y):
        """test github has license"""
        self.assertIsInstance(x, dict)
