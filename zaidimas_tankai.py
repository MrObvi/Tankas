import time
from random import randint
# judejimas=0
# ar_saudo=0

# def spausdinam():
#
#     print(f"""
#
#     [{Tankas.gridas[1]}][{Tankas.gridas[2]}][{Tankas.gridas[3]}][{Tankas.gridas[4]}] | [{Tankas.gridas[5]}][{Tankas.gridas[6]}][{Tankas.gridas[7]}][{Tankas.gridas[8]}]
#     [{Tankas.gridas[9]}][{Tankas.gridas[10]}][{Tankas.gridas[11]}][{Tankas.gridas[12]}] | [{Tankas.gridas[13]}][{Tankas.gridas[14]}][{Tankas.gridas[15]}][{Tankas.gridas[16]}]
#     [{Tankas.gridas[17]}][{Tankas.gridas[18]}][{Tankas.gridas[19]}][{Tankas.gridas[20]}] | [{Tankas.gridas[21]}][{Tankas.gridas[22]}][{Tankas.gridas[23]}][{Tankas.gridas[24]}]
#     [{Tankas.gridas[25]}][{Tankas.gridas[26]}][{Tankas.gridas[27]}][{Tankas.gridas[28]}] | [{Tankas.gridas[29]}][{Tankas.gridas[30]}][{Tankas.gridas[31]}][{Tankas.gridas[32]}]
#     ---------------------------
#     [{Tankas.gridas[33]}][{Tankas.gridas[34]}][{Tankas.gridas[35]}][{Tankas.gridas[36]}] | [{Tankas.gridas[37]}][{Tankas.gridas[38]}][{Tankas.gridas[39]}][{Tankas.gridas[40]}]
#     [{Tankas.gridas[41]}][{Tankas.gridas[42]}][{Tankas.gridas[43]}][{Tankas.gridas[44]}] | [{Tankas.gridas[45]}][{Tankas.gridas[46]}][{Tankas.gridas[47]}][{Tankas.gridas[48]}]
#     [{Tankas.gridas[49]}][{Tankas.gridas[50]}][{Tankas.gridas[51]}][{Tankas.gridas[52]}] | [{Tankas.gridas[53]}][{Tankas.gridas[54]}][{Tankas.gridas[55]}][{Tankas.gridas[56]}]
#     [{Tankas.gridas[57]}][{Tankas.gridas[58]}][{Tankas.gridas[59]}][{Tankas.gridas[60]}] | [{Tankas.gridas[61]}][{Tankas.gridas[62]}][{Tankas.gridas[63]}][{Tankas.gridas[64]}]
#
#     """)

def spausdinam():

    print(f"""

    [{gridas[1]}][{gridas[2]}][{gridas[3]}][{gridas[4]}] | [{gridas[5]}][{gridas[6]}][{gridas[7]}][{gridas[8]}]
    [{gridas[9]}][{gridas[10]}][{gridas[11]}][{gridas[12]}] | [{gridas[13]}][{gridas[14]}][{gridas[15]}][{gridas[16]}]
    [{gridas[17]}][{gridas[18]}][{gridas[19]}][{gridas[20]}] | [{gridas[21]}][{gridas[22]}][{gridas[23]}][{gridas[24]}]
    [{gridas[25]}][{gridas[26]}][{gridas[27]}][{gridas[28]}] | [{gridas[29]}][{gridas[30]}][{gridas[31]}][{gridas[32]}]
    ---------------------------
    [{gridas[33]}][{gridas[34]}][{gridas[35]}][{gridas[36]}] | [{gridas[37]}][{gridas[38]}][{gridas[39]}][{gridas[40]}]
    [{gridas[41]}][{gridas[42]}][{gridas[43]}][{gridas[44]}] | [{gridas[45]}][{gridas[46]}][{gridas[47]}][{gridas[48]}]
    [{gridas[49]}][{gridas[50]}][{gridas[51]}][{gridas[52]}] | [{gridas[53]}][{gridas[54]}][{gridas[55]}][{gridas[56]}]
    [{gridas[57]}][{gridas[58]}][{gridas[59]}][{gridas[60]}] | [{gridas[61]}][{gridas[62]}][{gridas[63]}][{gridas[64]}]

    """)
gridas = ["_", "→", "_", "_", "_", "_", "_", "_", "_",
          "_", "_", "_", "_", "_", "_", "_", "_",
          "_", "_", "_", "_", "_", "_", "_", "_",
          "_", "_", "_", "_", "_", "_", "_", "_",
          "_", "_", "_", "_", "_", "_", "_", "_",
          "_", "_", "_", "_", "_", "_", "_", "_",
          "_", "_", "_", "_", "_", "_", "_", "_",
          "_", "_", "_", "_", "_", "_", "_", "_"]

def generatorius(iteravimui, objektas):
    # result = []
    for index, elem in enumerate(iteravimui):
        if elem == objektas:
            yield index
idxs = generatorius(gridas, "_")
visi=list(idxs)
print(visi)

# def valom():
#     for valom in gridas[1:10]:
#         if valom == "→":
#             continue
#         gridas[gridas.index(valom)] = "_"
#
#     spausdinam()
# valom()

suviai_i_virsu=[]
suviai_i_apacia=[]
suviai_i_desine=[]
suviai_i_kaire=[]

