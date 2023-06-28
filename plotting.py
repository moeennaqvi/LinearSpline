import matplotlib.pyplot as plt


def plot_linear_spline(xp, yp, evaluation_points=None, interpolated_values=None):
    """
    Plot the linear spline function using the given knots and values.

    Args:
        xp (list): List of knots (x-coordinates).
        yp (list): List of values corresponding to the knots (y-coordinates).
        evaluation_points (list, optional): List of points to be evaluated on the spline.
        interpolated_values (list, optional): List of interpolated values corresponding to the evaluation points.
    """
    # Plot the original data points
    plt.plot(xp, yp, 'bo-', label='Original Data')
    plt.xlabel('x')
    plt.ylabel('y')

    if evaluation_points and interpolated_values:
        # Plot the interpolated points if provided
        plt.plot(evaluation_points, interpolated_values, 'ro', label='Interpolated Points')

    plt.legend()
    plt.show()


def plotall_linear_spline(xp, yp, evaluation_points, *interpolated_values):
    """
    Plot the linear spline function defined by the knots and multiple sets of interpolated values.

    Args:
        xp (list): List of knots (x-coordinates).
        yp (list): List of values corresponding to the knots (y-coordinates).
        evaluation_points (list, optional): List of points to be evaluated on the spline.
        *interpolated_values: Variable number of lists containing interpolated values.
    """
    # Plot the original data points
    plt.plot(xp, yp, 'bo-', label='Original Data')
    plt.xlabel('x')
    plt.ylabel('y')

    for values in interpolated_values:
        # Plot the interpolated points if provided
        plt.plot(evaluation_points, values, 'ro', label='Interpolated Points')

    plt.legend()
    plt.show()
