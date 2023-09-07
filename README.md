# Hangman Game

Hangman is a classic word guessing game that can be played by two or more players. In this game, one player thinks of a word, phrase, or sentence, while the other player(s) attempt to guess it by suggesting letters within a certain number of guesses. The goal is to guess the word correctly before the "hangman" is fully drawn.

## Rules of the Game

1. **Word Selection**: One player (the "word chooser") selects a word, phrase, or sentence to be guessed by the other player(s). This word is kept secret.

2. **Guessing**: The player(s) who are trying to guess the word (the "guessers") take turns suggesting letters. They can suggest any letter from the alphabet.

3. **Wrong Guesses**: When a guesser suggests a letter that is not in the word, a part of a "hangman" figure is drawn. The hangman typically consists of a gallows and a stick figure.

4. **Limited Guesses**: The guessers have a limited number of guesses, often represented by the number of body parts in the hangman figure. Commonly, there are six incorrect guesses allowed before the game is lost.

5. **Winning**: The game is won when the guessers correctly guess all the letters in the word, phrase, or sentence before the hangman figure is completed.

6. **Losing**: If the hangman figure is fully drawn (all body parts are shown) before the word is guessed, the guessers lose the game.

## Example

Let's say the word chooser selects the word "HANGMAN" as the secret word. The hangman figure starts empty:

```
   -----
   |   |
       |
       |
       |
       |
```

The guessers take turns suggesting letters. If they guess a letter correctly, it is revealed in the word. If they guess incorrectly, a body part is added to the hangman figure. For example:

Guess: "A"

```
   -----
   |   |
       |
       |
       |
       |
```

Guess: "G"

```
   -----
   |   |
       |
       |
       |
       |
```

Guess: "N"

```
   -----
   |   |
       |
       |
       |
       |
```

Guess: "X" (incorrect)

```
   -----
   |   |
   O   |
       |
       |
       |
```

Guess: "M"

```
   -----
   |   |
   O   |
       |
       |
       |
```

Guess: "H"

```
   -----
   |   |
   O   |
       |
       |
       |
```

Guess: "Y" (incorrect)

```
   -----
   |   |
   O   |
   |   |
       |
       |
```

Guess: "Z" (incorrect)

```
   -----
   |   |
   O   |
  /|   |
       |
       |
```

Guess: "T" (incorrect)

```
   -----
   |   |
   O   |
  /|\  |
       |
       |
```

Guess: "E" (incorrect)

```
   -----
   |   |
   O   |
  /|\  |
  /    |
       |
```

Guess: "R" (incorrect)

```
   -----
   |   |
   O   |
  /|\  |
  / \  |
       |
```

Unfortunately, the hangman figure is now complete, and the guessers have lost the game.

This is the basic format of the Hangman game, and it can be adapted with variations in rules and word categories for added fun and challenge. Enjoy playing!
