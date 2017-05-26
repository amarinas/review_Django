import random
#make a list of words
words = [
'apple',
'banana',
'orange',
'coconut',
'strawberry',
'lime'
]

while True:
    start = input("press enter/return to start or enter Q to quit")
    if start.lower() == "q":
        break
# pick a random words
    secret_word = random.choice(words)
    bad_guesses = []
    good_guesses =  []

    while len(bad_guesses)< 7 and len(good_guesses) != len(secret_word):

        # draw guessed letters and strikes
        # draw spaces
        for letter in secret_word:
            if letter in good_guesses:

                print(leter, end='')
            else:
                print('-', end='')
        print('')
        print('Strikes: {}/7'.format(len(bad_guesses)))
        print('')
        # take guess
        guess = input("Guess a letter: ").lower()


# print win or lose
