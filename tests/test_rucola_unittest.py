import unittest
from tests.constant_test_cases import PUBLIC_TEST_CASES, SECRET_TEST_CASES
from rucola.rucola import get_page_content
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class BlossomTestCase(unittest.TestCase):
    """Такие же тестовые случаи, но реализованные через unittest."""

    def setUp(self):
        """Начальные условия для тестов."""
        self.all_test_cases = PUBLIC_TEST_CASES + SECRET_TEST_CASES

    def test_rucola(self):
        """Тесирование функции подсчета кратеров."""
        for test_case in self.all_test_cases:
            test_input = test_case.get("test_input")
            expected = test_case.get("expected")
            self.assertEqual(expected, get_page_content(test_input)["get_page_content"]["is_success"])
