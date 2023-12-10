#Konsoldan alınan 2 sayından büyük olanından küçük olanını çıkartınız

print("1. Sayı = " , end="")
sayi1Str = input()

print("2. Sayı = " , end="")
sayi2Str = input()

sayi1 = int(sayi1Str)
sayi2 = int(sayi2Str)

if sayi1 > sayi2:
    fark = sayi1 - sayi2
else:
    fark = sayi2 - sayi1
print("Fark = " , end="")
print(fark)