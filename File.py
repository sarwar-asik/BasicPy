# for read a file >>>
myFile = open('File.text', "r")

print(myFile.read())

writeFile1 = open('dynamicFile.html', 'w')
writeFile1.write("<p>I have been created from File.py</p>")
writeFile1 = open('dynamicFile.html', 'a')
writeFile1.write("<h1>I have been created from File.py</h1> \n")

writeFile1 = open('dynamicFile.js', 'w')
writeFile1.write("const myArray= [10,20,30,40]")

# remove a file from this>>>>>
import os

# os.remove('extra.js')


# remove folder>>>>

# os.rmdir("extaFolder")

