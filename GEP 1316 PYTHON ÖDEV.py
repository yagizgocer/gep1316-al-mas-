"GEP 1316 ÖDEV"

"Problem 7"
def is_prime(n):
    """Check if a number is a prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % i + 2 == 0:
            return False
        i += 6
    return True

def find_nth_prime(n):
    """Find the nth prime number."""
    count = 0
    candidate = 2
    while count < n:
        if is_prime(candidate):
            count += 1
        candidate += 1
    return candidate - 1

# Find the 10001st prime number
nth_prime = find_nth_prime(10001)
print(nth_prime)

"Problem 1"
# Initialize a variable to store the sum
total_sum = 0

# Loop through all numbers below 1000
for number in range(1000):
    # Check if the number is a multiple of 3 or 5
    if number % 3 == 0 or number % 5 == 0:
        # Add the number to the total sum
        total_sum += number

# Print the final sum
print("The sum of all multiples of 3 or 5 below 1000 is:", total_sum)

"Problem 9"
# Loop through possible values of a and b
for a in range(1, 1000):
    for b in range(a + 1, 1000 - a):
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            # If a^2 + b^2 == c^2, we have found the triplet
            print(f"The Pythagorean triplet is: a = {a}, b = {b}, c = {c}")
            print(f"The product abc is: {a * b * c}")
            break
    else:
        continue
    break

"Problem 10"
def sieve_of_eratosthenes(limit):
    # Create a boolean array "is_prime[0..limit]" and initialize
    # all entries it as true. A value in is_prime[i] will
    # finally be false if i is Not a prime, else true.
    is_prime = [True] * limit
    is_prime[0] = is_prime[1] = False # 0 and 1 are not prime numbers
    
    p = 2
    while (p * p < limit):
        # If is_prime[p] is still true, then it is a prime
        if (is_prime[p] == True):
            # Updating all multiples of p to false
            for i in range(p * p, limit, p):
                is_prime[i] = False
        p += 1
    
    # Collect all prime numbers
    prime_numbers = [p for p in range(limit) if is_prime[p]]
    return prime_numbers

# Set the limit
limit = 2000000

# Get all primes below the limit
primes_below_limit = sieve_of_eratosthenes(limit)

# Calculate the sum of all prime numbers below the limit
sum_of_primes = sum(primes_below_limit)

print("The sum of all primes below two million is:", sum_of_primes)


"Problem 16"
# Calculate 2 raised to the power of 1000
number = 2 ** 1000

# Convert the number to a string to iterate over each digit
number_str = str(number)

# Initialize the sum of digits to 0
sum_of_digits = 0

# Iterate over each digit in the string representation of the number
for digit in number_str:
    # Convert the digit back to an integer and add it to the sum
    sum_of_digits += int(digit)

# Print the final sum of the digits
print("The sum of the digits of the number 2^1000 is:", sum_of_digits)

"Problem 19"
def is_leap_year(year):
    """Returns True if the given year is a leap year, otherwise False."""
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

def days_in_month(year, month):
    """Returns the number of days in the given month of the given year."""
    if month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    if month == 2:
        return 29 if is_leap_year(year) else 28
    return 31

def count_sundays_on_first():
    """Counts the number of Sundays that fell on the first of the month during the twentieth century."""
    day_of_week = 1  # 1 Jan 1900 was a Monday, so 1 Jan 1901 was a Tuesday (day_of_week = 2)
    sundays_on_first = 0

    for year in range(1900, 2001):
        for month in range(1, 13):
            if year >= 1901:
                if day_of_week == 0:  # 0 means Sunday
                    sundays_on_first += 1
            # Move to the first day of the next month
            day_of_week = (day_of_week + days_in_month(year, month)) % 7

    return sundays_on_first

print("Number of Sundays that fell on the first of the month during the twentieth century:", count_sundays_on_first())

"Problem 22"
def read_names(filename):
    """Reads names from the given filename and returns a sorted list of names."""
    with open(filename, 'r') as file:
        content = file.read()
        # Remove quotes and split the names by comma
        names = content.replace('"', '').split(',')
        # Sort the names in alphabetical order
        names.sort()
    return names

def alphabetical_value(name):
    """Calculates the alphabetical value of a given name."""
    return sum(ord(char) - ord('A') + 1 for char in name)

def calculate_name_scores(names):
    """Calculates the total of all the name scores in the given list of names."""
    total_score = 0
    for index, name in enumerate(names):
        # Calculate the alphabetical value of the name
        value = alphabetical_value(name)
        # Calculate the name score
        score = value * (index + 1)
        # Add the name score to the total score
        total_score += score
    return total_score

# Read names from the file
filename = 'names.txt'
names = read_names(filename)

# Calculate the total name score
total_score = calculate_name_scores(names)

print("The total of all the name scores in the file is:", total_score)

"Problem 24"
import math

def get_lexicographic_permutation(digits, position):
    permutation = []
    k = position - 1  # to adjust for 0-based indexing
    n = len(digits)
    
    # Calculate factorials
    factorials = [math.factorial(i) for i in range(n)]
    
    # Determine each digit of the permutation
    for i in range(n - 1, -1, -1):
        # Determine the index of the next digit
        idx = k // factorials[i]
        k %= factorials[i]
        
        # Append the digit at the calculated index
        permutation.append(digits.pop(idx))
    
    return ''.join(map(str, permutation))

# Define the digits and the position of the desired permutation
digits = list(range(10))
position = 1000000

# Get the millionth lexicographic permutation
result = get_lexicographic_permutation(digits, position)
print("The millionth lexicographic permutation of the digits 0 through 9 is:", result)

"Problem 31"
def count_ways_to_make_amount(coins, amount):
    # Initialize a list to store the number of ways to make each amount
    dp = [0] * (amount + 1)
    # There is one way to make amount 0: using no coins
    dp[0] = 1

    # Loop through each coin and update the dp array
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] += dp[x - coin]

    return dp[amount]

# Define the coins and the amount to be made
coins = [1, 2, 5, 10, 20, 50, 100, 200]
amount = 200  # 2 pounds

# Calculate the number of ways to make the amount
number_of_ways = count_ways_to_make_amount(coins, amount)
print("Number of ways to make £2:", number_of_ways)

"Problem 2"
def sum_even_fibonacci(limit):
    a, b = 1, 2  # Starting values of the Fibonacci sequence
    total_sum = 0

    while a <= limit:
        if a % 2 == 0:
            total_sum += a
        a, b = b, a + b  # Move to the next Fibonacci numbers

    return total_sum

# Define the limit
limit = 4000000

# Calculate the sum of even-valued Fibonacci terms that do not exceed the limit
result = sum_even_fibonacci(limit)
print("The sum of the even-valued terms in the Fibonacci sequence whose values do not exceed four million is:", result)









