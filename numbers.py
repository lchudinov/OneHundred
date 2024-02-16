import itertools

top_digit = 7
numbers = 4
target = 100

digits = list(range(1, top_digit + 1))

total_equations = 0
unique_equs = set()

# First find digits that, being summed up, produce the ending zero.
# Note that it's a rather inefficient enumeration; we could for example calculate
# the 4th digit based off the first three.
for lows in itertools.combinations(digits, numbers):
    if sum(lows) % 10 == 0:
        # Now see if the remaining digits produce what we need
        highs = [ i*10 for i in digits if i not in lows ]
        if sum(lows) + sum(highs) == target:
            # We've got separate lists of tens and ones, let's print all combinations
            pad_length = len(lows) - len(highs)
            if pad_length > 0:
                highs = [0]*pad_length + highs
            for shuffled_lows in itertools.permutations(lows):
                # Not very efficient, but it's easier to do join() later
                nums = [ h + l for h, l in zip(highs, shuffled_lows) ]
                left_side = ' + '.join([ f"{num:3}" for num in nums ])
                unique_equs.add(frozenset(nums))
                # We could have used `target` in place of sum(), but sum()
                # additionally verifies that we've done correct calculations
                print(f"{left_side} = {sum(nums)}")
                total_equations += 1

print("---")
print(f"Total listed: {total_equations}")
print(f"Unique equations found: {len(unique_equs)}")
