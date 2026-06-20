print('Kalkulator')
import sys
num1=int(sys.argv[1])
num2=int(sys.argv[3])
print(f"Pierwsza liczba to: {num1}")
print(f"Druga liczba to: {num2}")
if sys.argv[2]=='+':
    print("Wynik:", num1+num2 )

elif sys.argv[2] == '-':
    print("Wynik:", num1 - num2)
elif sys.argv[2] == '*':
     print("Wynik:", num1 * num2)
elif sys.argv[2] == '/':
    print("Wynik:", num1 / num2)