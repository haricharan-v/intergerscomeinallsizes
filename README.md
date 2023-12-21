# Power Calculator

This simple Python script allows you to calculate the power of two numbers and their sum. It includes input validation to ensure that the user provides valid and positive integers.

## Usage

1. Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/power-calculator.git
cd power-calculator
```

2. Run the script:

```bash
python power_calculator.py
```

3. Follow the prompts to enter the base and exponent for two numbers. The script will then calculate the power of each number and display the results.

## How to Use

The script provides a user-friendly interface to input two pairs of base and exponent. It ensures that the input is valid and positive, displaying appropriate error messages if the user provides invalid input.

### Functions

#### `get_valid_integer_input(prompt)`

This function takes a prompt as input and repeatedly prompts the user until a valid positive integer is provided. It handles invalid input gracefully and returns the validated integer.

#### `calculate_power(base, exponent)`

This function calculates the power of a given base raised to a given exponent and returns the result.

#### `main()`

The `main` function orchestrates the flow of the program. It uses the `get_valid_integer_input` function to obtain user input for two numbers and then calculates and displays the power of each number as well as their sum.

## Example

```bash
Enter the base of the first number: 2
Enter the exponent of the first number: 3

Enter the base of the second number: 4
Enter the exponent of the second number: 2

The power of the first number you entered is 8
The power of the second number you entered is 16

The sum of both of the powers is 24
```

## Input and Output

The script uses `stdin` for input and `stdout` for output. It provides clear prompts for the user to enter the required information and displays the results in a readable format.

## Error Handling

The script handles errors gracefully, providing informative error messages in case of invalid input or other exceptions during execution.
