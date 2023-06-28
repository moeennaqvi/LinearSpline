from linear_spline import interp
from data_utils import generate_synthetic_data, validate_data
from plotting import plot_linear_spline

if __name__ == '__main__':
    # Generate synthetic data
    num_points = 10
    range_min = 0
    range_max = 10
    xp, yp = generate_synthetic_data(num_points, range_min, range_max)

    # Validate the data
    validate_data(xp, yp)

    # Evaluate the linear spline function at multiple points
    x_values = [2.2, 4.3, 6.7, 8]
    interpolated_values = [interp(x, xp, yp, 'point-slope') for x in x_values]
    # Print the evaluated values
    print("Evaluated values:")
    for x, y in zip(x_values, interpolated_values):
        print(f"x = {x}, Linear-Spline = {y}")

    # Plot the linear spline function and the interpolated points
    plot_linear_spline(xp, yp, x_values, interpolated_values)