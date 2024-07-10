import random

def main():
    num1 = input("How many slides does your dice have? ")
    print(random.randint(0,int(num1)))
    

if __name__ == '__main__':
    main()