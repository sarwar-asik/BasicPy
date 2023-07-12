import re

myText1 = 'My name is Sarwar Hossain Asik'
myText2 = 'The rain in Spain'

a = re.findall("[a-m]", myText1)
print("show from a-m character", a)

b = re.findall('ai', myText1)
print("show ai", b)

pattern = "^My"
c = re.findall(pattern, myText1)
print("Is start with My?", c)

if c:
    print("started with My")
else:
    print("did not started")

d = re.split("\s", myText1)

print("split with s",d)
