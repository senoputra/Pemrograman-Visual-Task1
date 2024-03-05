class Mahasiswa:
    def __init__(self, nama_lengkap, nama_panggilan, kelas, prodi, fakultas, tempat_tinggal, asal):
        self.nama_lengkap = nama_lengkap
        self.nama_panggilan = nama_panggilan
        self.kelas = kelas
        self.prodi = prodi
        self.fakultas = fakultas
        self.tempat_tinggal = tempat_tinggal
        self.asal = asal

# Input Data Diri Kalian
senoputra = Mahasiswa("Senoaji Putra","seno","A 2021", "Pendidikan Komputer", "Keguruan dan Ilmu Pendidikan (FKIP)", "Ks.tubun dalam, gang wira tirta, rt 17", "Balikpapan"
)

# Menampilkan informasi mahasiswa
print(f"Nama Lengkap: {senoputra.nama_lengkap}")
print(f"Nama panggilan: {senoputra.nama_panggilan}")
print(f"Kelas: {senoputra.kelas}")
print(f"Prodi: {senoputra.prodi}")
print(f"Fakultas: {senoputra.fakultas}")
print(f"Tempat Tinggal: {senoputra.tempat_tinggal}")
print(f"Asal: {senoputra.asal}")

