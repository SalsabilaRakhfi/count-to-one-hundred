name = input("Enter your name: ")
age = input("Enter your age: ")

# ubah age ke tipe angka
age = int(age)

# hitung berapa tahun lagi menuju umur 100 (walau ga mau si)
years_to_100 = 100 - age

print(f"{name} will be 100 years old in {years_to_100} years")
