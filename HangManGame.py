import random
words = ('apple','orange','kiwi')
s = random.choice(words)
print(s)
l = len(s)
print(l, "l")
guess = []
guessed = []
failures = 0
success = 0
solved = []
guessWord = ''
for i in range(0,l):
    guess.append('_')
while success != l and failures < 10:
    print(guess)
    print("Guess the letters  ")
    A = input()
    for i in range(0,l):
        if A == s[i] and i not in guessed:
            print(s[i])
            guess[i] = A
            guessed.append(i)
            success += 1
        if A not in s:
            failures += 1
            break


for i in range(len(guess)):
    guessWord += guess[i]

if guessWord == s:
    print("you won")
else:
    print("you lost")