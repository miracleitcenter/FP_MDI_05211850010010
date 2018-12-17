import pyodbc
import matplotlib.pyplot as plt
import numpy as np
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
============================================================== JUMLAH MAHASISWA PER-FAKULTAS ==============================================================
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# Function Jumlah Mahasiswa FTIK
def ftik_mhs(conn):
    cursor = conn.cursor()
    sql = cursor.execute(
        "SELECT COUNT(DISTINCT NamaMhs) AS mhs_ftik FROM dbo.Mahasiswa WHERE FakultasMhs = 'Fakultas Teknologi Informasi dan Komunikasi (FTIK)'")
    get_data = sql.fetchone()
    fk = "Fakultas Teknologi Informasi dan Komunikasi (FTIK)"
    jml = get_data.mhs_ftik
    result = fk + "#" + str(jml)
    return result


# Function Jumlah Mahasiswa FTSLK
def ftslk_mhs(conn):
    cursor = conn.cursor()
    sql = cursor.execute(
        "SELECT COUNT(DISTINCT NamaMhs) AS mhs_ftslk FROM dbo.Mahasiswa WHERE FakultasMhs = 'Fakultas Teknik Sipil, Lingkungan, dan Kebumian (FTSLK)'")
    get_data = sql.fetchone()
    fk = "Fakultas Teknik Sipil, Lingkungan, dan Kebumian (FTSLK)"
    jml = get_data.mhs_ftslk
    result = fk + "#" + str(jml)
    return result


# Function Jumlah Mahasiswa FTK
def ftk_mhs(conn):
    cursor = conn.cursor()
    sql = cursor.execute(
        "SELECT COUNT(DISTINCT NamaMhs) AS mhs_ftk FROM dbo.Mahasiswa WHERE FakultasMhs = 'Fakultas Teknologi Kelautan (FTK)'")
    get_data = sql.fetchone()
    fk = "Fakultas Teknologi Kelautan (FTK)"
    jml = get_data.mhs_ftk
    result = fk + "#" + str(jml)
    return result


# Function Jumlah Mahasiswa PPS
def pps_mhs(conn):
    cursor = conn.cursor()
    sql = cursor.execute(
        "SELECT COUNT(DISTINCT NamaMhs) AS mhs_pps FROM dbo.Mahasiswa WHERE FakultasMhs = 'Program Pasca Sarjana (PPS)'")
    get_data = sql.fetchone()
    fk = "Program Pasca Sarjana (PPS)"
    jml = get_data.mhs_pps
    result = fk + "#" + str(jml)
    return result


# Function Jumlah Mahasiswa SPADA
def spada_mhs(conn):
    cursor = conn.cursor()
    sql = cursor.execute(
        "SELECT COUNT(DISTINCT NamaMhs) AS mhs_spada FROM dbo.Mahasiswa WHERE FakultasMhs = 'Sistem Pembelajaran Daring (SPADA) Indonesia'")
    get_data = sql.fetchone()
    fk = "Sistem Pembelajaran Daring (SPADA) Indonesia"
    jml = get_data.mhs_spada
    result = fk + "#" + str(jml)
    return result


# Function Jumlah Mahasiswa UPTMK
def uptmk_mhs(conn):
    cursor = conn.cursor()
    sql = cursor.execute(
        "SELECT COUNT(DISTINCT NamaMhs) AS mhs_uptmk FROM dbo.Mahasiswa WHERE FakultasMhs = 'UPT Penyelenggara Mata Kuliah Sosial Humaniora'")
    get_data = sql.fetchone()
    fk = "UPT Penyelenggara Mata Kuliah Sosial Humaniora"
    jml = get_data.mhs_uptmk
    result = fk + "#" + str(jml)
    return result


# Function Jumlah Mahasiswa FTI
def fti_mhs(conn):
    cursor = conn.cursor()
    sql = cursor.execute(
        "SELECT COUNT(DISTINCT NamaMhs) AS mhs_fti FROM dbo.Mahasiswa WHERE FakultasMhs = 'Fakultas Teknologi Industri (FTI)'")
    get_data = sql.fetchone()
    fk = "Fakultas Teknologi Industri (FTI)"
    jml = get_data.mhs_fti
    result = fk + "#" + str(jml)
    return result


# Function Jumlah Mahasiswa FIA
def fia_mhs(conn):
    cursor = conn.cursor()
    sql = cursor.execute(
        "SELECT COUNT(DISTINCT NamaMhs) AS mhs_fia FROM dbo.Mahasiswa WHERE FakultasMhs = 'Fakultas Ilmu Alam (FIA)'")
    get_data = sql.fetchone()
    fk = "Fakultas Ilmu Alam (FIA)"
    jml = get_data.mhs_fia
    result = fk + "#" + str(jml)
    return result


# Function Jumlah Mahasiswa UPMB
def upmb_mhs(conn):
    cursor = conn.cursor()
    sql = cursor.execute("SELECT COUNT(DISTINCT NamaMhs) AS mhs_upmb FROM dbo.Mahasiswa WHERE FakultasMhs = 'UPMB'")
    get_data = sql.fetchone()
    fk = "UPMB"
    jml = get_data.mhs_upmb
    result = fk + "#" + str(jml)
    return result


# Function Result Jumlah per-Fakultas
def data_fk_mhs(val):
    if val == 'ftik':
        data = ftik_mhs(conn)
        split_data = data.split("#")
        jml_mhs = int(split_data[1])
    elif val == 'ftslk':
        data = ftslk_mhs(conn)
        split_data = data.split("#")
        jml_mhs = int(split_data[1])
    elif val == 'ftk':
        data = ftk_mhs(conn)
        split_data = data.split("#")
        jml_mhs = int(split_data[1])
    elif val == 'pps':
        data = pps_mhs(conn)
        split_data = data.split("#")
        jml_mhs = int(split_data[1])
    elif val == 'spada':
        data = spada_mhs(conn)
        split_data = data.split("#")
        jml_mhs = int(split_data[1])
    elif val == 'uptmk':
        data = uptmk_mhs(conn)
        split_data = data.split("#")
        jml_mhs = int(split_data[1])
    elif val == 'fti':
        data = fti_mhs(conn)
        split_data = data.split("#")
        jml_mhs = int(split_data[1])
    elif val == 'fia':
        data = fia_mhs(conn)
        split_data = data.split("#")
        jml_mhs = int(split_data[1])
    elif val == 'upmb':
        data = upmb_mhs(conn)
        split_data = data.split("#")
        jml_mhs = int(split_data[1])
    else:
        jml_mhs = ""
    return jml_mhs


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
============================================================ JUMLAH MAHASISWA PER-JURUSAN(FK) ============================================================
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


