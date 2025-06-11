from prihlaseni import Prihlaseni
from update import Update
if __name__ == "__main__":
    p = Prihlaseni()
    uzivatel = p.run(1)
    if input("chcete stáhnout nejnovější verzi systoomu?[a/n]") == "a":
        u = Update()
        u.update()
