l1 = [1, 2, 4, 7, 9, 10, 524, 46, 65]
# Create a list containing all second powers of the elements from l1
# Sum all those second powers of l1

l1_2nd_powers = [x**2 for x in l1]
print(l1)
print(l1_2nd_powers)
print(sum(l1_2nd_powers))