#Write the program which print the Fibonacci series of a number

def fibonacci_series(n):
    fib_series = [0, 1]  # Initialize Fibonacci series with first two elements
    while fib_series[-1] + fib_series[-2] <= n:
        next_fib = fib_series[-1] + fib_series[-2]  # Calculate next Fibonacci number
        fib_series.append(next_fib)  # Add next Fibonacci number to the series
    return fib_series

# Test the function
number = int(input("Enter a number: "))
fib_series = fibonacci_series(number)
print("Fibonacci series up to", number, ":", fib_series)

