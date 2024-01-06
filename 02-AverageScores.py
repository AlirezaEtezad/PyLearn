
sum_of_scores=0
number_of_scores=0
while True:
    
    score = float(input("please enter your score: "))
    print ("or type '-1' to finish")

    if score == -1:
        break
        
    
    number_of_scores = number_of_scores + 1
    sum_of_scores = sum_of_scores + score

average = sum_of_scores / number_of_scores
print("your average is: ",average)