# Jurusan di FTIK (Split Value = SI + INFOR)
def jurusan_ftik_mhs(conn):
    cursor = conn.cursor()
    # Sistem Informasi (SI)
    sql_si = cursor.execute(
        "SELECT COUNT(DISTINCT NamaMhs) AS ftik_si FROM dbo.Mahasiswa WHERE JurusanMhs = 'Sistem Informasi' AND FakultasMhs = 'Fakultas Teknologi Informasi dan Komunikasi (FTIK)'")
    data_si = sql_si.fetchone()
    si = "Sistem Informasi"
    jml_si = data_si.ftik_si
    result_si = si + "#" + str(jml_si)
    # Teknik Informatika (INFOR)
    sql_infor = cursor.execute(
        "SELECT COUNT(DISTINCT NamaMhs) AS ftik_infor FROM dbo.Mahasiswa WHERE JurusanMhs = 'Informatika' AND FakultasMhs = 'Fakultas Teknologi Informasi dan Komunikasi (FTIK)'")
    data_infor = sql_infor.fetchone()
    infor = "Informatika"
    jml_infor = data_infor.ftik_infor
    result_infor = infor + "#" + str(jml_infor)
    # Result SI + INFOR
    result = result_si + "+" + result_infor
    return result


# Jurusan di FTSLK (Split Value = TGM + TS + TL + TGF)
def jurusan_ftslk_mhs(conn):
    cursor = conn.cursor()
    # Teknik Geomatika (TGM)
    sql_tgm = cursor.execute(
        "SELECT COUNT(DISTINCT NamaMhs) AS ftslk_tgm FROM dbo.Mahasiswa WHERE JurusanMhs = 'Teknik Geomatika' AND FakultasMhs = 'Fakultas Teknik Sipil, Lingkungan, dan Kebumian (FTSLK)'")
    data_tgm = sql_tgm.fetchone()
    tgm = "Teknik Geomatika"
    jml_tgm = data_tgm.ftslk_tgm
    result_tgm = tgm + "#" + str(jml_tgm)
    # Teknik Sipil (TS)
    sql_ts = cursor.execute(
        "SELECT COUNT(DISTINCT NamaMhs) AS ftslk_ts FROM dbo.Mahasiswa WHERE JurusanMhs = 'Teknik Sipil' AND FakultasMhs = 'Fakultas Teknik Sipil, Lingkungan, dan Kebumian (FTSLK)'")
    data_ts = sql_ts.fetchone()
    ts = "Teknik Sipil"
    jml_ts = data_ts.ftslk_ts
    result_ts = ts + "#" + str(jml_ts)
    # Teknik Lingkungan (TL)
    sql_tl = cursor.execute(
        "SELECT COUNT(DISTINCT NamaMhs) AS ftslk_tl FROM dbo.Mahasiswa WHERE JurusanMhs = 'Teknik Lingkungan' AND FakultasMhs = 'Fakultas Teknik Sipil, Lingkungan, dan Kebumian (FTSLK)'")
    data_tl = sql_tl.fetchone()
    tl = "Teknik Lingkkungan"
    jml_tl = data_tl.ftslk_tl
    result_tl = tl + "#" + str(jml_tl)
    # Teknik Geofisika (TGF)
    sql_tgf = cursor.execute(
        "SELECT COUNT(DISTINCT NamaMhs) AS ftslk_tgf FROM dbo.Mahasiswa WHERE JurusanMhs = 'Teknik Geofisika' AND FakultasMhs = 'Fakultas Teknik Sipil, Lingkungan, dan Kebumian (FTSLK)'")
    data_tgf = sql_tgf.fetchone()
    tgf = "Teknik Geofisika"
    jml_tgf = data_tgf.ftslk_tgf
    result_tgf = tgf + "#" + str(jml_tgf)
    # Result TGM + TS + TL + TGF
    result = result_tgm + "+" + result_ts + "+" + result_tl + "+" + result_tgf
    return result


# Jurusan di FTK (Split Value = TK + TP + TSP)
def jurusan_ftk_mhs(conn):
    cursor = conn.cursor()
    # Teknik Kelautan (TK)
    sql_tk = cursor.execute(
        "SELECT COUNT(DISTINCT NamaMhs) AS ftk_tk FROM dbo.Mahasiswa WHERE JurusanMhs = 'Teknik Kelautan' AND FakultasMhs = 'Fakultas Teknologi Kelautan (FTK)'")
    data_tk = sql_tk.fetchone()
    tk = "Teknik Kelautan"
    jml_tk = data_tk.ftk_tk
    result_tk = tk + "#" + str(jml_tk)
    # Teknik Perkapalan (TP)
    sql_tp = cursor.execute(
        "SELECT COUNT(DISTINCT NamaMhs) AS ftk_tp FROM dbo.Mahasiswa WHERE JurusanMhs = 'Teknik Perkapalan' AND FakultasMhs = 'Fakultas Teknologi Kelautan (FTK)'")
    data_tp = sql_tp.fetchone()
    tp = "Teknik Perkapalan"
    jml_tp = data_tp.ftk_tp
    result_tp = tp + "#" + str(jml_tp)
    # Teknik Sistem Perkapalan (TSP)
    sql_tsp = cursor.execute(
        "SELECT COUNT(DISTINCT NamaMhs) AS ftk_tsp FROM dbo.Mahasiswa WHERE JurusanMhs = 'Teknik Sistem Perkapalan' AND FakultasMhs = 'Fakultas Teknologi Kelautan (FTK)'")
    data_tsp = sql_tsp.fetchone()
    tsp = "Teknik Sistem Perkapalan"
    jml_tsp = data_tsp.ftk_tsp
    result_tsp = tsp + "#" + str(jml_tsp)
    # Result TK + TP + TSP
    result = result_tk + "+" + result_tp + "+" + result_tsp
    return result


# Jurusan di FTI (Split Value = TMM + TI + TF + TK + TM)
def jurusan_fti_mhs(conn):
    cursor = conn.cursor()
    # Teknik Material dan Metalurgi (TMM)
    sql_tmm = cursor.execute(
        "SELECT COUNT(DISTINCT NamaMhs) AS fti_tmm FROM dbo.Mahasiswa WHERE JurusanMhs = 'Teknik Material dan Metalurgi' AND FakultasMhs = 'Fakultas Teknologi Industri (FTI)'")
    data_tmm = sql_tmm.fetchone()
    tmm = "Teknik Material dan Metalurgi"
    jml_tmm = data_tmm.fti_tmm
    result_tmm = tmm + "#" + str(jml_tmm)
    # Teknik Industri (TI)
    sql_ti = cursor.execute(
        "SELECT COUNT(DISTINCT NamaMhs) AS fti_ti FROM dbo.Mahasiswa WHERE JurusanMhs = 'Teknik Industri' AND FakultasMhs = 'Fakultas Teknologi Industri (FTI)'")
    data_ti = sql_ti.fetchone()
    ti = "Teknik Industri"
    jml_ti = data_ti.fti_ti
    result_ti = ti + "#" + str(jml_ti)
    # Teknik Fisika (TF)
    sql_tf = cursor.execute(
        "SELECT COUNT(DISTINCT NamaMhs) AS fti_tf FROM dbo.Mahasiswa WHERE JurusanMhs = 'Teknik Fisika' AND FakultasMhs = 'Fakultas Teknologi Industri (FTI)'")
    data_tf = sql_tf.fetchone()
    tf = "Teknik Fisika"
    jml_tf = data_tf.fti_tf
    result_tf = tf + "#" + str(jml_tf)
    # Teknik Kimia (TK)
    sql_tk = cursor.execute(
        "SELECT COUNT(DISTINCT NamaMhs) AS fti_tk FROM dbo.Mahasiswa WHERE JurusanMhs = 'Teknik Kimia' AND FakultasMhs = 'Fakultas Teknologi Industri (FTI)'")
    data_tk = sql_tk.fetchone()
    tk = "Teknik Kimia"
    jml_tk = data_tk.fti_tk
    result_tk = tk + "#" + str(jml_tk)
    # Teknik Mesin (TM)
    sql_tm = cursor.execute(
        "SELECT COUNT(DISTINCT NamaMhs) AS fti_tm FROM dbo.Mahasiswa WHERE JurusanMhs = 'Teknik Mesin' AND FakultasMhs = 'Fakultas Teknologi Industri (FTI)'")
    data_tm = sql_tm.fetchone()
    tm = "Teknik Mesin"
    jml_tm = data_tm.fti_tm
    result_tm = tm + "#" + str(jml_tm)
    # Result TMM + TI + TF + TK + TM
    result = result_tmm + "+" + result_ti + "+" + result_tf + "+" + result_tk + "+" + result_tm
    return result


