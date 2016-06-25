#Create a list called dairy_section with four elements from the dairy section of a supermarket.
dairy_section = ['Fruits', 'Meat', 'Milk', 'Cheeses']

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

#Print out the values of all of the elements of the milk_carton using the values in the dictionary, and not, for instance, using the data in the milk_expiration tuple.
print("3. Milk info:\n" \
      "\t-- 3.1 --\n"
      "\texpiration date:\t%d/%d/%d;\n" \
      "\tfl.oz.:\t\t\t%0.2f;\n" \
      "\tcost:\t\t\t%0.2f %s;\n" \
      "\tbrand name:\t\t%s." % ( \
          milk_carton["expiration_date"][0], milk_carton["expiration_date"][1], milk_carton["expiration_date"][2], \
          milk_carton["fl_oz"], \
          milk_carton["Cost"][0], milk_carton["Cost"][1], \
          milk_carton["brand_name"]))

print("\t-- 3.2 --\n" \
      "%24s\t%d/%d/%d;\n" \
      "%24s\t%0.2f;\n" \
      "%24s\t%0.2f %s;\n" \
      "%24s\t%s." % ( \
          "expiration date:", milk_carton["expiration_date"][0], milk_carton["expiration_date"][1], milk_carton["expiration_date"][2], \
          "fl.oz.:", milk_carton["fl_oz"], \
          "cost:", milk_carton["Cost"][0], milk_carton["Cost"][1], \
          "brand name:", milk_carton["brand_name"]))

#Show how to calculate the cost of six cartons of milk based on the cost of milk_carton.
print("4. The cost of six cartons of milk is %.2f %s" % (6 * milk_carton["Cost"][0], milk_carton["Cost"][1]))

#Create a list called cheeses. List all of the cheeses you can think of. Append this list to the dairy_section list, and look at the contents of dairy_section.
cheeses = ['Areesh', 'Domiati', 'Karish', 'Mish', 'Roumy cheese']
dairy_section.append(cheeses)
print("5. %s" % (dairy_section))

#Then remove the list of cheeses from the array.
dairy_section.pop(len(dairy_section) - 1)
print("6. %s" % (dairy_section))

#How do you count the number of cheeses in the cheese list?
print("7. The number of cheeses: %d" % (len(cheeses)))

#Print out the first five letters of the name of your first cheese.
print("8. %s" % (cheeses[0][0:5]))
