message = "Hey"
print(message)

#problem 1.) if user enters a programming language that is from the list then 
# it will print that language

#Variables
programmingLanguages = ["Python", "Javascript", "HTML", "C++", "C#"]
userInput = input("Please type your favorite coding language: ")

#function
def findLangInList(userInput, programmingLanguages):
    for x in programmingLanguages:
        if(userInput == x):
          print(userInput)
          return userInput

#calling final function
findLangInList(userInput, programmingLanguages)

#problem 2.) write a function that takes a minimun and max number and returns a 
# random number between

#importing module
import random

#function
def randomNumInMaxMin(min, max):
    return random.randint(min, max)

# calling function
print(randomNumInMaxMin(1,5))

#problem 3.) write a function that takes a word and returns the reverse of that word

#function
def reversedWord(userInput):
   reversed = userInput[::-1] 
   return reversed

#calling function
print(reversedWord(input("Enter word")))

#problem 4.) write a function that print every number from 100 to 0 and 
#prints "Banana" if number is div by 4
#prints "Flamingo" if number is div by 7
#prints "Flamingo-Banana" if div by 4 and 7

def bananaFlamingo(num):
    for num in range(num, 0, -1):
        if(num % 7 == 0 and num % 4 == 0):
            print("Flamingo-Banana")
        elif(num % 7 == 0):
            print("Flamingo")
        elif(num % 4 == 0):
            print("Banana")
        else:
            print(num)

#calling function
bananaFlamingo(100)

#problem 5.) Write a function that takes a list of numbers and returns a new list 
# with all the numbers less than 5

#function
def lessThanFive(list):
    newList = []
    for x in list:
        if(x < 5):
            newList.append(x)
    print(newList)
    return newList

#Calling function
lessThanFive([1, 2, 3, 7, 8, 9, 45, 134, 43, 2, 3, 1, 6, 7, 5, 4])

#problem 6.) Write a function that prompts the user for their age and name,
#then prints out their name and what year they will turn 100

def hundredYears(name, age):
    
    currentYear = 2021
    yearsLeft = 100 - age
    final = currentYear + yearsLeft
    string = f"Hello {name}. In the year {str(final)}, you will turn 100!"
    print(string)
    return string

#calling function
hundredYears('spencer', 23)

#problem 7.) Write a function that takes two lists and compares them,
#then returns a list with all the elements in common between both

def commonLists(list1, list2):
    newList = []
    for i in list1:
        for j in list2:
            if(i == j):
                newList.append(i)
    print(newList)
    return newList

#calling function
commonLists([1,2,3,4,5],[1,3,5,6,4])

#problem 8.) write a function that knows if two words are an anagram

def findAnagram(word1, word2):
    isTrue = False
    
    if(len(word1) == len(word2)):
        for i in word1:
            for j in word2:
                if(i == j):
                    isTrue = True
        for i in word2:
            for j in word1:
                if(i == j):
                    isTrue = True
    else:
        isTrue = False
    return isTrue

#calling function

print(findAnagram("her", "erh"))

#problem 9.) Write a function that takes a sentence and reverses each word
#but maintains where the words are in the sentence ex.) "Hello world" prints "olleh dlrow"

def reverseWordsInSentence(sentence):
    string = list()

    for i in sentence:
        if(i == " "):
            string.append(i)

        else:
            while len(string) > 0:
                print(string[-1], end= "")
                string.pop()
            print(end = " ")

    while len(string) > 0:
        print(string[-1], end = "")
        string.pop()

reverseWordsInSentence("Hello World")

#problem 10.) print a downward pyramid pattern with star (asterisk)

print(" ")
print("* * * * *")
print(" * * * * ")  
print("  * * *  ")
print("   * *   ")
print("    *    ")              