# Jurusan di FIA (Split Value = Bio + Fis + Kim
def jurusan_fia_mhs(conn):
    cursor = conn.cursor()
    # Biologi (Bio)
    sql_bio = cursor.execute(
        "SELECT COUNT(DISTINCT NamaMhs) AS fia_bio FROM dbo.Mahasiswa WHERE JurusanMhs = 'Biologi' AND FakultasMhs = 'Fakultas Ilmu Alam (FIA)'")
    data_bio = sql_bio.fetchone()
    bio = "Biologi"
    jml_bio = data_bio.fia_bio
    result_bio = bio + "#" + str(jml_bio)
    # Fisika (Fis)
    sql_fis = cursor.execute(
        "SELECT COUNT(DISTINCT NamaMhs) AS fia_fis FROM dbo.Mahasiswa WHERE JurusanMhs = 'Fisika' AND FakultasMhs = 'Fakultas Ilmu Alam (FIA)'")
    data_fis = sql_fis.fetchone()
    fis = "Fisika"
    jml_fis = data_fis.fia_fis
    result_fis = fis + "#" + str(jml_fis)
    # Kimia (Kim)
    sql_kim = cursor.execute(
        "SELECT COUNT(DISTINCT NamaMhs) AS fia_kim FROM dbo.Mahasiswa WHERE JurusanMhs = 'Kimia' AND FakultasMhs = 'Fakultas Ilmu Alam (FIA)'")
    data_kim = sql_kim.fetchone()
    kim = "Kimia"
    jml_kim = data_kim.fia_kim
    result_kim = kim + "#" + str(jml_kim)
    # Result Bio + Fis + Kim
    result = result_bio + "+" + result_fis + "+" + result_kim
    return result


# Function Result Jurusan (FK)
def data_jurusan_mhs(fk, jurusan):
    if fk == 'ftik':
        data = jurusan_ftik_mhs(conn)
        split_data = data.split('+')
        if jurusan == 'Sistem Informasi':
            get_jurusan = split_data[0].split('#')
            jml_mhs = get_jurusan[1]
        else:
            get_jurusan = split_data[1].split('#')
            jml_mhs = get_jurusan[1]
    elif fk == 'ftk':
        data = jurusan_ftk_mhs(conn)
        split_data = data.split('+')
        if jurusan == 'Teknik Kelautan':
            get_jurusan = split_data[0].split('#')
            jml_mhs = get_jurusan[1]
        elif jurusan == 'Teknik Perkapalan':
            get_jurusan = split_data[1].split('#')
            jml_mhs = get_jurusan[1]
        else:
            get_jurusan = split_data[2].split('#')
            jml_mhs = get_jurusan[1]
    elif fk == 'ftslk':
        data = jurusan_ftslk_mhs(conn)
        split_data = data.split('+')
        if jurusan == 'Teknik Geomatika':
            get_jurusan = split_data[0].split('#')
            jml_mhs = get_jurusan[1]
        elif jurusan == 'Teknik Sipil':
            get_jurusan = split_data[1].split('#')
            jml_mhs = get_jurusan[1]
        elif jurusan == 'Teknik Lingkungan':
            get_jurusan = split_data[2].split('#')
            jml_mhs = get_jurusan[1]
        else:
            get_jurusan = split_data[3].split('#')
            jml_mhs = get_jurusan[1]
    elif fk == 'fti':
        data = jurusan_fti_mhs(conn)
        split_data = data.split('+')
        if jurusan == 'Teknik Material dan Metalurgi':
            get_jurusan = split_data[0].split('#')
            jml_mhs = get_jurusan[1]
        elif jurusan == 'Teknik Industri':
            get_jurusan = split_data[1].split('#')
            jml_mhs = get_jurusan[1]
        elif jurusan == 'Teknik Fisika':
            get_jurusan = split_data[2].split('#')
            jml_mhs = get_jurusan[1]
        elif jurusan == 'Teknik Kimia':
            get_jurusan = split_data[3].split('#')
            jml_mhs = get_jurusan[1]
        else:
            get_jurusan = split_data[4].split('#')
            jml_mhs = get_jurusan[1]
    elif fk == 'fia':
        data = jurusan_fia_mhs(conn)
        split_data = data.split('+')
        if jurusan == 'Biologi':
            get_jurusan = split_data[0].split('#')
            jml_mhs = get_jurusan[1]
        elif jurusan == 'Fisika':
            get_jurusan = split_data[1].split('#')
            jml_mhs = get_jurusan[1]
        else:
            get_jurusan = split_data[2].split('#')
            jml_mhs = get_jurusan[1]
    else:
        jml_mhs = "0";
    return jml_mhs


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
============================================================== JUMLAH DOSEN PER-FAKULTAS ==============================================================
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#Function Jumlah Dosen FTIK
def ftik(conn):
    cursor = conn.cursor()
    sql = cursor.execute("SELECT COUNT(DISTINCT NamaDosen) AS dsn_ftik FROM dbo.Dosen WHERE Fakultas = 'Fakultas Teknologi Informasi dan Komunikasi (FTIK)'")
    get_data = sql.fetchone()
    fk = "Fakultas Teknologi Informasi dan Komunikasi (FTIK)"
    jml = get_data.dsn_ftik
    result = fk + "#" + str(jml)
    return result

#Function Jumlah Dosen FTSLK
def ftslk(conn):
    cursor = conn.cursor()
    sql = cursor.execute("SELECT COUNT(DISTINCT NamaDosen) AS dsn_ftslk FROM dbo.Dosen WHERE Fakultas = 'Fakultas Teknik Sipil, Lingkungan, dan Kebumian (FTSLK)'")
    get_data = sql.fetchone()
    fk = "Fakultas Teknik Sipil, Lingkungan, dan Kebumian (FTSLK)"
    jml = get_data.dsn_ftslk
    result = fk + "#" + str(jml)
    return result

