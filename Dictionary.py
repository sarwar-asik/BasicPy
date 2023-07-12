print("Python Dictionaries")

profileDic = {
    "name": {
        "firstName": "Abul",
        "lastName": "Hossain"
    },
    "email": "hossain@gmail.com",
    "role": "Admin",
    "home": "Dhaka ",
    "country": "Bangladesh",
    "contact":  609947234123,
    "address": {
        "country":{
            "name": "BD",
            "district": {
                "name": "Noakhali"
            }
        }

    }

}
print(profileDic)
print(profileDic["name"])
print(profileDic["name"]["firstName"])
district = profileDic['address']['country']['district']['name']
print(district)

# or

print(profileDic.get('name'))


# get keys from a dictionary  ####

myKeys = profileDic.keys()
nameKeys = profileDic['name'].keys()
print("keys of dictionary", myKeys)


# get values from a dictionary

myValue = profileDic.values()
nameValue = profileDic['name'].values()
print("My value of dictionary", myValue)

# looping a dictionary >>>>>>

print("loop in dictionary >>>>>>>>>>>")
for x in profileDic:
    print(x)

# loop in keys
print("loop in keys >>>>>>>>>>>")
for y in profileDic.keys():
    print(y)

# loop in values
print("loop in values >>>>>>>>>>>")
for a in profileDic.values():
    print(a)

# loop in item >>>
print("loop in item >>>>>>>>>>>")
for item in profileDic.items():
    print(item)

# copy dictionary between two dictionary ::

print('copy dictionary>>>>>>>>>>>>>>>>>>>')

duplicateDictionary = profileDic.copy()
# or >>>>>
duplicateDictionary2 = dict(profileDic)
print(duplicateDictionary)
print(duplicateDictionary2)


# replace a value
profileDic['contact'] = 12341234000000

print(profileDic.get('contact'))
