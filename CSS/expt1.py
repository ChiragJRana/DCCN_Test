import string
import random
import math

def substitution(text, shift = 0):
    
    if not shift: # Check whether it is ROT13 or Substitution
        shift = int(input('Enter the number of position shifts: ')) 
    
    # Get the lower and upper case letters
    lowercase_letters=string.ascii_lowercase
    uppercase_letters=string.ascii_uppercase
    
    ll = len(lowercase_letters)
    ul = len(uppercase_letters)                            
                                
    ########## ENCRYPTION  ##########

    #Create a dictionary to store all letters with their substitution using formula (x+n)mod26
    substitutionDict1 = {}

    for i in range(ll) :
        substitutionDict1[lowercase_letters[i]]= lowercase_letters[(i+shift)%ll]
        
    for i in range(ul) :
        substitutionDict1[uppercase_letters[i]]= uppercase_letters[(i+shift)%ul]

    cipher_text = ''
    for c in text:
        cipher_text += substitutionDict1[c] if c in lowercase_letters or c in uppercase_letters else c

    print('Encrypted text :',cipher_text)

    ######### DECRYPTION ########

    # A dictionary for decrypting each letter (x-n)mod26
    substitutionDict2 = {}

    for i in range(ll) :
        substitutionDict2[lowercase_letters[i]]= lowercase_letters[(i-shift)%ll]
        
    for i in range(ul) :
        substitutionDict2[uppercase_letters[i]]= uppercase_letters[(i-shift)%ul]

    decrypt_text  = ''

    for char in cipher_text :
        decrypt_text  += substitutionDict2[char] if char in lowercase_letters or char in uppercase_letters else char 

    print('Decrypted Text: ', decrypt_text)


def rot13(text):
    substitution(text,shift = 13)

def Transpose(text):
    cipher_msg=''
    key=[]

    # Randomly generate a key
    key=random.sample(range(5),5)
    
    msg_len=len(text)
    col=len(key)
    row= int(math.ceil(msg_len/col))

    msg_list=list(text)   #Convert message into list

    ############# ENCRYPTION ###########

    fill_null = int((row * col) - msg_len) 
    msg_list.extend(['-']*fill_null)    
    # Put the _ character into empty cells at the end of the message.

    matrix=[ msg_list[i: i+col] for i in range(0,len(msg_list),col)]
    
    # Iterate matrix column wise
    for i in range(col):
        curr_idx=key[i]
        cipher_msg+=''.join([row[curr_idx] for row in matrix])    
        # Add all the letters in the current column represented by curr_idx

    print('Encrypted text : ',cipher_msg)
    ############# DECRYPTION ###########

    decrypt_msg=''  #Decrypted message
    cipher_idx=0    #Keep track of ciphered message index
    c_list=list(cipher_msg) #Convert cipher message into a list

    # Matrix to store deciphered message
    dec_matrix = [] 
    for i in range(row):
        dec_matrix+=[[None]*col]    #Fill all cells of matrix with None

    # Arrange the message columnwise into the decipher matrix according to the key
    for i in range(col):
        curr_idx=key[i]

        for j in range(row):
            dec_matrix[j][curr_idx]=c_list[cipher_idx]  
            #Take the letter from the cipher message and put it into correct position
            cipher_idx+=1

    decrypt_msg = ''.join(sum(dec_matrix, []))    

    null_count = decrypt_msg.count('-') 
    # Count of the _ character
    
    if null_count > 0: 
        decrypt_msg= decrypt_msg[: -null_count] #Remove the _ character from the message

    print('Decrypted Text: ',decrypt_msg)
    
