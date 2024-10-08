# You will define and write each function for the task in this file

#Task 1
def temperature_converter(temperature: int, unit: str): #Converts Farenheit or Celcius to its counterpart using a temperature and the specified unit via "C" or "F"
    if unit == "C": 
        newunit = (temperature*5/9)+32 #Conversion Equation
        converted = str(newunit) + " F" #Creating string
        return converted
    else:
        newunit = (temperature-32) * 5/9 #Ditto
        converted = str(newunit) + " C" #Ditto
        return converted

#print(temperature_converter(0, "C"))

#Task 2 
def reversal(string: str): #Reverses any given string
    if string == "":
        return string
    else:
        return reversal(string[1:]) + string[0] # String splices to pass each character to the recursion string to return it

#print(reversal("Fair123"))

#Task 3
def fib(N: int):
    if N <= 1: #If N is 1 or 0; Fibonacci sequence has 0 and 1 equal the same number.
        return N
    else:
        return fib(N-1) + fib(N-2) #Formula for the fibonacci sequence, using recursive functions

#print(fib(6))

