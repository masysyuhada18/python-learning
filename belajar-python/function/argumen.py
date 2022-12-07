''' fungsi dengan argumen (input)'''


 
def hello_world(nama):
     '''fungsi hello world menerima input dengan variabel'''
     print(f"Selamat datang dunia wahai {nama}")
    
hello_world("ucup") 
hello_world("adit")

# program tambah 

def tambah(angka1, angka2):
    '''fungsi tambah'''
    hasil = angka1 + angka2
    print(f"{angka1} + {angka2} = {hasil}") 
    
tambah(100000, 200000) 
# fungsi dengan nilai input list

def say_hi(list_peserta):
    '''fungsi say hi'''
    data_peserta = list_peserta.copy()
    for peserta in data_peserta:           
        print(f"Yang terhormat {peserta}")
        
anggota_boyband = ["Ucup", "Otong", "Dudung"]

say_hi(anggota_boyband) # anggota_boyband dan list peserta adalah sama 
