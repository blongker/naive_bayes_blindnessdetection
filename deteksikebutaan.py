import numpy as np
import pandas 
import os

data_t = pandas.read_csv(r'C:\Users\Whiteseries\Downloads\naivebayes\Blindness.csv')
data = pandas.DataFrame(data_t)

judul=('=======Deteksi Kebutaan=======')
kel=('=======Kelompok Naive Bayes=======')

print(judul.center(70))
print(kel.center(70))
print('================================================================')
print('================================================================')
print(data)
print('\n')


#umur 1 2 3 4
u1Y = 5/14
u1T = 4/19
u2Y = 1/14
u2T = 3/19
u3Y = 5/14
u3T = 5/19
u4Y = 3/14
u4T = 7/19

#diabetes Ya Tidak
dYY = 8/14
dYT = 10/19
dTY = 6/14
dTT = 9/19

#hipertensi Ya Tidak
hYY = 8/14
hYT = 7/19
hTY = 6/14
hTT = 12/19

#intraokular 1 2 3 4 
i1Y = 0/14
i1T = 0/19
i2Y = 7/14
i2T = 12/19
i3Y = 5/14
i3T = 7/19
i4Y = 2/14
i4T = 0/19

'''
#menampilkan kategori umur
w = input('Masukan Kategori Umur (UmurA, UmurB, UmurC, UmurD): ')

if w == 'UmurA': 
    print(data[(data['Umur'] >=35) & (data['Umur'] <45) & (data['Kebutaan'] == 'Ya')])
    print('====================================================')
    print(data[(data['Umur'] >=35) & (data['Umur'] <45) & (data['Kebutaan'] == 'Tidak')])
elif w == 'UmurB':
    print(data[(data['Umur'] >=45) & (data['Umur'] <55) & (data['Kebutaan'] == 'Ya')])
    print('====================================================')
    print(data[(data['Umur'] >=45) & (data['Umur'] <55) & (data['Kebutaan'] == 'Tidak')])
elif w == 'UmurC':
    print(data[(data['Umur'] >=55) & (data['Umur'] <65) & (data['Kebutaan'] == 'Ya')])
    print('====================================================')
    print(data[(data['Umur'] >=55) & (data['Umur'] <65) & (data['Kebutaan'] == 'Tidak')])
elif w == 'UmurD':
    print(data[(data['Umur'] >=65) & (data['Umur'] <=75) & (data['Kebutaan'] == 'Ya')])
    print('====================================================')
    print(data[(data['Umur'] >=65) & (data['Umur'] <=75) & (data['Kebutaan'] == 'Tidak')])
else:
    print('Tidak Ditemukan')

#menampilkan kategori diabetes
x = input('Kategori Diabetes (D1,D2) = ')

if x == 'D1':
    print(data[(data['Diabetes']=='Ya') & (data['Kebutaan']=='Ya')])
    print('====================================================')
    print(data[(data['Diabetes']=='Ya') & (data['Kebutaan']=='Tidak')])
elif x == 'D2':
    print(data[(data['Diabetes']=='Tidak') & (data['Kebutaan']=='Ya')])
    print('====================================================')
    print(data[(data['Diabetes']=='Tidak') & (data['Kebutaan']=='Tidak')])
else:
    print('Tidak Ditemukan')

#menampilkan kategori hipertensi
y = input('Kategori Hipertensi (H1,H2) = ')

if y == 'H1':
    print(data[(data['Hipertensi']=='Ya') & (data['Kebutaan']=='Ya')])
    print('====================================================')
    print(data[(data['Hipertensi']=='Ya') & (data['Kebutaan']=='Tidak')])
elif y == 'H2':
    print(data[(data['Hipertensi']=='Tidak') & (data['Kebutaan']=='Ya')])
    print('====================================================')
    print(data[(data['Hipertensi']=='Tidak') & (data['Kebutaan']=='Tidak')])
else:
    print('Tidak Ditemukan')

#menampilkan kategori intraokular
z = input('Kategori Intraokular (I1,I2,I3,I4) = ')

if z == 'I1':
    print(data[(data['Intraokular'] <21) & (data['Kebutaan'] == 'Ya')   ])
    print('====================================================')
    print(data[(data['Intraokular'] <21) & (data['Kebutaan'] == 'Tidak')   ])
elif z == 'I2':
    print(data[(data['Intraokular'] >=21) & (data['Intraokular'] <41) & (data['Kebutaan'] == 'Ya')   ])
    print('====================================================')
    print(data[(data['Intraokular'] >=21) & (data['Intraokular'] <41) & (data['Kebutaan'] == 'Tidak')   ])
elif z == 'I3':
    print(data[(data['Intraokular'] >=41) & (data['Intraokular'] <61) & (data['Kebutaan'] == 'Ya')   ])
    print('====================================================')
    print(data[(data['Intraokular'] >=41) & (data['Intraokular'] <61) & (data['Kebutaan'] == 'Tidak')   ])
elif z == 'I4':
    print(data[(data['Intraokular'] >=61) & (data['Kebutaan'] == 'Ya')   ])
    print('====================================================')
    print(data[(data['Intraokular'] >=61) & (data['Kebutaan'] == 'Tidak')   ])
else:
    print('Tidak Ditemukan')
'''



