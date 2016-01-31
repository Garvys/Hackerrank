N , integers = int(input()), input().split()
print(all([int(integer) > 0 for integer in integers]) and any([string == string[::-1] for string in integers]))