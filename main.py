import os
from calculator import Calculator

def clear_screen():
    # Fungsi untuk membersihkan layar terminal
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    calc = Calculator()
    while True:
        clear_screen()
        print("Code By Fajar Reiva Cahya\nGithub : fajar-reiva-cahya\nInstagram : fjrrivchy")
        print("\nKalkulator Sederhana Menggunakan Python\n")
        print("1. Tambah")
        print("2. Kurang")
        print("3. Kali")
        print("4. Bagi")
        print("5. Keluar\n")
        choice = input("Pilih operasi : ")

        if choice in ['1', '2', '3', '4']:
            num1 = float(input("\nMasukkan angka pertama: "))
            num2 = float(input("Masukkan angka kedua: "))

            if choice == '1':
                result = calc.add(num1, num2)
                print(f"Hasil: {num1} + {num2} = {result}")
            elif choice == '2':
                result = calc.subtract(num1, num2)
                print(f"Hasil: {num1} - {num2} = {result}")
            elif choice == '3':
                result = calc.multiply(num1, num2)
                print(f"Hasil: {num1} * {num2} = {result}")
            elif choice == '4':
                result = calc.divide(num1, num2)
                print(f"Hasil: {num1} / {num2} = {result}")

            # Tanya pengguna apakah ingin mengulang atau tidak
            while True:
                repeat = input("\nApakah Anda ingin mengulang operasi lain? (ya/tidak): ").lower()
                if repeat in ['ya','y','yes']:
                    break
                elif repeat in ['tidak','n','no']:
                    return
                else:
                    print("Input tidak valid. Harap jawab dengan 'ya' atau 'tidak'.")

        elif choice == '5':
            break
        else:
            print("Opsi tidak valid. Coba lagi.")

if __name__ == "__main__":
    main()