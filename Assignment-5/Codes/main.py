# B.ASLI
# CS21BTECH11011
# PROBABILITY

# probability that A occur
p_a = float(0.54)

# probability that B occur
p_b = float(0.69)

# probability that both occur
p_ab = float(0.35)

# probability that atleast one of A or B occur
p_atleast_one_occur = float(p_a + p_b - p_ab)

# probability that both not occur
p_both_notoccur = float(1 - p_atleast_one_occur)

# probability that only A occurs
p_only_A = float(p_a - p_ab)
p_only_A = "{:.2f}".format(p_only_A)

# probability that only B occurs
p_only_B = float(p_b - p_ab)
p_only_B = "{:.2f}".format(p_only_B)

print("probability that atleast one of A or B occur is ", p_atleast_one_occur)
print("probability that both not occur is ", p_both_notoccur)
print("probability that only A occurs is  ", p_only_A)
print("probability that only B occurs is  ", p_only_B)