#Langkah 2
print('=====Data Uji=====')
print('==================')
print('Memasukan Data Uji')
nama=input('Nama : ')
iu=eval(input('Masukan Umur : '))
idiabetes=input('Masukan Status Diabetes : ')
ihipertensi=input('Masukan Status Hipertensi : ')
iintraokular=eval(input('Masukan Intraokular : '))
print('=======================================================\n')

#Langkah 1
#menghitung jumlah class/label
print('Langkah 1')
print('Mencari Jumlah Class / Label')
print('============================')
jml_class=data.groupby('Kebutaan').size()
print(round(jml_class, 3))
print('\n')
print('Menghitung Nilai Class')
print('============================')
jml_classYA = 14/33
jml_classTIDAK = 19/33
print('(P Kebutaan = Ya) = 14/33 =',(round(jml_classYA,3)))
print('(P Kebutaan = Tidak) = 19/33 =',(round(jml_classTIDAK,3)))
print('\n')

print('Langkah 2')
print('Hitung Probabilitas Bersyarat Untuk Setiap Kelas P(B|Ai)')
print('=======================================================')
#umur A B C D
if iu >= 35 and iu < 45 :
    print('P Umur = '+str(iu)+ '| Kebutaan = Ya = ',(round(u1Y,3)))
    print('P Umur = '+str(iu)+ '| Kebutaan = Tidak = ',(round(u1T,3)))
elif iu >= 45 and iu < 55 :
    print('P Umur = '+str(iu)+ '| Kebutaan = Ya = ',(round(u2Y,3)))
    print('P Umur = '+str(iu)+ '| Kebutaan = Tidak = ',(round(u2T,3)))
elif iu >= 55 and iu < 65 :
    print('P Umur = '+str(iu)+ '| Kebutaan = Ya = ',(round(u3Y,3)))
    print('P Umur = '+str(iu)+ '| Kebutaan = Tidak = ',(round(u3T,3)))
elif iu >= 65 and iu <=75 :
    print('P Umur = '+str(iu)+ '| Kebutaan = Ya = ',(round(u4Y,3)))
    print('P Umur = '+str(iu)+ '| Kebutaan = Tidak = ',(round(u4T,3)))

#diabetes ya dan tidak
if idiabetes == 'Ya' :
    print('P Diabetes '+idiabetes+' | Kebutaan = (Ya) = ',(round(dYY, 3)))
    print('P Diabetes '+idiabetes+' | Kebutaan = (Tidak) = ',(round(dYT, 3)))
elif idiabetes == 'Tidak' :
    print('P Diabetes '+idiabetes+' | Kebutaan = (Ya) = ',(round(dTY, 3)))
    print('P Diabetes '+idiabetes+' | Kebutaan = (Tidak) = ',(round(dTT, 3)))

#hipertensi ya dan tidak
if ihipertensi == 'Ya' :
    print('P Hipertensi '+ihipertensi+' | Kebutaan = (Ya) = ',(round(hYY, 3)))
    print('P Hipertensi '+ihipertensi+' | Kebutaan = (Tidak) = ',(round(hYT, 3)))
elif ihipertensi == 'Tidak' :
    print('P Hipertensi '+ihipertensi+' | Kebutaan = (Ya) = ',(round(hTY, 3)))
    print('P Hipertensi '+ihipertensi+' | Kebutaan = (Tidak) = ',(round(hTT, 3)))

