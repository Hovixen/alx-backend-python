#!/usr/bin/env python3
""" test_client test case """
import unittest
from typing import Dict
from unittest.mock import Mock, patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """ class to test githuborgclient.org """

    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"})
        ])
    @patch('client.get_json')
    def test_org(self, org_name: str,
                 response: Dict, mock_get_json) -> None:
        """ test test_org for the right output """

        mock_get_json.return_value = response

        client = GithubOrgClient(org_name)
        result = client.org()

        self.assertEqual(result, response)
        mock_get_json.assert_called_once_with(
                "https://api.github.com/orgs/{}".format(org_name))
