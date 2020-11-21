age = False
year_of_birth = False
Input = int(input('Enter your age/year of birth: '))
if age:
    print(f"You are {Input} yeras old")
elif year_of_birth:
    print(f"You are borned in the year {Input}")
if len(Input)==2:
    age=True
elif len(Input)==4:
    year_of_birth=True
