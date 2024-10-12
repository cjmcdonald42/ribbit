     package:   ribbit.py
      author:   Charles J McDonald <<cmcdonald@woonsocketschools.com>>
        date:   2024.10.12
     version:   0.1
    maturity:   inDev

# ribbit
A reimagining of the game Bulls and Cows. Our version uses a swampy theme with frogs and toads.

## History:
Bulls and cows is a code-breaking paper-and-pencil game for two or more players. The game is played in turns by two
opponents who aim to decipher the other's secret code by trial and error.

Bulls and cows predates the commercially marketed, 1971 Hasbro board game “Mastermind” (see inset picture) and the
word-based version predates the hit word game Wordle. “Mastermind” is played with 6 colours of pegs using Black and
White pegs to indicate Bulls and Cows. A version known as MOO was widely available for early mainframe computers, Unix
and Multics systems, among others.

## Directions:
The first player is the Swampmaster. They secretly choose a three-digit number using the numbers zero to 9 with no
duplicates. The second player, the Amphibian-Tamer, gets 10 tries to guess the secret number. After each guess, the
Swampmaster “scores” using the following code:

**Swamp**: None of the digits in your guess are in the secret code.

**Frog**: One digit in your guess is correct and in the correct position of the secret code. Please note that if you
          have three Bulls, you win and may lead a victory dance of one lap about the room!

**Toad**: One digit of your guess is present in the secret code, but in the wrong position. If you get three Cows,
          your guess has all the correct digits, but all in the wrong place!

## Development Cycle
### Round 1:
- [x] Take notes during our sample playthrough.
- [x] Plan out your game using pseudocode with a healthy amount of comments.
- [x] Code the game of Bulls and Cows as described: Numbers 0 through 9, choose three digits, no duplicates.
- [x] Assume all input is valid
- [x] The Keymaster gets 10 tries. Instead of Bulls, Cows, and Bagels, develop a custom naming system.
- [x] Reward a successful Keymaster for breaking the code.

### Round 2:
- [ ] Proof input for validity
- [ ] Allow the Gatemaster to choose the number of digits in the code. Consider what reasonable limits this option should have.
- [ ] Allow the Gatemaster the option of using duplicate numbers.

### Round 3:
- [ ] The board with each line and its score should be updated and reprinted each round before asking for the next guess - or the player should have the option of printing a table with guesses and responses thus far.
- [ ] Create a scoring system based on the number or tries, Bulls, and Cows. Present the final score to the winner.
- [ ] Consider the player experience and create a UI that is easy to read and yet very informative.

### Challenge Round:
- [ ] Allow the game to be played by one person with the computer taking the role of the Gatekeeper.
