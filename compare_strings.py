strings = ['john', 'rosie', 'john', 'santiago', 'michael', 'rosie']

equal_str = all(a == nexta for a, nexta in zip(strings, strings[1:])) # All equal
less_than = all(a < nexta for a, nexta in zip(strings, strings[1:])) # Strictly ascending

print(equal_str)
print(less_than)