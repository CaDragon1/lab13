#########################################
#
#         70-100pt - Making a game
#
#########################################


# 70pt - Add buttons for left, right and down that move the player circle
# 100pt - using lab 11 as an example, add in three horizontally scrolling "enemies"
# Make them scroll at different speeds and directions.

from Tkinter import *
root = Tk()

drawpad = Canvas(root, width=800,height=600, background='white')
player = drawpad.create_oval(390,580,410,600, fill="green4")

# Create your "enemies" here, before the class
baddie1 = drawpad.create_oval(30, 30, 70, 70, fill='red')
baddie2 = drawpad.create_oval(140, 125, 185, 170, fill='red')
baddie3 = drawpad.create_oval(400, 300, 525, 425, fill='red')
direction = 8
direction2 = 4
direction3 = 1
#def animate():
 #   global direction
  #  x1, y1, x2, y2 = drawpad.coords(circle)
   # if x2 > drawpad.winfo_width(): 
    #    direction = - 1
    #elif x1 < 0:
     #   direction = 1
    #drawpad.move(circle,direction,0)
    #drawpad.after(1, animate)

#animate()
#root.mainloop()



class MyApp:
	def __init__(self, parent):
       	    global drawpad
       	    self.myParent = parent  
       	    self.myContainer1 = Frame(parent)
       	    self.myContainer1.pack()
       	    
       	    # Up button
       	    self.up = Button(self.myContainer1)
       	    self.up.configure(text="up", background= "green")
       	    self.up.grid(row=0,column=1)
       	    # Bind an event to the first button
       	    self.up.bind("<Button-1>", self.upClicked)
       	    # Left button
       	    self.left = Button(self.myContainer1)
       	    self.left.configure(text="left", background= "pink2")
       	    self.left.grid(row=1,column=0)
       	    self.left.bind("<Button-1>", self.leftClicked)
       	    # Right button
       	    self.right = Button(self.myContainer1)
       	    self.right.configure(text="right", background= "red2")
       	    self.right.grid(row=1,column=2)
       	    self.right.bind("<Button-1>", self.rightClicked)
       	    # Down button
       	    self.down = Button(self.myContainer1)
       	    self.down.configure(text="down", background= "skyblue")
       	    self.down.grid(row=2,column=1)
       	    self.down.bind("<Button-1>", self.downClicked)
       	    
       	    # No need to edit this - just includes the drawpad into our frame
       	    drawpad.pack(side=RIGHT)
       	    # call the animate function to start our recursion
       	    self.animate()
	
	def animate(self):
	    global drawpad
	    global player
	    # Remember to include your "enemies" with "global"
	    global baddie1
            global direction
            x1, y1, x2, y2 = drawpad.coords(baddie1)
            if x2 < 0: 
                direction = 16
            elif x1 > drawpad.winfo_width():
                direction = -16
            drawpad.move(baddie1, direction,0)
            
            global baddie2
            global direction2
            x1, y1, x2, y2 = drawpad.coords(baddie2)
            if x2 > drawpad.winfo_width(): 
                direction2 = -12
            elif x1 < 0:
                direction2 = 12
            drawpad.move(baddie2, direction2, 0)
            
            global baddie3
            global direction3
            x1, y1, x2, y2 = drawpad.coords(baddie3)
            if x2 > drawpad.winfo_width(): 
                direction3 = -8
            elif x1 < 0:
                direction3 = 8
            drawpad.move(baddie3, direction3, 0)
       	    
	    #Uncomment this when you're ready to test out your animation!
	    drawpad.after(10,self.animate)
		
	def upClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,0,-20)
	  
	def leftClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,-20,0)
	
	def rightClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,20,0)
	   
	def downClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,0,20)
		
app = MyApp(root)
root.mainloop()