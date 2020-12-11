
# def add_prices(basket):
# 	# Initialize the variable that will be used for the calculation
# 	total = 0
# 	# Iterate through the dictionary items
# 	for precio in basket.values():
# 		# Add each price to the total calculation
# 		# Hint: how do you access the values of
# 		# dictionary items?
# 		total += precio
# 	# Limit the return value to 2 decimal places
# 	return round(total, 2)  

# groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59, 
# 	"coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

# print(add_prices(groceries)) # Should print 28.44






# wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
# new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
# wardrobe.update(new_items)


# print(wardrobe)



# def groups_per_user(group_dictionary):
# 	user_groups = {}
# 	# Go through group_dictionary
# 	for grupo, usuarios in group_dictionary.items():
# 		# Now go through the users in the group
# 		for nuevo in usuarios :

# 			if nuevo in user_groups:
# 				user_groups[nuevo]=user_groups[nuevo]+[grupo]
# 			else:
# 				user_groups[nuevo]=[grupo]
# 			# Now add the group to the the list of
# # groups for this user, creating the entry
# # in the dictionary if necessary

# 	return(user_groups)

# print(groups_per_user({"local": ["admin", "userA"],
# 		"public":  ["admin", "userB"],
# 		"administrator": ["admin"] }))





# def email_list(domains):
# 	emails = []
# 	for dominio,users in domains.items():
# 	    for user in users:
# 		    emaill=user+"@"+dominio
# 		    emails.append(emaill)
# 	return(emails)

# print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))