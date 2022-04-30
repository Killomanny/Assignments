# B.ASLI
# CS21BTECH11011
# PROBABILITY

# probability that Anil passes
p_a = float(0.05)

# probability that Anisha passes
p_b = float(0.10)

# probability that both passes
p_ab = float(0.02)

# probability that‘both Anil and Ashima will not qualify the examination
p_both_not_qualify = float(1 - p_a - p_b + p_ab)
p_both_not_qualify = "{:.2f}".format(p_both_not_qualify)

# probability that atleast one will qualify
p_atleast = float(1 - p_ab)
p_atleast = "{:.2f}".format(p_atleast)

# probability that only one of them will qualify the examination
p_only = float(p_a + p_b - p_ab - p_ab)
p_only = "{:.2f}".format(p_only)

print("probability that‘both Anil and Ashima will not qualify the examination is ", p_both_not_qualify)
print("probability that atleast one will qualify is ", p_atleast)
print("probability that only one of them will qualify the examination is ", p_only)
