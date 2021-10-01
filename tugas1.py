class Ekosistem :
    def intro (self):
        print("===Ekosistem laut adalah ekosistem yang terdapat di peraoran laut tempat terjadinya interksi makhluk hidup dan memiliki banyak manfaat. Ekosistem laut ada 3, yaitu: Mangrove, Lamun, dan terumbu karang===")

    def Karakter(self):
        print("===Keberadaan ekosistem-ekosistem ini memiliki banyak manfaat. Seperti menjadi tempat hidup dan mencari makan biota laut didalamnya. Disamping itu juga mempunyai fungsi sebagai pelindung pantai dari gelombang dan abrasi.===")

class Mangrove(Ekosistem):
    def Karakter(self):
        print("===Ekosistem Mangrove/hutan mangrove merupakan komunitas vegetasi pantai tropis dan sub tropis, yang didominasi oleh beberapa jenis pohon mangrove yang mampu tumbuh dan berkembang pada daerah pasang surut pantai berlumpur. Formasi mangrove merupakan perpaduan antara daratan dan lautan. Mangrove tergantung pada air laut(pasang) dan air tawar sebagai sumber makanannya serta endapan debu(silt) dari erosi daerah hulu sebagai bahan pendukung substratnya.===")

class Lamun(Ekosistem):
    def Karakter(self):
        print("===Lamun merupakan istilah untuk rumput laut(sea grass), harus dibedakan dengan rumput laut(sea weed) yang merupakan anggota dari kelompok vegetasi yang dikenal sebagai alga(ganggang). Sea weed ini biasanya dapat ditemui di perairan yang berasosiasi dengan keberadaan ekosistem terumbu karang. Sedangkan lamun merupakan tumbuhan berbunga(angiospermae) yang hidup di perairan pesisir/pantai laut, membentuk ekosistem penting sebagai produsen primer di perairan laut tropis selain fitoplankton.===")

class TerumbuKarang(Ekosistem):
    def Karakter(self):
        print("Terumbu karang adalah ekosistem di dasar laut yang penghuni utamanya sejenis binatang berongga penghasil kapur yang dikenal dengan nama karang batu(stony coral). Karang batu yang bentuk koloninya beraneka ragam ini merupakan substrat dasar terumbu karang yang sangat keras dan berfungsi sebagai rumah/tempat tinggal, tempat berlindung tempat mencari makan dan tempat memijah bagi berbagai macam jenis biota.")

obj_Ekosistem = Ekosistem()
obj_Mangrove = Mangrove()
obj_Lamun = Lamun()
obj_TerumbuKarang = TerumbuKarang()

print("-------------------------------")
print("\n")
obj_Ekosistem.intro()
obj_Ekosistem.Karakter()
print("\n")
print("-------------------------------")
print("\n")
obj_Mangrove.intro()
obj_Mangrove.Karakter()
print("\n")
print("-------------------------------")
print("\n")
obj_Lamun.intro()
obj_Lamun.Karakter()
print("\n")
print("------------------------------")
print("\n")
obj_TerumbuKarang.intro()
obj_TerumbuKarang.Karakter()
print("\n")
print("------------------------------")