def Double_Transpose(text):
    cipher_msg1=''
    cipher_msg2=''
    key=[]

    key=random.sample(range(5),5)
    # Randomly generate a key

    msg_len=len(text)

    col=len(key)
    row=int(math.ceil(msg_len/col))

    ############# ENCRYPTION ###########

    msg_list1=list(text)   #Convert message into list
    
    fill_null = int((row * col) - msg_len) 
    msg_list1.extend('-' * fill_null)    
    # Put the _ character into empty cells at the end of the message.

    matrix1=[ msg_list1[i: i+col] for i in range(0,len(msg_list1),col) ]  
    
    # Iterate matrix column wise
    for i in range(col):
        curr_idx=key[i]
        cipher_msg1+=''.join([row[curr_idx]
                        for row in matrix1])    
        # Add all the letters in the current column represented by curr_idx
    
    #### Encrypt again
    msg_list2=list(cipher_msg1)

    matrix2=[ msg_list2[i: i+col]
              for i in range(0,len(msg_list2),col)]

    for i in range(col):
        curr_idx=key[i]
        cipher_msg2+=''.join([row[curr_idx] for row in matrix2])
    
    print('Encrypted text 1 : ',cipher_msg1)
    print('Encrypted text 2: ',cipher_msg2)

    ############# DECRYPTION ###########

    decrypt_msg1=''  #Decrypted message
    decrypt_msg2=''  #Decrypted message

    cipher_idx1=0    #Keep track of ciphered message index
    c_list1=list(cipher_msg2) #Convert cipher message into a list

    # Matrix to store deciphered message
    dec_matrix1 = [] 
    for i in range(row):
        dec_matrix1+=[[None]*col]    #Fill all cells of matrix with None

    # Arrange the message columnwise into the decipher matrix according to the key
    for i in range(col):
        curr_idx=key[i]
        for j in range(row):
            dec_matrix1[j][curr_idx]=c_list1[cipher_idx1]  
            #Take the letter from the cipher message and put it into correct position
            cipher_idx1+=1

    # Convert decipher matrix into decrypted message
    # Sum() combines all the rwos in the matrix into a single array
    # And then join all the elements to form a string
    decrypt_msg1 = ''.join(sum(dec_matrix1, []))    

    ###### decrypt again

    cipher_idx2=0       #Keep track of the first decrypted message
    c_list2=list(decrypt_msg1)  

    # Second matrix 
    dec_matrix2=[]
    for i in range(row):
        dec_matrix2+=[[None]*col]

    for i in range(col) :
        curr_idx=key[i]
        for j in range(row):
            dec_matrix2[j][curr_idx]=c_list2[cipher_idx2]
            cipher_idx2+=1
        
    decrypt_msg2=''.join(sum(dec_matrix2,[]))

    null_count = decrypt_msg2.count('-') 
    # Count of the _ character
    
    if null_count > 0: 
        decrypt_msg2= decrypt_msg2[: -null_count] #Remove the _ character from the message
    
    print('Decrypted Text 1: ',decrypt_msg1)
    print('Decrypted Text 2: ',decrypt_msg2)

def Vernam_Cipher(text):
    letters=string.ascii_lowercase
    
    key = input('Enter the key: ')
    msg_len=len(text)
    key_len = len(key)
    if key_len != msg_len:
        print("Enter the key of the same length")
        print("Try again")
        return

    # Convert strings into lists
    input_msg_list=list(text)
    key_list=list(key)
    # Numbers corresponding to the letters in the input msg and key
    msg_letter_numbers=[]
    key_letter_numbers=[]
    
    # Add numbers to list
    for i in range(msg_len):
        msg_letter_numbers.append(letters.index(input_msg_list[i]))
        key_letter_numbers.append(letters.index(key_list[i]))
    
    #########  ENCRYPTION #########

    cipher_list=[]

    # Iterate through the lists
    for i in range(len(msg_letter_numbers)) :
        # XOR the numbers from both lists
        sumval=msg_letter_numbers[i]^key_letter_numbers[i]
        sumval=sumval%26
        char=letters[sumval] # Get the character corresponding to the numbers
        cipher_list.append(char)

    cipher_text=''.join(cipher_list)    # The cipher text
   
    
    print('Encrypted text : ',cipher_text)
    #########  DECRYPTION #########

    dec_list=[]

    # Iterate through the lists
    for i in range(len(cipher_list)) :
        # XOR the numbers from both lists
        sumval=letters.index(cipher_list[i])^key_letter_numbers[i]
        sumval=sumval%26
        char=letters[sumval] # Get the character corresponding to the numbers
        dec_list.append(char)
    

    decrypt_msg=''.join(dec_list)
    print('Decrypted Text: ',decrypt_msg)


def main():

    option = int(input(''' 
    Select from the Cryptography Method
        1) Substitution
        2) ROT 13
        3) Transpose
        4) Double Transposition
        5) Vernam Cipher 
    Your Choice: '''))

    options = {
        1: substitution,
        2: rot13,
        3: Transpose,
        4: Double_Transpose,
        5: Vernam_Cipher,
    }

    funct = options.get(option,lambda: 'Invalid')
    text= input('Enter the Plain Text to be encrypted: ')

    return funct(text)

    



if __name__ == '__main__':
    
    while True:
        main()
        condition = input('Want to continue?')
        if condition == 'No':
            break
    