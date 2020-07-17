#tutorial
"""
def addCalc(number1, number2):
    answer = number1 + number2
    return answer

addedNumber = addCalc(5,5)
print(addedNumber + 20)
________________________________________________
"""
#exercise community page

#create function to calculate the final mark
def ictGrade():
    #get the name and marks
    name = input("Please enter your name here: ")
    homework = int(input("Please enter your homework mark here: "))
    assessment = int(input("Please enter your assessment mark here: ")) 
    finalExam = int(input("Please enter your final exam mark here: "))
    #calculate the final mark 
    hm = (homework/25)*100                                                      
    assmt = (assessment/50)*100   
    fe=(finalExam/100)*100
    finalMark = (hm+assmt+fe)/3  
    #return the final mark
    return finalMark

#create function to print the final grade
def printGrade(finalGrade):
    if finalGrade >=70:
        return("A")
    elif finalGrade >= 60:
        return("B")
    elif finalGrade >= 50:
        return("C")
    else:
        return("Fail")

print(printGrade(ictGrade()))