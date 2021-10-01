import random,time

print("Choose one from ROCK-PAPER-SCISSOR while computer selects its own...")
user = input()
arr = ['ROCK','PAPER','SCISSOR']

computer = random.randint(1,3)
computer = arr[computer-1]
print("Computer chose: ",computer)
result = 0  # 0:no result, 1:user wins, 2:computer wins

if user == 'ROCK':
    if computer == 'SCISSOR':
        result = 1
    elif computer == 'PAPER':
        result = 2
elif user == 'PAPER':
    if computer == 'ROCK':
        result = 2
    elif computer == 'SCISSOR':
        result = 2
else:
    if computer == 'ROCK':
        result = 2
    elif computer == 'PAPER':
        result = 1

print("Winner is...", end='')
time.sleep(1)
if result == 0:
    print('DRAW')
elif result == 1:
    print("USER")
else:
    print("COMPUTER")
