# aritmeticke op.
## +, -, /, *, //, %, **
# relacni
## ==, !=, <, >, <=, <=, is, not, in
# logicky
## and or
# prirazovaci
## =, +=, -=, *=, /= 
# bitovy
## &, |, ^, <<, >>, ~

# A = 0b10100111
# B = 0b10011010

# A & B = 0b10000010
# A | B = 0b10111111
# A ^ B = 0b00111101
# ~A = 0b01011000
# A << 4 = 0b01110000
# B >> 4 = 0b00001001

## Nactete INT (s) ze vstupu a naformatujte ho na hh:mm:ss

## 360 -> 00:06:00
def time_fomate():
    str_time = input("Zadej cas v S:")
    time = int(str_time)
    hour =  time // 3600
    minut = (time % 3600) // 60
    second = (time % 3600) % 60
    print(f"{hour}:{minut}:{second}")


if __name__ == "__main__":
# vytvorte automat, ktery vam rozmeni castku X na:
# 5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1
    value = int(input("Zadej castku: "))
    money = [5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
    for item in money:
        count = value // 5000
        value = value - (count * 5000)
        print(f"{count}x{item}")