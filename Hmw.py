import random 

password = ""

characters = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","0","1","2","3","4","5","6","7","8","9","-","£","$","%","^","|","&","(",")",",","_","=","+","{","}","]","[",";",":","@",".","/")



for num_characters in range(8):
    letter = random.randint(0,82)
    
    password += characters[letter]

print("Your randomly generated password is ", password)