#Function Jumlah Dosen FTK
def ftk(conn):
    cursor = conn.cursor()
    sql = cursor.execute("SELECT COUNT(DISTINCT NamaDosen) AS dsn_ftk FROM dbo.Dosen WHERE Fakultas = 'Fakultas Teknologi Kelautan (FTK)'")
    get_data = sql.fetchone()
    fk = "Fakultas Teknologi Kelautan (FTK)"
    jml = get_data.dsn_ftk
    result = fk + "#" + str(jml)
    return result

#Function Jumlah Dosen PPS
def pps(conn):
    cursor = conn.cursor()
    sql = cursor.execute("SELECT COUNT(DISTINCT NamaDosen) AS dsn_pps FROM dbo.Dosen WHERE Fakultas = 'Program Pasca Sarjana (PPS)'")
    get_data = sql.fetchone()
    fk = "Program Pasca Sarjana (PPS)"
    jml = get_data.dsn_pps
    result = fk + "#" + str(jml)
    return result

#Function Jumlah Dosen SPADA
def spada(conn):
    cursor = conn.cursor()
    sql = cursor.execute("SELECT COUNT(DISTINCT NamaDosen) AS dsn_spada FROM dbo.Dosen WHERE Fakultas = 'Sistem Pembelajaran Daring (SPADA) Indonesia'")
    get_data = sql.fetchone()
    fk = "Sistem Pembelajaran Daring (SPADA) Indonesia"
    jml = get_data.dsn_spada
    result = fk + "#" + str(jml)
    return result

#Function Jumlah Dosen UPTMK
def uptmk(conn):
    cursor = conn.cursor()
    sql = cursor.execute("SELECT COUNT(DISTINCT NamaDosen) AS dsn_uptmk FROM dbo.Dosen WHERE Fakultas = 'UPT Penyelenggara Mata Kuliah Sosial Humaniora'")
    get_data = sql.fetchone()
    fk = "UPT Penyelenggara Mata Kuliah Sosial Humaniora"
    jml = get_data.dsn_uptmk
    result = fk + "#" + str(jml)
    return result

#Function Jumlah Dosen FTI
def fti(conn):
    cursor = conn.cursor()
    sql = cursor.execute("SELECT COUNT(DISTINCT NamaDosen) AS dsn_fti FROM dbo.Dosen WHERE Fakultas = 'Fakultas Teknologi Industri (FTI)'")
    get_data = sql.fetchone()
    fk = "Fakultas Teknologi Industri (FTI)"
    jml = get_data.dsn_fti
    result = fk + "#" + str(jml)
    return result

#Function Jumlah Dosen FIA
def fia(conn):
    cursor = conn.cursor()
    sql = cursor.execute("SELECT COUNT(DISTINCT NamaDosen) AS dsn_fia FROM dbo.Dosen WHERE Fakultas = 'Fakultas Ilmu Alam (FIA)'")
    get_data = sql.fetchone()
    fk = "Fakultas Ilmu Alam (FIA)"
    jml = get_data.dsn_fia
    result = fk + "#" + str(jml)
    return result

#Function Jumlah Dosen UPMB
def upmb(conn):
    cursor = conn.cursor()
    sql = cursor.execute("SELECT COUNT(DISTINCT NamaDosen) AS dsn_upmb FROM dbo.Dosen WHERE Fakultas = 'UPMB'")
    get_data = sql.fetchone()
    fk = "UPMB"
    jml = get_data.dsn_upmb
    result = fk + "#" + str(jml)
    return result

#Function Result Fakultas
def data_fk(val):
    if val == 'ftik':
        data = ftik(conn)
        split_data = data.split("#")
        jml_dsn = int(split_data[1])
    elif val == 'ftslk':
        data = ftslk(conn)
        split_data = data.split("#")
        jml_dsn = int(split_data[1])
    elif val == 'ftk':
        data = ftk(conn)
        split_data = data.split("#")
        jml_dsn = int(split_data[1])
    elif val == 'pps':
        data = pps(conn)
        split_data = data.split("#")
        jml_dsn = int(split_data[1])
    elif val == 'spada':
        data = spada(conn)
        split_data = data.split("#")
        jml_dsn = int(split_data[1])
    elif val == 'uptmk':
        data = uptmk(conn)
        split_data = data.split("#")
        jml_dsn = int(split_data[1])
    elif val == 'fti':
        data = fti(conn)
        split_data = data.split("#")
        jml_dsn = int(split_data[1])
    elif val == 'fia':
        data = fia(conn)
        split_data = data.split("#")
        jml_dsn = int(split_data[1])
    elif val == 'upmb':
        data = upmb(conn)
        split_data = data.split("#")
        jml_dsn = int(split_data[1])
    else:
        jml_dsn = ""
    return jml_dsn


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
============================================================== JUMLAH DOSEN PER-JURUSAN(FK) ==============================================================
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Jurusan di FTIK (Split Value = SI + INFOR)
def jurusan_ftik(conn):
    cursor = conn.cursor()
    # Sistem Informasi (SI)
    sql_si = cursor.execute(
        "SELECT COUNT(DISTINCT NamaDosen) AS ftik_si FROM dbo.Dosen WHERE Jurusan = 'Sistem Informasi' AND Fakultas = 'Fakultas Teknologi Informasi dan Komunikasi (FTIK)'")
    data_si = sql_si.fetchone()
    si = "Sistem Informasi"
    jml_si = data_si.ftik_si
    result_si = si + "#" + str(jml_si)
    # Teknik Informatika (INFOR)
    sql_infor = cursor.execute(
        "SELECT COUNT(DISTINCT NamaDosen) AS ftik_infor FROM dbo.Dosen WHERE Jurusan = 'Informatika' AND Fakultas = 'Fakultas Teknologi Informasi dan Komunikasi (FTIK)'")
    data_infor = sql_infor.fetchone()
    infor = "Informatika"
    jml_infor = data_infor.ftik_infor
    result_infor = infor + "#" + str(jml_infor)
    # Result SI + INFOR
    result = result_si + "+" + result_infor
    return result


