#### Fonction secondaire
def ispalindrome(p):
    p = p.lower()
    return p == p[::-1]

#### Fonction principale
def main():
    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie", "test"]:
        print(f"{s} : {ispalindrome(s)}")

if __name__ == "__main__":
    main()
