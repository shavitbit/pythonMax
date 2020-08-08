customer = {
    "name": "Oren bahar",
    "age": 34,
    "is_VIP": True
}
print(customer["name"])
print(customer.get("age"))
customer["age"] = 16
# add new key value to the dictionary
customer["birthdate"] = "Jan 3 1986"
