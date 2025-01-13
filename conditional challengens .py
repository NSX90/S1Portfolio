# Challenge 1
#This Function prints a message/ determines wheter you are egilble to vote
#to vote
#18 years or over
#U.S Citizen
def vote_Check():
    #Collect your input
    age = int(input("Please enter your age: "))#Input by defult collects a string
    Citizen = input("Are you a U.S Citizen(Yes, No):")
    #Process the data/ conditional statements
    if int(age)  > 17 and Citizen =="Yes" : #Evaluates TRUE OR FALSE
        print("You are old enough to vote")
    else:
        print("You are NOT eligible to vote")
    #Process the data using conditional statments
#vote_Check()
#Challenge 2
#a = integer #b = integers #c = integers
#Prints the largest of the three numbers(a,b,c)
def max_num(a,b,c):
    #No input needed
    #Use conditional statements to figure out max number
    if a > b and a > c:
        print("a is the largest, the value of a is:" +str(a))
    if b < a and b > c:
        print("b is the largest, the value of a is" +str(b))
    if c < a and c < b:
        print("c is the largest, the value of a is" +str(c))
#max_num(10,3,5)

#Challenge 3
#This function takes in a score (integer) and print a grade(string)
#score = integer
def score_to_grade(score):
    if score >= 90 and score <= 100:
        print("A")
    elif score <=89 and score >= 80:
        print("B")
    elif score <=79 and score >= 70:
        print("C")
    elif score <=69 and score >= 60:
        print("D")
    elif score <=59 and score >= 0:
        print("F")
    elif score < 0 or score > 100:
        print("Invaild Input. Please try again")
score_to_grade(100)
