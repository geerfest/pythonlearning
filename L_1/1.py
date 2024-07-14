# int - целочисленные -2^32 0 -2^31  int8, int16, int32, int64
# float - числа с плавающей точкой 2.16
# bool (boolean) - логический тип. true & false  1, 0
# string - "s jfsdlfjsdkjfksdjfksjfsdkl"

# <, >, ==, >=, <=,  


# g o o d   d a y
# 0 1 2 3 4 5 6 7

# alphabetUpper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

k = 5
incomingMessage = input("Please input some message: ")

alphabetLower = "abcdefghijklmnopqrstuvwxyz"

secretMessage = ""

for char in incomingMessage:
    if char == " " :
        secretMessage = secretMessage + char
        continue
    # берем одну букву из нашего введеного сообщения
    # далее ищем ее позицию в строке алфавита
    index = alphabetLower.find(char)
    newIndex = index + k
    
    if newIndex > len(alphabetLower) - 1 : 
        newIndex = newIndex - len(alphabetLower)

    nextCharInAlph = alphabetLower[newIndex]
    secretMessage = secretMessage + nextCharInAlph


print(secretMessage)












































