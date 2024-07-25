import random
import string

def main():
  try:
    lenght = int(input("Masukkan panjang password yang diinginkan: "))
    use_special_chars = input("Gunakan karakter khusus? (y/n): ").strip().lower() == 'y'

    password = generate_password(lenght, use_special_chars)
    print(f"Password yang dihasilkan: {password}")
  except ValuerError:
    pring("Panjang password harus berupa angka")

def generate_password(lenght=12, use_special_chars=True):
  chars = string.ascii_letters + string.digits
  if use_special_chars:
    chars += string.punctuation #tanda baca
  
  #generate password
  password = ''.join(random.choice(chars) for _ in range(lenght))

  return password

if __name__ == "__main__":
  main()