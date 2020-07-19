soru = print('Yapay Zeka :: Lütfen bilgileri giriniz..')
x = input('Yapay Zeka :: İsmi yazınız.')
c = input('Yapay Zeka :: Şifre yazınız.')

if x == "username" and c == "pass":
    print('Yapay Zeka :: Giriş başarılı!')
    tss = input('Yapay Zeka :: Ne işlem yapmamı istersin? \nDediklerini tekrar etme: tekraret \n\n')
    if tss == "tekraret":
      tkr = input('Yapay Zeka :: Neyi tekrar edeyim : ')
      print(tkr)

    if tss == "hesapla":
    	hsp = input('Yapay Zeka :: Ne işlem yapayım(Örnek : 2*5) : ')
    	print(eval(hsp))

elif x == "username" and c != "pass":
    print("Yapay Zeka :: Şifre yanlış!")

else:
    print('Yapay Zeka :: Hatalı kullanıcı adı veya şifre! Lütfen tekrar deneyiniz..')
input()
