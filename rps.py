import random
import simplegui


COMPUTER_SCORE = 0
HUMAN_SCORE = 0
human_choice = ""
computer_choice = ""


def choice_to_number(choice):
    """Convert choice to number."""
    if human_choice == 'rock':
        return 0
    elif human_choice == 'paper':
        return 1
    return 2


def number_to_choice(number):
    """Convert number to choice."""
    if human_choice == 0:
        return 'rock'
    elif human_choice == 1:
        return 'paper'
    return 'scissors'


def random_computer_choice():
    """Choose randomly for computer."""
    lst = ['rock', 'paper', 'scissors']
    return random.choice(lst)


def choice_result(human_choice, computer_choice):
    global COMPUTER_SCORE
    global HUMAN_SCORE
    if human_choice =='rock' and computer_choice=='scissors':
        COMPUTER_SCORE +=1
    elif human_choice=='paper' and computer_choice=='rock':
        COMPUTER_SCORE +=1
    elif human_choice == 'scissors' and computer_choice=='paper':
        COMPUTER_SCORE +=1
    elif computer_choice =='rock' and human_choice=='scissors':
        HUMAN_SCORE +=1
    elif computer_choice=='paper' and human_choice=='rock':
        HUMAN_SCORE +=1
    elif computer_choice == 'scissors' and human_choice=='paper':
        HUMAN_SCORE +=1  
    else:
        return 
    # based on the given human_choice and computer_choice
    # determine who won and increment their score by 1.
    # if tie, then don't increment anyone's score.    


def test_choice_to_number():
    assert choice_to_number('rock') == 0
    assert choice_to_number('paper') == 1
    assert choice_to_number('scissors') == 2
    
def test_number_to_choice():
    assert number_to_choice(0) == 'rock'
    assert number_to_choice(1) == 'paper'
    assert number_to_choice(2) == 'scissors'
    
def test_all():
    test_choice_to_number()
    test_number_to_choice()
    

# Handler for mouse click on rock button.
# This code is for the GUI part of the game.
def rock():
    global human_choice, computer_choice
    global HUMAN_SCORE, COMPUTER_SCORE
    
    human_choice = 'rock'
    computer_choice = random_computer_choice()
    choice_result(computer_choice, human_choice)

def paper():
    global human_choice, computer_choice
    global HUMAN_SCORE, COMPUTER_SCORE
    
    human_choice = 'paper'
    computer_choice = random_computer_choice()
    choice_result(computer_choice, human_choice)
    
# Handler for mouse click on paper button.
def scissors():
    global human_choice, computer_choice
    global HUMAN_SCORE, COMPUTER_SCORE
    
    human_choice = 'scissors'
    computer_choice = random_computer_choice()
    choice_result(computer_choice, human_choice)

# Handler to draw on canvas
def draw(canvas):
    
    try:
        # Draw choices
        canvas.draw_text("You: " + human_choice, [10,40], 48, "Green")
        canvas.draw_text("Comp: " + computer_choice, [10,80], 48, "Red")
        
        # Draw scores
        canvas.draw_text("Human Score: " + str(HUMAN_SCORE), [10,150], 30, "Green")
        canvas.draw_text("Comp Score: " + str(COMPUTER_SCORE), [10,190], 30, "Red")
        
    except TypeError:
        pass
    

# Create a frame and assign callbacks to event handlers
def play_rps():
    frame = simplegui.create_frame("Home", 300, 200)
    frame.add_button("Rock", rock)
    frame.add_button("Paper", paper)
    frame.add_button("Scissors", scissors)
    frame.set_draw_handler(draw)

    # Start the frame animation
    frame.start()
 
play_rps()
