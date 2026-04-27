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

    entropy = len(password) * math.log2(charset)
    return entropy

def check_password(password, common_passwords): # fungsi yang memriksa kekuatan password
    score = 0

    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[!@#$%^&*]", password):
        score += 1

    if score <= 2:
        return "lemah"
    elif score <= 4:
        return "sedang"
    else:
        return "kuat"

# skor akhir
def evaluate_password(password, common_passwords):
    entropy = calculate_entropy(password)

    # rating entropy
    if entropy < 28:
        rating = "sangat lemah"
    elif entropy < 36:
        rating = "lemah"
    elif entropy < 60:
        rating = "sedang"
    else:
        rating = "kuat"

    return rating, entropy
    
common_passwords = load_common_passwords() # memuat daftar password ke dalam variabel

pwd = input("Masukkan password: ") # cek password sederhana
rating, entropy = evaluate_password(pwd, common_passwords)
print("\n====== Hasil Akhir ======")
print("Rating:", rating)
print(f"Entropy: {entropy:.2f} bits\n") # hasil akhir