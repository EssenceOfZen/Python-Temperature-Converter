#Temperature Conversion GUI
#Programmed by Zane "ZenOokami"
#www.EssenceOfZen.org

from tkinter import *

class Main_Window:
	
	def __init__(self, master):
		print("Starting Program...")
		
		master.title("Temperature Conversion") # Window Title
		master.geometry("280x230") # Set default window size
		
		self.celsius = 0.00 # We create basic variables for later
		self.fahrenheit = 0.00 # Another basic variable to use later
		self.version = "Current Version: 1.2.1"
		self.creator = "Coded by: ZenOokami | www.EssenceOfZen.org \n"
		
		frame = Frame(master) # We create a frame to have all of our items in.
		frame.pack() # We use the pack module to make organize and allow the frame to appear
		
		self.version_label = Label(frame, text=self.version) # We create our first label for program version
		self.version_label.pack()
		
		#Creator Label
		self.creator_label = Label(frame, text=self.creator) # This is the creator label, the "Created by me" and such
		self.creator_label.pack()
		
		#Fahrenheit=====================================
		self.user_label = Label(frame, text="Fahrenheit to Celsius") # Create a basic Label to clarify which bar is which
		self.user_label.pack()
		
		self.user_temp1 = Entry(frame) # We create a simple text field for fahrenheit
		self.user_temp1.insert(0, self.fahrenheit) # This is used to have a default value for the text field
		self.user_temp1.pack()
		
		self.converted_label1 = Label(frame, text=self.celsius) # Another Label
		self.converted_label1.pack()
		
		#Celsius========================================
		self.user_label2 = Label(frame, text="Celsius to Fahrenheit") # Create a basic Label
		self.user_label2.pack()
		
		self.user_temp2 = Entry(frame) # This is our text field for celsius
		self.user_temp2.insert(0, self.celsius) # Default value for celsius 
		self.user_temp2.pack()
		
		self.converted_label2 = Label(frame, text=self.fahrenheit)
		self.converted_label2.pack()
		
		#Buttons=========================================
		self.convert_button = Button(frame, text="Convert", fg="green", command=self.update) # This is our convert button!
		self.convert_button.pack(side=LEFT)
		
		self.quit_button = Button(frame, text="QUIT", fg="red", command=frame.quit) # This is our quit button -- will make a quit function for next version
		self.quit_button.pack(side=RIGHT)
		
		print("Program reached passed Button Code")
		
		
		
		
	def update(self): # This is a function that causes the GUI to update after the "Convert" button is clicked
		print("Updating GUI...")
		self.celsius = self.fahrenheit_to_celsius(self.user_temp1.get()) # Call the equation functions!
		self.fahrenheit = self.celsius_to_fahrenheit(self.user_temp2.get())
		
		self.converted_label1.config(text=self.celsius) # we use the .config to update the labels!
		self.converted_label2.config(text=self.fahrenheit)
		
	def set_size(self): # Not working just yet
		print("Setting Size")
		
	def fahrenheit_to_celsius(self, fahrenheit): # Equation for converting
		print("Running FaH to Cel...")
		celsius = (float(fahrenheit) - 32) * (5/9)
		return celsius
		
	def celsius_to_fahrenheit(self, celsius): # Equation for converting
		print("Running Cel to Fah...")
		fahrenheit = float(celsius) * (9/5) + 32
		return fahrenheit
		
		
main_window = Tk() # We create a TK object

main_program = Main_Window(main_window) # We then make a new object which is an instance of the class - using "main_window" as the "master" for the class 

main_window.mainloop() # This is the classic loop to keep the GUI running
main_window.destroy() # Destroys the GUI after the mainloop finishes
	
	
	
	
	