#intraokular 1 2 3 4
if iintraokular < 21 :
    print('Intraokular = '+str(iintraokular)+'| Kebutaan = (Ya) = ',(round(i1Y,3)))
    print('Intraokular = '+str(iintraokular)+'| Kebutaan = (Tidak)=',(round(i1T,3)))
elif iintraokular >=21 and iintraokular <41 :
    print('Intraokular = '+str(iintraokular)+'| Kebutaan = (Ya) = ',(round(i2Y,3)))
    print('Intraokular = '+str(iintraokular)+'| Kebutaan = (Tidak)=',(round(i2T,3)))
elif iintraokular >=41 and iintraokular <61 :
    print('Intraokular = '+str(iintraokular)+'| Kebutaan = (Ya) = ',(round(i3Y,3)))
    print('Intraokular = '+str(iintraokular)+'| Kebutaan = (Tidak)=',(round(i3T,3)))
elif iintraokular >=61 :
    print('Intraokular = '+str(iintraokular)+'| Kebutaan = (Ya) = ',(round(i4Y,3)))
    print('Intraokular = '+str(iintraokular)+'| Kebutaan = (Tidak)=',(round(i4T,3)))

print('=======================================================\n')

#Langkah 3
#P(X|Kebutaan = Ya)
print('Langkah 3')
print('===Mencari P(X|Kebutaan = Ya )===')
print('=================================')
#Kategori umur dan Kebutaan Ya
if iu >= 35 and iu < 45 :
    print('P Umur = '+str(iu)+ '| Kebutaan = Ya = ',(round(u1Y,3)))
    uky = (round(u1Y,3))
elif iu >= 45 and iu < 55 :
    print('P Umur = '+str(iu)+ '| Kebutaan = Ya = ',(round(u2Y,3)))
    uky = (round(u2Y,3))
elif iu >= 55 and iu < 65 :
    print('P Umur = '+str(iu)+ '| Kebutaan = Ya = ',(round(u3Y,3)))
    uky = (round(u3Y,3))
elif iu >= 65 and iu <=75 :
    print('P Umur = '+str(iu)+ '| Kebutaan = Ya = ',(round(u4Y,3)))
    uky = (round(u4Y,3))

#Kategori diabetes ya dan kebutaan ya
if idiabetes == 'Ya' :
    print('P Diabetes '+idiabetes+' | Kebutaan = (Ya) = ',(round(dYY, 3)))
    dky = (round(dYY,3))
elif idiabetes == 'Tidak' :
    print('P Diabetes '+idiabetes+' | Kebutaan = (Ya) = ',(round(dTY, 3)))
    dky = (round(dTY,3))

#Kategori hipertensi ya dan Kebutaan ya
if ihipertensi == 'Ya' :
    print('P Hipertensi '+ihipertensi+' | Kebutaan = (Ya) = ',(round(hYY, 3)))
    hky = (round(hYY,3))
elif ihipertensi == 'Tidak' :
    print('P Hipertensi '+ihipertensi+' | Kebutaan = (Ya) = ',(round(hTY, 3)))
    hky = (round(hTY,3))

#intraokular 1 2 3 4
if iintraokular < 21 :
    print('Intraokular = '+str(iintraokular)+'| Kebutaan = (Ya) = ',(round(i1Y,3)))
    iky = (round(i1Y,3))
elif iintraokular >=21 and iintraokular <41 :
    print('Intraokular = '+str(iintraokular)+'| Kebutaan = (Ya) = ',(round(i2Y,3)))
    iky = (round(i2Y,3))
elif iintraokular >=41 and iintraokular <61 :
    print('Intraokular = '+str(iintraokular)+'| Kebutaan = (Ya) = ',(round(i3Y,3)))
    iky = (round(i3Y,3))
elif iintraokular >=61 :
    print('Intraokular = '+str(iintraokular)+'| Kebutaan = (Ya) = ',(round(i4Y,3)))
    iky = (round(i4Y,3))

hasilPYA=float(uky*dky*hky*iky)
print('=======================================================')
print('P(X|Kebutaan = Ya ) = '+str(uky)+'*'+str(dky)+'*'+str(hky)+'*'+str(iky)+' = ',(round(hasilPYA,3)))
print('=======================================================\n')

