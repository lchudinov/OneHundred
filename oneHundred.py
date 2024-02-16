from itertools import permutations

digits = [1, 2, 3, 4, 5, 6, 7]
solutions = []
one_hundred = 100

for i in range(7):
  number = digits[i]
  rest = digits[:i] + digits[i+1:]
  for perm in permutations(rest, 6):
    candidate = (number, 10 * perm[0] + perm[1], 10 * perm[2] + perm[3], 10 * perm[4] + perm[5])
    if one_hundred == sum(candidate):
      solutions.append(candidate)

print ("Solutions found:", len(solutions))
print ("Are solutions unique?", len(solutions) == len(set(solutions)))
print ("Are solutions correct?", all(one_hundred == sum(solution) for solution in solutions))
for solution in solutions:
  print (solution)
