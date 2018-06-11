import sys
import unittest

from blocklister.summerizer import Summerizer


class TestSummerizer(unittest.TestCase):
    def test_range_of_one(self):
        smr = Summerizer(
            ['213.239.193.209-213.239.193.209'])
        result = smr.summary()
        expected = ['213.239.193.209']
        if sys.version_info[0] == 3:  # noqa
            self.assertCountEqual(result, expected)
        else:
            self.assertItemsEqual(result, expected)

    def test_ordinary_range(self):
        smr = Summerizer(
            ['213.221.87.72-213.221.87.79'])
        result = smr.summary()
        expected = ['213.221.87.72-213.221.87.79']
        if sys.version_info[0] == 3:  # noqa
            self.assertCountEqual(result, expected)
        else:
            self.assertItemsEqual(result, expected)

    def test_range_overflow(self):
        smr = Summerizer(
            ['72.32.242.248-72.32.243.255', '64.69.78.73'])
        result = smr.summary()
        expected = (
            ['72.32.242.248-72.32.243.255', '64.69.78.73'])
        if sys.version_info[0] == 3:  # noqa
            self.assertCountEqual(result, expected)
        else:
            self.assertItemsEqual(result, expected)

    def test_reverse_order(self):
        smr = Summerizer(
            ['72.32.243.255-72.32.242.248'])
        result = smr.summary()
        expected = ['72.32.242.248-72.32.243.255']
        if sys.version_info[0] == 3:  # noqa
            self.assertCountEqual(result, expected)
        else:
            self.assertItemsEqual(result, expected)

    def test_overlaps(self):
        smr = Summerizer(
            ['1.1.1.1-1.1.1.5', '1.1.1.2'])
        result = smr.summary()
        expected = ['1.1.1.1-1.1.1.5']
        if sys.version_info[0] == 3:  # noqa
            self.assertCountEqual(result, expected)
        else:
            self.assertItemsEqual(result, expected)
