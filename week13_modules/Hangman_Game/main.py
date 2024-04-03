import random
from hangman_ascii import stages, logo
from words import words
keep_playing = True
while keep_playing:

    # choose a random words
    chosen_word = random.choice(words)
    len_chosen_word = len(chosen_word)
    # print(chosen_word)
    print(logo)
    # Create a list with as many dashes as letters in word
    word_display = []
    for _ in range(len_chosen_word):
        word_display.append('_')

    # have the game keep playing

    # take a flag to keep track of game result
    game_over = False
    # take a counter to keep track of lives left
    lives_left = 7
    # keep track f incorrect guessed letters
    incorrect_guessed_letters = []

    game_over = False
    while not game_over:
        print(word_display)
        guessed_letter = input('Guess a letter: ').lower()

        if guessed_letter in word_display or guessed_letter in incorrect_guessed_letters:
            print(f"You have already guessed {guessed_letter} try again")
            print(f"Number of lives left: {lives_left}")
        elif guessed_letter not in chosen_word:
            print(f"Your guess {guessed_letter} is not in the chosen word. You lose a life")
            lives_left -= 1
            print(f"Number of lives left: {lives_left}")
            incorrect_guessed_letters.append(guessed_letter)
            if lives_left == 0:
                game_over = True
                print(f"Game Over the word was {chosen_word}")
        else:
            for idx, val in enumerate(chosen_word):
                if val == guessed_letter:
                    word_display[idx] = guessed_letter
                    print(f"Your guess {guessed_letter} is the {idx + 1} spot")
            print(f"Number of lives left: {lives_left}")
        if '_' not in word_display:
            game_over = True
            print(f"You win the word is {chosen_word}")
        print(stages[lives_left])
    user_answer = input("Do you want to keep playing? y/n: ").lower()
    if user_answer == "n":
        keep_playing = False