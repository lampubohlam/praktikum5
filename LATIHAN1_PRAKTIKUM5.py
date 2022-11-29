print('NAMA :Abdul aziz')
print('NIM : 312210022')
print(50*'=')
kontak={'Ari':'081278888','Dina':'087677776'}

print('|Ari                      : ',kontak['Ari'],'\n')

kontak['|Riko']='087654544'
print('Menambah kontak Riko     : ',kontak,'\n')

kontak['|Dina']='0889997890'
print('Mengubah kontak Dina     : ',kontak,'\n')

print('Menampilkan semua Nama   :',kontak.keys(),'\n')
print('Menampilkan semua Nomor  :',kontak.values(),'\n')

print('Semua Kontak             :',kontak,'\n')

del kontak['Dina']
print('Menghapus kontak Dina    :',kontak'\n')