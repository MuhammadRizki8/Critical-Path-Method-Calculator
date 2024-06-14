Critical Path Method Calculator
---------------------------------
Critical Path Method (CPM) adalah sebuah algoritma untuk menjadwalkan serangkaian aktivitas dalam proyek. Jalur kritis ditentukan dengan mengidentifikasi rangkaian terpanjang dari aktivitas-aktivitas yang saling bergantung dan mengukur waktu yang dibutuhkan untuk menyelesaikannya dari awal hingga akhir. Sistem dibangun dengan data proyek implementasi ERP pada PT Perkebunan Nusantara tahun 2016.

Preview
--------------------------------
![image](https://github.com/MuhammadRizki8/Critical-Path-Method-Calculator/assets/100481579/4d3d2764-a125-4a25-9db9-ef7457463606)
![image](https://github.com/MuhammadRizki8/Critical-Path-Method-Calculator/assets/100481579/859dbbed-7eed-4f7d-9356-96c30b6bdafd)

Refensi & Sumber Data
--------------------
> Purwadi, A. T. (2016). Pembuatan Work Breakdown Structure Dictionary Untuk Program Implementasi ERP SAP DI PT Perkebunan Nusantara XI. Institut Teknologi Sepuluh Nopember.

Kegunaan
----------------------
- Aktivitas apa pun di jalur kritis, jika tertunda, dapat menunda proyek
- Jalur kritis juga memberikan waktu sesingkat mungkin untuk menyelesaikan proyek
- "Jalur kritis" adalah jalur terpanjang dalam jaringan dengan hanya nol aktivitas mengambang

Fitur
------------------------------
Menerapkan program Python untuk:
- membaca file dengan tabel yang berisi tugas, durasi, dan ketergantungan
- membangun Activity-on-Node (AON) dengan ES, EF, LS dan LF untuk setiap tugas
- menentukan untuk setiap tugas, apakah tugas tersebut berada di jalur kritis
- menampilkan hasil dalam bentuk tabel
- menampilkan hasil dalam bentuk visualisasi.

Cara Penggunaan
------------------------------
- Clone kode github
  > git clone https://github.com/MuhammadRizki8/Critical-Path-Method-Calculator.git
  
  > cd Critical-Path-Method-Calculator
- Setup virtual  env
  > python -m venv venv
  
  > venv\Scripts\activate
- Install library
  > pip install -r requirements.txt
- Jalankan program
  > python main.py

Semoga membantu...




