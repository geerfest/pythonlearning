k = 5
secret = input("Please input secret message: ")

alphabetLower = "abcdefghijklmnopqrstuvwxyz"

simpleMessage = ""

for char in secret:
    if char == " " :
        simpleMessage = simpleMessage + char
        continue
    # берем одну букву из нашего введеного сообщения
    # далее ищем ее позицию в строке алфавита
    index = alphabetLower.find(char)
    newIndex = index - k
    
    if newIndex < 0 : 
        newIndex = len(alphabetLower) - (newIndex * -1)

    nextCharInAlph = alphabetLower[newIndex]
    simpleMessage = simpleMessage + nextCharInAlph


print(simpleMessage)