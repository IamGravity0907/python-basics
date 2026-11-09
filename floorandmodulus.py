total    = 560       # total harvest in kg
bag_size = 25        # each bag holds 25 kg

bags     = total // bag_size  # 560 // 25 = 22 full bags
leftover = total % bag_size   # 560 % 25  = 10 kg left over

print("Full bags:", bags)      # Output: 22
print("Leftover:", leftover)   # Output: 10