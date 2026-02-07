from functools import reduce 

numbers = [14, 20,5, 6, 26, 10]

mult_by_two = list(map(lambda x: x * 2, numbers))
sum_of_numbers_mult_by_two = reduce(lambda x, y: x+y, mult_by_two)

print(f"List: {numbers}")
print(f"mult_by_two: {mult_by_two}")
print(f"sum_of_numbers_mult_by_two: {sum_of_numbers_mult_by_two}")

sum_of_numbers_mult_by_two_shorthand = reduce(lambda x, y: x + y, map(lambda x: x * 2, numbers))
print(f"The result of the chained function is: {sum_of_numbers_mult_by_two_shorthand}")

# sum of all even numbers

sum_of_ev = reduce(lambda x, y: x + y, filter(lambda x: x % 2 == 0, numbers))
print(f"sum_of_ev: {sum_of_ev}")
print(f"from {list(filter(lambda x: x % 2 == 0, numbers))}")

print(f"max: {max(numbers)}, min: {min(numbers)}")