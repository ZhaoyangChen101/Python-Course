# get a high score or higher score than the dealer
# without going above the score of 21, or else the
# player is said to have bust and the game is over.
# the deal must have 17 or more
# Tkinter 8.6 支持png，早期版本支持ppm，本python的tk是8.6版本的

import random

try:
    import tkinter
except ImportError:  # python2
    import Tkinter as tkinter


def load_images(card_images):
    suits = ['heart', 'club', 'diamond', 'spade']
    face_cards = ['jack', 'queen', 'king']

    if tkinter.TkVersion >= 8.6:
        extension = 'png'
    else:
        extension = 'ppm'

    # for each suit, retrieve the image for the cards
    for suit in suits:
        # first the number cards 1 to 10
        for card in range(1, 11):
            name = "cards/{}_{}.{}".format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((card, image,))

        # next the face cards
        for card in face_cards:
            name = 'cards/{}_{}.{}'.format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image,))


def _deal_card(frame):
    # pop the next card of the top of the deck
    next_card = deck.pop(0)
    # put the next_card at the bottom of the deck
    deck.append(next_card)
    # add the image to a label and display the label
    # 一个window/frame的里面pack和grid不要混用，同一层面只能用一种manager。
    # 此处用pack更加方便，直接挨着添加就好。
    tkinter.Label(frame, image=next_card[1], relief='raised').pack(side='left')
    # now return the card's face value
    return next_card


def score_hand(hand):
    # calculate the total score of all cards in the list
    # only one ace can have the value 11, and this will be reduced to 1 if the hand would bust.
    score = 0
    ace = False

    for next_card in hand:
        card_value = next_card[0]
        if card_value == 1 and not ace:
            ace = True
            card_value = 11
        score += card_value
        # if we would bust, check if there is an ace and subtract 10
        if score > 21 and ace:
            score -= 10
            ace = False
    return score


def deal_dealer():
    dealer_score = score_hand(dealer_hand)
    while 0 < dealer_score < 17:
        dealer_hand.append(_deal_card(dealer_card_frame))
        dealer_score = score_hand(dealer_hand)
        dealer_score_label.set(dealer_score)

    player_score = score_hand(player_hand)
    if player_score > 21:
        result_text.set("Dealer Wins!")
    elif dealer_score > 21 or dealer_score < player_score:
        result_text.set("Player Wins!")
    elif dealer_score > player_score:
        result_text.set("Dealer Wins")
    else:
        result_text.set("Draw!")


def deal_player():
    player_hand.append(_deal_card(player_card_frame))
    player_score = score_hand(player_hand)

    player_score_label.set(player_score)
    if player_score > 21:
        result_text.set("Dealer Wins!")
    # # player_score = 0   # assigning value to a global variable in the function make it a local variable
    # global player_score
    # global player_ace
    # card_value = deal_card(player_card_frame)[0]
    # if card_value == 1 and not player_ace:
    #     player_ace = True
    #     card_value = 11
    # player_score += card_value
    # # if we would bust, check if there is an ace and subtract
    # if player_score > 21 and player_ace:
    #     player_score -= 10
    #     player_ace = False
    # player_score_label.set(player_score)
    # if player_score > 21:
    #     result_text.set("Dealer wins!")
    # # print(locals())


def initial_deal():
    deal_player()
    dealer_hand.append(_deal_card(dealer_card_frame))
    dealer_score_label.set(score_hand(dealer_hand))
    deal_player()


def new_game():
    global dealer_card_frame
    global player_card_frame
    global dealer_hand
    global player_hand
    global deck
    # embedded frame to hold the card images
    dealer_card_frame.destroy()
    dealer_card_frame = tkinter.Frame(card_frame, background="green")
    dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)
    player_card_frame.destroy()
    player_card_frame = tkinter.Frame(card_frame, background="green")
    player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)

    result_text.set('')

    # # get a brand new deck of cards, which is not quite realistic
    # deck = []
    # load_images(deck)
    # random.shuffle(deck)
    # create the list to store the dealer's and player's hands
    dealer_hand = []
    player_hand = []
    initial_deal()


def shuffle():
    global deck
    random.shuffle(deck)


# print(__name__)

def play():
    initial_deal()
    main_window.mainloop()


# __name__ = "__main__"

main_window = tkinter.Tk()

# set up the screen and frames for the dealer and player
main_window.title("Black Jack")
main_window.geometry("640x480")
main_window.configure(background="green")

result_text = tkinter.StringVar()
result = tkinter.Label(main_window, textvariable=result_text)

result.grid(row=0, column=0, columnspan=3)

card_frame = tkinter.Frame(main_window, relief='sunken', borderwidth=1, background="green")
card_frame.grid(row=1, column=0, sticky='ew', columnspan=3, rowspan=2)

# dealer score
dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Dealer", background="green", fg="white").grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label, background="green", fg="white").grid(row=1, column=0)
# embedded frame hold the card games
dealer_card_frame = tkinter.Frame(card_frame, background="green")
dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)

# player score
player_score_label = tkinter.IntVar()
# player_score = 0
# player_ace = False
tkinter.Label(card_frame, text="Player", background="green", fg="white").grid(row=2, column=0)
tkinter.Label(card_frame, textvariable=player_score_label, background="green", fg="white").grid(row=3, column=0)
# embedded frame to hold the card images
player_card_frame = tkinter.Frame(card_frame, background="green")
player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)

# buttons
button_frame = tkinter.Frame(main_window)
button_frame.grid(row=3, column=0, columnspan=3, sticky='w')
# dealer button
dealer_button = tkinter.Button(button_frame, text="Dealer", command=deal_dealer)
dealer_button.grid(row=0, column=0)
# player button
player_button = tkinter.Button(button_frame, text="Player", command=deal_player)
player_button.grid(row=0, column=1)
# reset button
new_game_button = tkinter.Button(button_frame, text="New game", command=new_game)
new_game_button.grid(row=0, column=2)
# shuffle button
shuffle_button = tkinter.Button(button_frame, text="Shuffle", command=shuffle)
shuffle_button.grid(row=0, column=3)
# load cards
cards = []
load_images(cards)
print(cards)
# create a new deck of cards and shuffle them
deck = list(cards)   # 元素一样，但是不同的list。
# random.shuffle(deck)
shuffle()

# create the list to store the dealer's and player's hands
dealer_hand = []
player_hand = []

# new_game()
# def new_game has these lines, so in order to avoid duplicates, delete them.
# deal_player()
# dealer_hand.append(deal_card(dealer_card_frame))
# dealer_score_label.set(score_hand(dealer_hand))
# deal_player()


if __name__ == '__main__':
    play()
