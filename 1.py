#Konsoldan alınan 2 sayından büyük olanını yazdırınız

print("Hangi Sayı Daha Büyük?")

print("1. Sayınız = " , end="")
sayi1Str = input()
print("2. Sayınız = " , end="")
sayi2Str = input()

sayi1 = int(sayi1Str)
sayi2 = int(sayi2Str)

if sayi1 > sayi2:
    print(sayi1)
else:
    print(sayi2)

print(" daha büyüktür.")