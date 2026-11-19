# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a playable Hangman game in Python to practice strings, lists, loops, conditionals, random selection, and user input.

## 📝 Tasks

### 🛠️ Set Up the Game

#### Description
Use the provided starter code to choose a secret word and prepare the game state before play begins.

#### Requirements
Completed program should:

- Randomly select a secret word from the provided `words` list.
- Track the letters the player has guessed and the number of incorrect guesses.
- Set a maximum number of incorrect guesses.
- Display the secret word as underscores, with correctly guessed letters revealed.

### 🛠️ Play a Round of Hangman

#### Description
Create a game loop that accepts guesses, updates the game state, and ends when the player wins or runs out of attempts.

#### Requirements
Completed program should:

- Prompt the player to guess a letter and compare it with the secret word.
- Reveal matching letters or increase the incorrect-guess count when a guess is wrong.
- Continue displaying the word's progress and remaining attempts after each guess.
- End when all letters are guessed or the maximum number of incorrect guesses is reached.
- Display a clear win or loss message; on a loss, reveal the secret word.
