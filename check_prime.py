num = int(input('number to check: '))

num_range = range(2, num - 1)

prime = True

i = 2

while prime == True and i < num:

    if num%i == 0:
      prime = False
    
    i += 1

if prime == True:
  print('is prime')
else:
  print('not prime')