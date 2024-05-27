#!/usr/bin/env python3
""" test_client test case """
import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrg(unittest.TestCase):
    """ class to test githuborgclient.org """

    @parameterized.expand([
        ("google",),
        ("abc",)
        ])
    @patch('client.get_json')
    def test_org(self, org_name: str, mock_get_json) -> None:
        """ test test_org for the right output """
        result_mocked = {"login": org_name}
        mock_get_json.return_value = result_mocked

        client = GithubOrgClient(org_name)
        result = client.org

        self.assertEqual(result, result_mocked)
        mock_get_json.assert_called_once_with(
                "https://api.github.com/orgs/{}".format(org_name))
