thisdict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict1["year"] = 2018
print(thisdict1)

print("_____________________________")

thisdict2 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict2.update({"year": 2020})
print(thisdict2)
