# Linear Spline Project

This project provides a Python implementation of linear spline evaluation. It allows you to evaluate a linear spline function defined by knots and values at a specific point, with support for constant extrapolation outside the knot range.

## Prerequisites

To run this project, you need to have Python 3 installed on your system. You can download and install Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

## Installation

1. Clone the repository to your local machine:
    ```
    git clone https://github.com/moeennaqvi/linear-spline-project.git
    ```

2. Change to the project directory:
    ```
    cd linear-spline-project
    ```

3. (Optional) Set up a virtual environment to isolate project dependencies:
    ```
    python3 -m venv venv
    ```

4. (Optional) Activate the virtual environment:

- For Windows:
  ```
  venv\Scripts\activate.bat
  ```

- For macOS/Linux:
  ```
  source venv/bin/activate
  ```

5. Install the required dependencies:
    ```
    pip install -r requirements.txt
    ```

## Usage

The `main.py` file serves as the entry point for the project. You can run the project by executing the following command:

python main.py


The code in `main.py` demonstrates the usage of the linear spline evaluation functionality. It generates synthetic data, validates the data, plots the linear spline function, and evaluates the spline at a specific point.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

Feel free to use, modify, and distribute this code for both commercial and non-commercial purposes.
