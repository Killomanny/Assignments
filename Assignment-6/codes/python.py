# B.ASLI
# CS21BTECH11011
# PROBABILITY


# probability that A occur ( 1st child is girl )
p_a = float(0.50)

# probability that B occur ( 2nd child is girl )
p_b = float(0.50)

# probability that both occur ( 1st child and 2nd child both are girls )
p_ab = float(p_a*p_b)


# probability that atleast one of A or B occur
p_aoc = float(p_a + p_b - p_ab)

p_boga = float(p_ab) / p_aoc
p_boga = "{:.2f}".format(p_boga)

print("probability that both occur given that B occurs is ", p_a)

print("probability that both occur given that at least one occurs is ", p_boga)
