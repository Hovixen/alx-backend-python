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
        path: Tuple[str], expected: str
        ) -> None:
        """ test that KeyError is raised with expected message """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), expected)


