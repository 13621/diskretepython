from operator import truediv
from typing import List
from euklid import euklidalgos

alphabet = list("abcdefghijklmnopqrstuvwxyz".upper())
alphabet_mit_leerzeichen_vorne = list(" abcdefghijklmnopqrstuvwxyz".upper())

class symmetric:
    # a = 0, b = 1 usw.
    def caesar(message: str, shift: int, prnt: bool = True) -> str:
        result = []
        for c in list(message.upper()):
            if c == ' ':
                result.append(c)
                continue
            c_number = ord(c) - 65
            enc_number = (c_number + shift) % 26
            enc_char = alphabet[enc_number]
            result.append(enc_char)
            if prnt:
                print(f"{c} ({c_number}) + {shift} => {enc_number} ({enc_char})")
        
        return ''.join(result)
        # print(''.join(result))

    def vigenere(message: str, key: str, prnt: bool = True) -> str:
        # result len = msg len
        # A: 65, Z: 90
        result = []
        for i, c in enumerate(list(message.upper())):
            msg_number = ord(c) - 65
            key_c = list(key.upper())[i % len(key)]
            key_c_number = ord(key_c) - 65
            result.append(alphabet[((msg_number + key_c_number) % 26)])
            if prnt:
                print(f"Nachrichtenbuchstabe: {c}({msg_number}), Schlüsselbuchstabe: {key_c}({key_c_number}), Ergebnis: {alphabet[((msg_number + key_c_number) % 26)]}({(msg_number + key_c_number) % 26})")
        # print(''.join(result))
        return ''.join(result)

    def enumalphabet():
        for i, c in enumerate(alphabet):
            print(f"{i}:{c}")

    def message_to_numbers(message: str, prnt: bool = True) -> List[int]:
        lis = []
        for c in list(message.upper()):
            if prnt:
                print(f"'{c}' -> {ord(c) - 65}")
            lis.append(ord(c) - 65)
        return lis

