from appJar import gui

#Function to greet the user and ask for a category
#Completed by - Jamie Engelhardt
import pandas
picfixdf=pandas.read_csv("picfix.csv")
printslist = list(picfixdf.Prints)
canvaslist = list(picfixdf.Canvas)
frameslist = list(picfixdf.Frames)
albumslist = list(picfixdf.Albums)

def greet_user(greeting,sentinel,categoryq,readyq):
    canswer = ' '
    ranswer = sentinel
    print(greeting)
    while ranswer == sentinel:
        canswer = input(categoryq)
        ranswer = input(readyq)
    if canswer == "Prints":
        prints("Welcome to our Prints section! Here are your choices:",printslist,"Which size print would you like or enter None? ")
    elif canswer == "Canvas":
        canvas("Welcome to our Canvas section!  Here are your choices:",canvaslist,"Which size canvas would you like or enter None? ")
    elif canswer == "Frames":
        frames("Welcome to our Frames section! Here are your choices:",frameslist,"Which color frame would you like or enter None? ")
    elif canswer == "Albums":
        albums("Welcome to our Albums section! Here are your choices:",albumslist,"How many pages would you like in your album or enter None? ")
    else:
        print('Please enter Prints, Canvas, Frames, or Albums.')

#Function ask user to pick Prints
#Completed by - Justin Chang
def prints(greeting,selection,pickq):
    print(greeting)
    for item in selection:
        print(item)
    printspick = input(pickq)
    if printspick == "None":
        print("Goodbye")
    elif printspick == "5x4":
        closing("5x4", .15, "Your 5x4 PicFix Prints has been selected!")
    elif printspick == "5x5":
        closing("5x5",.20, "Your 5x5 PicFix Prints has been selected!")
    elif printspick == "6x4":
        closing("6x4",.25, "Your 6x4 PicFix Prints has been selected!")
    elif printspick == "7x5":
        closing("7x5",.30, "Your 7x5 PicFix Prints has been selected!")
    elif printspick == "8x4":
        closing("8x4",.35, "Your 8x4 PicFix Prints has been selected!")
    else:
        closing("Please choose a Prints in the size 5x4, 5x5, 6x4, 7x5, 8x4" )

#Function ask user to pick Canvas
#Completed by - Jamie Engelhardt
def canvas(greeting,selection,pickq):
    print(greeting)
    for item in selection:
        print(item)
    canvaspick = input(pickq)
    if canvaspick == "None":
        print("Goodbye")
    elif canvaspick == "20x16":
        closing("20x16",30,"Your 20x16 PicFix Canvas has been selected!" )
    elif canvaspick == "16x16":
        closing("16x16",25,"Your 16x16 PicFix Canvas has been selected!" )
    elif canvaspick == "24x16":
        closing("24x16",15,"Your 24x16 PicFix Canvas has been selected!")
    elif canvaspick == "16x12":
        closing("16x12",10,"Your 16x12 PicFix Canvas has been selected!")
    elif canvaspick == "24x12":
        closing("24x12",5,"Your 24x12 Pic Fix Canvas has been selected!")
    else:
        closing("Please choose a Canvas in the size 20x16, 16x16, 24x16, 16x12, 24x12." )

#Function ask user to pick Frames
#Completed by - Tiyanna Calderon 
def frames(greeting,selection,pickq):
    print(greeting)
    for item in selection:
        print(item)
    framespick = input(pickq)
    if framespick == "None":
        print("Goodbye")
    elif framespick == "White Frame":
        closing("White Frame",20,"Your White PicFix Frame has been selected!")
    elif framespick == "Black":
        closing("Black Frame",20,"Your Black PicFix Frame has been selected!")
    elif framespick == "Silver":
        closing("Silver Frame",30,"Your Silver PicFix Frame has been selected!")
    elif framespick == "Gold":
        closing("Gold Frame",30,"Your Gold PicFix Frame has been selected!")
    elif framespick == "Mahogany":
        closing("Mahogany Frame",40,"Your Mahogany Pic Fix Frame has been selected!")
    else:
        closing("Please choose a Frame in either White, Black, Silver, Gold, or Mahogany" )

#Function ask user to pick Albums
#Completed by - Jamie Engelhardt
def albums(greeting,selection,pickq):
    print(greeting)
    for item in selection:
        print(item)
    albumspick = input(pickq)
    if albumspick == "None":
        print("Goodbye")
    elif albumspick == "10":
        closing("10 pages",15,"Your 10 page PicFix Album has been selected!")
    elif albumspick == "20":
        closing("20 pages",25,"Your 20 page PicFix Album has been selected!")
    elif albumspick == "30":
        closing("30 pages",35,"Your 30 page PicFix Album has been selected!")
    elif albumspick == "40":
        closing("40 pages",45,"Your 40 page PicFix Album has been selected!")
    elif albumspick == "50":
        closing("50 pages",55,"Your 50 page PicFix Album has been selected!")
    else:
        closing("Please choose how many pages: 10, 20, 30, 40, 50")

#Function to give user total price of purchase
#Completed by - Tiyanna Calderon
def closing(pickeditem,price,goodbye):
    print("Your grand total for your PicFix",pickeditem,"is $"+str(price))
    more = input("Would you like to continue shopping with PicFix (y/n)? ")
    if more == "y":
        greet_user("Great!", "n", "What category would you like to browse Prints, Canvas, Frames, Albums? ", "Ready to shop (y/n)? ")
    else:
        for l in goodbye:
            print(l)

#Function for button names
#Completed by - Jamie Engelhardt
def press(btn):
    if btn == "Exit":
        app.stop()
    elif btn == "Greeting":
        greet_user("Welcome to PicFix", "n", "What category would you like to browse Prints, Canvas, Frames, Albums? ", "Ready to shop (y/n)? ")
    elif btn == "Prints":
        prints("Welcome to our Prints section! Here are your choices:",printslist,"Which size print would you like or enter None? ")
    elif btn == "Canvas":
        canvas("Welcome to our Canvas section!  Here are your choices:",canvaslist,"Which size canvas would you like or enter None? ")
    elif btn == "Frames":
        frames("Welcome to our Frames section! Here are your choices:",frameslist,"Which color frame would you like or enter None? ")     
    elif btn == "Albums":
        albums("Welcome to our Albums section! Here are your choices:",albumslist,"How many pages would you like in your album or enter None? ")     
    else:
        print('Choose another option')

#appJar
#Completed by - Justin Chang
app=gui("Main Menu","500x500")

#Title Page
app.addLabel("title", "Welcome to PicFix's Main Menu")

#Color
app.setLabelBg("title", "#E59866")

#Gif and Font Size
app.addImage("decor","teamproject.gif")
app.setFont(18)

#Buttons
app.addButton("Greeting", press)
app.addButton("Prints", press)
app.addButton("Canvas", press)
app.addButton("Frames", press)
app.addButton("Albums", press)
app.addButton("Exit",press)
app.go()      