# Jurusan di FTSLK (Split Value = TGM + TS + TL + TGF)
def jurusan_ftslk(conn):
    cursor = conn.cursor()
    # Teknik Geomatika (TGM)
    sql_tgm = cursor.execute(
        "SELECT COUNT(DISTINCT NamaDosen) AS ftslk_tgm FROM dbo.Dosen WHERE Jurusan = 'Teknik Geomatika' AND Fakultas = 'Fakultas Teknik Sipil, Lingkungan, dan Kebumian (FTSLK)'")
    data_tgm = sql_tgm.fetchone()
    tgm = "Teknik Geomatika"
    jml_tgm = data_tgm.ftslk_tgm
    result_tgm = tgm + "#" + str(jml_tgm)
    # Teknik Sipil (TS)
    sql_ts = cursor.execute(
        "SELECT COUNT(DISTINCT NamaDosen) AS ftslk_ts FROM dbo.Dosen WHERE Jurusan = 'Teknik Sipil' AND Fakultas = 'Fakultas Teknik Sipil, Lingkungan, dan Kebumian (FTSLK)'")
    data_ts = sql_ts.fetchone()
    ts = "Teknik Sipil"
    jml_ts = data_ts.ftslk_ts
    result_ts = ts + "#" + str(jml_ts)
    # Teknik Lingkungan (TL)
    sql_tl = cursor.execute(
        "SELECT COUNT(DISTINCT NamaDosen) AS ftslk_tl FROM dbo.Dosen WHERE Jurusan = 'Teknik Lingkungan' AND Fakultas = 'Fakultas Teknik Sipil, Lingkungan, dan Kebumian (FTSLK)'")
    data_tl = sql_tl.fetchone()
    tl = "Teknik Lingkkungan"
    jml_tl = data_tl.ftslk_tl
    result_tl = tl + "#" + str(jml_tl)
    # Teknik Geofisika (TGF)
    sql_tgf = cursor.execute(
        "SELECT COUNT(DISTINCT NamaDosen) AS ftslk_tgf FROM dbo.Dosen WHERE Jurusan = 'Teknik Geofisika' AND Fakultas = 'Fakultas Teknik Sipil, Lingkungan, dan Kebumian (FTSLK)'")
    data_tgf = sql_tgf.fetchone()
    tgf = "Teknik Geofisika"
    jml_tgf = data_tgf.ftslk_tgf
    result_tgf = tgf + "#" + str(jml_tgf)
    # Result TGM + TS + TL + TGF
    result = result_tgm + "+" + result_ts + "+" + result_tl + "+" + result_tgf
    return result


# Jurusan di FTK (Split Value = TK + TP + TSP)
def jurusan_ftk(conn):
    cursor = conn.cursor()
    # Teknik Kelautan (TK)
    sql_tk = cursor.execute(
        "SELECT COUNT(DISTINCT NamaDosen) AS ftk_tk FROM dbo.Dosen WHERE Jurusan = 'Teknik Kelautan' AND Fakultas = 'Fakultas Teknologi Kelautan (FTK)'")
    data_tk = sql_tk.fetchone()
    tk = "Teknik Kelautan"
    jml_tk = data_tk.ftk_tk
    result_tk = tk + "#" + str(jml_tk)
    # Teknik Perkapalan (TP)
    sql_tp = cursor.execute(
        "SELECT COUNT(DISTINCT NamaDosen) AS ftk_tp FROM dbo.Dosen WHERE Jurusan = 'Teknik Perkapalan' AND Fakultas = 'Fakultas Teknologi Kelautan (FTK)'")
    data_tp = sql_tp.fetchone()
    tp = "Teknik Perkapalan"
    jml_tp = data_tp.ftk_tp
    result_tp = tp + "#" + str(jml_tp)
    # Teknik Sistem Perkapalan (TSP)
    sql_tsp = cursor.execute(
        "SELECT COUNT(DISTINCT NamaDosen) AS ftk_tsp FROM dbo.Dosen WHERE Jurusan = 'Teknik Sistem Perkapalan' AND Fakultas = 'Fakultas Teknologi Kelautan (FTK)'")
    data_tsp = sql_tsp.fetchone()
    tsp = "Teknik Sistem Perkapalan"
    jml_tsp = data_tsp.ftk_tsp
    result_tsp = tsp + "#" + str(jml_tsp)
    # Result TK + TP + TSP
    result = result_tk + "+" + result_tp + "+" + result_tsp
    return result


# Jurusan di FTI (Split Value = TMM + TI + TF + TK + TM)
def jurusan_fti(conn):
    cursor = conn.cursor()
    # Teknik Material dan Metalurgi (TMM)
    sql_tmm = cursor.execute(
        "SELECT COUNT(DISTINCT NamaDosen) AS fti_tmm FROM dbo.Dosen WHERE Jurusan = 'Teknik Material dan Metalurgi' AND Fakultas = 'Fakultas Teknologi Industri (FTI)'")
    data_tmm = sql_tmm.fetchone()
    tmm = "Teknik Material dan Metalurgi"
    jml_tmm = data_tmm.fti_tmm
    result_tmm = tmm + "#" + str(jml_tmm)
    # Teknik Industri (TI)
    sql_ti = cursor.execute(
        "SELECT COUNT(DISTINCT NamaDosen) AS fti_ti FROM dbo.Dosen WHERE Jurusan = 'Teknik Industri' AND Fakultas = 'Fakultas Teknologi Industri (FTI)'")
    data_ti = sql_ti.fetchone()
    ti = "Teknik Industri"
    jml_ti = data_ti.fti_ti
    result_ti = ti + "#" + str(jml_ti)
    # Teknik Fisika (TF)
    sql_tf = cursor.execute(
        "SELECT COUNT(DISTINCT NamaDosen) AS fti_tf FROM dbo.Dosen WHERE Jurusan = 'Teknik Fisika' AND Fakultas = 'Fakultas Teknologi Industri (FTI)'")
    data_tf = sql_tf.fetchone()
    tf = "Teknik Fisika"
    jml_tf = data_tf.fti_tf
    result_tf = tf + "#" + str(jml_tf)
    # Teknik Kimia (TK)
    sql_tk = cursor.execute(
        "SELECT COUNT(DISTINCT NamaDosen) AS fti_tk FROM dbo.Dosen WHERE Jurusan = 'Teknik Kimia' AND Fakultas = 'Fakultas Teknologi Industri (FTI)'")
    data_tk = sql_tk.fetchone()
    tk = "Teknik Kimia"
    jml_tk = data_tk.fti_tk
    result_tk = tk + "#" + str(jml_tk)
    # Teknik Mesin (TM)
    sql_tm = cursor.execute(
        "SELECT COUNT(DISTINCT NamaDosen) AS fti_tm FROM dbo.Dosen WHERE Jurusan = 'Teknik Mesin' AND Fakultas = 'Fakultas Teknologi Industri (FTI)'")
    data_tm = sql_tm.fetchone()
    tm = "Teknik Mesin"
    jml_tm = data_tm.fti_tm
    result_tm = tm + "#" + str(jml_tm)
    # Result TMM + TI + TF + TK + TM
    result = result_tmm + "+" + result_ti + "+" + result_tf + "+" + result_tk + "+" + result_tm
    return result


