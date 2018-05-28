import tkinter #importing tkinter libraries
from random import randint #importing randint function to generate random function
import time

wordList = [] 
while True:
	with open("word.txt") as f: # opening the txt file located in the same folder
		content = f.readlines() # reading line by line from the txt file
	content = [x.strip() for x in content] # removing the /n from the content
	for word in content:
		wordmeaning = word.split(); #converting to list
		title= wordmeaning[0].upper(); #seprating the title
		meaning = ' '.join(wordmeaning[1:]) #joining the rest of the list which contain the meaning
		wordList.append([title,meaning]) #appending list in a list 

	class Dictnory():
		def __init__(self,wordList,show_interval,hide_interval):
			self.wordList = wordList
			self.show_int = show_interval
			self.hide_int = hide_interval
			self.rand = randint(0,(len(self.wordList) - 1))
			self.window = tkinter.Tk()
			self.window.title('Dictionary')
			tkinter.Frame(self.window, width=250, height=100).pack()
			tkinter.Label(self.window, text=self.wordList[self.rand][0],font='Times 15 bold').place(x=125, y=10,anchor="center")
			tkinter.Label(self.window, text=self.wordList[self.rand][1],font='Times 12',bd=1,relief='solid',wraplength='250').place(x=125, y=50,anchor="center")
			self.window.after(2000, lambda: self.window.destroy())
		
	

		def start(self):
			self.window.mainloop()

	if __name__ == "__main__":
		
		r = Dictnory(wordList,3,6)
		r.start()
		
	time.sleep(5)
		
		
	
