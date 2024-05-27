Critical Path Method Calculator
---------------------------------
Critical Path Method (CPM) adalah sebuah algoritma untuk menjadwalkan serangkaian aktivitas dalam proyek. Jalur kritis ditentukan dengan mengidentifikasi rangkaian terpanjang dari aktivitas-aktivitas yang saling bergantung dan mengukur waktu yang dibutuhkan untuk menyelesaikannya dari awal hingga akhir. Sistem dibangun dengan data proyek implementasi ERP pada PT Perkebunan Nusantara tahun 2016.

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

![WhatsApp Image 2024-05-25 at 11 10 08](https://github.com/MuhammadRizki8/Critical-Path-Method-Calculator/assets/100481579/f023adf9-96ff-47d9-9b72-3045989c4d7f)
![WhatsApp Image 2024-05-25 at 11 01 26](https://github.com/MuhammadRizki8/Critical-Path-Method-Calculator/assets/100481579/e1619b13-bbd9-4ea8-a2d6-0bcc09bb6374)

