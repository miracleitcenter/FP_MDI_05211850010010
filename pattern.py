import pandas.io.sql as pdo
import pyodbc
import matplotlib.pyplot as plt
import pandas as pd

#FUNCTION JUMLAH MAHASISWA NON-AKTIF
def n_nonactive_mhs(conn):
    cursor = conn.cursor()
    sql = cursor.execute("SELECT COUNT(DISTINCT lg.Nama) AS nonactive FROM dbo.MHS m JOIN dbo.Login lg on m.Mahasiswa=lg.users WHERE lg.days > 30")
    get_data = sql.fetchone()
    jml = get_data.nonactive
    return jml

#FUNCTION JUMLAH MAHASISWA AKTIF
def n_active_mhs(conn):
    cursor = conn.cursor()
    sql = cursor.execute("SELECT COUNT(DISTINCT lg.Nama) AS active FROM dbo.MHS m JOIN dbo.Login lg on m.Mahasiswa=lg.users WHERE lg.days <= 30")
    get_data = sql.fetchone()
    jml = get_data.active
    return jml

#FUNCTION JUMLAH DOSEEN NON-AKTIF
def n_nonactive_dsn(conn):
    cursor = conn.cursor()
    sql = cursor.execute("SELECT COUNT(DISTINCT lg.Nama) AS nonactive FROM dbo.Dosen m JOIN dbo.Login lg on m.Dosen=lg.users WHERE lg.days > 30")
    get_data = sql.fetchone()
    jml = get_data.nonactive
    return jml

#FUNCTION JUMLAH DOSEEN AKTIF
def n_active_dsn(conn):
    cursor = conn.cursor()
    sql = cursor.execute("SELECT COUNT(DISTINCT lg.Nama) AS active FROM dbo.Dosen m JOIN dbo.Login lg on m.Dosen=lg.users WHERE lg.days <= 30")
    get_data = sql.fetchone()
    jml = get_data.active
    return jml

def night_dsn(conn):
    cursor = conn.cursor()
    sql = cursor.execute("SELECT SUM(jml_akses) AS jml_akses FROM dbo.jam_dsn WHERE ket_jam='NIGHT'")
    get_data = sql.fetchone()
    jml = get_data.jml_akses
    return jml

def earlydays_dsn(conn):
    cursor = conn.cursor()
    sql = cursor.execute("SELECT SUM(jml_akses) AS jml_akses FROM dbo.jam_dsn WHERE ket_jam='EARLY DAYS'")
    get_data = sql.fetchone()
    jml = get_data.jml_akses
    return jml

def workinghours_dsn(conn):
    cursor = conn.cursor()
    sql = cursor.execute("SELECT SUM(jml_akses) AS jml_akses FROM dbo.jam_dsn WHERE ket_jam='WORKING HOURS'")
    get_data = sql.fetchone()
    jml = get_data.jml_akses
    return jml

def latenight_dsn(conn):
    cursor = conn.cursor()
    sql = cursor.execute("SELECT SUM(jml_akses) AS jml_akses FROM dbo.jam_dsn WHERE ket_jam='LATE NIGHT'")
    get_data = sql.fetchone()
    jml = get_data.jml_akses
    return jml

def night_mhs(conn):
    cursor = conn.cursor()
    sql = cursor.execute("SELECT SUM(jml_akses) AS jml_akses FROM dbo.jam_mhs WHERE ket_jam='NIGHT'")
    get_data = sql.fetchone()
    jml = get_data.jml_akses
    return jml

def earlydays_mhs(conn):
    cursor = conn.cursor()
    sql = cursor.execute("SELECT SUM(jml_akses) AS jml_akses FROM dbo.jam_mhs WHERE ket_jam='EARLY DAYS'")
    get_data = sql.fetchone()
    jml = get_data.jml_akses
    return jml

def workinghours_mhs(conn):
    cursor = conn.cursor()
    sql = cursor.execute("SELECT SUM(jml_akses) AS jml_akses FROM dbo.jam_mhs WHERE ket_jam='WORKING HOURS'")
    get_data = sql.fetchone()
    jml = get_data.jml_akses
    return jml

