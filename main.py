# A = 90 - 100

# B = 80 - 89

# C = 70 - 79

# D = 60 - 69

# E = 50 - 59

# F = 0 - 49

score = int(input("Enter your score out of 100 :"))
if score <= 100 and  score >= 90:
    print("You got an A!")

elif score <= 89 and  score >= 80:
    print("You got an B!")

elif score <= 79 and  score >= 70:
    print("You got an C!")

elif score <= 69 and  score >= 60:
    print("You got an D!")

elif score <= 59 and  score >= 50:
    print("You got an E!")

elif score <= 49 and  score >= 0:
    print("You got an F!")

else:
    print("Score is invalid")

    