import hashlib
import csv
class Prihlaseni():
    """
    Přihlášní do Systoomu \n
    Pro aktivaci je tu funkce run \n
    Výce info o ní najdete v jejím popisu
    """
    def hashfun(self, heslo:str, jmeno:str) ->str:
        for i in range(1000000):
            jmeno = hashlib.sha512(jmeno.encode()).hexdigest()    
            heslo = hashlib.sha512(heslo.encode()).hexdigest()
            heslo = str(heslo) + str(jmeno) + str(i) + str(i**2) 
        return heslo
    def run(self, output:int):
        """
        Funkce pro spuštění přihlašování se vstupem 1 nebo 0(nebo cokolv jiného)\n
        1: výstup jméno přihlášeného \n
        0: bez výstupu
        """
        spravne_udaje = True
        while spravne_udaje:
            spravne_udaje = False
            uzivatelske_jmeno =  input("Výtejte v Systoom .Zadejte uživatelské jméno nebo \'RT\' pro registraci ")
            if uzivatelske_jmeno == "RT":
                self.registrace()
                spravne_udaje = True
            else:
                heslo = input("Zadejte svoje heslo: ")
                if self.sprvavne_udaje(uzivatelske_jmeno, heslo):
                    print(f"Uživatel {uzivatelske_jmeno} se přihlásil ůspěšně")
                    if output == 1:
                        return uzivatelske_jmeno
                else:
                    print("Zadali jste špatné jméno nebo heslo")
                    spravne_udaje = True
    def sprvavne_udaje(self,jmeno:str, heslo:str) -> bool:
                if self.uzivatelexistuje(jmeno):
                    heslo_hash = self.hashfun(heslo, jmeno) 
                    with open("uzivatele.csv", "r", encoding="utf-8") as f:
                        ctecka = (radek for radek in csv.reader(f) if radek)
                        next(ctecka, None)  
                        for radek in ctecka:
                            if radek[0] == jmeno and radek[1] == heslo_hash:
                                return True
                        return False
                else:
                    return False


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
                heslo = input("Zadejte svoje budoucí heslo: ")
                heslo_hash = self.hashfun(heslo, nuzivatel) 
                with open("uzivatele.csv", "a", encoding="utf-8", newline='') as f:
                    zapisovac = csv.writer(f)
                    zapisovac.writerow( [nuzivatel,heslo_hash])

    def uzivatelexistuje(self, jmeno_uzivatele : str) -> bool:
        with open("uzivatele.csv", "r", encoding="utf-8") as f:
            cteni = csv.reader(f)
            for radek in cteni:
                if radek and radek[0] == jmeno_uzivatele:
                    return True
        return False
