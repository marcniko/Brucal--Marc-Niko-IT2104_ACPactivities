set1 = {8, 16, 24, 32, 44}
set2 = {7, 14, 8, 32, 21}

set1_minus_set2 = set1 - set2
set2_minus_set1 = set2 - set1

union_sets = set1 | set2

symmetric_difference_set2_set1 = set2 ^ set1
symmetric_difference_set1_set2 = set1 ^ set2

intersection_set1_set2 = set1 & set2
intersection_set2_set1 = set2 & set1

print("Set Difference (set1 - set2):", set1_minus_set2)
print("Set Difference (set2 - set1):", set2_minus_set1)
print("Union of Sets (set1 | set2):", union_sets)
print("Symmetric Difference (set2 ^ set1):", symmetric_difference_set2_set1)
print("Symmetric Difference (set1 ^ set2):", symmetric_difference_set1_set2)
print("Set Intersection (set1 & set2):", intersection_set1_set2)
print("Set Intersection (set2 & set1):", intersection_set2_set1)
