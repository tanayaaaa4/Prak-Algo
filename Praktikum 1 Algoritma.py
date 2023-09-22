print("hitung luas ruang")
panjang = int(input("masukan panjang ruangan :"))
lebar = int(input("masukan lebar ruangan :"))
satuan = str(input("masukan satuan (meter/inci) :"))
hasil = panjang * lebar
if satuan == "meter" : 
    print("luas ruangan dengan panjang", panjang, "dan lebar", "adalah", hasil, satuan)
elif satuan == "inci" :
    print("luas ruangan dengan panjang", panjang, "dan lebar", lebar, "adal", hasil,  satuan)
else: 
    print("input salah")
