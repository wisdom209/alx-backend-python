#!/usr/bin/env python3
"""TestClient test module"""
import unittest
import requests
from unittest import mock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


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
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, x, y, expected_result):
        """test github has license"""
        result = GithubOrgClient.has_license(x, y)
        self.assertEqual(result, expected_result)


@parameterized_class([
    {"name": "orgs_payload"},
    {"name": "repos_payload"},
    {"name": "expected_repos"},
    {"name": "apache2_repos"},
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test"""
    get_patcher = mock.patch('request.get')

    @classmethod
    def setUpClass(cls) -> None:
        mock_method = cls.get_patcher.start()
        mock_method.json.return_value = TEST_PAYLOAD
        return super().setUpClass()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.get_patcher.stop()
        return super().tearDown()
