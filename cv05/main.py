def linear():
    x = int(input("Zadej kolik chceš čísel: "))
    lst = []
    for _ in range(x):
        i = int(input("Zadej číslo: "))
        lst.append(i)
    p = int(input("Zadej číslo, které hledáš: "))    
    for index, num in enumerate(lst): 
        if num == p:
            print(f"Číslo se nachází v seznamu na indexu {index}")
            return    
    print("Číslo se nenachází v seznamu")   


def binarysearch():
    search = 8
    lst = [6,1,2,3,4,5,5,6,8,4,5,6]
    lst.sort()
    left = 0
    right = len(lst) - 1
    middle = (left + right) // 2
    while right - left != 1:
        middle = (left + right) // 2
        if lst[middle] == search:
            print("Nalezeno")
            return 1
        if lst[middle] > search:
            right = middle
        if lst[middle] < search:
            left = middle

    if lst[0] == search or lst[-1] == search:
        print("Nalezeno")    
        return 1

    print("Nenalezeno")      



if __name__ == "__main__":
    binarysearch()