import re
import os
import math 

# memuat daftar password
def load_common_passwords():
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, "most_common_pw_sample.txt")

    with open(file_path, "r") as file:
        return set(file.read().splitlines())  
    
# kalkulasi entropy password
def calculate_entropy(password):
    charset = 0

    if re.search(r"[a-z]", password):
        charset += 26
    if re.search(r"[A-Z]", password):
        charset += 26
    if re.search(r"[0-9]", password):
        charset += 10
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        charset += 32

    if charset == 0:
        return 0

    entropy = len(password) * math.log2(charset) #rumus entropy yang digunakan = panjang password * log2(jumlah karakter unik dalam password)
    return entropy

# fungsi pendeteksi pola umum dalam password
def dictionary_match(password, common_passwords):
    password_lower = password.lower()
    for word in common_passwords:
        if word in password_lower:
            return True
    return False

def has_sequence(password): # password dengan pola umum
    sequences = ["123", "abc", "qwerty", "password", "admin", "test"]
    return any(seq in password.lower() for seq in sequences)

def has_repetition(password): # password dengan karakter berulang
    return any(password.count(c) > len(password)//2 for c in password)

# analsis kekuatan password dan feedback
def analyze_password(password, common_passwords):
    issues = []

    if len(password) < 8:
        issues.append("Password terlalu pendek (minimum 8 karakter)")

    if not re.search(r"[A-Z]", password):
        issues.append("Password tidak mengandung huruf kapital")

    if not re.search(r"[a-z]", password):
        issues.append("Password tidak mengandung huruf kecil")

    if not re.search(r"[0-9]", password):
        issues.append("Password tidak mengandung angka")

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        issues.append("Password tidak mengandung karakter khusus")

    if dictionary_match(password, common_passwords):
        issues.append("Password mengandung kata-kata yang terlalu umum")

    if has_sequence(password):
        issues.append("Password mengandung urutan yang dapat terlalu diprediksi")

    if has_repetition(password):
        issues.append("Password mengandung karakter berulang terlalu banyak")

    return issues

# skor akhir
def evaluate_password(password, common_passwords):
    entropy = calculate_entropy(password)
    issues = analyze_password(password, common_passwords)

    # rating entropy
    if entropy < 28:
        rating = "sangat lemah"
    elif entropy < 36:
        rating = "lemah"
    elif entropy < 60:
        rating = "sedang"
    else:
        rating = "kuat"

     # Penaalti apabila password memiliki banyak masalah
    if len(issues) >= 3:
        rating = "Weak"

    return rating, entropy, issues
    
common_passwords = load_common_passwords() # memuat daftar password ke dalam variabel

pwd = input("Masukkan password: ") # cek password sederhana
rating, entropy, issues = evaluate_password(pwd, common_passwords)
print("\n====== Hasil Akhir ======")
print("Rating:", rating)
print(f"Entropy: {entropy:.2f} bits") # hasil akhir
if issues:
    print("\nMasalah yang ditemukan:")
    for issue in issues:
        print("-", issue)
else:
    print("\nPassword sudah bagus") #tambahan feedback untuk pengguna