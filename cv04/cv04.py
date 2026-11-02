def mean():
    N = int(input("Zadej kolik chces zadat cisel: "))
    numbers = []
    for i in range(N):
        number = int(input(f"Zadej {i+1}. cislo: "))
        numbers.append(number)

    print(sum(numbers) / len(numbers))



n = 156432 # [1,5,6,4,3,2]
lst = []
while n != 0:
    lst.append(n % 10)
    n = n // 10
print(lst)
