import random  # imports the random functions 
from hangman_ascii import stages, logo  # Imports the stages and logo array and variable from the ascii file
from words import words  # imports the list of words from the word file 
keep_playing = True  # sets the variable to keep playing as true so that the game starts 
while keep_playing:  # as long as keep playing is true the game will restart

    # choose a random words
    chosen_word = random.choice(words)  # Uses the random choice function to pick a word from the word list to pick a word.
    len_chosen_word = len(chosen_word)  # Gets the length of the word that was picked
    # print(chosen_word)
    print(logo)  # print the logo from the ascii file
    # Create a list with as many dashes as letters in word
    word_display = []  # creates a placeholder array for the blanks and correct letters
    for _ in range(len_chosen_word):  # for how long the length of the word is put a _ in the array
        word_display.append('_')  # Append the array to add the _

    # have the game keep playing

    # take a flag to keep track of game result
    game_over = False  # set the game over to false because the game needs to keep going 
    # take a counter to keep track of lives left
    lives_left = 7  # Sets lives left before the game
    # keep track f incorrect guessed letters
    incorrect_guessed_letters = []  # Creates an array that holds all of the guesses that were incorect 
 
    while not game_over:  # While the game over is not true the game keeps playing 
        print(word_display)  # To start each round print the correct letters and underscores
        guessed_letter = input('Guess a letter: ').lower()  # gets the guessed letter and makes it lowercase

        if guessed_letter in word_display or guessed_letter in incorrect_guessed_letters:  # If the guessed letter is in the correct guessed or incorect guessed
            print(f"You have already guessed {guessed_letter} try again")  # print to try again
            print(f"Number of lives left: {lives_left}")  # prints number of lives 
        elif guessed_letter not in chosen_word:  # else if the guess letter is not in the chosen word
            print(f"Your guess {guessed_letter} is not in the chosen word. You lose a life")  # print the guess ed letter and say it is not in the chosen word and we lose a life
            lives_left -= 1  # subtract a life
            print(f"Number of lives left: {lives_left}")  # print the lives left
            incorrect_guessed_letters.append(guessed_letter)  # add the guessed letter to incorrect guessed
            if lives_left == 0:  # if the lives left is 0 game is over
                game_over = True  # change game over to true 
                print(f"Game Over the word was {chosen_word}")  # print the game is over and the chosen word
        else:  # the only other option is if it is correct 
            for idx, val in enumerate(chosen_word):  # for the number of letter in chosen word run the for loop with the val of the index of the number of the for loop
                if val == guessed_letter:  # if the value we are on is equal to guessed letter
                    word_display[idx] = guessed_letter  # add the letter to the display in the correct spot by using the idx in for loop
                    print(f"Your guess {guessed_letter} is the {idx + 1} spot")  # print that you guessed the correct letter and what spot it is in 
            print(f"Number of lives left: {lives_left}")  # print number of lives once you put the letters in correct spot 
        if '_' not in word_display:  # if there are no more _ in the word display then they guessed all of the letters
            game_over = True  # change the game over to true since they guessed the word
            print(f"You win the word is {chosen_word}")  # print they won and guessed word
        print(stages[lives_left])  # after every turn print the lives left ascii 
    user_answer = input("Do you want to keep playing? y/n: ").lower()  # get the users answer for if they want to keep playing with y or n
    if user_answer == "n":  # if the user picked n then end the game but if they put anything else then keep the value the same and game will restart
        keep_playing = False  # change keep playing to false so the game ends