#P(X|Kebutaan = Tidak)
print('===Mencari P(X|Kebutaan = Tidak )===')
print('=================================')

#Umur kebutaan tidak
if iu >= 35 and iu < 45 :
    print('P Umur = '+str(iu)+ '| Kebutaan = Tidak = ',(round(u1T,3)))
    ukt = (round(u1T,3))
elif iu >= 45 and iu < 55 :
    print('P Umur = '+str(iu)+ '| Kebutaan = Tidak = ',(round(u2T,3)))
    ukt = (round(u2T,3))
elif iu >= 55 and iu < 65 :
    print('P Umur = '+str(iu)+ '| Kebutaan = Tidak = ',(round(u3T,3)))
    ukt = (round(u3T,3))
elif iu >= 65 and iu <=75 :
    print('P Umur = '+str(iu)+ '| Kebutaan = Tidak = ',(round(u4T,3)))
    ukt = (round(u4T,3))

#diabetes kebutaan tidak
if idiabetes == 'Ya' :
    print('P Diabetes '+idiabetes+' | Kebutaan = (Tidak) = ',(round(dYT, 3)))
    dkt = (round(dYT,3))
elif idiabetes == 'Tidak' :
    print('P Diabetes '+idiabetes+' | Kebutaan = (Tidak) = ',(round(dTT, 3)))
    dkt = (round(dTT,3))

#hipertensi kebutaan tidak
if ihipertensi == 'Ya' :
    print('P Hipertensi '+ihipertensi+' | Kebutaan = (Tidak) = ',(round(hYT, 3)))
    hkt = (round(hYT,3))
elif ihipertensi == 'Tidak' :
    print('P Hipertensi '+ihipertensi+' | Kebutaan = (Tidak) = ',(round(hTT, 3)))
    hkt = (round(hTT,3))

#intraokular kebutaan tidak
if iintraokular < 21 :
    print('Intraokular = '+str(iintraokular)+'| Kebutaan = (Tidak)=',(round(i1T,3)))
    ikt = (round(i1T,3)) 
elif iintraokular >=21 and iintraokular <41 :
    print('Intraokular = '+str(iintraokular)+'| Kebutaan = (Tidak)=',(round(i2T,3)))
    ikt = (round(i2T,3)) 
elif iintraokular >=41 and iintraokular <61 :
    print('Intraokular = '+str(iintraokular)+'| Kebutaan = (Tidak)=',(round(i3T,3)))
    ikt = (round(i3T,3)) 
elif iintraokular >=61 :
    print('Intraokular = '+str(iintraokular)+'| Kebutaan = (Tidak)=',(round(i4T,3)))
    ikt = (round(i4T,3)) 
    
hasilPTIDAK = float(ukt*dkt*hkt*ikt)
print('+======================================================+')
print('P(X|Kebutaan = Tidak ) = '+str(ukt)+'*'+str(dkt)+'*'+str(hkt)+'*'+str(ikt)+' = ',(round(hasilPTIDAK,3)))
print('========================================================\n')

#Langkah 4
#menentukan probabilitas posterior
print('Langkah 4')
print('===Menentukan Probabilitas Posterior===')
print('=======================================')
posteriorY = ((hasilPYA) * (jml_classYA))
posteriorT = ((hasilPTIDAK) * (jml_classTIDAK))
print('P(X|Kebutaan = Ya = '+str(round(hasilPYA,3))+') * P(Kebutaan = Ya = '+str(round(jml_classYA,3))+') = ',(round(posteriorY,3)))
print('P(X|Kebutaan = Tidak = '+str(round(hasilPTIDAK,3))+') * P(Kebutaan = Tidak = '+str(round(jml_classTIDAK,3))+') = ',(round(posteriorT,3)))
print('===Menentukan Nilai Maksimum===')
print('=======================================')
arr = np.array([posteriorY,posteriorT])
print('argmax P(A|B) = {'+str(round(posteriorY,3))+','+str(round(posteriorT,3))+'}')
print('Nilai Maksimum ', np.argmax(arr))
print('\n')
print('Conclusion')
if posteriorY > posteriorT :
    print('Jadi Pasien Bernama '+nama+' Memiliki Kemungkinan Resiko Kebutaan')
else: 
    print('Jadi Pasien Bernama '+nama+' Tidak Memiliki Resiko Kebutaan')
