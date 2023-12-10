#Konsoldan gün adı isteğiniz eğer gün pazartesi ise yemek domates çorbası salı ise yemek tarhana
#çorbası çarşamba ise mercimek çorbası girilen gün perşembe ise yemek menemen cuma ise yemek
#karnıyarık cumartesi ise yemek salata paza ise yemek brokoli

print("Günün yemeğini öğrenmek için haftanın gününü yazınız.")
print("Haftanın Günü= ", end="")
haftaningunu = input()
print("Günün Yemeği= ", end="")

if haftaningunu == "pazartesi":
    print("Domates Çorbası")

if haftaningunu == "salı":
    print("Tarhana Çorbası")

if haftaningunu == "çarşamba":
    print("Mercimek Çorbası")

if haftaningunu == "perşembe":
    print("Menemen")

if haftaningunu == "cuma":
    print("Karnıyarık")

if haftaningunu == "cumartesi":
    print("Salata")

if haftaningunu == "pazar":
    print("Brokoli")