# Jurusan di FIA (Split Value = Bio + Fis + Kim
def jurusan_fia(conn):
    cursor = conn.cursor()
    # Biologi (Bio)
    sql_bio = cursor.execute(
        "SELECT COUNT(DISTINCT NamaDosen) AS fia_bio FROM dbo.Dosen WHERE Jurusan = 'Biologi' AND Fakultas = 'Fakultas Ilmu Alam (FIA)'")
    data_bio = sql_bio.fetchone()
    bio = "Biologi"
    jml_bio = data_bio.fia_bio
    result_bio = bio + "#" + str(jml_bio)
    # Fisika (Fis)
    sql_fis = cursor.execute(
        "SELECT COUNT(DISTINCT NamaDosen) AS fia_fis FROM dbo.Dosen WHERE Jurusan = 'Fisika' AND Fakultas = 'Fakultas Ilmu Alam (FIA)'")
    data_fis = sql_fis.fetchone()
    fis = "Fisika"
    jml_fis = data_fis.fia_fis
    result_fis = fis + "#" + str(jml_fis)
    # Kimia (Kim)
    sql_kim = cursor.execute(
        "SELECT COUNT(DISTINCT NamaDosen) AS fia_kim FROM dbo.Dosen WHERE Jurusan = 'Kimia' AND Fakultas = 'Fakultas Ilmu Alam (FIA)'")
    data_kim = sql_kim.fetchone()
    kim = "Kimia"
    jml_kim = data_kim.fia_kim
    result_kim = kim + "#" + str(jml_kim)
    # Result Bio + Fis + Kim
    result = result_bio + "+" + result_fis + "+" + result_kim
    return result


# Function Result Jurusan (FK)
def data_jurusan(fk, jurusan):
    if fk == 'ftik':
        data = jurusan_ftik(conn)
        split_data = data.split('+')
        if jurusan == 'Sistem Informasi':
            get_jurusan = split_data[0].split('#')
            jml_mhs = get_jurusan[1]
        else:
            get_jurusan = split_data[1].split('#')
            jml_mhs = get_jurusan[1]
    elif fk == 'ftk':
        data = jurusan_ftk(conn)
        split_data = data.split('+')
        if jurusan == 'Teknik Kelautan':
            get_jurusan = split_data[0].split('#')
            jml_mhs = get_jurusan[1]
        elif jurusan == 'Teknik Perkapalan':
            get_jurusan = split_data[1].split('#')
            jml_mhs = get_jurusan[1]
        else:
            get_jurusan = split_data[2].split('#')
            jml_mhs = get_jurusan[1]
    elif fk == 'ftslk':
        data = jurusan_ftslk(conn)
        split_data = data.split('+')
        if jurusan == 'Teknik Geomatika':
            get_jurusan = split_data[0].split('#')
            jml_mhs = get_jurusan[1]
        elif jurusan == 'Teknik Sipil':
            get_jurusan = split_data[1].split('#')
            jml_mhs = get_jurusan[1]
        elif jurusan == 'Teknik Lingkungan':
            get_jurusan = split_data[2].split('#')
            jml_mhs = get_jurusan[1]
        else:
            get_jurusan = split_data[3].split('#')
            jml_mhs = get_jurusan[1]
    elif fk == 'fti':
        data = jurusan_fti(conn)
        split_data = data.split('+')
        if jurusan == 'Teknik Material dan Metalurgi':
            get_jurusan = split_data[0].split('#')
            jml_mhs = get_jurusan[1]
        elif jurusan == 'Teknik Industri':
            get_jurusan = split_data[1].split('#')
            jml_mhs = get_jurusan[1]
        elif jurusan == 'Teknik Fisika':
            get_jurusan = split_data[2].split('#')
            jml_mhs = get_jurusan[1]
        elif jurusan == 'Teknik Kimia':
            get_jurusan = split_data[3].split('#')
            jml_mhs = get_jurusan[1]
        else:
            get_jurusan = split_data[4].split('#')
            jml_mhs = get_jurusan[1]
    elif fk == 'fia':
        data = jurusan_fia(conn)
        split_data = data.split('+')
        if jurusan == 'Biologi':
            get_jurusan = split_data[0].split('#')
            jml_mhs = get_jurusan[1]
        elif jurusan == 'Fisika':
            get_jurusan = split_data[1].split('#')
            jml_mhs = get_jurusan[1]
        else:
            get_jurusan = split_data[2].split('#')
            jml_mhs = get_jurusan[1]
    else:
        jml_mhs = "0";
    return jml_mhs


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
======================================================================= GRAFIK DATA DOSEN ================================================================
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Figure Fakultas
def fig_fk():
    plt.figure(1)
    fakultas = ['FTK', 'FTSLK', 'FTI', 'FIA', 'FTIK']
    jml_ftk = data_fk('ftk')
    jml_ftslk = data_fk('ftslk')
    jml_fti = data_fk('fti')
    jml_fia = data_fk('fia')
    jml_ftik = data_fk('ftik')
    jml_fakultas = [jml_ftk, jml_ftslk, jml_fti, jml_fia, jml_ftik]

    print("FTK = " + str(jml_ftk))
    print("FTSLK = " + str(jml_ftslk))
    print("FTI = " + str(jml_fti))
    print("FIA = " + str(jml_fia))
    print("FTIK = " + str(jml_ftik))

    plt.bar(fakultas, jml_fakultas)
    plt.xlabel('Fakultas', fontsize=8)
    plt.ylabel('Jumlah Dosen', fontsize=8)
    plt.title("Jumlah Dosen yang Mengakses ShareITS berdasarkan Fakultas")

    plt.show()

# Figure Jurusan FTIK
def fig_ftik():
    plt.figure("Fakultas Teknologi Informasi dan Komunikasi (FTIK)")
    jurusan = ['Sistem Informasi', 'Informatika']
    jml_si = int(data_jurusan('ftik', 'Sistem Informasi'))
    jml_infor = int(data_jurusan('ftik', 'Informatika'))
    jml_jurusan = [jml_si, jml_infor]

    print("Sistem Informasi = " + str(jml_si))
    print("Informatika = " + str(jml_infor))

    plt.bar(jurusan, jml_jurusan)
    plt.xlabel('Jurusan', fontsize=8)
    plt.ylabel('Jumlah Dosen', fontsize=8)
    plt.title("Jumlah Dosen FTIK yang Mengakses ShareITS berdasarkan Jurusan")

    plt.show()

# Figure Jurusan FTK
def fig_ftk():
    plt.figure("Fakultas Teknik Kelautan (FTK)")
    jurusan = ['Teknik Kelautan', 'Teknik Perkapalan', 'Teknik Sistem Perkapalan']
    jml_tk = int(data_jurusan('ftk', 'Teknik Kelautan'))
    jml_tp = int(data_jurusan('ftk', 'Teknik Perkapalan'))
    jml_tsp = int(data_jurusan('ftk', 'Teknik Sistem Perkapalan'))
    jml_jurusan = [jml_tk, jml_tp, jml_tsp]

    print("Teknik Kelautan = " + str(jml_tk))
    print("Teknik Perkapalan = " + str(jml_tp))
    print("Teknik Sistem Perkapalan = " + str(jml_tsp))

    plt.bar(jurusan, jml_jurusan)
    plt.xlabel('Jurusan', fontsize=8)
    plt.ylabel('Jumlah Dosen', fontsize=8)
    plt.title("Jumlah Dosen FTK yang Mengakses ShareITS berdasarkan Jurusan")

    plt.show()

