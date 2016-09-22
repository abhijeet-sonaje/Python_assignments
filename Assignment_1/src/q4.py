complexno1 = 2 + 3j
complexno2 = 4 + 6j

def addition(no1,no2):
    no3 = no1 + no2  
    print('Addition of two complex numbers:',no1,'+',no2,'=',no3)

def subtraction(no1,no2):
    no3 = no1 - no2
    print('Subtraction of two complex numbers:',no1,'+',no2,'=',no3)

def multiplication(no1,no2):
    no3 = no1 * no2
    print('Multiplication of two complex numbers:',no1,'+',no2,'=',no3)

def swap(no1,no2):
    no1 = complex(no1.imag,no1.real)
    no2 = complex(no2.imag,no2.real)
    print('Swapping of two complex numbers:',no1,no2)

addition(complexno1,complexno2)
subtraction(complexno1,complexno2)
multiplication(complexno1,complexno2)
swap(complexno1,complexno2)
