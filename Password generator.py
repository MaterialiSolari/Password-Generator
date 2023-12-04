import random
import string

def password():
    
    def generate_randomUpperCase_letter():
        num_count = 0
        randomLetters = []
        
        user_input_letters = int(input('How many upper case letters should your password have? '))
        if user_input_letters > 0:     
            
            while num_count < user_input_letters:
                upperCaseLetter = chr(random.randint(65, 90))
                randomLetters.append(upperCaseLetter)
                num_count += 1
                            
            print(f'These are your randomly chosen upper case letters: {" - ".join(randomLetters)}')
        
        elif user_input_letters == 0:
            print('No upper case letter will be added')
        return randomLetters
      
    def generate_randomLowerCase_letter():
        num_count = 0
        randomLower_Case_Letters = []
        
        user_input_letter = int(input('How many lower case letters should your password have? '))
        if user_input_letter > 0:
            
            while num_count < user_input_letter:
                randomlowercase = chr(random.randint(97, 122))
                randomLower_Case_Letters.append(randomlowercase)
                num_count += 1
            print(f'These are your randomly chosen lower case letters: {" - ".join(randomLower_Case_Letters)}')
            
        elif user_input_letter == 0:
            print('No lower case letters will be added')
        
        return randomLower_Case_Letters
        
              
    def generate_random_number():
        num_count = 0
        num_array = []
        user_input_number = int(input('How many numbers should your password have? '))
        
        if user_input_number > 0:
            
            while num_count < user_input_number:
                random_number = random.randint(0, 9)
                num_array.append(str(random_number))
                num_count += 1
            print(f'These are your randomly chosen numbers: {" - ".join(num_array)}')
            
        elif user_input_number == 0:
            print('No numbers will be added')
        return num_array
              
    def generate_random_punctuation_sign():
        punctuation_count = 0
        punctuation_array = []
        user_input_punctuation = int(input('How many punctuations should your password have?'))

        if user_input_punctuation > 0:
            while punctuation_count < user_input_punctuation:
                random_punctuation = random.choice(string.punctuation)
                punctuation_array.append(random_punctuation)
                punctuation_count += 1

            print(f'These are your randomly chosen punctuations: {" ,".join(punctuation_array)}')

        elif user_input_punctuation == 0:
            print('No punctuations will be added')
            
        return punctuation_array  
    
    password_gen = (
        generate_randomUpperCase_letter() +
        generate_randomLowerCase_letter() +
        generate_random_number() +
        generate_random_punctuation_sign()
    )
    
    random.shuffle(password_gen)
    shuffled_password = ''.join(password_gen)
    print(f'This is your password: {shuffled_password}')
     
password()
