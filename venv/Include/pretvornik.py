print "Hello user. Tukaj pretvarjamo enote."

while True:

    km = int(raw_input("Vnesi kilometre: "))
    milja= km*0.62137

    print "{0} km je {1} milj".format(km ,milja)

    nadaljuj = raw_input("Ponovi? (DA/NE)")
    if nadaljuj != "DA":
        print "Ne bom ponovil"
        break
    else:
        print "Bom ponovil"