def latenight_mhs(conn):
    cursor = conn.cursor()
    sql = cursor.execute("SELECT SUM(jml_akses) AS jml_akses FROM dbo.jam_mhs WHERE ket_jam='LATE NIGHT'")
    get_data = sql.fetchone()
    jml = get_data.jml_akses
    return jml

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
========================================================================= GRAFIK= ========================================================================
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#FIGURE MAHASISIWA AKTIF DAN NON-AKTIF
def aktif_mhs():
    plt.figure(1)
    ket = ['Aktif', 'Non-Aktif']
    aktif = int(n_active_mhs(conn))
    non_aktif = int(n_nonactive_mhs(conn))
    jumlah = [aktif, non_aktif]

    print("Aktif = " + str(aktif))
    print("Non-Aktif = " + str(non_aktif))

    plt.bar(ket, jumlah)
    plt.xlabel('Keterangan', fontsize=8)
    plt.ylabel('Jumlah Mahasiswa', fontsize=8)
    plt.title("Jumlah Mahasiswa Aktif dan Non-Aktif (Tidak login selama 30 hari)")

    plt.show()

#FIGURE DOSEN AKTIF DAN NON-AKTIF
def aktif_dsn():
    plt.figure(1)
    ket = ['Aktif', 'Non-Aktif']
    aktif = int(n_active_dsn(conn))
    non_aktif = int(n_nonactive_dsn(conn))
    jumlah = [aktif, non_aktif]

    print("Aktif = " + str(aktif))
    print("Non-Aktif = " + str(non_aktif))

    plt.bar(ket, jumlah)
    plt.xlabel('Keterangan', fontsize=8)
    plt.ylabel('Jumlah Mahasiswa', fontsize=8)
    plt.title("Jumlah Dosen Aktif dan Non-Aktif (Tidak login selama 30 hari)")

    plt.show()

#FIGURE FREKUENSI AKSES DAYS PERMINGGU DOSEN
def day_week_dsn():
    sql = "SELECT d.Last_access AS day, COUNT(*) AS jml_akses FROM dbo.Dosen d JOIN dbo.Login lg on d.Dosen = lg.users GROUP BY d.Last_access HAVING (COUNT(d.Last_access) > 1) ORDER BY jml_akses DESC"
    dfo = pdo.read_sql(sql, conn)
    df = pd.DataFrame(dfo)
    print(df)
    x = df['day']
    y = df['jml_akses']
    plt.bar(x,y)
    plt.xlabel('Hari', fontsize=8)
    plt.ylabel('Jumlah Akses', fontsize=8)
    plt.title("Jumlah Frekuensi Akses Dosen pada ShareITS per-Minggu")
    plt.show()

#FIGURE FREKUENSI AKSES DAYS PERMINGGU MAHASISWA
def day_week_mhs():
    sql = "SELECT m.Last_access AS day, COUNT(*) AS jml_akses FROM dbo.MHS m JOIN dbo.Login lg on m.Mahasiswa = lg.users GROUP BY m.Last_access HAVING (COUNT(m.Last_access) > 1) ORDER BY jml_akses DESC"
    dfo = pdo.read_sql(sql, conn)
    df = pd.DataFrame(dfo)
    print(df)
    x = df['day']
    y = df['jml_akses']
    plt.bar(x,y)
    plt.xlabel('Hari', fontsize=8)
    plt.ylabel('Jumlah Akses', fontsize=8)
    plt.title("Jumlah Frekuensi Akses Mahasiswa pada ShareITS per-Minggu")
    plt.show()

#FIGURE FREKUENSI AKSES DOSEN PERTAHUN
def year_dsn():
    sql = "SELECT YEAR(tanggal) AS year, COUNT(*) AS jml_akses FROM dbo.Dosen GROUP BY YEAR(tanggal) HAVING (COUNT(YEAR(tanggal)) > 1) ORDER BY YEAR(tanggal) ASC"
    dfo = pdo.read_sql(sql, conn)
    df = pd.DataFrame(dfo)
    print(df)
    x = df['year']
    y = df['jml_akses']
    plt.bar(x,y)
    plt.xlabel('Tahun', fontsize=8)
    plt.ylabel('Jumlah Akses', fontsize=8)
    plt.title("Jumlah Frekuensi Akses Dosen pada ShareITS per-Tahun")
    plt.show()

#FIGURE FREKUENSI AKSES MAHASISWA PERTAHUN
def year_mhs():
    sql = "SELECT YEAR(tanggal) AS year, COUNT(*) AS jml_akses FROM dbo.MHS GROUP BY YEAR(tanggal) HAVING (COUNT(YEAR(tanggal)) > 1) ORDER BY YEAR(tanggal) ASC"
    dfo = pdo.read_sql(sql, conn)
    df = pd.DataFrame(dfo)
    print(df)
    x = df['year']
    y = df['jml_akses']
    plt.bar(x,y)
    plt.xlabel('Tahun', fontsize=8)
    plt.ylabel('Jumlah Akses', fontsize=8)
    plt.title("Jumlah Frekuensi Akses Mahasiswa pada ShareITS per-Tahun")
    plt.show()

