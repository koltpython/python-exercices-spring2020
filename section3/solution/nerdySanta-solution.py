age = int(input("Ho ho hooo! What is your age?:"))
isPrime = True

while age > 0:
    if age == 1:
        print("Sorry, I don't have a gift for you")
    else:
        for number in range(2, age):
            if age % number == 0:
                print("Sorry, I don't have a gift for you")
                isPrime = False
                break
        if isPrime:
            print("I have a gift for you!")
    age = int(input("Ho ho hooo! What is your age?:"))

if age <= 0:
    print("Sorry, age is invalid.")
