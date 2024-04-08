#!/usr/bin/env python3

import unittest
from unittest.mock import patch
from client import GithubOrgClient
from parameterized import parameterized

"""
Module containing unit tests for client.py
"""


class TestGithubOrgClient(unittest.TestCase):
    """
    Test cases for GithubOrgClient class
    """

    @patch("client.get_json")
    @parameterized.expand([("google",), ("abc",)])
    def test_org(self, org_name, mock_get_json):
        """
        Test org method of GithubOrgClient class
        """
        test_payload = {"name": org_name}
        mock_get_json.return_value = test_payload

        client = GithubOrgClient(org_name)
        result = client.org

        a = f"https://api.github.com/orgs/{org_name}"

        mock_get_json.assert_called_once_with(a)
        self.assertEqual(result, test_payload)

    @patch("client.GithubOrgClient.org", new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """
        Test _public_repos_url property of GithubOrgClient class
        """
        mock_org.return_value = {
            "repos_url": "https://api.github.com/orgs/example/repos"
        }

        client = GithubOrgClient()
        result = client._public_repos_url

        self.assertEqual(result, "https://api.github.com/orgs/example/repos")

    @patch("client.GithubOrgClient.get_json")
    b = new_callable = PropertyMock

    @patch("client.GithubOrgClient._public_repos_url", b)
    def test_public_repos(self, mock_repos_url, mock_get_json):
        """
        Test public_repos method of GithubOrgClient class
        """

        c = "https://api.github.com/orgs/example/repos"
        mock_repos_url.return_value = c
        test_payload = [{"name": "repo1"}, {"name": "repo2"}]
        mock_get_json.return_value = test_payload

        client = GithubOrgClient()
        result = client.public_repos()

        mock_repos_url.assert_called_once()
        mock_get_json.assert_called_once_with(
            "https://api.github.com/orgs/example/repos"
        )
        self.assertEqual(result, test_payload)

    @parameterized.expand(
        [
            ({"license": {"key": "my_license"}}, "my_license", True),
            ({"license": {"key": "other_license"}}, "my_license", False),
        ]
    )
    def test_has_license(self, repo, license_key, expected):
        """
        Test has_license method of GithubOrgClient class
        """
        client = GithubOrgClient()
        result = client.has_license(repo, license_key)
        self.assertEqual(result, expected)
