import unittest


class TestColorScale(unittest.TestCase):

    pass
    # def test_log_interpolate_10_10K(self):
    #     linear = ['rgb(0,0,0)', 'rgb(255,255,255)']
    #     self.assertEqual(
    #         _log_interpolate(linear, 10, 10000),
    #         [[0, 'rgb(0.0, 0.0, 0.0)'],
    #             [0.0001, 'rgb(0.0, 0.0, 0.0)'],
    #             [0.001, 'rgb(63.75, 63.75, 63.75)'],
    #             [0.01, 'rgb(127.5, 127.5, 127.5)'],
    #             [0.1, 'rgb(191.25, 191.25, 191.25)'],
    #             [1, 'rgb(255.0, 255.0, 255.0)']]
    #     )
    #
    # def test_log_interpolate_tenth_10(self):
    #     linear = ['rgb(0,0,0)', 'rgb(255,255,255)']
    #     self.assertEqual(
    #         _log_interpolate(linear, 0.1, 10),
    #         [[0, 'rgb(0.0, 0.0, 0.0)'],
    #             [0.001, 'rgb(0.0, 0.0, 0.0)'],
    #             [0.01, 'rgb(85.0, 85.0, 85.0)'],
    #             [0.1, 'rgb(170.0, 170.0, 170.0)'],
    #             [1, 'rgb(255.0, 255.0, 255.0)']]
    #     )
    #
    # # When the domain covers fewer order of magnitude, results aren't ideal.
    #
    # def test_log_interpolate_5_15(self):
    #     linear = ['rgb(0,0,0)', 'rgb(255,255,255)']
    #     self.assertEqual(
    #         _log_interpolate(linear, 5, 15),
    #         [[0, 'rgb(0.0, 0.0, 0.0)'],
    #          [0.1, 'rgb(0.0, 0.0, 0.0)'],
    #          [1, 'rgb(255.0, 255.0, 255.0)']]
    #     )
    #
    # def test_log_interpolate_5_6(self):
    #     linear = ['rgb(0,0,0)', 'rgb(255,255,255)']
    #     self.assertEqual(
    #         _log_interpolate(linear, 5, 6),
    #         [[0, 'rgb(0.0, 0.0, 0.0)'],
    #          [0.1, 'rgb(0.0, 0.0, 0.0)'],
    #          [1, 'rgb(255.0, 255.0, 255.0)']]
    #     )