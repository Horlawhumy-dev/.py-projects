# It is commonly said that one human year is equivalently 7 dog years.
# 1 human year = 7 dog years.
human_years = float(input("What years are you?: "))
negative = "-"
if human_years % 2 == 0 and human_years >= 2: #
    Dog_Age = (human_years / 2) * 10.5
    print("Your age in dog years is ", Dog_Age)
elif human_years % 2 != 0 and human_years > 2:
    Dog_Age = ((human_years % 2) * 4) + ((human_years / 2) * 10.5)
    print("Your equivalent age to dog years is ", Dog_Age)
elif human_years < 2 and human_years > 1:
    Dog_Age = 4 + ((2 - human_years) * 4)
    print("Your age in dog years is ", Dog_Age)
elif human_years == 1:
    print("Your age is 4 dog years ")
elif human_years < 1:
    print("You are ", (human_years * 4), " in dog years")
else:
    if human_years == negative:
        print("Your age entered  must positive")





