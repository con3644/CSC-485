
#    Group #2 - Program 2 - Grade Averaging Program             
#    Andrew Weaver, Jordan Westfall, Max Conroy                 
#    CSC 485 - Special Topics in Computer Science - Python      

#Basic grade calculator program

# Command handler
def main():

    printTitle()
    promptInput()
    
    
    

    
    
# This function is used to dipslay the title for the program    
def printTitle():
    print("-----------------------------------------------------------------------------------")
    print("                       Welcome to the Grade Calculator Program                     ")
    print("-----------------------------------------------------------------------------------")
    print(" - Enter a valid grade between 0 and 100   ")
    print(" - Entering a grade outside of the range will terminate input")
    print(" - After entering an invalid grade the program will calculate all of the grades")
    print(" - If no valid grades are entered the program will terminate")
    print("-----------------------------------------------------------------------------------")
    
    
# promptInput() is a loop that prompts the user for input as long as the grades are in a valid range    
def promptInput():
    programCounter = 0      # Program counter for the input
    gradeInput = 0          # Variable used to store grade input
    gradeList = []          # List that stores all of the grades input by the user
    
    while gradeInput >= 0 and gradeInput <= 100:        #Loop executes while the users input is within the valid range
        gradeInput = raw_input("Enter a grade: ")       #Prompt for grade input
       
        if isNumber(gradeInput) == True:                #Handle if the user entered a valid number and not a letter/word
            gradeInput = float(gradeInput)              #Converts the local variable to a float
            if gradeInput < 0 or gradeInput > 100:      #Checks to see if the grade is valid
                promptCalculation(gradeList)            #Calls the invalid Grade function to terminate input and calculate totals 
            else:
                gradeList.append(gradeInput)            #Inserts the valid grade into the list at the address of the program counter
                programCounter += 1                     #Increment the program counter
        else:
            print("You did not enter a valid number, please enter valid number.")   #Warning message to the user
            gradeInput = 0                              #Reset the input to meet loop conditions
 
# promptCalculation() is accepts the program counter and the list of grades to call the calculation functions           
def promptCalculation(gradesList):
   
    numberElements = len(gradesList)                        # Retrieves the number of elements in a list
    
    if numberElements > 0:                                      # Handle if the user didn't enter any values
        gradeSum = sum(gradesList)                              # Sums the elements in the list
        averageGrades = gradeSum/numberElements                 # Divides the sum of the grades by the number of grades to get the average
        letterGrade = calculateLetterGrade(averageGrades)       # Determines the letter grade

        printTotal(numberElements, gradeSum, averageGrades, letterGrade) 
    else:
        print("Sorry, you did not enter any valid grades for calculation!")
        print("Program Terminated, restart the program to enter valid grades.")
    
    
# This functions prints out the information to the user
def printTotal(numberOfElements, sumOfGrades, averageOfGrades, letterOfGrades):
    print("Grade out of valid range totals now being calculated...")
    print("-----------------------------------------------------------------------------------")   
    print("There were a total of "+ str(numberOfElements) +" grades entered that totaled up to "+ str(sumOfGrades))
    print("The average of the grades entered was " + str("{:.2f}".format(averageOfGrades)) + " which is an average letter grade of: " + str(letterOfGrades))
    
 
# This function handles the letter grade using simple if based logic   
def calculateLetterGrade(gradeAverage):
    if gradeAverage <= 60:
        letterGrade = "F"
    elif gradeAverage > 60 and gradeAverage < 70:
        letterGrade = "D"
    elif gradeAverage > 70 and gradeAverage < 80:
        letterGrade = "C"
    elif gradeAverage > 80 and gradeAverage < 90:
        letterGrade = "B"
    elif gradeAverage >= 90:
        letterGrade = "A"
        
    return letterGrade  

# Checks to see if the number is a number or not
def isNumber(x): 
    try:                    #Try statement to handle exception if the string cannot be cast
        x = float(x)        #Casting statement
        return True         #If the cast is successful return true
    except ValueError:      #Catch the ValueError exception if the string cannot be converted to a float
        return False        #Return False back to the function
    

main()    
