import random


def generate_synthetic_data(num_points, range_min, range_max):
    """
    Generate synthetic data for testing or experimentation.

    Args:
        num_points: The number of data points to generate.
        range_min: The minimum value for the data range.
        range_max: The maximum value for the data range.

    Returns:
        Two lists representing the synthetic knots and values.
    """
    xp = sorted(random.uniform(range_min, range_max) for _ in range(num_points))
    yp = [random.uniform(range_min, range_max) for _ in range(num_points)]
    return xp, yp


def validate_data(xp, yp):
    """
    Validate the input data for linear spline evaluation.

    Args:
        xp: A list of knots.
        yp: A list of corresponding values.

    Raises:
        ValueError: If the lengths of xp and yp do not match,
                    or if xp is not sorted in ascending order.
    """
    # Check if the knot arrays are empty
    if len(xp) == 0 or len(yp) == 0:
        raise ValueError("Error: Empty knot array!")

    # Check if the knot arrays have the same length
    if len(xp) != len(yp):
        raise ValueError("Lengths of xp and yp must match.")

    #Check if the knot arrays are sorted
    if xp != sorted(xp):
        raise ValueError("xp must be sorted in ascending order.")
