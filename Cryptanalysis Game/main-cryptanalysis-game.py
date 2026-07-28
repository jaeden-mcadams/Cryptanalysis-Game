
#SETUP:

#Library

import random
import ts_spacepod


#Variables

turns = 5
digit_1 = random.randint(1,5)
digit_2 = random.randint(1,5)
digit_3 = random.randint(1,5)


#Graphics

ts_spacepod.show_screen()


#GAME LOOP:
while turns >= 0:


    #User guess

    guess = input("guess 3 digits with each digit being from 1-5 ")
    if not ts_spacepod.is_guess_valid(str(guess)):
        print()
        continue
   
    
    
        


    #Result output

    correct_count = ts_spacepod.get_correct_count(guess)
    print(str(correct_count) + " digits are correct")
    misplaced_count = ts_spacepod.get_misplaced_count(guess)
    print(str(misplaced_count) + " digits are misplaced")
    ts_spacepod.update_screen(guess)
    print()
    if guess != ts_spacepod.get_answer():
        print("You have " + str(turns) + " turns remaining")
        

    #Win check
    if guess == ts_spacepod.get_answer():
        ts_spacepod.show_win()
        print("you won")
        break


    #Turn end
    
    if guess != ts_spacepod.get_answer():
        turns -= 1


#Out of turns result
else:
    ts_spacepod.show_loss()
    print("You ran out of turns and lost")
    print("The correct combination was: " + ts_spacepod.get_answer())

