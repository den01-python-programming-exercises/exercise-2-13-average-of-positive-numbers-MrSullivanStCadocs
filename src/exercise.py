def main():
    #write your code below this line
    amountOfPositiveNumbers = 0
    sumOfNumbers = 0
    

    while True:
      number = int(input("Give a number:"))

      if (number == 0):
        break
      
      if (number > 0):
        amountOfPositiveNumbers = amountOfPositiveNumbers + 1
        sumOfNumbers = sumOfNumbers + number
        averageOfNumbers = int(sumOfNumbers/amountOfPositiveNumbers)
    
    if(averageOfNumbers>0):
      print(averageOfNumbers)
    else:
      print("Cannot calculate the average")

if __name__ == '__main__':
    main()
