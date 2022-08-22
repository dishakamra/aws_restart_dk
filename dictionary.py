myFavoriteFruitDictionary = {
  "ap" : "apple",
  "ba" : "banana",
  "pi" : "pineapple"
}
print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))

print(myFavoriteFruitDictionary["ap"])
print(myFavoriteFruitDictionary["pi"])
print(myFavoriteFruitDictionary["ba"])

myFavoriteFruitDictionary["ba"] = "orange"

print("The new values")

print(myFavoriteFruitDictionary["ap"])
print(myFavoriteFruitDictionary["pi"])
print(myFavoriteFruitDictionary["ba"])