# Figure Jurusan FTSLK
def fig_ftslk():
    plt.figure("Fakultas Teknik Sipil, Lingkungan, dan Kebumian (FTSLK)")
    jurusan = ['Teknik Geomatika', 'Teknik Sipil', 'Teknik Lingkungan', 'Teknik Geofisika']
    jml_tgm = int(data_jurusan('ftslk', 'Teknik Geomatika'))
    jml_ts = int(data_jurusan('ftslk', 'Teknik Sipil'))
    jml_tl = int(data_jurusan('ftslk', 'Teknik Lingkungan'))
    jml_tgs = int(data_jurusan('ftslk', 'Teknik Geofisika'))
    jml_jurusan = [jml_tgm, jml_ts, jml_tl, jml_tgs]

    print("Teknik Geomatika = " + str(jml_tgm))
    print("Teknik Sipil = " + str(jml_ts))
    print("Teknik Lingkungan = " + str(jml_tl))
    print("Teknik Geofisika = " + str(jml_tgs))

    plt.bar(jurusan, jml_jurusan)
    plt.xlabel('Jurusan', fontsize=8)
    plt.ylabel('Jumlah Dosen', fontsize=8)
    plt.title("Jumlah Dosen FTSLK yang Mengakses ShareITS berdasarkan Jurusan")

    plt.show()

# Figure Jurusan FTI
def fig_fti():
    plt.figure("Fakultas Teknik Industri (FTI)")
    jurusan = ['Teknik Material dan Metalurgi', 'Teknik Industri', 'Teknik Fisika', 'Teknik Kimia', 'Teknik Mesin']
    jml_tmm = int(data_jurusan('fti', 'Teknik Material dan Metalurgi'))
    jml_ti = int(data_jurusan('fti', 'Teknik Industri'))
    jml_tf = int(data_jurusan('fti', 'Teknik Fisika'))
    jml_tk = int(data_jurusan('fti', 'Teknik Kimia'))
    jml_tm = int(data_jurusan('fti', 'Teknik Mesin'))
    jml_jurusan = [jml_tmm, jml_ti, jml_tf, jml_tk, jml_tm]

    print("Teknik Material dan Metalurgi = " + str(jml_tmm))
    print("Teknik Industri = " + str(jml_ti))
    print("Teknik Fisika = " + str(jml_tf))
    print("Teknik Kimia = " + str(jml_tk))
    print("Teknik Mesin = " + str(jml_tm))

    plt.bar(jurusan, jml_jurusan)
    plt.xlabel('Jurusan', fontsize=8)
    plt.ylabel('Jumlah Dosen', fontsize=8)
    plt.title("Jumlah Dosen FTSLK yang Mengakses ShareITS berdasarkan Jurusan")

    plt.show()

# Figure Jurusan FIA
def fig_fia():
    plt.figure("Fakultas Ilmu Alam (FIA)")
    jurusan = ['Biologi', 'Fisika', 'Kimia']
    jml_bio = int(data_jurusan('fia', 'Biologi'))
    jml_fis = int(data_jurusan('fia', 'Fisika'))
    jml_kimia = int(data_jurusan('fia', 'Kimia'))
    jml_jurusan = [jml_bio, jml_fis, jml_kimia]

    print("Biologi = " + str(jml_bio))
    print("Fisika = " + str(jml_fis))
    print("Kimia = " + str(jml_kimia))

    plt.bar(jurusan, jml_jurusan)
    plt.xlabel('Jurusan', fontsize=8)
    plt.ylabel('Jumlah Dosen', fontsize=8)
    plt.title("Jumlah Dosen FIA yang Mengakses ShareITS berdasarkan Jurusan")

    plt.show()

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
================================================================= GRAFIK DATA MAHAHSISWA =================================================================
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# Figure Fakultas
def fig_fk_mhs():
    plt.figure(1)
    fakultas = ['FTK', 'FTSLK', 'FTI', 'FIA', 'FTIK']
    jml_ftk = data_fk_mhs('ftk')
    jml_ftslk = data_fk_mhs('ftslk')
    jml_fti = data_fk_mhs('fti')
    jml_fia = data_fk_mhs('fia')
    jml_ftik = data_fk_mhs('ftik')
    jml_fakultas = [jml_ftk, jml_ftslk, jml_fti, jml_fia, jml_ftik]

    print("FTK = " + str(jml_ftk))
    print("FTSLK = " + str(jml_ftslk))
    print("FTI = " + str(jml_fti))
    print("FIA = " + str(jml_fia))
    print("FTIK = " + str(jml_ftik))

    plt.bar(fakultas, jml_fakultas)
    plt.xlabel('Fakultas', fontsize=8)
    plt.ylabel('Jumlah Mahasiswa', fontsize=8)
    plt.title("Jumlah Mahasiswa yang Mengakses ShareITS berdasarkan Fakultas")

    plt.show()


# Figure Jurusan FTIK
def fig_ftik_mhs():
    plt.figure("Fakultas Teknologi Informasi dan Komunikasi (FTIK)")
    jurusan = ['Sistem Informasi', 'Informatika']
    jml_si = int(data_jurusan_mhs('ftik', 'Sistem Informasi'))
    jml_infor = int(data_jurusan_mhs('ftik', 'Informatika'))
    jml_jurusan = [jml_si, jml_infor]

    print("Sistem Informasi = " + str(jml_si))
    print("Informatika = " + str(jml_infor))

    plt.bar(jurusan, jml_jurusan)
    plt.xlabel('Jurusan', fontsize=8)
    plt.ylabel('Jumlah Mahasiswa', fontsize=8)
    plt.title("Jumlah Mahasiswa FTIK yang Mengakses ShareITS berdasarkan Jurusan")

    plt.show()


# Figure Jurusan FTK
def fig_ftk_mhs():
    plt.figure("Fakultas Teknik Kelautan (FTK)")
    jurusan = ['Teknik Kelautan', 'Teknik Perkapalan', 'Teknik Sistem Perkapalan']
    jml_tk = int(data_jurusan_mhs('ftk', 'Teknik Kelautan'))
    jml_tp = int(data_jurusan_mhs('ftk', 'Teknik Perkapalan'))
    jml_tsp = int(data_jurusan_mhs('ftk', 'Teknik Sistem Perkapalan'))
    jml_jurusan = [jml_tk, jml_tp, jml_tsp]

    print("Teknik Kelautan = " + str(jml_tk))
    print("Teknik Perkapalan = " + str(jml_tp))
    print("Teknik Sistem Perkapalan = " + str(jml_tsp))

    plt.bar(jurusan, jml_jurusan)
    plt.xlabel('Jurusan', fontsize=8)
    plt.ylabel('Jumlah Mahasiswa', fontsize=8)
    plt.title("Jumlah Mahasiswa FTK yang Mengakses ShareITS berdasarkan Jurusan")

    plt.show()


