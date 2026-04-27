import re 

def load_common_passwords(): # fungsi untuk memuat daftar password dari file teks
    with open("PW_Checker/most_common_pw_sample.txt", "r") as file:
        passwords = file.read().splitlines()
    return passwords

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
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"
    
common_passwords = load_common_passwords() # memuat daftar password ke dalam variabel

pwd = input("Enter password: ") # cek password sederhana
result = check_password(pwd, common_passwords) # hasil
print("Strength:", result)