import sys
import os



def generatefile(name):
    bpFile = "demofile.txt"
    bpf = open(bpFile, "r")
    data = bpf.read()
    bpf.close()  
    filename = name + str(".py")

    outputf = open(filename, "a")
    outputf.write(data)
    outputf.close()

    # Optional command to test the working of the file
    os.system("python " + filename + " " + bpFile )



