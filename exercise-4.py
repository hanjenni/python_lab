# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

print('enter the lengths of 3 sides of a triangle')
side_a = input('Enter the length of side a ')
side_b = input('Enter the length of side b ')
side_c = input('Enter the lenght of side c ')
if side_a == side_b == side_c:
    print(f'A triangle with sides of {side_a}, {side_b} & {side_c} is a equalateral triangle')
elif side_a != side_b and side_a != side_c and side_b != side_c:
    print(f'A triangle with sides of {side_a}, {side_b} & {side_c} is a scalene triangle')
elif side_a == side_b or side_a == side_c or side_b == side_c:
    print(f'A triangle with sides of {side_a}, {side_b} & {side_c} is a isosceles triangle')
