'''
the ord () function is used to print the ASCII code.

c = 'g'
# print the ASCII value of assigned character in c 
print("The ASCII value of '" + c + "' is", ord(c)) 

'''






#print("Enter a String: ", end="") 
text = input("Enter a String:") 
#textlength = len(text) 
for char in text: 
	ascii = ord(char) 
	print(char, "\t", ascii) 
