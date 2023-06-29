import unittest
from linear_spline import interp, interp_matrix, interp_point_slope, interp_piecewise_linear


class TestLinearSpline(unittest.TestCase):
    def test_interp(self):
        """
        Test cases for the interp function.
        """
        xp = [1, 2, 4, 7]
        yp = [3, 5, 6, 10]

        # Test within the knot range
        self.assertAlmostEqual(interp(1.5, xp, yp), 4, places=2)
        self.assertAlmostEqual(interp(3.5, xp, yp), 5.75, places=2)
        self.assertAlmostEqual(interp(6, xp, yp), 8.666, places=2)

        # Test constant extrapolation
        self.assertAlmostEqual(interp(0, xp, yp), 3, places=2)
        self.assertAlmostEqual(interp(8, xp, yp), 10, places=2)

    def test_interp_point_slope(self):
        """Test interp_point_slope() function."""
        xp = [1, 2, 3, 4, 5]
        yp = [2, 4, 6, 8, 10]
        x = 3.5
        expected_value = 7.0

        # Compute the interpolated value
        interpolated_value = interp_point_slope(x, xp, yp)

        # Check if the interpolated value matches the expected value
        self.assertEqual(interpolated_value, expected_value)

    def test_interp_piecewise_linear(self):
        """Test interp_piecewise_linear() function."""
        xp = [1, 2, 3, 4, 5]
        yp = [2, 4, 6, 8, 10]
        x = 3.5
        expected_value = 7.0

        # Compute the interpolated value
        interpolated_value = interp_piecewise_linear(x, xp, yp)

        # Check if the interpolated value matches the expected value
        self.assertEqual(interpolated_value, expected_value)

    # def test_interp_matrix(self):
    #     """Test interp_matrix() function."""
    #     xp = [1, 2, 3, 4, 5]
    #     yp = [2, 4, 6, 8, 10]
    #     x = 3.5
    #     expected_value = 7.0
    #
    #     # Compute the interpolated value
    #     interpolated_value = interp_matrix(x, xp, yp)
    #
    #     # Check if the interpolated value matches the expected value
    #     self.assertEqual(interpolated_value, expected_value)


if __name__ == '__main__':
    unittest.main()
