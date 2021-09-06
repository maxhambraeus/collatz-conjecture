import matplotlib.pyplot as plt
from random import randint
from matplotlib.animation import FuncAnimation
import argparse

parser = argparse.ArgumentParser()#set command line args
parser.add_argument("-f", "--framerate", default=60, type=int, help="set framerate")
parser.add_argument("-s", "--save", help="specifies filename and saves video")
args = parser.parse_args()

x = []
y = []
fig = plt.figure()
ax = plt.axes() 
framerate = args.framerate


number = int(input("enter a number: "))

def collatz(number): #returns a list of numbers using the input as source
	numbers = []

	while number != 1:
		if number % 2:
			number = (number*3)+1
		else:
			number = number/2

		numbers.append(number)

	return numbers

def animate(frame, *fargs):#plots the numbers, one by one
	x.append(frame)
	y.append(numbers[frame])

	ax.clear()
	ax.plot(x, y)

numbers = collatz(number)

ani = FuncAnimation(fig, animate, fargs=numbers, frames=len(numbers), interval=1000/framerate, repeat=False) #renders the animation 

if args.save: #if --save is specified save as mp4, else show animation
	ani.save(args.save)
else:
	plt.show()
