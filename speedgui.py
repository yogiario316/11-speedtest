import os
import platform
import speedtest
import tkinter as tk
from tkinter import messagebox, scrolledtext

def test_speed():
    st = speedtest.Speedtest()
    result_box.insert(tk.END, "Mengambil daftar server...\n")
    st.get_servers()
    result_box.insert(tk.END, "Memilih server terbaik...\n")
    best = st.get_best_server()
    result_box.insert(tk.END, f"Server terbaik dipilih: {best['host']} di {best['country']}\n")

    result_box.insert(tk.END, "Mengukur kecepatan unduh...\n")
    download_speed = st.download()
    result_box.insert(tk.END, "Mengukur kecepatan unggah...\n")
    upload_speed = st.upload()
    ping = st.results.ping

    result_box.insert(tk.END, f"Kecepatan Unduh: {download_speed / 1_000_000:.2f} Mbps\n")
    result_box.insert(tk.END, f"Kecepatan Unggah: {upload_speed / 1_000_000:.2f} Mbps\n")
    result_box.insert(tk.END, f"Ping: {ping:.2f} ms\n")

def custom_ping(domain):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = f"ping {param} 4 {domain}"
    result_box.insert(tk.END, f"Hasil ping ke {domain}:\n")
    result = os.popen(command).read()
    result_box.insert(tk.END, result + "\n")

def on_speedtest_button_click():
    result_box.delete(1.0, tk.END)
    test_speed()

def on_ping_button_click():
    domain = ping_entry.get()
    if domain:
        result_box.delete(1.0, tk.END)
        custom_ping(domain)
    else:
        messagebox.showwarning("Peringatan", "Masukkan domain atau IP!")

if __name__ == "__main__":
    app = tk.Tk()
    app.title("Speedtest Lite by Yogi Ario")
    app.geometry("600x400")

    label = tk.Label(app, text="Speedtest Lite by Yogi Ario", font=("Arial", 16))
    label.pack(pady=10)

    speedtest_button = tk.Button(app, text="Test Kecepatan Internet", command=on_speedtest_button_click)
    speedtest_button.pack(pady=5)

    ping_label = tk.Label(app, text="Ping ke domain atau IP:")
    ping_label.pack(pady=5)

    ping_entry = tk.Entry(app, width=50)
    ping_entry.pack(pady=5)

    ping_button = tk.Button(app, text="Mulai Ping", command=on_ping_button_click)
    ping_button.pack(pady=5)

    result_box = scrolledtext.ScrolledText(app, width=70, height=10, wrap=tk.WORD)
    result_box.pack(pady=10)

    app.mainloop()
