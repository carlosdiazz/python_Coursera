
def octal_to_string(octal):
    result = ""
    value_letters = [(4,"r"),(2,"w"),(1,"x")]
    # Iterate over each of the digits in octal
    for i in [int(n) for n in str(octal)]:
        # Check for each of the permissions values
        for value, letter in value_letters:
            if ___ >= value:
                result += ___
                ___ -= value
            else:
                ___
    return result
    
print(octal_to_string(755)) # Should be rwxr-xr-x
print(octal_to_string(644)) # Should be rw-r--r--
print(octal_to_string(750)) # Should be rwxr-x---
print(octal_to_string(600)) # Should be rw-------






# def guest_list(guests):
# 	for i in guests:	
# 		print("{} is {} years old and works as {}".format(i[0],i[1],i[2]))

# guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])


# def group_list(group, users):
#     members = group + ": "
#     for i in users:
#         members= members + i + ", "
    
#     if members.endswith(", "):
#         members=members[0:-2]
    
#     return members


# print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
# print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
# print(group_list("Users", "")) # Should be "Users:"




# def pig_latin(text):
#     say = "ay"
#   # Separate the text into words
#     words = text.split()
#     lista=[]
  
#     for word in words:

#         say=word[1:]+word[0]+"ay"
#         lista.append(say)

    
#     return " ".join(lista)
		
# print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
# print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"



# filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]

# def cambiar(filesnames):
#     new=[]
#     for i in filenames:

#         if i.endswith(".hpp"):
#             nueva=i[0:i.find(".hpp")]+".h"
#             new.append(nueva)
#         else:
#             nueva=i
#             new.append(nueva)

#     return new


# nueva=cambiar(filenames)

# print(nueva

# #print(newfilenames) 
# # Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]