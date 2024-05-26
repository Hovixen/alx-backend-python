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
        ("no_nest", {"a": 1}, ("a",), 1),
        ("one_nest", {"a": {"b": 2}}, ("a",), {'b': 2}),
        ("two_path", {"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(
            self, name: str, nested_map: Dict,
            path: Tuple[str], expected: Union[Dict, int]) -> None:
        """ test assertEqual function """
        self.assertEqual(access_nested_map(nested_map, path), expected)
