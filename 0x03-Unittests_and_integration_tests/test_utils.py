#!/usr/bin/env python3
""" Parameterized unittest 1 """
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """ class to test access_nested_map function """
    @parameterized.expand([
        ("no_nest", {"a": 1}, ("a",), 1),
        ("one_nest", {"a": {"b": 2}}, ("a",), {'b': 2}),
        ("two_path", {"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, name, nested_map, path, expected):
        """ test assertEqual function """
        self.assertEqual(access_nested_map(nested_map, path), expected)
