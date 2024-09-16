PACK_SAUSAGES=10
PACK_BUNS=8
Participants=int(input('Введите количество участников пикника: '))
Hot_Dog_Participants=int(input('Введите количество хот-догов на учатника: '))
Nuber_Hot_Dog=Participants*Hot_Dog_Participants
#Nuber_PACK_SAUSAGES=Nuber_Hot_Dog / PACK_SAUSAGES
#Nuber_PACK_BUNS=Nuber_Hot_Dog / PACK_BUNS
print ('Количество хот-догов: ', Nuber_Hot_Dog)
if Nuber_Hot_Dog % PACK_SAUSAGES != 0:
    print ('Количество пачек сосисок',(Nuber_Hot_Dog // PACK_SAUSAGES)+1)
    print ('Количество оставшихся сосисок:', (((Nuber_Hot_Dog // PACK_SAUSAGES)+1)*10)-Nuber_Hot_Dog)
else:
   print ('Количество пачек сосисок:', Nuber_Hot_Dog // PACK_SAUSAGES)
   print ('Количество оставшихся сосисок:', ((Nuber_Hot_Dog // PACK_SAUSAGES)*10)-Nuber_Hot_Dog)

if Nuber_Hot_Dog % PACK_BUNS != 0:
   print ('Количество пачек булочек',(Nuber_Hot_Dog // PACK_BUNS)+1)
   print ('Количество оставшихся булочек',(((Nuber_Hot_Dog // PACK_BUNS)+1)*8-Nuber_Hot_Dog))
else:
   print ('Количество пачек булочек: ', (Nuber_Hot_Dog // PACK_BUNS))
   print ('Количество оставшихся булочек',((Nuber_Hot_Dog // PACK_BUNS)*8)-Nuber_Hot_Dog)
