import random
def hangman():
    word = random.choice(["computer", "pillow", "chrome", "videocall", "laptop", "bedsheet", "curtains", "board", "avengers", "table"])
    valid_letters = "abcdefghijklmonpqrstuvwxyz"
    turns = 10
    guess_made= ""
  
    while len(word)> 0:
        main= ""
        missed= 0
        
        for letter in word:
            if letter in guess_made:
                main = main + letter
            else:
                main = main + "_" + ""
        
        if main == word:
            print(main)
            print("You win, cutie.")
            break
        
        print("Guess the word:", main)
        guess = input()    
        
        if guess in valid_letters:
            guess_made= guess_made + guess
        else:
            print("Enter a valid character")
            guess= input()
        
        if guess not in word:
            turns = turns - 1
            if turns == 9:
                print("9 turns left!")
                print("---------")
            if turns == 8:
                print("8 turns left!")
                print("---------")
                print("    0    ")
            if turns == 7:
                print("7 turns left, careful!")
                print("---------")
                print("    0    ")  
                print("    |    ")    
            if turns == 6:
                print("6 turns left!")
                print("---------")
                print("    0    ")  
                print("    |    ")
                print("   /     ")
            if turns == 5:
                print("5 turns left!")
                print("---------")
                print("    0    ")  
                print("    |    ")
                print("   / \   ")    
            if turns == 4:
                print("Damn!4 turns left.")
                print("---------")
                print("  \ 0    ")  
                print("    |    ")
                print("   / \   ")    
            if turns == 3:
                print("Slow down!3 turns left.")
                print("---------")
                print("  \ 0 /  ")  
                print("    |    ")
                print("   / \   ")   
            if turns == 2:
                print("Heyy? 2 turns left.")
                print("---------")
                print("  \ 0 /| ")  
                print("    |    ")
                print("   / \   ")
            if turns == 1:
                print("Pray for yourself! 1 turn left.")
                print("---------")
                print("  \ 0_|/ ")  
                print("    |    ")
                print("   / \   ")
            if turns == 0:
                print("You lost! The man is dead.")
                print("---------")
                print("    0_|  ")  
                print("   /|\   ")
                print("   / \   ")
                break
name= input("Enter your name: ")
print("Welcome",name,".You look cute today!" )
print("_________________________")
print("Try to guess the word in less than 10 attempts.")
hangman()