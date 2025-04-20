name = input("Enter your name: ")
age = int(input("Enter your age: "))

year_to_100 = 100 - age

# hitung berapa tahun lagi menuju umur 100 (walau ga mau si)
years_to_100 = 100 - age

current_year = 2025 
year_when_100 = current_year + year_to_100

print(f"{name} will be 100 years old in {year_when_100}")
