# belajar continue 

# dari 1 sampai 99 yang di tampilkan hanya angka yang genap
for i in range(1, 100):
    if i % 2 == 1:
        continue
    print(i)
    
# dari 1 sampai 99 yang di tampilkan hanya angka yang ganjil
for i in range(1, 100):
    if i % 2 == 0:
        continue
    print(i)
