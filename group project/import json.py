import json
#load json file
with open("inventory_list.json","r") as file:
    inventory =json.load(file)
#add new item
inventory.append({
    "name": "water",
    "price": 0.70 ,
    "category":"drinks",
    "quantity":"0"
#save it to json file
with open("inventory.json", "w") as file:
    json.dump(inventory,file, indent=2)

})

