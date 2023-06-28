import numpy as np


def interp(x, xp, yp, method='point-slope'):
    """
    Evaluate a linear spline function using the specified interpolation method at a point x,
        defined by knots xp and values yp.
        Uses constant extrapolation outside the range of knots.

    Args:
        x (float): The point at which to evaluate the spline function.
        xp (array-like): A list of knots (sorted in ascending order).
        yp (array-like): A list of corresponding values.
        method (str, optional): Interpolation method to use. Options:
        'point-slope', 'piecewise-linear', 'matrix'.
            Defaults to 'point-slope'.

    Returns:
        float: The interpolated value at the given point.
    """
    if method == 'point-slope':
        return interp_point_slope(x, xp, yp)
    elif method == 'piecewise-linear':
        return interp_piecewise_linear(x, xp, yp)
    elif method == 'matrix':
        return interp_matrix(x, xp, yp)
    else:
        raise ValueError(f"Invalid interpolation method: {method}")


def interp_point_slope(x, xp, yp):
    """
    Evaluate the linear spline function using the point-slope formula.

    Args:
        x (float): The point at which to evaluate the spline.
        xp (array-like): List or array of knots (x-coordinates).
        yp (array-like): List or array of values corresponding to the knots (y-coordinates).

    Returns:
        float: The interpolated value at the given point.
    """
    n = len(xp)

    # Check if x is outside the range of knots
    if x < xp[0]:
        return yp[0]  # Constant extrapolation using the first knot's value
    elif x > xp[-1]:
        return yp[-1]  # Constant extrapolation using the last knot's value

    # Compute the interpolated value using Point-slope formula
    for i in range(n - 1):
        if x >= xp[i] and x <= xp[i + 1]:
            slope = (yp[i + 1] - yp[i]) / (xp[i + 1] - xp[i])
            return yp[i] + (x - xp[i]) * slope

    return np.nan


def interp_piecewise_linear(x, xp, yp):
    """
    Evaluate the linear spline function using piecewise linear interpolation with constant extrapolation.

    Args:
        x (float): The point at which to evaluate the spline.
        xp (array-like): List or array of knots (x-coordinates).
        yp (array-like): List or array of values corresponding to the knots (y-coordinates).

    Returns:
        float: The interpolated value at the given point.
    """
    n = len(xp)

    # Handle extrapolation
    if x <= xp[0]:
        return yp[0]
    elif x >= xp[n - 1]:
        return yp[n - 1]

    # Find the interval where the point falls
    i = 0
    while x > xp[i + 1]:
        i += 1

    # Perform piecewise linear interpolation
    interval_x = xp[i + 1] - xp[i]
    interval_y = yp[i + 1] - yp[i]
    t = (x - xp[i]) / interval_x
    return yp[i] + t * interval_y


def interp_matrix(x, xp, yp):
    """
    Evaluate the linear spline function using matrix representation with constant extrapolation.

    Args:
        x (float): The point at which to evaluate the spline.
        xp (array-like): List or array of knots (x-coordinates).
        yp (array-like): List or array of values corresponding to the knots (y-coordinates).

    Returns:
        float: The interpolated value at the given point.
    """
    n = len(xp)

    # Handle extrapolation
    if x <= xp[0]:
        return yp[0]
    elif x >= xp[n - 1]:
        return yp[n - 1]

    # Construct the linear system of equations
    A = np.zeros((n, n))
    b = np.zeros(n)

    for i in range(1, n - 1):
        A[i, i - 1] = xp[i] - xp[i - 1]
        A[i, i] = 2 * (xp[i + 1] - xp[i - 1])
        A[i, i + 1] = xp[i + 1] - xp[i]
        b[i] = 6 * ((yp[i + 1] - yp[i]) / (xp[i + 1] - xp[i]) - (yp[i] - yp[i - 1]) / (xp[i] - xp[i - 1]))

    # Set boundary conditions for constant extrapolation
    A[0, 0] = 1
    A[n - 1, n - 1] = 1

    # Solve the linear system to obtain the coefficients
    c = np.linalg.solve(A, b)

    # Find the interval where the point falls
    i = 0
    while x > xp[i + 1]:
        i += 1

    # Evaluate the spline using matrix representation
    h = xp[i + 1] - xp[i]
    t = (x - xp[i]) / h
    p1 = (1 - t) * yp[i]
    p2 = t * yp[i + 1]
    p3 = ((t ** 3 - t) / 6) * ((yp[i + 1] - yp[i]) / h - (h / 6) * (c[i + 1] - c[i]))
    return p1 + p2 + p3