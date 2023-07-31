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
    {"name": 'org_payload', "value": TEST_PAYLOAD[0][0]},
    {"name": 'repos_payload', "value": TEST_PAYLOAD[0][1]},
    {"name": 'expected_repos', "value": TEST_PAYLOAD[0][2]},
    {"name": 'apache2_repos', "value": TEST_PAYLOAD[0][3]},
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test"""

    @classmethod
    def setUpClass(cls) -> None:
        def getPayload(url):
            return mock.Mock({cls.name: cls.value})
        cls.get_patcher = mock.patch("requests.get", side_effect=getPayload)
        cls.get_patcher.start()

    def test_public_repos_with_license(self):
        """test public repos with license"""
        self.assertTrue(True)

    def test_public_repos(self):
        """test public repos"""
        self.assertTrue(True)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.get_patcher.stop()