class rsa:
    # [leerzeichen] = 0, a = 1, b = 2 usw.
    def find_e(e_guess: int, rsamodul_euler: int) -> int:
        for i in range(e_guess-2, rsamodul_euler):
            if (euklidalgos.euklid(i, rsamodul_euler) == 1):
                return i
        raise Exception(f"Kein e gefunden für {e_guess}")

    def publickey(prime1: int, prime2: int, e: int, prnt: bool = True):
        rsamodul = prime1 * prime2
        rsamodul_euler = (prime1 - 1) * (prime2 - 1) #geht nur weil beide primzahlen sind
        assert(rsamodul_euler == rsa.eulerschephi(prime1*prime2))

        #ggt(e, euler)
        if(euklidalgos.euklid(e, rsamodul_euler) != 1) and (e < rsamodul_euler):
            #suchen
            print(f"{e} kommt als Schlüssel nicht infrage, weil entweder e größer als eulerschephi(N) ist oder ggT(e, eulerschephi(N)) != 1 bzw. ggt({e}, {rsamodul_euler}) = {euklidalgos.euklid(e, rsamodul_euler)} Suche neues e...")
            e = rsa.find_e(e, rsamodul_euler)
        elif prnt:
            print(f"{e} passt, weil ggT(e, eulerschephi(N) = ggT({e}, {rsamodul_euler} = 1 und e < eulerschephi(N)")
        if prnt:
            print(f"Öffentlicher Schlüssel ist: e = {e}, N = {prime1}*{prime2} = {rsamodul}")
        return e, rsamodul

    def privatekey(prime1: int, prime2: int, e: int, prnt: bool = True):
        rsamodul = prime1 * prime2
        rsamodul_euler = (prime1 - 1) * (prime2 - 1) #geht nur weil beide primzahlen sind
        assert(rsamodul_euler == rsa.eulerschephi(prime1*prime2))

        if(euklidalgos.euklid(e, rsamodul_euler) != 1):
            #suchen
            e = rsa.find_e(e, rsamodul_euler)
            print(f"Setze e auf {e}")

        d, s, t = euklidalgos.erweuklid(e, rsamodul_euler, prnt)
        if prnt:
            print(f"erweiterter euklid liefert: {s}")
        if s < 0:
            s = rsamodul_euler + s
        if prnt:
            print(f"Private key gefunden, d = {s}, N = {prime1}*{prime2} = {rsamodul}")
        return(s, rsamodul)

    def chiffrieren(message: str, e: int, N: int, prnt: bool = True):
        # ci = mi**e % N
        chiffrat = []
        # for m in list(message.upper()):
        for i in range(0, len(message), 2):
            m = message[i]
            m_next = message[i+1]
            m_number = alphabet_mit_leerzeichen_vorne.index(m)
            if m_number < 10:
                m_number = f"0{m_number}"
            m_next_number = alphabet_mit_leerzeichen_vorne.index(m_next)
            if m_next_number < 10:
                m_next_number = f"0{m_next_number}"
            block = int(f"{m_number}{m_next_number}")
            
            if prnt:
                print(f"{m} ({m_number}) und {m_next} ({m_next_number}) = {block} => {block}**{e} (mod {N}) = {(block**e) % N}")
                # print(f"{block}**{e} mod {N} = {(block**e) % N}")
            chiffrat.append((block**e) % N)
        return chiffrat

    def dechiffrieren(message: List[int], d: int, N: int, prnt: bool = True):
        # mi = ci**d % N
        dechif = []
        for m in message:
            m_dechif = (m**d) % N
            if prnt:
                print(f"{m}**{d} (mod {N}) = {m_dechif}")
            m_dechif_string = f"{m_dechif}"
            if m_dechif < 1000:
                m_dechif_string = f"0{m_dechif}"
            if m_dechif < 100:
                m_dechif_string = f"00{m_dechif}"
            if m_dechif < 10:
                m_dechif_string = f"000{m_dechif}"
            if m_dechif == 0:
                m_dechif_string = "0000"

            if prnt:
                print(f"{m_dechif_string}: {m_dechif_string[:2]}, {m_dechif_string[2:]}")

            links = int(m_dechif_string[:2])
            rechts = int(m_dechif_string[2:])

            dechif.append(alphabet_mit_leerzeichen_vorne[links % 27])
            dechif.append(alphabet_mit_leerzeichen_vorne[rechts % 27])

        return "".join(dechif)

    def prime_factors(n):
        i = 2
        factors = []
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.append(i)
        if n > 1:
            factors.append(n)
        return factors

    def eulerschephi(N: int, prnt: bool = False):
        produkt_result = 1
        primfaktoren = list(set(rsa.prime_factors(N)))
        # print(primfaktoren)
        for p in primfaktoren:
            produkt_result *= (1-(1/p))

        if prnt:
            print(f"Primfaktoren von {N} sind {primfaktoren}, deswegen ist eul({N})={N*produkt_result}")
        return N*produkt_result

    def message_to_numbers(message: str, prnt: bool = True) -> List[int]:
        lis = []
        for c in list(message.upper()):
            lis.append(alphabet_mit_leerzeichen_vorne.index(c))
            if prnt:
                print(f"{c} -> {alphabet_mit_leerzeichen_vorne.index(c)}")

        return lis
        

# print(symmetric.vigenere('fliege', 'ruby'))
# print(symmetric.vigenere('URHEBERRECHTSVERLETZUNG', 'ruby'))

# print(symmetric.caesar('MILA HAT LIMO', 21))

# print(symmetric.vigenere('linsen', 'carlos', True))

# print(f"public key ist:{rsa.publickey(41, 131, 21)}")

# print(f"private key ist: {rsa.privatekey(41, 131, 21)}")

# print(rsa.chiffrieren("LADEKLAPPE", 21, 5371, True))

# print(rsa.privatekey(73, 163, 15))
# print(rsa.dechiffrieren([1423,2684,3096,679,1035,1832,1636], 223, 4141))