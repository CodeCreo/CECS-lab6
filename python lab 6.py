#Alex Hwang
#018306793

#assign all of the vowels in an array to compare to later
vowels_list = ["a", "e", "i", "o", "u"]
#Ask for word from user
def get_word():
    user_word = input("Please enter a word:")
    return user_word
#Search to see if the letter is one of the vowels that are in the array
def is_vowel(letter):
    if letter in vowels_list:
        return True
    else:
        return False

#Start the count at 0, so that a count exists even if no vowels do
#Find if the first letter is a vowel or a consonant
#Begin for loop excluding first character to check each letter if it's a
#vowel or consonant and using a if statement, add 1 to count if last character
#was a vowel and current is a consonant. After finding all VC's return count
def calculate_measure(string):
    count = 0
    first_letter = is_vowel(string[0])
    if(first_letter == True):
        measure = 'V'
    else:
        measure = 'C'
    for i in range (1, len(string)):
        letter = is_vowel(string[i])
        if(letter == True):
            measure = "{0}V".format(measure)
        else:
            if(measure.endswith('V')):
                count +=1
            measure = "{0}C".format(measure)   
    return count
            
#Execute everything, then print.
def main():    
    word = get_word()
    count = calculate_measure(word)
    print("{0} has a measure of {1}.".format(word, count))
    

main()
    
    
