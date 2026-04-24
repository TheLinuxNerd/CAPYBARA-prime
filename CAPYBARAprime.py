import time
import random
import pygame
import turtle
version = ("1.0.0-pyCLI_alpha")

#Sign-up

def signUP():
    print('\n')
    print("**********************")
    print("Capybara PRIME Sign-up")
    print("**********************\n")
    FirstNAME = input("Type in your first name: ")
    print("Your first name is " + FirstNAME + ".\n")
    time.sleep(1)
    MiddleNAME = input("Type in your middle name: ")
    print("Your middle name is " + MiddleNAME + ".\n")
    time.sleep(1)
    LastNAME = input("Type in your last name: ")
    print("Your last name is " + LastNAME + ".\n")
    time.sleep(1)
    print()
    print("So your full name is " + FirstNAME + " " + MiddleNAME + " " + LastNAME + ".\n")
    Username = input("What do you want your user name to be?: ")
    print('\n')
    print("Your username is " + Username + ".\n")
    Age = input ("How old are you?: ")
    print('\n')
    if Age == "1":
        print("You are " + Age + " Year old... Wait! How do you know how use this?\n")
        OYOUCPA = input("How are you using a computer if your 1 year old?: ")
        #BTW OYOUCPA stands for: One Year Old Using Capybara Prime App
        print("Your said " + OYOUCPA + " WoW... :-P")
        print("Maybe you should wait until your older...")
        Age = 0
        exit()
    print("You are " + Age + " Years old.\n")

#Sign-up(END)

#Log-in

def logIN():
    print('\n')
    print("*********************")
    print("Capybara PRIME Log-in")
    print("*********************\n")
    print('Loading....\n')
    time.sleep(random.randint(1,4))
    print('...\n')
    time.sleep(random.randint(1,3))
    print('..\n')
    time.sleep(random.randint(1,2))
    print('.\n')
    time.sleep(1.4)
    print("Done!\n")
    print('\n')
    

#Log-in(END)

#Main MENU

def mainMENU():
    print('\n')
    time.sleep(random.randint(1,3))
    print("Loading....\n")
    time.sleep(random.randint(1,3))
    print("...\n")
    time.sleep(random.randint(1,3))
    print("..\n")
    time.sleep(random.randint(1,3))
    print(".\n")
    time.sleep(1.5)
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("Capybara PRIME offical app")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$\n")
    print("your version is " + version)
    print('\n')
    print("1 = Sign-up     2 = Log-in     3 = Exit")
    Option = input("Choose any option: \n")
    if Option == "1":
        signUP()
    if Option == "2":
        logIN()
    if Option == "3":
        print("Bye....\n")
        exit()

#Main MENU(END)

#Calculator

def calculator():
  print("Welcome to the CAPYBARA-prime Calculator!")
  print("Available operations: +, -, *, /, ^ (exponentiation), q (quit)")

  while True:
    try:
      num1 = float(input("Enter the first number: "))
      operator = input("Enter the operator (+, -, *, /, ^, q): ")

      if operator == 'q':
        break  # Exit the loop if the user wants to quit

      num2 = float(input("Enter the second number: "))

      if operator == '+':
        result = num1 + num2
      elif operator == '-':
        result = num1 - num2
      elif operator == '*':
        result = num1 * num2
      elif operator == '/':
        if num2 == 0:
          print("Error: Division by zero!")
          continue  # Go back to the beginning of the loop
        result = num1 / num2
      elif operator == '^':
        result = num1 ** num2
      else:
        print("Invalid operator!")
        continue # Go back to the beginning of the loop

      print("Result:", result)

    except ValueError:
      print("Invalid input. Please enter numbers only.")
      mainMENU()

#Calculator(END)

#Pong

