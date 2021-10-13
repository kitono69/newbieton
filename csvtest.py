import pandas as pd

pita = pd.read_csv("data/6.csv", encoding='latin1')
#print (pita.head(5))

drop_pita = pita.drop(pita.columns[7],axis=1) #ini hapus kolom file info
#print (drop_pita.head())

sort_pita = drop_pita.sort_values(by=['Level (dBµV/m)']) #sort kolom level dari yang paling kecil
#print (sort_pita.head(20)) 

hitung_data = pita.shape[0] #hitung jumlah baris
print (hitung_data)
