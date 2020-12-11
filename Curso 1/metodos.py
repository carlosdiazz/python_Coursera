
def get_word(sentence, n):
	# Only proceed if n is positive 
	if n > 0:
		words = sentence.split()
		# Only proceed if n is not more than the number of words 
		if n <= len(words):
			return(words[n-1])
	return("Nothing")

print(get_word("This is a lesson about lists", 4)) # Should print: lesson
print(get_word("This is a lesson about lists", -4)) # Nothing
print(get_word("Now we are cooking!", 1)) # Should print: Now
print(get_word("Now we are cooking!", 5)) # Nothing





def replace_ending(sentence, old, new):

	if sentence.endswith(old):

		i=len(old)

		new_sentence = sentence[0:len(sentence)-i] + new
		return new_sentence

	return sentence
	
#print(replace_ending("It's raining cats and cats", "cats", "dogs")) 
# Should display "It's raining cats and dogs"
#print(replace_ending("She sells seashells by the seashore", "seashells", "donuts")) 
# Should display "She sells seashells by the seashore"
#print(replace_ending("The weather is nice in May", "may", "april")) 
# Should display "The weather is nice in May"




def is_palindrome(input_string):
	# We'll create two strings, to compare them
	new_string = ""
	reverse_string = ""
	rever=""
	ok=-1

	for i in input_string.upper():
		reverse_string =  reverse_string + input_string[ok]
		ok=ok-1
		
	# Traverse through each letter of the input string
	for i in reverse_string.upper():
		if i != " ":
			rever=rever+i

	for i in input_string.upper():
		# Add any non-blank letters to the 
		# end of one string, and to the front
		# of the other string. 
		if i != " ":
			new_string = new_string+i

	# Compare the strings
	if new_string == rever:
		return True
	return False


#print(is_palindrome("Never Odd or Even")) # Should be True
#print(is_palindrome("abc")) # Should be False
#print(is_palindrome("kayak")) # Should be True


# def impuesto(precio,impuesto):
#     return ("El precio del producto es: {:.2f} y con impuesto seria: {:.2f}".format(precio,precio+(precio*impuesto/100)))

# print(impuesto(50,50))

# def to_celsius(x):
#     return(x-32)*5/9

# for x in range(0,101,10):
#     print("{:>3} F || {:>6.2f} C".format(x,to_celsius(x)))


# def impuesto(precio,impuesto):
#     return ("El precio del producto es: {:.2f} y con impuesto seria: {:.2f}".format(precio,precio+(precio*impuesto/100)))



# print(impuesto(50,50))


# def initials(phrase):
#     words = phrase.upper()
#     result = words[0]
#     contador=0
#     for word in words:
#         if word ==" ":
#             result = result+words[contador+1]
#         contador=contador+1
#     return result

# print(initials("Universal Serial Bus")) # Should be: USB
# print(initials("local area network")) # Should be: LAN
# print(initials("Operating system")) # Should be: OS



# #Un metodo para agreagr varible en una cadena
# def student_grade(name, grade):
# 	return "{} received {}% on the exam".format(name,grade)

# print(student_grade("Reed", 80))
# print(student_grade("Paige", 92))
# print(student_grade("Jesse", 85))


# #Para saber si una cadena termina con un caracte
# print("hola como estas".endswith("s"))


# #Eliminr espacio en blanco,  la izquierda
# print("    hola    ".lstrip())

# #Eliminr espacio en blanco a la derecha
# print("    hola    ".rstrip())

#print("32342".isnumeric())
#print("sdfa".isnumeric())

#Este metodo es para unirlo depediendo el caracte que este en el join
#print(" ".join(["hola","como","esta","estoy","bien"]))
#print("----".join(["hola","como","esta","estoy","bien"]))

#esto lo devuelve enun lista
#print(" hola como estas yo estoy bien".split())