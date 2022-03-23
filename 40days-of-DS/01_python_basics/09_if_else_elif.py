ahsan_age = 1
required_age_at_school = 5

# Question: can ahsan go to school?
if ahsan_age == required_age_at_school:
    print("Congratulations! Ahsan can join the school.")
elif ahsan_age > required_age_at_school:
    print("Ahsan should join higher secondary school.")
elif ahsan_age <= 2:
    print("You should take care of Ahsan, he is still a baby!")
else:
    print("Ahsan can not go to school.")