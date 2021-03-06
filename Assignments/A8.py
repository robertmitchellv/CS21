"""
A8--Word Games

--> Change user input string into Pig latin and Turkey Irish
--> Display number of vowels in user input string
   
"""
def main():
    # local variables
    endProgram = 0
    
    print('/nChange a few words into Pig Latin, Turkey Irish, and count \
           all vowels in a sentence of your choosing with Python!')
           
    while endProgram != 1:      
        # call getString function + assign to targetList variable
        targetList = getString()
        # call pigLatin; pass targetList + return string to new variable
        pigLatinTranslation = pigLatin(targetList)
        print('\nPig Latin: ', pigLatinTranslation)
        # call turkeyIrish; pass targetList + return string to new variable
        turkeyIrishTranslation = turkeyIrish(targetList)
        print('\nTurkey Irish: ', turkeyIrishTranslation)
        # test the list to vowel count code
        vowelsNumber = countvowels(targetList)   
        print('\nNumber of vowels', vowelsNumber)
        
        ans = str(input("\nWould you like to translate another \
                         sentence? ('Y' or 'N')\n--> ")).lower()
        try:
            #
            if ans not in ['y', 'n', 'yes', 'no']:
                ans = str(input("\nPlease enter 'Y', or, 'Yes' to continue; \
                                 'N', or, 'No' to quit.\n--> ")).lower()
        except NameError:
            ans = str(input("\nThat was not a valid entry; enter \
                             'Y', or 'N'\n--> ")).lower()
        # if no; exit
        if ans == 'n' or ans == 'no':
            endProgram = 1

def getString():
    # local variables
    flag = False
    # use flag to exit while loop if and only if user input is correct
    while flag != True:
        # ask the user to enter a string
        aString = str(input('\nNEW WORD SET\nEnter a sentence below. \
                             \n(Please note that sentences must contain at \
                             \nleast three words). \
                             \nEnter string here:--> ')).lower()
     
        # use split method to convert string into a separated list
        splitString = aString.split()
        
        if len(splitString) >= 3:
            # return the value as a list                             
            flag = True
        else:
            # remind user that their sentence must contain at least 3 words!
            print('\nSENTENCE MUST CONTAIN AT LEAST THREE WORDS')
    
    # return the list to main()
    return splitString
    
# conver list to pigLatin and return to main as string
def pigLatin(aList):
    pigList = aList[:]
    # for loop to move through each word; move first letter to end + 'ay'
    for index in range(len(pigList)):
        word = pigList[index]
        pigList[index] = word[1:] + word[0:1] + 'ay'
    
    # return translation as string
    return ' '.join(pigList)
        
# add 'ab' before each vowel
def turkeyIrish(aList):
    turkeyList = aList[:]
    # local variables / str for vowels + int for replacing word in list
    vowels = 'aeiou'
    i = 0
    # using the for loop to iterate through words --> letters
    for index in range(len(turkeyList)):
        eachWord = turkeyList[index]
        for letter in eachWord:
            if letter in vowels:
                # replace the letter with 'ab' then add the letter back 
                eachWord = eachWord.replace(letter, 'ab' + letter)
            # replaces the old word with the new word
            turkeyList[i] = eachWord
        # accumulator for int
        i += 1
    
    # returns the translation as a string        
    return ' '.join(turkeyList)
                
# count the vowels and return number to main
def countvowels(aList):
    # list of vowels to look for
    vowels = "aeiou"
    vowelsFromString = ""
    # convert to string before vowel hunting (easier)
    aString = ' '.join(aList)
    for eachWord in aString:
        if eachWord in vowels:
            vowelsFromString = vowelsFromString + eachWord
            
    # return the number of vowels to main
    return len(vowelsFromString)

# call the main function    
main()          