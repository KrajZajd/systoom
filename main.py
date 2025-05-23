import hashlib
import csv
class Prihlaseni():
    def run(self):
        self.uzivatelske_jmeno =  input("Výtejte v Systoom .Zadejte uživatelské jméno nebo \'RT\' pro registraci ")
        if self.uzivatelske_jmeno == "RT":
            self.registrace()
        else:
            print("Zatím je systoom ve vývojové verzy. Pravidelně kontrolujte nové verze pro zpřístupnění této a mnoho dalších funkcí😀.")
    def registrace(self):
        print("Výtejte v průvodci registrací.")
        spravne_jmeno = True
        while spravne_jmeno:
            spravne_jmeno = False
            nuzivatel = input("Jak se chceš jmenovat? ")
            if self.uzivatelexistuje(nuzivatel):
                print("Uživatel byl již zaregistrován, zvolte si jiné jméno")
                spravne_jmeno = True
            else:
                self.heslo = input("Zadejte svoje budoucí heslo: ")
                self.heslo_hash = hashlib.sha256(self.heslo.encode()).hexdigest()
                with open("uzivatele.csv", "a", encoding="utf-8") as f:
                    zapisovac = csv.writer(f)
                    zapisovac.writerow([nuzivatel,self.heslo_hash])

    def uzivatelexistuje(self, jmeno_uzivatele : str) -> bool:
        
        with open("uzivatele.csv", "r", encoding="utf-8") as f:
            cteni = csv.reader(f)
            for radek in cteni:
                if radek and radek[0] == jmeno_uzivatele:
                    return True
        return False
if __name__ == "__main__":
    p = Prihlaseni()
    p.run()