# Blackjack_game
Blackjack Game in Python
A simple, interactive text-based Blackjack game built with Python. The player competes against the computer (dealer) to reach a score of 21 without exceeding it, following traditional Blackjack rules.

Features:
Classic Blackjack gameplay where the player plays against the dealer.
The game handles card dealing, shuffling, and calculating scores.
The user can choose to hit (draw a card) or stand (end the turn).
Automatic gameplay adjustments such as the dealer drawing cards until they reach a score of 17 or higher.
Checks for Blackjack (a score of 21 with two cards) and busts (going over 21).
A clean and simple user interface displaying the player's and dealer's cards, with ASCII art to enhance the visual experience.
How to Play:
Clone the repository or download the project.
Run the blackjack.py file in your terminal or IDE.
Follow the on-screen prompts to make decisions (hit or stand) and try to get closer to 21 than the dealer without going over!
Technologies Used:
Python (No external libraries required, pure Python implementation)
Game Flow:
The player is dealt two cards, and the dealer is dealt two cards (one face-up and one face-down).
The player can choose to draw more cards or stand based on their hand.
The dealer draws cards until their hand total is 17 or higher.
The winner is determined based on who has the higher score without exceeding 21.
Rules:
Aces are worth 11 points unless that would cause a bust, in which case they are worth 1 point.
Face cards (King, Queen, Jack) are worth 10 points each.
If the player or dealer gets exactly 21 with two cards, it's a Blackjack!
If the player's score exceeds 21, they lose automatically (bust).
