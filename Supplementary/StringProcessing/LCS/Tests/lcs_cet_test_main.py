from Supplementary.StringProcessing.LCS.lcs_cet import *

if __name__ == "__main__":
    pairs = [
        ("ABCBDAB", "BDCAB"),               # BDAB (n=4)
        ("GTTCCTAATA", "CGATAATTGAGA"),     # GTTTAA (6)
        ("GTTCCTAAT", "CGATAATTGAG"),       # GTTTA (5)
        ("12345", "23415"),                 # 2345 (4)
        ("123", "1323"),                    # 123 (3)
        ("126548", "216544"),               # 2654 (4)
        ("AGGTAB", "GXTXAYB"),              # GTAB (4)
        ("BD", "ABCD"),                     # BD (2)
        ("ABCDGH", "AEDFHR"),               # ADH (3)
        ("ABCDE", "ACE"),                   # ACE (3)
        ( "hofubmnylkra", "pqhgxgdofcvmr"), # hofmr (5)
        ("oxcpqrsvwf", "shmtulqrypy"),      # qr (2) @TODO: Bug-fixing in progress
        ("ABC", "DEF"),                     # ∅ (0)
    ]
    for p in pairs:
        # print(f"LCS{p} = ", TP_LCS(*p))
        cet = CET_LCS(*p)
        r1 = cet[0]
        r2 = []
        for q in cet[1]: r2.append([q.popleft() for e in range(len(q))])
        print(f"{p}\n{r1}\n{r2}\n")
