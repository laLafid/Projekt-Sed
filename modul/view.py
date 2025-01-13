from tabulate import tabulate as t
class kacheww:
    def tabel(data):
        head=("No","Nama","Shift","Upah","Total Gaji")
        isi=[[i+1,d.nama,d.waktu,f'Rp{d.gaji}',f'Rp{d.gaji*d.waktu}']for i, d in enumerate(data)]
        print(t(isi,headers=head,tablefmt="grid"))