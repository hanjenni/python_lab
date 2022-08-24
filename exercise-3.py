# exercise-03 Calculate Dog Years

# Write the code that:
# 1. Prompts the user to enter a dog's age in human years like this:
#      Input a dog's age in human years: 
# 2. Calculates the equivalent dog years, where:
#      - The first two years count as 10 years each
#      - Any remaining years count as 7 years each
# 3. Prints the answer in the following format:
#      The dog's age in dog years is xx

# Hint:  Use the int() function to convert the string returned from input() into an integer


h_years = int(input('input a dogs age into human years:'))
if h_years < 3:
    d_years = human_years * 10
else:
    d_years = 20 + (h_years- 2) * 7
print(f'the dogs age in dog years is {d_years}')