import deck

def player_turn(player, player_hand, main_deck):
    player_hand.move_random_card(main_deck)
    print("Your second card is " + player_hand[1].card_eng_name)
    hand_value = calculate_hand(player_hand)
    #check bj
    print("You have " + str(hand_value))
    if hand_value == "bj":
        pass
    elif len(player_hand) == 2:
        #check split        
        if player_hand[0].card_point == player_hand[1].card_point:
            user_answer = user_choice("do you want to split?[Y/N]")
            split_decision(user_answer, player, player_hand, main_deck)
        #check double
        elif hand_value == 20 and player_hand[0].card_point == 1 or hand_value == 20 and player_hand[1].card_point ==1 \
        or hand_value == 19 and player_hand[0].card_point == 1 or hand_value == 19 and player_hand[1].card_point ==1 \
        or hand_value == 9 or hand_value == 10:
            user_answer = user_choice("do you want to double down?[Y/N]")
            double_decision(user_answer, player, player_hand, main_deck)
        else:
            hit_decision_loop(player, player_hand, main_deck)
    else:
        hit_decision_loop(player, player_hand, main_deck)
    return player_hand
        
def calculate_hand(hand):
    if len(hand) == 2:
        if hand[0].card_point == 1 or hand[1].card_point == 1:
            if hand[0].card_point == 10 or hand[1].card_point == 10:
                hand_value = "bj"
            else:
                hand_value = 0
                for i in hand:
                    hand_value = hand_value + i.card_point
                if hand_value <= 10:
                    hand_value = hand_value + 10
        else:
            hand_value = 0
            for i in hand:
                hand_value = hand_value + i.card_point
    else:
        hand_value = 0
        Ace = False
        for i in hand:
            hand_value = hand_value + i.card_point
            if i.card_point == 1:
                Ace = True
            else:
                pass
        if Ace == True and hand_value <= 10:
            hand_value = hand_value + 10 
        else:
            pass
    return hand_value
        
def check_winner(player, player_hand, dealer_hand):
    player_point = calculate_hand(player_hand)
    print("you have " + str(player_point))
    dealer_point = calculate_hand(dealer_hand)
    print("the dealer has " + str(dealer_point))
    if player_point == "bj":
        if dealer_point == "bj":
            payout = 1
            outcome = "it's a draw"
        else:
            payout = 2.5
            outcome = "you won 1.5x with a bj"
    elif player_point > 21:
        payout = 0
        outcome = "you lose"
    elif player_point == dealer_point:
        payout = 1
        outcome = "it's a draw"
    elif dealer_point > 21 or player_point > dealer_point:
        payout = 2
        outcome = "you won"
    else:
        payout = 0
        outcome = "you lose"
    if player_hand.double == True:
        payout = payout * 2
    print(outcome)
    player.acct_balance = player.acct_balance + player.bet * payout
    print("your bankroll is now " + str(player.acct_balance))
        
def new_game(user_answer, player, dealer):
    if user_answer == "Y":
        player.hand.clear()
        player.bet = 0
        dealer.hand.clear()
    else:
        pass
    
def hit_decision(user_answer, player, player_hand, main_deck):
    if user_answer == "Y":
        player_hand.move_random_card(main_deck)        
    else:
        hand_value = calculate_hand(player_hand)
        player.add_hand_value(hand_value)
    return player_hand

def split_decision(user_answer, player, player_hand, main_deck):
    if user_answer == "Y":
        split_hand = deck.Deck()
        split_hand.move_random_card(player_hand)
        player.add_deck(split_hand)
        bet_amount = player.bet
        bet_amount = bet_amount*(-1)
        player.adjust_fund(bet_amount)
        player_turn(player, player_hand, main_deck)
    elif player_hand[0] == 5:
        user_choice = user_choice("do you want to double down?[Y/N]")
        double_hand(player, player_hand, main_deck)
    else:
        hit_decision_loop(player, player_hand, main_deck)
    
def double_decision(user_answer, player, player_hand, main_deck):
    if user_answer == "Y":
        bet_amount = player.bet
        bet_amount = bet_amount * -1
        player.adjust_fund(bet_amount)
        player_hand.move_random_card(main_deck)
        print(player_hand[2].card_eng_name)
        hand_value = calculate_hand(player_hand)
        player.add_hand_value(hand_value)
        player_hand.double = True
    else:
        hit_decision_loop(player, player_hand, main_deck)
           
def dealer_turn(player_hand, dealer_hand, main_deck):
    print("the dealer's hand is as follow:")
    dealer_hand.hand_reader()
    player_point = calculate_hand(player_hand)
    if player_point == "bj":
        if dealer_hand[0].card_point == 1 or dealer_hand[0].card_point == 10:
            dealer_hand.move_random_card(main_deck)
            dealer_hand.hand_reader()
        else:
            pass            
    elif player_point > 21:
        pass
    else:
        dealer_point = calculate_hand(dealer_hand)
        print("the dealer has " + str(dealer_point))
        if dealer_point == "bj":
            pass
        elif dealer_point < 17:
            dealer_hand.move_random_card(main_deck)
            dealer_turn(player_hand, dealer_hand, main_deck)
        elif dealer_point == 17:
            if dealer_hand[0].card_point == 1 or dealer_hand[1].card_point == 1:
                if dealer_hand[0].card_point == 6 or dealer_hand[1].card_point == 6:
                    dealer_hand.move_random_card(main_deck)
                    dealer_turn(player_hand, dealer_hand, main_deck)
                else:
                    pass
            else:
                pass
        else:
            pass
            
def user_choice(question):
    user_answer = input(question)
    if user_answer == "Y" or user_answer =="N":
        pass
    else:
        print("please answer [Y/N]")
        user_answer = user_choice(question)
    return user_answer
    
def hit_decision_loop(player, player_hand, main_deck):
    while True:
        user_answer = user_choice("do you want an additional card?[Y/N]")
        player_hand = hit_decision(user_answer, player, player_hand, main_deck)
        hand_value = calculate_hand(player_hand)
        print("you have " + str(hand_value))   
        if hand_value > 21 or user_answer == "N":
            break
        else:
            continue