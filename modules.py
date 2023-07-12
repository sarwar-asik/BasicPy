import interators


a = interators.MyList
# print(a)

import interators as listNAME

b =listNAME
# print(listNAME)

import  platform

x =platform.system()
print("platform system",x)

y = dir(platform)
print("dir===", y)


from  mymodules import person1
print("imported from mymodule", person1)
