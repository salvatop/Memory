# implementation of card game - Memory
import simplegui
import random

# helper function to initialize globals
DECK = range(8) + range(8)
 
def new_game():
    global cards,exposed,turn,paired,state,DECK
    cards = DECK
    random.shuffle(cards)
    exposed = []
    paired = []
    turn = 0
    label.set_text("Turn: " + str(turn))
    state  = 0
    for card in cards:
        exposed.append(False)
    
# define event handlers
def mouseclick(pos):
    global exposed,state,turn,previous_card,current_card,paired   
    card_index = pos[0] // 50
    
    if exposed[card_index] == False:
        if state == 0:
            previous_card = card_index
            exposed[card_index] = True
            state = 1
        elif state == 1:
            current_card = card_index
            exposed[card_index] = True
            state = 2
            turn +=1
            label.set_text("Turn: " + str(turn))
        else:
            if cards[previous_card] == cards[current_card]:
                paired.append(previous_card)
                paired.append(current_card)
                exposed[card_index] = True
                previous_card = card_index
            else:
                exposed[previous_card] = False
                exposed[current_card] = False
                exposed[card_index] = True
                previous_card = card_index
            state = 1           

# draw handler   
def draw(canvas):
    global cards,exposed,paired
    p3 = 25 # x pos green rectangle 
    p2 = 50 # x pos card frame
    p1 = 13 # x pos card value
    for card_index in range(len(cards)):
        #borders
        canvas.draw_line((1, 10), (p2,10), 2, 'White')#top
        canvas.draw_line((1, 85), (1, 10), 2, 'White')#left
        canvas.draw_line((p2, 85),(p2, 10), 2, 'White')#right
        canvas.draw_line((1, 85), (p2,85), 2, 'White')#bottom
        p2 += 50
        #card values
        card_pos = [p1,65]
        canvas.draw_text(str(cards[card_index]), card_pos, 50,"White")
        p1 += 50         
        #green rectancle aka the card's back
        if exposed[card_index] == False and card_index not in paired:
            canvas.draw_polygon([[p3, 80], [p3, 15], [p3, 80], [p3, 15]], 40, 'Green', 'Green')
        p3 += 50

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 801, 95)
frame.add_button("Reset", new_game)
label = frame.add_label('Turn: 0')

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
