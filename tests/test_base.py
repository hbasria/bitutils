# coding: utf-8

import unittest

from bitutils import to_bytes, base43, base58


class TestUtils(unittest.TestCase):
    def test_str_to_bytes(self):
        self.assertEqual(to_bytes('testdata'), b'testdata')

    def test_base43(self):
        self.assertEqual(base43(b'testdata'), '913.NKLC2N-+')

    def test_base58(self):
        self.assertEqual(base58(b'testdata'), 'LUC1e943SYQ')
