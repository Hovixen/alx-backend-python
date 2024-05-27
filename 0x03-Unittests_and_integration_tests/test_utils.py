#!/usr/bin/env python3
""" Parameterized unittest 1 module """
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from typing import Union, Dict, Tuple, Any
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """ class to test access_nested_map function """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(
            self, nested_map: Dict,
            path: Tuple[str], expected: Union[Dict, int]) -> None:
        """ test assertEqual function """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "'a'"),
        ({"a": {}}, ("a", "b"), "'b'")
        ])
    def test_access_nested_map_exception(
            self, nested_map: Dict,
            path: Tuple[str], expected: str) -> None:
        """ test that KeyError is raised with expected message """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), expected)


class TestGetJson(unittest.TestCase):
    """ class to test get_json function """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
        ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url: str,
            test_payload: Dict, mock_get) -> None:
        """ test the get_json function using mock """
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        result = get_json(test_url)
        self.assertEqual(result, test_payload)
        mock_get.assert_called_once_with(test_url)

        mock_get.reset_mock()
