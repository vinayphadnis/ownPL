import sys
import os



def generatefile(name):
    inputFile = "demofile.txt"
    inputf = open(inputFile, "r")
    data = inputf.read()
    inputf.close()  
    filename = name + str(".py")

    outputf = open(filename, "a")
    outputf.write(data)
    outputf.close()

    # Optional command to test the working of the file
    os.system("python " + filename + " " + inputFile )



