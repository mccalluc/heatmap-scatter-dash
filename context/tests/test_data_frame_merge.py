import unittest
from io import StringIO

import pandas

from app.data_frame_merge import DataFrameMerge


class TestDataFrameMerge(unittest.TestCase):

    def setUp(self):
        self.dataframes = [pandas.DataFrame([
                [1, 4, 1, 5],
                [8, 4, 8, 5],
                [2, 4, 2, 5],
                [9, 4, 9, 5]],
            columns=['c1', 'c2', 'c3', 'c4'],
            index=['r1', 'r2', 'r3', 'r4']
        )]

    def assertEqualDataFrames(self, a, b):
        self.assertEqual(a.as_matrix().tolist(), b.as_matrix().tolist())
        self.assertEqual(a.columns.tolist(),     b.columns.tolist())
        self.assertEqual(a.index.tolist(),       b.index.tolist())

    def test_no_change(self):
        merged_frame = DataFrameMerge(self.dataframes).count_frame
        self.assertEqualDataFrames(merged_frame, self.dataframes[0])

    def test_cluster(self):
        # Anything more than this should be tested in test_cluster.py
        merged_frame = DataFrameMerge(self.dataframes, clustering=True).count_frame
        self.assertEqualDataFrames(merged_frame, pandas.DataFrame([
                [1, 1, 4, 5],
                [2, 2, 4, 5],
                [8, 8, 4, 5],
                [9, 9, 4, 5]],
            columns=['c1', 'c3', 'c2', 'c4'],
            index=['r1', 'r3', 'r2', 'r4']
        ))