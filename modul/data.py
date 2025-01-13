class orang:
    def __init__(self,nama,waktu,gaji):
        self.nama=nama
        self.waktu=waktu
        self.gaji=gaji
        
class inputa:
    def valid(pr):
        while True:
            try:
                v=float(input(pr))
                if v>0:return v
                else:print('masukin lebih dari nol')
            except ValueError:print('inputnya harus angka')
            
    def kolek():
        nama=input('masuan nama: ')
        gaji=inputa.valid('berapa gaji: ')
        waktu=inputa.valid('berapa lama ia bekerja? ')
        return orang(nama,gaji,waktu)
    