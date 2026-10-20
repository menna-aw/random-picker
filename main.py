import random
choices=[1,2,3,4,5]
for i in range(1,6):
  choice = random.choice(choices)
  print("The random choice is: ", choice)
print("The random choices are: ", choices)
print("Done!")