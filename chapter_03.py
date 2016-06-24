#Create a list called dairy_section with four elements from the dairy section of a supermarket.
dairy_section = ['Fruits', 'Meat', 'Milk', 'Bread']

#Print a string with the first and last elements of the dairy_section list.
print("1. first: %s; last: %s" % (dairy_section[0], dairy_section[len(dairy_section) - 1]))

#Create a tuple called milk_expiration with three elements: the month, day, and year of the expiration date on the nearest carton of milk.
milk_expiration = (12, 10, 2009)

#Print the values in the milk_expiration tuple in a string that reads “This milk carton will expire on 12/10/2009.”
print("2. This milk carton will expire on %d/%d/%d." % (milk_expiration))

#Create an empty dictionary called milk_carton.
milk_carton = {}

#Add the following key/value pairs. You can make up the values or use a real milk carton:
#❑ expiration_date: Set it to the milk_expiration tuple.
#❑ fl_oz: Set it to the size of the milk carton on which you are basing this.
#❑ Cost: Set this to the cost of the carton of milk.
#❑ brand_name: Set this to the name of the brand of milk you’ re using.
milk_carton["expiration_date"] = milk_expiration
milk_carton["fl_oz"] = 33.33
milk_carton["Cost"] = (0.79, "Euro")
milk_carton["brand_name"] = "My favorite farm"

print("3. Milk info:\n\texpiration date:\t%d/%d/%d;\n\tfl.oz.:\t\t\t%0.2f;\n\tcost:\t\t\t%0.2f %s\n\tbrand name:\t\t%s" % (milk_carton["expiration_date"][0], milk_carton["expiration_date"][1], milk_carton["expiration_date"][2], milk_carton["fl_oz"], milk_carton["Cost"][0], milk_carton["Cost"][1], milk_carton["brand_name"]))