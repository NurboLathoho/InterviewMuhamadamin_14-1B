# 1
# for i in range(1, 6):
#     print(f'{i} - 0')

# 2
# import random

# language = ["Python", "Java", "Kotlin", "JavaScript", "C#", "RUBY"]

# def randomaiser(lst=language):
#     result = random.choice(lst)

#     py = open('result.txt', 'w')
#     py.write(result)
#     py.close()

#     print(result)

# randomaiser()

# 3
names = ["azat", "zina", "kuma", "anna", "sas"]

result = filter(lambda name: name == name[::-1] , names)
print(list(result))