# Figure Jurusan FTSLK
def fig_ftslk_mhs():
    plt.figure("Fakultas Teknik Sipil, Lingkungan, dan Kebumian (FTSLK)")
    jurusan = ['Teknik Geomatika', 'Teknik Sipil', 'Teknik Lingkungan', 'Teknik Geofisika']
    jml_tgm = int(data_jurusan_mhs('ftslk', 'Teknik Geomatika'))
    jml_ts = int(data_jurusan_mhs('ftslk', 'Teknik Sipil'))
    jml_tl = int(data_jurusan_mhs('ftslk', 'Teknik Lingkungan'))
    jml_tgs = int(data_jurusan_mhs('ftslk', 'Teknik Geofisika'))
    jml_jurusan = [jml_tgm, jml_ts, jml_tl, jml_tgs]

    print("Teknik Geomatika = " + str(jml_tgm))
    print("Teknik Sipil = " + str(jml_ts))
    print("Teknik Lingkungan = " + str(jml_tl))
    print("Teknik Geofisika = " + str(jml_tgs))

    plt.bar(jurusan, jml_jurusan)
    plt.xlabel('Jurusan', fontsize=8)
    plt.ylabel('Jumlah Mahasiswa', fontsize=8)
    plt.title("Jumlah Mahasiswa FTSLK yang Mengakses ShareITS berdasarkan Jurusan")

    plt.show()


# Figure Jurusan FTI
def fig_fti_mhs():
    plt.figure("Fakultas Teknik Industri (FTI)")
    jurusan = ['Teknik Material dan Metalurgi', 'Teknik Industri', 'Teknik Fisika', 'Teknik Kimia', 'Teknik Mesin']
    jml_tmm = int(data_jurusan_mhs('fti', 'Teknik Material dan Metalurgi'))
    jml_ti = int(data_jurusan_mhs('fti', 'Teknik Industri'))
    jml_tf = int(data_jurusan_mhs('fti', 'Teknik Fisika'))
    jml_tk = int(data_jurusan_mhs('fti', 'Teknik Kimia'))
    jml_tm = int(data_jurusan_mhs('fti', 'Teknik Mesin'))
    jml_jurusan = [jml_tmm, jml_ti, jml_tf, jml_tk, jml_tm]

    print("Teknik Material dan Metalurgi = " + str(jml_tmm))
    print("Teknik Industri = " + str(jml_ti))
    print("Teknik Fisika = " + str(jml_tf))
    print("Teknik Kimia = " + str(jml_tk))
    print("Teknik Mesin = " + str(jml_tm))

    plt.bar(jurusan, jml_jurusan)
    plt.xlabel('Jurusan', fontsize=8)
    plt.ylabel('Jumlah Mahasiswa', fontsize=8)
    plt.title("Jumlah Mahasiswa FTI yang Mengakses ShareITS berdasarkan Jurusan")

    plt.show()


# Figure Jurusan FIA
def fig_fia_mhs():
    plt.figure("Fakultas Ilmu Alam (FIA)")
    jurusan = ['Biologi', 'Fisika', 'Kimia']
    jml_bio = int(data_jurusan_mhs('fia', 'Biologi'))
    jml_fis = int(data_jurusan_mhs('fia', 'Fisika'))
    jml_kimia = int(data_jurusan_mhs('fia', 'Kimia'))
    jml_jurusan = [jml_bio, jml_fis, jml_kimia]

    print("Biologi = " + str(jml_bio))
    print("Fisika = " + str(jml_fis))
    print("Kimia = " + str(jml_kimia))

    plt.bar(jurusan, jml_jurusan)
    plt.xlabel('Jurusan', fontsize=8)
    plt.ylabel('Jumlah Mahasiswa', fontsize=8)
    plt.title("Jumlah Mahasiswa FIA yang Mengakses ShareITS berdasarkan Jurusan")

    plt.show()

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
======================================================================= GRAFIK DATA COMBINE ===============================================================
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def fig_compare_fk():
    plt.figure("Perbandingan Dosen dan Freq Mahasiswa yang Mengakses ShareITS")
    dsn_ftk = data_fk('ftk')
    dsn_ftslk = data_fk('ftslk')
    dsn_fti = data_fk('fti')
    dsn_fia = data_fk('fia')
    dsn_ftik = data_fk('ftik')
    mhs_ftk = data_fk_mhs('ftk')
    mhs_ftslk = data_fk_mhs('ftslk')
    mhs_fti = data_fk_mhs('fti')
    mhs_fia = data_fk_mhs('fia')
    mhs_ftik = data_fk_mhs('ftik')
    n_groups = 5
    dosen = (dsn_ftk, dsn_ftslk, dsn_fti, dsn_fia, dsn_ftik)
    mahasiswa = (mhs_ftk, mhs_ftslk, mhs_fti, mhs_fia, mhs_ftik)

    n_dsn = dsn_ftk + dsn_ftslk + dsn_fti + dsn_fia + dsn_ftik
    n_mhs = mhs_ftk + mhs_ftslk + mhs_fti + mhs_fia + mhs_ftik
    freq_ftk = round(mhs_ftk/dsn_ftk, 0)
    freq_ftslk = round(mhs_ftslk/dsn_ftslk, 0)
    freq_fti = round(mhs_fti/dsn_fti, 0)
    freq_fia = round(mhs_fia/dsn_fia, 0)
    freq_ftik = round(mhs_ftik/dsn_ftik, 0)
    freq_mhs = (freq_ftk, freq_ftslk, freq_fti, freq_fia, freq_ftik)

    # create plot
    index = np.arange(n_groups)
    bar_width = 0.35
    opacity = 0.8

    print("Dosen FTK = " + str(dsn_ftk))
    print("Mahasiswa FTK = " + str(freq_ftk))
    print("Dosen FTSLK = " + str(dsn_ftslk))
    print("Mahasiswa FTSLK = " + str(freq_ftslk))
    print("Dosen FTI = " + str(dsn_fti))
    print("Mahasiswa FTI = " + str(freq_fti))
    print("Dosen FIA = " + str(dsn_fia))
    print("Mahasiswa FIA = " + str(freq_fia))
    print("Dosen FTIK = " + str(dsn_ftik))
    print("Mahasiswa FTIK = " + str(freq_ftik))

    bar_dsn = plt.bar(index, dosen, bar_width,
                     alpha=opacity,
                     color='b',
                     label='Dosen')

    bar_mhs = plt.bar(index + bar_width, freq_mhs, bar_width,
                     alpha=opacity,
                     color='r',
                     label='Freq Mahasiswa')

    plt.xlabel('Fakultas')
    plt.ylabel('Jumlah Pengakses')
    plt.title('Perbandingan Dosen dan Freq Mahasiswa yang Mengakses Share ITS')
    plt.xticks(index + bar_width, ('FTK', 'FTSLK', 'FTI', 'FIA', 'FTIK'))
    plt.legend()

    plt.tight_layout()
    plt.show()

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
======================================================================== EXECUTION ========================================================================
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# EXECUTION START
conn = pyodbc.connect("Driver={SQL Server};"
                      "Server=AVIV-PC;"
                      "Database=datashareits;"
                      "Trusted_Connection=yes;")

fig_compare_fk()