#FIGURE FREKUENSI JUMLAH JAM AKSES MAHASISWA
def freq_time_mhs():
    plt.figure(1)
    ket = ['EARLY DAYS', 'WORKING HOURS', 'NIGHT', 'LATE NIGHT']
    earlydays = int(earlydays_mhs(conn))
    workinghours = int(workinghours_mhs(conn))
    night = int(night_mhs(conn))
    latenight = int(latenight_mhs(conn))
    jumlah = [earlydays, workinghours, night, latenight]

    print("EARLY DAYS    (00:00 - 06:00) = " + str(earlydays))
    print("WORKING HOURS (07:00 - 16:00) = " + str(workinghours))
    print("NIGHT         (17:00 - 21:00) = " + str(night))
    print("LATE NIGHT    (21:00 - 23:00) = " + str(latenight))

    plt.bar(ket, jumlah)
    plt.xlabel('Jam Akses', fontsize=8)
    plt.ylabel('Jumlah Mahasiswa', fontsize=8)
    plt.title("Frekuensi Jumlah Jam Akses Mahasiswa pada ShareITS")

    plt.show()

#FIGURE FREKUENSI JUMLAH JAM AKSES DOSEN
def freq_time_dsn():
    plt.figure(1)
    ket = ['EARLY DAYS', 'WORKING HOURS', 'NIGHT', 'LATE NIGHT']
    earlydays = int(earlydays_dsn(conn))
    workinghours = int(workinghours_dsn(conn))
    night = int(night_dsn(conn))
    latenight = int(latenight_dsn(conn))
    jumlah = [earlydays, workinghours, night, latenight]

    print("EARLY DAYS    (00:00 - 06:00) = " + str(earlydays))
    print("WORKING HOURS (07:00 - 16:00) = " + str(workinghours))
    print("NIGHT         (17:00 - 21:00) = " + str(night))
    print("LATE NIGHT    (21:00 - 23:00) = " + str(latenight))

    plt.bar(ket, jumlah)
    plt.xlabel('Jam Akses', fontsize=8)
    plt.ylabel('Jumlah Dosen', fontsize=8)
    plt.title("Frekuensi Jumlah Jam Akses Dosen pada ShareITS")

    plt.show()

def freq_time():
    plt.figure(1)
    ket = ['EARLY DAYS', 'WORKING HOURS', 'NIGHT', 'LATE NIGHT']
    earlydays = int(earlydays_mhs(conn))
    workinghours = int(workinghours_mhs(conn))
    night = int(night_mhs(conn))
    latenight = int(latenight_mhs(conn))
    jumlah = [earlydays, workinghours, night, latenight]
    print("PEAK HOUR MAHASISWA")
    print("EARLY DAYS    (00:00 - 06:00) = " + str(earlydays))
    print("WORKING HOURS (07:00 - 16:00) = " + str(workinghours))
    print("NIGHT         (17:00 - 21:00) = " + str(night))
    print("LATE NIGHT    (21:00 - 23:00) = " + str(latenight))

    plt.bar(ket, jumlah)
    plt.xlabel('Jam Akses', fontsize=8)
    plt.ylabel('Jumlah Mahasiswa', fontsize=8)
    plt.title("Frekuensi Jumlah Jam Akses Mahasiswa pada ShareITS")

    plt.show()

    plt.figure(2)
    ket = ['EARLY DAYS', 'WORKING HOURS', 'NIGHT', 'LATE NIGHT']
    earlydays = int(earlydays_dsn(conn))
    workinghours = int(workinghours_dsn(conn))
    night = int(night_dsn(conn))
    latenight = int(latenight_dsn(conn))
    jumlah = [earlydays, workinghours, night, latenight]
    print("PEAK HOUR DOSEN")
    print("EARLY DAYS    (00:00 - 06:00) = " + str(earlydays))
    print("WORKING HOURS (07:00 - 16:00) = " + str(workinghours))
    print("NIGHT         (17:00 - 21:00) = " + str(night))
    print("LATE NIGHT    (21:00 - 23:00) = " + str(latenight))

    plt.bar(ket, jumlah)
    plt.xlabel('Jam Akses', fontsize=8)
    plt.ylabel('Jumlah Dosen', fontsize=8)
    plt.title("Frekuensi Jumlah Jam Akses Dosen pada ShareITS")

    plt.show()
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
======================================================================== EXECUTION ========================================================================
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

conn = pyodbc.connect("Driver={SQL Server};"
                      "Server=AVIV-PC;"
                      "Database=db_final;"
                      "Trusted_Connection=yes;")

year_mhs()