#break & continue

maaslar = [8000,5000,2000,1000,3000,7000,1000]

maaslar.sort()
# print(maaslar.sort())

for i in maaslar:
    if i ==3000:
        print("kesildi")
        break # 3000 değerine geldi ve döngüyü durdurdu.
    print(i)

for i in maaslar:
    if i == 3000:
        continue # bu değer kontrol ifadesine takıldı ve 3000 değeri atlandı.
    print(i)

