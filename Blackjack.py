#*********************ashrit patel******************************
import random

def deal_card():
    """"Return from a random card from the deck """

    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calculate_scores(cards):
    """TAKE A LIST OF CARD AND RETURN FROM DEAL_CARDS """

    if sum(cards) == 21 and len(cards) == 21:
        return 0 
    

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(u_scores,c_scores):
    if u_scores == c_scores:
        return("It's a draw 😵‍💫!!")
    elif c_scores == 0 :
        return "Lose ,Opponent has a Blackjack 😱"
    elif u_scores == 0:
        return ("You win with a Blackjack 😎 ")
    elif u_scores > 21 :
        return("You went over ..You lose 🥴")
    elif c_scores > 21: 
        return("Opponent went over . You  Win 🥳")
    elif u_scores > c_scores: 
        return("You Win 🥳")
    else:
        return("You lose 🥴")
    

def play_game():
    
    print('''
          _____
         |A .  | _____
         | /.\ ||A ^  | _____
         |(_._)|| / \ ||A _  | _____
         |  |  || \ / || ( ) ||A_ _ |
         |____V||  .  ||(_'_)||( v )|
                |____V||  |  || \ / |
                       |____V||  .  |
                              |____V|
    ''')

    user_cards = []
    computer_cards = []
    computer_scores = -1
    user_scores = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())



    while not is_game_over:

        user_scores = calculate_scores(user_cards)
        computer_scores = calculate_scores(computer_cards)
        print(f"Your card : {user_cards}")
        print(f"Computer_cards : {computer_cards}")

        if user_scores == 0 or computer_scores == 0 or user_scores> 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' for yes and 'n' to pass :" )
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_scores != 0 and computer_scores < 17 : 
        computer_cards.append(deal_card())
        computer_scores = calculate_scores(computer_cards)


    #Print the final result :

    print(f"Your final hand: {user_cards}, final score: {user_scores}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_scores}")
    print(compare(user_scores, computer_scores))

while input("Do you want to play a game of Blackjack? Type 'y' for yes else 'no :   " ):
   # print("\n"*20)
    play_game()
