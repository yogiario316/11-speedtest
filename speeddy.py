import os
import sys
import ctypes
import platform
import speedtest

nama = "Speedtest Lite by Yogi Ario"
print(nama)
print("\n")

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin():
    if not is_admin():
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        sys.exit()

def test_speed():
    st = speedtest.Speedtest()
    print("Mengambil daftar server...")
    st.get_servers()
    print("Memilih server terbaik...")
    best = st.get_best_server()
    print(f"Server terbaik dipilih: {best['host']} di {best['country']}")

    print("Mengukur kecepatan unduh...")
    download_speed = st.download()
    print("Mengukur kecepatan unggah...")
    upload_speed = st.upload()
    ping = st.results.ping

    print(f"Kecepatan Unduh: {download_speed / 1_000_000:.2f} Mbps")
    print(f"Kecepatan Unggah: {upload_speed / 1_000_000:.2f} Mbps")
    print(f"Ping: {ping:.2f} ms")

def custom_ping(domain):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = f"ping {param} 4 {domain}"
    os.system(command)

def main():
    while True:
        print("Pilih opsi:")
        print("1. Test kecepatan internet")
        print("2. Ping ke domain atau IP tertentu")
        print("Tekan Enter untuk keluar.")
        choice = input("Pilihan Anda: ")

        if choice == '1':
            test_speed()
        elif choice == '2':
            domain = input("Masukkan domain atau IP: ")
            custom_ping(domain)
        else:
            break

        print("\nTerima kasih telah menggunakan program ini.")
        print("Tekan 1 untuk mengulang atau tekan Enter untuk keluar.")
        choice = input("Pilihan Anda: ")
        if choice != '1':
            break

if __name__ == "__main__":
    if platform.system().lower() == "windows":
        run_as_admin()
    main()
