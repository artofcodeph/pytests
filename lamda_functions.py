from functools import reduce 

numbers = [14, 20,5, 6, 26, 10]

mult_by_two = list(map(lambda x: x * 2, numbers))
sum_of_numbers_mult_by_two = reduce(lambda x, y: x+y, mult_by_two)

print(f"List: {numbers}")
print(f"mult_by_two: {mult_by_two}")
print(f"sum_of_numbers_mult_by_two: {sum_of_numbers_mult_by_two}")
