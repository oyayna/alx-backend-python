#!/usr/bin/env python3
"""test utils """
import unittest
from parameterized import parameterized
from utils import access_nested_map
from typing import Any, Tuple, Dict
from unittest.mock import patch
from utils import get_json
from utils import memoize


class TestAccessNestedMap(unittest.TestCase):
    """test access netedmap"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
        self, nested_map: Dict[str, Any], path: Tuple[str], expected: Any
    ) -> None:
        """ FUNC """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(
            self, nested_map: Dict[str, Any], path: Tuple[str]) -> None:
        """FUNC """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """tEST GET JSON"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(
            self, test_url: str, test_payload: Dict[str, Any]) -> None:
        """FUNC """
        with patch('requests.get') as mocked_get:
            mocked_get.return_value.json.return_value = test_payload
            response = get_json(test_url)
            self.assertEqual(response, test_payload)
            mocked_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Test Memoize """

    def test_memoize(self) -> None:
        """func doc"""

        class TestClass:
            """class test"""

            def a_method(self) -> int:
                """func DOC"""
                return 42

            @memoize
            def a_property(self) -> int:
                """DOC"""
                return self.a_method()

        with patch.object(
                TestClass, 'a_method', return_value=42) as mock_method:
            instance = TestClass()
            self.assertEqual(instance.a_property, 42)  # Calls the a_method
            self.assertEqual(instance.a_property, 42)  # Uses memoized value
            mock_method.assert_called_once()