class Tankas:
    # def __init__(self,judejimas,ar_saudo):
    #     self.judejimas = judejimas
    #     self.ar_saudo = ar_saudo

    # gridas=[0,1, 2, 3, 4, 5, 6, 7, 8,
    #           9, 10,11,12,13,14,15,16,
    #           17,18,19,20,21,22,23,24,
    #           25,26,27,28,29,30,31,32,
    #           33,34,35,36,37,38,39,40,
    #           41,42,43,44,45,46,47,48,
    #           49,50,51,52,53,54,55,56,
    #           57,58,59,60,61,62,63,64]
    # Rodykles  → ← ↑ ↓



    def virsun(self):
        # print (f"Juda virsun{gridas[1:9]}")
        for elementas in gridas[1:9]:
            if elementas == "↑" or elementas == "↓" or elementas == "←" or elementas == "→":
                print("negalymas ejimas")
                continue

        # if gridas[1] == "→" or gridas[2] == "→" or gridas[3] == "→" or gridas[4] == "→" or gridas[5] == "→" or gridas[6] == "→" or gridas[7] == "→" or gridas[8] == "→":
        #     print("negalymas ejimas")

        #IS ANTROS I PIRMA
        if gridas[9] != "_" and gridas[9] != "T":
            gridas[1]="↑"
            gridas[9] = "_"
        elif gridas[10] != "_" and gridas[10] != "T":
            gridas[2]="↑"
            gridas[10] = "_"
        elif gridas[11] != "_" and gridas[11] != "T":
            gridas[3]="↑"
            gridas[11] = "_"
        elif gridas[12] != "_" and gridas[12] != "T":
            gridas[4]="↑"
            gridas[12] = "_"
        elif gridas[13] != "_" and gridas[13] != "T":
            gridas[5]="↑"
            gridas[13] = "_"
        elif gridas[14] != "_" and gridas[14] != "T":
            gridas[6]="↑"
            gridas[14] = "_"
        elif gridas[15] != "_" and gridas[15] != "T":
            gridas[7]="↑"
            gridas[15] = "_"
        elif gridas[16] != "_" and gridas[16] != "T":
            gridas[8]="↑"
            gridas[16] = "_"

        # IS Trecios I antra
        elif gridas[17] != "_" and gridas[17] != "T":
            gridas[9] = "↑"
            gridas[17] = "_"
        elif gridas[18] != "_" and gridas[18] != "T":
            gridas[10] = "↑"
            gridas[18] = "_"
        elif gridas[19] != "_" and gridas[19] != "T":
            gridas[11] = "↑"
            gridas[19] = "_"
        elif gridas[20] != "_" and gridas[20] != "T":
            gridas[12] = "↑"
            gridas[20] = "_"
        elif gridas[21] != "_" and gridas[21] != "T":
            gridas[13] = "↑"
            gridas[21] = "_"
        elif gridas[22] != "_" and gridas[22] != "T":
            gridas[14] = "↑"
            gridas[22] = "_"
        elif gridas[23] != "_" and gridas[23] != "T":
            gridas[15] = "↑"
            gridas[23] = "_"
        elif gridas[24] != "_" and gridas[24] != "T":
            gridas[16] = "↑"
            gridas[24] = "_"

        # IS ketvirtos I trecia
        elif gridas[25] != "_" and gridas[25] != "T":
            gridas[17]="↑"
            gridas[25] = "_"
        elif gridas[26] != "_" and gridas[26] != "T":
            gridas[18]="↑"
            gridas[26] = "_"
        elif gridas[27] != "_" and gridas[27] != "T":
            gridas[19]="↑"
            gridas[27] = "_"
        elif gridas[28] != "_" and gridas[28] != "T":
            gridas[20]="↑"
            gridas[28] = "_"
        elif gridas[29] != "_" and gridas[29] != "T":
            gridas[21]="↑"
            gridas[29] = "_"
        elif gridas[30] != "_" and gridas[30] != "T":
            gridas[22]="↑"
            gridas[30] = "_"
        elif gridas[31] != "_" and gridas[31] != "T":
            gridas[23]="↑"
            gridas[31] = "_"
        elif gridas[32] != "_" and gridas[32] != "T":
            gridas[24]="↑"
            gridas[32] = "_"

        # IS penktos I ketvirta
        elif gridas[33] != "_" and gridas[33] != "T":
            gridas[25]="↑"
            gridas[33] = "_"
        elif gridas[34] != "_" and gridas[34] != "T":
            gridas[26]="↑"
            gridas[34] = "_"
        elif gridas[35] != "_" and gridas[35] != "T":
            gridas[27]="↑"
            gridas[35] = "_"
        elif gridas[36] != "_" and gridas[36] != "T":
            gridas[28]="↑"
            gridas[36] = "_"
        elif gridas[37] != "_" and gridas[37] != "T":
            gridas[29]="↑"
            gridas[37] = "_"
        elif gridas[38] != "_" and gridas[38] != "T":
            gridas[30]="↑"
            gridas[38] = "_"
        elif gridas[39] != "_" and gridas[39] != "T":
            gridas[31]="↑"
            gridas[39] = "_"
        elif gridas[40] != "_" and gridas[40] != "T":
            gridas[32]="↑"
            gridas[40] = "_"

        # IS sestos I penkta
        elif gridas[41] != "_" and gridas[41] != "T":
            gridas[33]="↑"
            gridas[41] = "_"
        elif gridas[42] != "_" and gridas[42] != "T":
            gridas[34]="↑"
            gridas[42] = "_"
        elif gridas[43] != "_" and gridas[43] != "T":
            gridas[35]="↑"
            gridas[43] = "_"
        elif gridas[44] != "_" and gridas[44] != "T":
            gridas[36]="↑"
            gridas[44] = "_"
        elif gridas[45] != "_" and gridas[45] != "T":
            gridas[37]="↑"
            gridas[45] = "_"
        elif gridas[46] != "_" and gridas[46] != "T":
            gridas[38]="↑"
            gridas[46] = "_"
        elif gridas[47] != "_" and gridas[47] != "T":
            gridas[39]="↑"
            gridas[47] = "_"
        elif gridas[48] != "_" and gridas[48] != "T":
            gridas[40]="↑"
            gridas[48] = "_"

        # IS septinots I sesta
        elif gridas[49] != "_" and gridas[49] != "T":
            gridas[41]="↑"
            gridas[49] = "_"
        elif gridas[50] != "_" and gridas[50] != "T":
            gridas[42]="↑"
            gridas[50] = "_"
        elif gridas[51] != "_" and gridas[51] != "T":
            gridas[43]="↑"
            gridas[51] = "_"
        elif gridas[52] != "_" and gridas[52] != "T":
            gridas[44]="↑"
            gridas[52] = "_"
        elif gridas[53] != "_" and gridas[53] != "T":
            gridas[45]="↑"
            gridas[53] = "_"
        elif gridas[54] != "_" and gridas[54] != "T":
            gridas[46]="↑"
            gridas[54] = "_"
        elif gridas[55] != "_" and gridas[55] != "T":
            gridas[47]="↑"
            gridas[55] = "_"
        elif gridas[56] != "_" and gridas[56] != "T":
            gridas[48]="↑"
            gridas[56] = "_"

        # IS astuntos I septinta
        elif gridas[57] != "_" and gridas[57] != "T":
            gridas[49]="↑"
            gridas[57] = "_"
        elif gridas[58] != "_" and gridas[58] != "T":
            gridas[50]="↑"
            gridas[58] = "_"
        elif gridas[59] != "_" and gridas[59] != "T":
            gridas[51]="↑"
            gridas[59] = "_"
        elif gridas[60] != "_" and gridas[60] != "T":
            gridas[52]="↑"
            gridas[60] = "_"
        elif gridas[61] != "_" and gridas[61] != "T":
            gridas[53]="↑"
            gridas[61] = "_"
        elif gridas[62] != "_" and gridas[62] != "T":
            gridas[54]="↑"
            gridas[62] = "_"
        elif gridas[63] != "_" and gridas[63] != "T":
            gridas[55]="↑"
            gridas[63] = "_"
        elif gridas[64] != "_" and gridas[64] != "T":
            gridas[56]="↑"
            gridas[64] = "_"



        spausdinam()

    def zemyn(self):
        print("Juda zemyn")
        for elementas in gridas[57:65]:
            if elementas == "→" or elementas == "←" or elementas == "↓":
                print("negalymas ejimas")
                continue

        # IS pirmos I antra

        if gridas[1] != "_" and gridas[1] != "T":
            gridas[9] = "↓"
            gridas[1] = "_"
        elif gridas[2] != "_" and gridas[2] != "T":
            gridas[10] = "↓"
            gridas[2] = "_"
        elif gridas[3] != "_" and gridas[3] != "T":
            gridas[11] = "↓"
            gridas[3] = "_"
        elif gridas[4] != "_" and gridas[4] != "T":
            gridas[12] = "↓"
            gridas[4] = "_"
        elif gridas[5] != "_" and gridas[5] != "T":
            gridas[13] = "↓"
            gridas[5] = "_"
        elif gridas[6] != "_" and gridas[6] != "T":
            gridas[14] = "↓"
            gridas[6] = "_"
        elif gridas[7] != "_" and gridas[7] != "T":
            gridas[15] = "↓"
            gridas[7] = "_"
        elif gridas[8] != "_" and gridas[8] != "T":
            gridas[16] = "↓"
            gridas[8] = "_"

        # IS antros I trecia
        elif gridas[9] != "_" and gridas[9] != "T":
            gridas[17] = "↓"
            gridas[9] = "_"
        elif gridas[10] != "_" and gridas[10] != "T":
            gridas[18] = "↓"
            gridas[10] = "_"
        elif gridas[11] != "_" and gridas[11] != "T":
            gridas[19] = "↓"
            gridas[11] = "_"
        elif gridas[12] != "_" and gridas[12] != "T":
            gridas[20] = "↓"
            gridas[12] = "_"
        elif gridas[13] != "_" and gridas[13] != "T":
            gridas[21] = "↓"
            gridas[13] = "_"
        elif gridas[14] != "_" and gridas[14] != "T":
            gridas[22] = "↓"
            gridas[14] = "_"
        elif gridas[15] != "_" and gridas[15] != "T":
            gridas[23] = "↓"
            gridas[15] = "_"
        elif gridas[16] != "_" and gridas[16] != "T":
            gridas[24] = "↓"
            gridas[16] = "_"

        # IS trecios I ketvirta
        elif gridas[17] != "_" and gridas[17] != "T":
            gridas[25] = "↓"
            gridas[17] = "_"
        elif gridas[18] != "_" and gridas[18] != "T":
            gridas[26] = "↓"
            gridas[18] = "_"
        elif gridas[19] != "_" and gridas[19] != "T":
            gridas[27] = "↓"
            gridas[19] = "_"
        elif gridas[20] != "_" and gridas[20] != "T":
            gridas[28] = "↓"
            gridas[20] = "_"
        elif gridas[21] != "_" and gridas[21] != "T":
            gridas[29] = "↓"
            gridas[21] = "_"
        elif gridas[22] != "_" and gridas[22] != "T":
            gridas[30] = "↓"
            gridas[22] = "_"
        elif gridas[23] != "_" and gridas[23] != "T":
            gridas[31] = "↓"
            gridas[23] = "_"
        elif gridas[24] != "_" and gridas[24] != "T":
            gridas[32] = "↓"
            gridas[24] = "_"

        # IS ketvirtos I penkta
        elif gridas[25] != "_" and gridas[25] != "T":
            gridas[33] = "↓"
            gridas[25] = "_"
        elif gridas[26] != "_" and gridas[26] != "T":
            gridas[34] = "↓"
            gridas[26] = "_"
        elif gridas[27] != "_" and gridas[27] != "T":
            gridas[35] = "↓"
            gridas[27] = "_"
        elif gridas[28] != "_" and gridas[28] != "T":
            gridas[36] = "↓"
            gridas[28] = "_"
        elif gridas[29] != "_" and gridas[29] != "T":
            gridas[37] = "↓"
            gridas[29] = "_"
        elif gridas[30] != "_" and gridas[30] != "T":
            gridas[38] = "↓"
            gridas[30] = "_"
        elif gridas[31] != "_" and gridas[31] != "T":
            gridas[39] = "↓"
            gridas[31] = "_"
        elif gridas[32] != "_" and gridas[32] != "T":
            gridas[40] = "↓"
            gridas[32] = "_"

        # IS penktos I sesta
        elif gridas[33] != "_" and gridas[33] != "T":
            gridas[41] = "↓"
            gridas[33] = "_"
        elif gridas[34] != "_" and gridas[34] != "T":
            gridas[42] = "↓"
            gridas[34] = "_"
        elif gridas[35] != "_" and gridas[35] != "T":
            gridas[43] = "↓"
            gridas[35] = "_"
        elif gridas[36] != "_" and gridas[36] != "T":
            gridas[44] = "↓"
            gridas[36] = "_"
        elif gridas[37] != "_" and gridas[37] != "T":
            gridas[45] = "↓"
            gridas[37] = "_"
        elif gridas[38] != "_" and gridas[38] != "T":
            gridas[46] = "↓"
            gridas[38] = "_"
        elif gridas[39] != "_" and gridas[39] != "T":
            gridas[47] = "↓"
            gridas[39] = "_"
        elif gridas[40] != "_" and gridas[40] != "T":
            gridas[48] = "↓"
            gridas[40] = "_"

        # IS sestos I septinta
        elif gridas[41] != "_" and gridas[41] != "T":
            gridas[49] = "↓"
            gridas[41] = "_"
        elif gridas[42] != "_" and gridas[42] != "T":
            gridas[50] = "↓"
            gridas[42] = "_"
        elif gridas[43] != "_" and gridas[43] != "T":
            gridas[51] = "↓"
            gridas[43] = "_"
        elif gridas[44] != "_" and gridas[44] != "T":
            gridas[52] = "↓"
            gridas[44] = "_"
        elif gridas[45] != "_" and gridas[45] != "T":
            gridas[53] = "↓"
            gridas[45] = "_"
        elif gridas[46] != "_" and gridas[46] != "T":
            gridas[54] = "↓"
            gridas[46] = "_"
        elif gridas[47] != "_" and gridas[47] != "T":
            gridas[55] = "↓"
            gridas[47] = "_"
        elif gridas[48] != "_" and gridas[48] != "T":
            gridas[56] = "↓"
            gridas[48] = "_"

        # IS septintos I astunta
        elif gridas[49] != "_" and gridas[49] != "T":
            gridas[57] = "↓"
            gridas[49] = "_"
        elif gridas[50] != "_" and gridas[50] != "T":
            gridas[58] = "↓"
            gridas[50] = "_"
        elif gridas[51] != "_" and gridas[51] != "T":
            gridas[59] = "↓"
            gridas[51] = "_"
        elif gridas[52] != "_" and gridas[52] != "T":
            gridas[60] = "↓"
            gridas[52] = "_"
        elif gridas[53] != "_" and gridas[53] != "T":
            gridas[61] = "↓"
            gridas[53] = "_"
        elif gridas[54] != "_" and gridas[54] != "T":
            gridas[62] = "↓"
            gridas[54] = "_"
        elif gridas[55] != "_" and gridas[55] != "T":
            gridas[63] = "↓"
            gridas[55] = "_"
        elif gridas[56] != "_" and gridas[56] != "T":
            gridas[64] = "↓"
            gridas[56] = "_"
        spausdinam()

    def kairen(self):
        print("Juda kairen")
        if gridas[1] != "_" or gridas[9] != "_" or gridas[17] != "_" or gridas[25] != "_" or gridas[33] != "_" or gridas[41] != "_" or gridas[49] != "_" or gridas[57] != "_":
            print("negalymas ejimas")
        else:

            # IS astunto I septinta
            if gridas[8] != "_" and gridas[8] != "T":
                gridas[7] = "←"
                gridas[8] = "_"
            elif gridas[16] != "_" and gridas[16] != "T":
                gridas[15] = "←"
                gridas[16] = "_"
            elif gridas[24] != "_" and gridas[24] != "T":
                gridas[23] = "←"
                gridas[24] = "_"
            elif gridas[32] != "_" and gridas[32] != "T":
                gridas[31] = "←"
                gridas[32] = "_"
            elif gridas[40] != "_" and gridas[40] != "T":
                gridas[39] = "←"
                gridas[40] = "_"
            elif gridas[48] != "_" and gridas[48] != "T":
                gridas[47] = "←"
                gridas[48] = "_"
            elif gridas[56] != "_" and gridas[56] != "T":
                gridas[55] = "←"
                gridas[56] = "_"
            elif gridas[64] != "_" and gridas[64] != "T":
                gridas[63] = "←"
                gridas[64] = "_"
            # IS septinto I sesta

            elif gridas[7] != "_" and gridas[7] != "T":
                gridas[6] = "←"
                gridas[7] = "_"
            elif gridas[15] != "_" and gridas[15] != "T":
                gridas[14] = "←"
                gridas[15] = "_"
            elif gridas[23] != "_" and gridas[23] != "T":
                gridas[22] = "←"
                gridas[23] = "_"
            elif gridas[31] != "_" and gridas[31] != "T":
                gridas[30] = "←"
                gridas[31] = "_"
            elif gridas[39] != "_" and gridas[39] != "T":
                gridas[38] = "←"
                gridas[39] = "_"
            elif gridas[47] != "_" and gridas[47] != "T":
                gridas[46] = "←"
                gridas[47] = "_"
            elif gridas[55] != "_" and gridas[55] != "T":
                gridas[54] = "←"
                gridas[55] = "_"
            elif gridas[63] != "_" and gridas[63] != "T":
                gridas[62] = "←"
                gridas[63] = "_"

            # IS sesto I penkta
            elif gridas[6] != "_" and gridas[6] != "T":
                gridas[5] = "←"
                gridas[6] = "_"
            elif gridas[14] != "_" and gridas[14] != "T":
                gridas[13] = "←"
                gridas[14] = "_"
            elif gridas[22] != "_" and gridas[22] != "T":
                gridas[23] = "←"
                gridas[22] = "_"
            elif gridas[30] != "_" and gridas[30] != "T":
                gridas[29] = "←"
                gridas[30] = "_"
            elif gridas[38] != "_" and gridas[38] != "T":
                gridas[37] = "←"
                gridas[38] = "_"
            elif gridas[46] != "_" and gridas[46] != "T":
                gridas[45] = "←"
                gridas[46] = "_"
            elif gridas[54] != "_" and gridas[54] != "T":
                gridas[53] = "←"
                gridas[54] = "_"
            elif gridas[62] != "_" and gridas[62] != "T":
                gridas[61] = "←"
                gridas[62] = "_"

            # IS penkto I ketvirta
            elif gridas[5] != "_" and gridas[5] != "T":
                gridas[4] = "←"
                gridas[5] = "_"
            elif gridas[13] != "_" and gridas[13] != "T":
                gridas[12] = "←"
                gridas[13] = "_"
            elif gridas[23] != "_" and gridas[23] != "T":
                gridas[22] = "←"
                gridas[23] = "_"
            elif gridas[29] != "_" and gridas[29] != "T":
                gridas[28] = "←"
                gridas[29] = "_"
            elif gridas[37] != "_" and gridas[37] != "T":
                gridas[36] = "←"
                gridas[37] = "_"
            elif gridas[45] != "_" and gridas[45] != "T":
                gridas[44] = "←"
                gridas[45] = "_"
            elif gridas[53] != "_" and gridas[53] != "T":
                gridas[52] = "←"
                gridas[53] = "_"
            elif gridas[61] != "_" and gridas[61] != "T":
                gridas[60] = "←"
                gridas[61] = "_"

            # IS ketvirto I trecia
            elif gridas[4] != "_" and gridas[4] != "T":
                gridas[3] = "←"
                gridas[4] = "_"
            elif gridas[12] != "_" and gridas[12] != "T":
                gridas[11] = "←"
                gridas[12] = "_"
            elif gridas[20] != "_" and gridas[20] != "T":
                gridas[19] = "←"
                gridas[20] = "_"
            elif gridas[28] != "_" and gridas[28] != "T":
                gridas[27] = "←"
                gridas[28] = "_"
            elif gridas[36] != "_" and gridas[36] != "T":
                gridas[35] = "←"
                gridas[36] = "_"
            elif gridas[44] != "_" and gridas[44] != "T":
                gridas[43] = "←"
                gridas[44] = "_"
            elif gridas[52] != "_" and gridas[52] != "T":
                gridas[51] = "←"
                gridas[52] = "_"
            elif gridas[60] != "_" and gridas[60] != "T":
                gridas[59] = "←"
                gridas[60] = "_"

            # IS trecio I antra
            elif gridas[3] != "_" and gridas[3] != "T":
                gridas[2] = "←"
                gridas[3] = "_"
            elif gridas[11] != "_" and gridas[11] != "T":
                gridas[10] = "←"
                gridas[11] = "_"
            elif gridas[19] != "_" and gridas[19] != "T":
                gridas[18] = "←"
                gridas[19] = "_"
            elif gridas[27] != "_" and gridas[27] != "T":
                gridas[26] = "←"
                gridas[27] = "_"
            elif gridas[35] != "_" and gridas[35] != "T":
                gridas[34] = "←"
                gridas[35] = "_"
            elif gridas[43] != "_" and gridas[43] != "T":
                gridas[42] = "←"
                gridas[43] = "_"
            elif gridas[51] != "_" and gridas[51] != "T":
                gridas[50] = "←"
                gridas[51] = "_"
            elif gridas[59] != "_" and gridas[59] != "T":
                gridas[58] = "←"
                gridas[59] = "_"

            # IS antro i pirma stulpeli
            elif gridas[2] != "_" and gridas[2] != "T":
                gridas[1] = "←"
                gridas[2] = "_"
            elif gridas[10] != "_" and gridas[10] != "T":
                gridas[9] = "←"
                gridas[10] = "_"
            elif gridas[18] != "_" and gridas[18] != "T":
                gridas[17] = "←"
                gridas[18] = "_"
            elif gridas[26] != "_" and gridas[26] != "T":
                gridas[25] = "←"
                gridas[26] = "_"
            elif gridas[34] != "_" and gridas[34] != "T":
                gridas[33] = "←"
                gridas[34] = "_"
            elif gridas[42] != "_" and gridas[42] != "T":
                gridas[41] = "←"
                gridas[42] = "_"
            elif gridas[50] != "_" and gridas[50] != "T":
                gridas[49] = "←"
                gridas[50] = "_"
            elif gridas[58] != "_" and gridas[58] != "T":
                gridas[57] = "←"
                gridas[58] = "_"

        spausdinam()


    def desinen(self):
        print("Juda desinen")
        if gridas[8] != "_" or gridas[16] != "_" or gridas[24] != "_" or gridas[32] != "_" or gridas[40] != "_" or gridas[48] != "_" or gridas[56] != "_" or gridas[64] != "_":
            print("negalymas ejimas")
        else:
            # IS pirmo i antra stulpeli
            if gridas[1] != "_" and gridas[1] != "T":
                gridas[2] = "→"
                gridas[1] = "_"
            elif gridas[9] != "_" and gridas[9] != "T":
                gridas[10] = "→"
                gridas[9] = "_"
            elif gridas[17] != "_" and gridas[17] != "T":
                gridas[18] = "→"
                gridas[17] = "_"
            elif gridas[25] != "_" and gridas[25] != "T":
                gridas[26] = "→"
                gridas[25] = "_"
            elif gridas[33] != "_" and gridas[33] != "T":
                gridas[34] = "→"
                gridas[33] = "_"
            elif gridas[41] != "_" and gridas[41] != "T":
                gridas[42] = "→"
                gridas[41] = "_"
            elif gridas[49] != "_" and gridas[49] != "T":
                gridas[50] = "→"
                gridas[49] = "_"
            elif gridas[57] != "_" and gridas[57] != "T":
                gridas[58] = "→"
                gridas[57] = "_"

            # IS antro I trecia
            elif gridas[2] != "_" and gridas[2] != "T":
                gridas[3] = "→"
                gridas[2] = "_"
            elif gridas[10] != "_" and gridas[10] != "T":
                gridas[11] = "→"
                gridas[10] = "_"
            elif gridas[18] != "_" and gridas[18] != "T":
                gridas[19] = "→"
                gridas[18] = "_"
            elif gridas[26] != "_" and gridas[26] != "T":
                gridas[27] = "→"
                gridas[26] = "_"
            elif gridas[34] != "_" and gridas[34] != "T":
                gridas[35] = "→"
                gridas[34] = "_"
            elif gridas[42] != "_" and gridas[42] != "T":
                gridas[43] = "→"
                gridas[42] = "_"
            elif gridas[50] != "_" and gridas[50] != "T":
                gridas[51] = "→"
                gridas[50] = "_"
            elif gridas[58] != "_" and gridas[58] != "T":
                gridas[59] = "→"
                gridas[58] = "_"

            # IS trecio I ketvirta
            elif gridas[3] != "_" and gridas[3] != "T":
                gridas[4] = "→"
                gridas[3] = "_"
            elif gridas[11] != "_" and gridas[11] != "T":
                gridas[12] = "→"
                gridas[11] = "_"
            elif gridas[19] != "_" and gridas[19] != "T":
                gridas[20] = "→"
                gridas[19] = "_"
            elif gridas[27] != "_" and gridas[27] != "T":
                gridas[28] = "→"
                gridas[27] = "_"
            elif gridas[35] != "_" and gridas[35] != "T":
                gridas[36] = "→"
                gridas[35] = "_"
            elif gridas[43] != "_" and gridas[43] != "T":
                gridas[44] = "→"
                gridas[43] = "_"
            elif gridas[51] != "_" and gridas[51] != "T":
                gridas[52] = "→"
                gridas[51] = "_"
            elif gridas[59] != "_" and gridas[59] != "T":
                gridas[60] = "→"
                gridas[59] = "_"

            # IS ketvirto I penkta
            elif gridas[4] != "_" and gridas[4] != "T":
                gridas[5] = "→"
                gridas[4] = "_"
            elif gridas[12] != "_" and gridas[12] != "T":
                gridas[13] = "→"
                gridas[12] = "_"
            elif gridas[20] != "_" and gridas[20] != "T":
                gridas[21] = "→"
                gridas[20] = "_"
            elif gridas[28] != "_" and gridas[28] != "T":
                gridas[29] = "→"
                gridas[28] = "_"
            elif gridas[36] != "_" and gridas[36] != "T":
                gridas[37] = "→"
                gridas[36] = "_"
            elif gridas[44] != "_" and gridas[44] != "T":
                gridas[45] = "→"
                gridas[44] = "_"
            elif gridas[52] != "_" and gridas[52] != "T":
                gridas[53] = "→"
                gridas[52] = "_"
            elif gridas[60] != "_" and gridas[60] != "T":
                gridas[61] = "→"
                gridas[60] = "_"

            # IS penktos I sesta
            elif gridas[5] != "_" and gridas[5] != "T":
                gridas[6] = "→"
                gridas[5] = "_"
            elif gridas[13] != "_" and gridas[13] != "T":
                gridas[14] = "→"
                gridas[13] = "_"
            elif gridas[21] != "_" and gridas[21] != "T":
                gridas[22] = "→"
                gridas[21] = "_"
            elif gridas[29] != "_" and gridas[29] != "T":
                gridas[30] = "→"
                gridas[29] = "_"
            elif gridas[37] != "_" and gridas[37] != "T":
                gridas[38] = "→"
                gridas[37] = "_"
            elif gridas[45] != "_" and gridas[45] != "T":
                gridas[46] = "→"
                gridas[45] = "_"
            elif gridas[53] != "_" and gridas[53] != "T":
                gridas[54] = "→"
                gridas[53] = "_"
            elif gridas[61] != "_" and gridas[61] != "T":
                gridas[62] = "→"
                gridas[61] = "_"

            # IS sestos I septinta
            elif gridas[6] != "_" and gridas[6] != "T":
                gridas[7] = "→"
                gridas[6] = "_"
            elif gridas[14] != "_" and gridas[14] != "T":
                gridas[15] = "→"
                gridas[14] = "_"
            elif gridas[22] != "_" and gridas[22] != "T":
                gridas[23] = "→"
                gridas[22] = "_"
            elif gridas[30] != "_" and gridas[30] != "T":
                gridas[31] = "→"
                gridas[30] = "_"
            elif gridas[38] != "_" and gridas[38] != "T":
                gridas[39] = "→"
                gridas[38] = "_"
            elif gridas[46] != "_" and gridas[46] != "T":
                gridas[47] = "→"
                gridas[46] = "_"
            elif gridas[54] != "_" and gridas[54] != "T":
                gridas[55] = "→"
                gridas[54] = "_"
            elif gridas[62] != "_" and gridas[62] != "T":
                gridas[63] = "→"
                gridas[62] = "_"

            # IS septintos I astunta
            elif gridas[7] != "_" and gridas[7] != "T":
                gridas[8] = "→"
                gridas[7] = "_"
            elif gridas[15] != "_" and gridas[15] != "T":
                gridas[16] = "→"
                gridas[15] = "_"
            elif gridas[23] != "_" and gridas[23] != "T":
                gridas[24] = "→"
                gridas[23] = "_"
            elif gridas[31] != "_" and gridas[31] != "T":
                gridas[32] = "→"
                gridas[31] = "_"
            elif gridas[39] != "_" and gridas[39] != "T":
                gridas[40] = "→"
                gridas[39] = "_"
            elif gridas[47] != "_" and gridas[47] != "T":
                gridas[48] = "→"
                gridas[47] = "_"
            elif gridas[55] != "_" and gridas[55] != "T":
                gridas[56] = "→"
                gridas[55] = "_"
            elif gridas[63] != "_" and gridas[63] != "T":
                gridas[64] = "→"
                gridas[63] = "_"

        spausdinam()

    def suvis(self):
        print("Saudom")
        # Gaunam kordinates tanko

        for judesys in gridas:

            if judesys == "→":
                suviai_i_desine.append(1)

                vieta = gridas.index("→")
                print("Saudo i desine")
                if vieta < 9:
                    for saudom in visi[vieta:8]:
                        if saudom == "→":
                            gridas[saudom] = "→"
                            pass
                        else:
                            gridas[saudom] = "*"
                            time.sleep(1)
                            spausdinam()


                if vieta >= 9:
                    for saudom in visi[vieta:16]:
                        if saudom == "→":
                            gridas[saudom] = "→"
                            pass
                        else:
                            gridas[saudom] = "*"
                            time.sleep(1)
                            spausdinam()

                if vieta >= 16:
                    for saudom in visi[vieta:24]:
                        if saudom == "→":
                            gridas[saudom] = "→"
                            pass
                        else:
                            gridas[saudom] = "*"
                            time.sleep(1)
                            spausdinam()

                if vieta >= 24:
                    for saudom in visi[vieta:32]:
                        if saudom == "→":
                            gridas[saudom] = "→"
                            pass
                        else:
                            gridas[saudom] = "*"
                            time.sleep(1)
                            spausdinam()

                if vieta >= 32:
                    for saudom in visi[vieta:40]:
                        if saudom == "→":
                            gridas[saudom] = "→"
                            pass
                        else:
                            gridas[saudom] = "*"
                            time.sleep(1)
                            spausdinam()

                if vieta >= 40:
                    for saudom in visi[vieta:48]:
                        if saudom == "→":
                            gridas[saudom] = "→"
                            pass
                        else:
                            gridas[saudom] = "*"
                            time.sleep(1)
                            spausdinam()

                if vieta >= 48:
                    for saudom in visi[vieta:56]:
                        if saudom == "→":
                            gridas[saudom] = "→"
                            pass
                        else:
                            gridas[saudom] = "*"
                            time.sleep(1)
                            spausdinam()

                if vieta >= 56:
                    for saudom in visi[vieta:64]:
                        if saudom == "→":
                            gridas[saudom] = "→"
                            pass
                        else:
                            gridas[saudom] = "*"
                            time.sleep(1)
                            spausdinam()






            # if pozicija == "*":


            if judesys == "←":
                vieta = gridas.index("←")
                suviai_i_kaire.append(1)
                print("Saudo i kaire")
                print(vieta)
                # Pirma eile
                if vieta < 9:
                    for saudom in visi[vieta::-1]:
                        if saudom == "←":
                            gridas[saudom] = "←"
                            pass
                        else:
                            gridas[saudom-2] = "*"
                            time.sleep(1)
                            spausdinam()

                # Antra eile
                if vieta < 17:
                    for saudom in visi[vieta::-1]:
                        if saudom >= 10:
                            if saudom == "←":
                                gridas[saudom] = "←"
                                pass
                            else:
                                gridas[saudom-2] = "*"
                                time.sleep(1)
                                spausdinam()

                # Trecia eile
                if vieta < 25:
                    for saudom in visi[vieta::-1]:
                        if saudom >= 18:
                            if saudom == "←":
                                gridas[saudom] = "←"
                                pass
                            else:
                                gridas[saudom - 2] = "*"
                                time.sleep(1)
                                spausdinam()

                # Ketvirta eile
                if vieta < 33:
                    for saudom in visi[vieta::-1]:
                        if saudom >= 26:
                            if saudom == "←":
                                gridas[saudom] = "←"
                                pass
                            else:
                                gridas[saudom-2] = "*"
                                time.sleep(1)
                                spausdinam()

                # Penkta eile
                if vieta < 41:
                    for saudom in visi[vieta::-1]:
                        if saudom >= 34:
                            if saudom == "←":
                                gridas[saudom] = "←"
                                pass
                            else:
                                gridas[saudom-2] = "*"
                                time.sleep(1)
                                spausdinam()

                # Sesta eile
                if vieta < 49:
                    for saudom in visi[vieta::-1]:
                        if saudom >= 42:
                            if saudom == "←":
                                gridas[saudom] = "←"
                                pass
                            else:
                                gridas[saudom-2] = "*"
                                time.sleep(1)
                                spausdinam()

                # Septinta eile
                if vieta < 57:
                    for saudom in visi[vieta::-1]:
                        if saudom >= 50:
                            if saudom == "←":
                                gridas[saudom] = "←"
                                pass
                            else:
                                gridas[saudom-2] = "*"
                                time.sleep(1)
                                spausdinam()

                # Astunta eile
                if vieta < 65:
                    for saudom in visi[vieta::-1]:
                        if saudom >= 58:
                            if saudom == "←":
                                gridas[saudom] = "←"
                                pass
                            else:
                                gridas[saudom-2] = "*"
                                time.sleep(1)
                                spausdinam()


            if judesys == "↓":
                print("Saudo i apacia")
                vieta = gridas.index("↓")
                suviai_i_apacia.append(1)
                # Is pirmo i apacia
                # i = 1
                print(gridas[vieta])
                while (vieta < 64):
                    if gridas[vieta] == "↓":

                        vieta+=8
                        pass

                    print(vieta)
                    gridas[vieta] = "*"
                    vieta += 8
                    time.sleep(1)
                    spausdinam()
                # if vieta < 65:
                #     for saudom in visi[vieta:65]:
                #         if saudom >= 0:
                #             if saudom == "↓":
                #                 gridas[saudom] = "↓"
                #                 pass
                #             else:
                #                 buferis = saudom+7
                #                 gridas[buferis] = "*"
                #                 time.sleep(1)
                #                 spausdinam()
            if judesys == "↑":

                print("Saudo i virsu")
                vieta = gridas.index("↑")
                suviai_i_virsu.append(1)
                # Is pirmo i apacia
                # i = 1
                print(gridas[vieta])
                while (vieta < 64 and vieta > 0):
                    if gridas[vieta] == "↑":
                        vieta -= 8
                        pass

                    print(vieta)
                    gridas[vieta] = "*"
                    vieta -= 8
                    time.sleep(1)
                    spausdinam()

        for valom in gridas:
            if valom == "→" or valom == "←" or valom == "↓" or valom == "↑":
                continue

            gridas[gridas.index(valom)] = "_"

        spausdinam()


    def info(self):
        print("info")
        print(f"Atlikti suviai i Desine: {len(suviai_i_desine)}, Kaire: {len(suviai_i_kaire)}, Virsu: {len(suviai_i_virsu)}, Apacia: {len(suviai_i_apacia)}")
        print(f"ISVISO SUVIU: {len(suviai_i_desine)+len(suviai_i_kaire)+len(suviai_i_virsu)+len(suviai_i_apacia)}")

        for pozicija in gridas:
            if pozicija == "T":
                print(f"Taikynio pozicija: {gridas.index(pozicija)}")
            if pozicija == "→" or pozicija == "←" or pozicija == "↓" or pozicija == "↑":
                print(f"Tankas Pasisukes i: {pozicija}")
                print(f"kordinates: {gridas.index(pozicija)}")
            else:
                pass


def taikinys():
    x=int(input("iveskite taikynio pozicija"))
    gridas[x]="T"
    spausdinam()

taikinys()


# for elementas in gridas:
#     elementas = "_"
#     print(elementas)


while True:
    judejimas = input("""Kur vaziuojam? W - Virsun S - Zemyn A - Kairen D - Desinen SPACE - Saudyti\n""")
    tankas=Tankas()
    if judejimas == "w":
        tankas.virsun()
        tankas.info()
    if judejimas == "s":
        tankas.zemyn()
        tankas.info()
    if judejimas == "a":
        tankas.kairen()
        tankas.info()
    if judejimas == "d":
        tankas.desinen()
        tankas.info()
    if judejimas == "":
        tankas.suvis()
        tankas.info()





