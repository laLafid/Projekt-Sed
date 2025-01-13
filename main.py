from modul.data import inputa
from modul.view import kacheww
def main():
    print("="*5+"Kalkulator slip gaji"+"="*5)
    data=[]
    while True:
        minta=inputa.kolek()
        data.append(minta)
        lagi=input('apakah masih ada lagi? ')
        if lagi != 'y':
            break
        
    print("Tabel Pekerja")
    kacheww.tabel(data)
        
main()