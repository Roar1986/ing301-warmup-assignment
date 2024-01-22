from pathlib import Path


# Dette er start-koden til den første programmeringsoppgave i ING 301
#
# Du skal utvikle et programm som finner det hyppigste ordet i en gitt tekstfil.
# Dette høres kanskje litt komplisiert ut, men fortvil ikke!
# Vi har forberedt den grove strukturen allerede. Din oppgave er å implementere
# noen enkelte funskjoner som trengs for det hele til å virke.
# Enhver funksjon kommer med en dokumentasjon som forklarer hva skal gjøres.


def read_file(file_name):

    
    """
    Denne koden opner ei fil, og les den linje for linje og lagrer den linje for linje i ei fil.
    fil_innhald[0] lagrer då første linja i index 0, neste linje i index 1 osv
    """
    with open(file_name, "r", encoding="utf-8") as file:
        fil_innhald = file.readlines()
    
    # Tips: kanksje "open"-funksjonen kunne være nyttig her: https://docs.python.org/3/library/functions.html#open
    return fil_innhald  # TODO: Du må erstatte denne linjen

def lines_to_words(lines):

    charsToStrip = ["!","?",":",";",".",",","\n"]
    
    # Tom liste, klar til å fylles
    listeMedOrd = []

    # bruker str.maketrans for å fjerne uønska karakterer som er med i ordet.
    tegnFjernest = str.maketrans('','',"!?.,:;")
    
    # Loop for å køyre gjennom kvar streng i den inisielle lista.
    for line in lines:
        # tar vekk \n fra enden av kvar index
        stripped_line = line.strip()
        # splitter til ord, basert på mellomrom
        alleOrd = stripped_line.split()
        # Leger til kvart ord i den nye lista
        for kvartOrd in alleOrd:
            # Fjerner tegn frå kvart ord.
            ordUtanTegn = kvartOrd.translate(tegnFjernest) 
            # Liste med ord utan tegn
            listeMedOrd.append(ordUtanTegn)

    # Tips: se på "split()"-funksjonen https://docs.python.org/3/library/stdtypes.html#str.split
    # i tillegg kan "strip()": https://docs.python.org/3/library/stdtypes.html#str.strip
    # og "lower()": https://docs.python.org/3/library/stdtypes.html#str.lower være nyttig
    return listeMedOrd  # TODO: Du må erstatte denne linjen


def compute_frequency(words):

    # Oppretter ei ordbok for å lagre forekomstene av orda.
    frekvens_tabell = {}
    
    for ord in words:
        # Logikk for å sjekke antall ord
        if ord in frekvens_tabell:
            frekvens_tabell[ord] += 1
        else:
            frekvens_tabell[ord] = 1
    
    #utskrift til test
    #for ord, antall in frekvens_tabell.items():
    #    print(f"'{ord}': {antall} gang(er)")


    return frekvens_tabell  


FILL_WORDS = ['og', 'dei', 'i', 'eg', 'som', 'det', 'han', 'til', 'skal', 'på', 'for', 'då', 'ikkje', 'var', 'vera']


def remove_filler_words(frequency_table):

    # oppretter ei liste, som ikkje innheld ord som ligg i FILL_WORDS
    frekvensTabell = [ord for ord in frequency_table if ord not in FILL_WORDS]
    print(frekvensTabell)

    return frekvensTabell  


def largest_pair(par_1, par_2):

    # OBS: Tenk også på situasjonen når to tall er lik! Vurder hvordan du vil handtere denne situasjonen
    # kanskje du vil skrive noen flere test metoder ?!

    # Første ord har største heiltall
    if par_1[1] > par_2[1]:
        return par_1
    # Begge ord har like store heiltall, returer begge
    if par_1[1] == par_2[1]:
        return par_1 + par_2
    # Andre ord er størst
    else:
        return par_2
    

def find_most_frequent(frequency_table):
    

    max_freq = -1  # Initialiserer til et tall lavere enn noen forventet frekvens
    max_freq_word = None
    
    for word, freq in frequency_table.items():
        print(word,freq)
        if freq > max_freq:
            max_freq = freq
            max_freq_word = word
    
    # Sjekker om vi faktisk har funnet et ord (i tilfelle tabellen ikke var tom)
    if max_freq_word is not None:
        return (max_freq_word, max_freq)
    else:
        return None



    """
    Nå er det på tide å sette sammen alle bitene du har laget.
    Den funksjonen får frekvenstabllen som innputt og finner det ordet som dykket opp flest.
    """
    # Tips: se på "dict.items()" funksjonen (https://docs.python.org/3/library/stdtypes.html#dict.items)
    # og kanskje du kan gjenbruke den "largest_pair" metoden som du nettopp har laget
    return NotImplemented  # TODO: Du må erstatte denne linjen

"""Kode del 1"""
filsti = "C:\\ING301\\ing301warmUpAssignment\\ing301-warmup-assignment\\tests\\voluspaa.txt"
filInnhold = read_file(filsti)

print("\nDeloppgåve 1: skriver ut fil i liste form")
print(filInnhold)


"""Kode del 2"""
listeMedOrd = lines_to_words(filInnhold)
print("\nDeloppgåve 2: Deler liste opp i ord, og fjerner uønska tegn")
print(listeMedOrd)

"""Kode del 3"""
frekvenstabell = compute_frequency(listeMedOrd)
print("\nDeloppgåve 3: Printer ut frekvenstabell")
print(frekvenstabell)


"""Kode del 4"""
frekvensTabellUtanFyll = remove_filler_words(frekvenstabell)
print("\nDeloppgåve 4: Skriv ut frekvenstabell utan fyll ord")
print(frekvensTabellUtanFyll)

"""Kode del 5"""
førstePar = ("GammalOst",5)
AndrePar = ("Sveits",5)
print("\nDeloppgåve 5: Finner det paret med størst heiltall")
størsteTall = largest_pair((førstePar),(AndrePar))
print(størsteTall)

"""Kode del 6"""
mestFrekventeOrd = find_most_frequent(frekvenstabell)
if mestFrekventeOrd:
    print(f"Det mest frekvente ordet er: {mestFrekventeOrd[0]} med en frekvens på {mestFrekventeOrd[1]}")
else:
    print("Frekvenstabellen er tom.")

############################################################
#                                                          #
# Her slutter dendelen av filen som er relevant for deg ;-)#
#                                                          #
############################################################


def main():
    file = str(Path(__file__).parent.absolute()) + "/voluspaa.txt"
    lines = read_file(file)
    words = lines_to_words(lines)
    table = compute_frequency(words)
    table = remove_filler_words(table)
    most_frequent = find_most_frequent(table)
    print(f"The most frequent word in {file} is '{most_frequent}'")


if __name__ == '__main__':
    main()