def Pong():
    SCREEN_WIDTH = 500
    SCREEN_HEIGHT = 500
    LOOP_DELAY = 40
    BACKGROUND_COLOR = 'CadetBlue2' #(0,0,0) # Black background

    win = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption("Kim\'s Pong Game")

    # set up variables for my paddle object
    paddleX = 250
    paddleY = 465
    paddleWidth = 50
    paddleHeight = 20
    paddleVelocity = 20 # number of pixels to move on each pass of the main loop
    paddleColor = (255,0,0) # red

    # to keep main game loop running
    keepPlaying = True

    # you need to do this every time you use the pygame library, initializes
    pygame.init()

    # object to store information about our game paddle
    paddleRect = pygame.Rect(paddleX, paddleY, paddleWidth, paddleHeight)

    def movePaddle( paddleRect, movement ):

        newX = paddleRect.x + movement
        if ( ( newX >= -10 ) and ( newX <= SCREEN_WIDTH - 15)):
            paddleRect.x = newX
            print('Moving paddle', newX )

    # main game loop starting here
    while keepPlaying:
        pygame.time.delay(LOOP_DELAY) # keeps things from moving too fast

        # look for events - action by user
        for event in pygame.event.get():
            if ( event.type == pygame.QUIT ): # for when window X is closed
                keepPlaying = False
            if ( event.type == pygame.KEYDOWN ):
                if ( event.key == pygame.K_x ): #exit on the X key
                    keepPlaying = False

        #returns a list of booleans that are true for each key currently pushed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            movePaddle(paddleRect, -paddleVelocity)
        if keys[pygame.K_RIGHT]:
            movePaddle(paddleRect, paddleVelocity)

        # redraw the screen and paddle
        win.fill(BACKGROUND_COLOR)
        pygame.draw.rect(win, paddleColor, paddleRect) #draws rectangle for paddle
        pygame.display.update()

    print('Leaving pong game ...')
    pygame.quit()

#Pong(END)

#PETcapybara

def PETcapybara():
   # Set up the screen and turtle
   screen = turtle.Screen()
   screen.setup(width=1000, height=1000)
   screen.bgcolor("green")
   screen.title("Random Turtle Adventure")

   pen = turtle.Turtle()
   pen.speed(0)  # Set speed to fastest
   pen.shape("turtle")
   pen.color(random.choice(("green","yellow")))  # Choose a color
   pen.pensize(5)

   # Define movement directions
   directions = ["north", "east", "south", "west"]

   # Function to move the turtle randomly
   def move_turtle():
         # Move a fixed distance
       pen.right(random.randint(0, 360))  # Random direction
       pen.forward(50)

   # Set the number of loops
   num_loops = 5

   # Main loop
   pen.speed(0)
   while(True):
       for j in range(3):  # Multiple smaller loops for variety
           move_turtle()
           pen.color(random.choice(("green","yellow")))
           #pen.left(random.randint(1, 360))
           if(pen.pos()[0] > 500 or pen.pos()[0] < -500 or pen.pos()[0] > 500 or pen.pos()[0] < -500):
               pen.right(180)
               pen.forward(100)
             # Random turn after moving
       # Optionally add a pause between loops
       # turtle.delay(50)

   # Keep the window open until closed manually
   screen.mainloop()

#PETcapybara(END)

#UNLOCKED menu

def unlockedMENU():
    print('\n')
    time.sleep(random.randint(1,3))
    print("Loading....\n")
    time.sleep(random.randint(1,2))
    print("...\n")
    time.sleep(random.randint(1,2))
    print("..\n")
    time.sleep(random.randint(1,3))
    print(".\n")
    time.sleep(1.5)
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("Capybara PRIME app... It is unlocked!")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n")
    print("your version is " + version)
    print('\n')
    print("1 = Pong     2 = Website     3 = Exit")
    Option = input("Choose any option: \n")
    if Option == "1":
        Pong()
    if Option == "2":
        SITE()
    if Option == "3":
        print("Bye....\n")
        exit()

#UNLOCKED menu(END)

mainMENU()
