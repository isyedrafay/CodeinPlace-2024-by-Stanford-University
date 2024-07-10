import random

num_1 = random.randint(10,99)
num_2 = random.randint(10,99)
def main():
    print("Khansole Academy")
    print("What is " + str(num_1) + " + " + str(num_2) + "?")
    Correct_Ans = num_1 + num_2
    User_Ans = int(input("Your answer: "))

    if User_Ans == Correct_Ans:
        print("Correct!")
    else:
        print("Incorrect.")
        print("The expected answer is",Correct_Ans)
    
    
    
if __name__ == '__main__':
    main()