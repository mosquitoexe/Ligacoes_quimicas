print("""
   _
  | | If you're not part
  / \  of the solution
 /   \  then you must be  |
(_____)  the precipitate. |    -Trina L. Short-
Aluno: Marcos Pires Viana
Turma: Engenharia Elétrica - 3 período
Universidade: UVV
""")
print("ATENÇÃO: não funciona com Cobre, Prata, Ouro e Molibdênio, Nióbio, Rutênio, Ródio, Paládio e Platina.")





LinusPauling = ['1s2', '2s2', '2p6', '3s2', '3p6', '4s2', '3d10', '4p6', '5s2','4d10', '5p6', '6s2', '4f14', '5d10', '6p6', '7s2', '5f14', '6d10','7p6']
Lp = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]


# função 1
def distribuição_eletronica(n):
    lista = []
    contador = 0
    for i in range(n):
        contador = contador + Lp[i]
        lista.append(LinusPauling[i])
        if (contador == n):
            return lista
            break
        elif (contador > n):
            ultimoElemento = lista.pop()
            contador = contador - Lp[i]
            x = n - contador
            a = list(ultimoElemento)
            if (len(a) == 3):
                a[2] = str(x)
                A = a[0] + a[1] + a[2]
                lista.append(A)
                return lista
            elif (len(a) == 4):
                ultimo = a.pop()
                penultimo = a.pop()
                azinho = penultimo + ultimo
                a.append(azinho)
                a[2] = str(x)
                A = a[0] + a[1] + a[2]
                lista.append(A)
                return lista
            break


# função 2
def impressao(z):
    K = []
    L = []
    M = []
    N = []
    O = []
    P = []
    Q = []
    for i in range(len(z)):
        elem = z[i]
        if "1" in elem[0]:
            K.append(elem)
        elif "2" in elem[0]:
            L.append(elem)
        elif "3" in elem[0]:
            M.append(elem)
        elif "4" in elem[0]:
            N.append(elem)
        elif "5" in elem[0]:
            O.append(elem)
        elif "6" in elem[0]:
            P.append(elem)
        elif "7" in elem[0]:
            Q.append(elem)

    camadas = [K, L, M, N, O, P, Q]
    filtro = []
    for i in range(len(camadas)):
        if len(camadas[i]) != 0:
            filtro.append(camadas[i])
    return filtro


# função3
def valencia(v):
    camada_de_valencia = v[-1]
    return camada_de_valencia

def neletrons(u):
    vazio=[]
    for i in range(len(u)):
        a=u[i]
        if len(a)==3:
            vazio.append(int(a[-1]))
        elif len(a)==4 in u:
            print("ERRO")
    return sum(vazio)



elementos ={"Ac":89,
            "Ag":47,
            "Al":13,
            "Am":95,
            "Ar":18,
            "As":33,
            "At":85,
            "Au":79,
            "B":5 ,
            "Ba":56,
            "Be":4,
            "Bh":107,
            "Bi":83,
            "Bk":97,
            "Br":35,
            "C":6,
            "Ca":20,
            "Cd":48,
            "Ce":58,
            "Cf":98,
            "Cl":17,
            "Cm":96,
            "Cn":112,
            "Co":27,
            "Cr":24,
            "Cs":55,
            "Cu":29,
            "Db":105,
            "Ds":110,
            "Dy":66,
            "Er":68,
            "Es":99,
            "Eu":63,
            "F":9 ,
            "Fe":26,
            "Fl":114,
            "Fm":100,
            "Fr":87,
            "Ga":31,
            "Gd":64,
            "Ge":32,
            "H":1 ,
            "He":2 ,
            "Hf":72,
            "Hg":80,
            "Ho":67,
            "Hs":108,
            "I":53,
            "In":49,
            "Ir":77,
            "K":19,
            "Kr":36,
            "La":57,
            "Li":3 ,
            "Lr":103,
            "Lu":71,
            "Lv":116,
            "Mc":115,
            "Md":101,
            "Mg":12,
            "Mn":25,
            "Mo":42,
            "Mt":109,
            "N":7 ,
            "Na":11,
            "Nb":41,
            "Nd":60,
            "Ne":10,
            "Nh":113,
            "Ni":28,
            "No":102,
            "Np":93,
            "O":8 ,
            "Og":118,
            "Os":76,
            "P":15,
            "Pa":91,
            "Pb":82,
            "Pd":46,
            "Pm":61,
            "Po":84,
            "Pr":59,
            "Pt":78,
            "Pu":94,
            "Ra":88,
            "Rb":37,
            "Re":75,
            "Rf":104,
            "Rg":111,
            "Rh":45,
            "Rn":86,
            "Ru":44,
            "S":16,
            "Sb":51,
            "Sc":21,
            "Se":34,
            "Sg":106,
            "Si":14,
            "Sm":62,
            "Sn":50,
            "Sr":38,
            "Ta":73,
            "Tb":65,
            "Tc":43,
            "Te":52,
            "Th":90,
            "Ti":22,
            "Tl":81,
            "Tm":69,
            "Ts":117,
            "U":92,
            "V":23,
            "W":74,
            "Xe":54,
            "Y":39,
            "Yb":70,
            "Zn":30,
            "Zr":40,}
while True:
    elemento1 = input("ELEMENTO 1: ")
    nome_do_elemento1 = elemento1
    elemento1 = elementos[elemento1]

    print("\nexibição 1\n",distribuição_eletronica(elemento1))
    elemento1 = distribuição_eletronica(elemento1)
    elemento1 = impressao(elemento1)
    camadadevalencia1 = valencia(elemento1)
    numero_de_eletrons_Valencia=neletrons(camadadevalencia1)

    print("\nCamada de valência: ",camadadevalencia1)

    print("\nNúmero de eletrons na camada de valência: ",numero_de_eletrons_Valencia)

    print("\nexibição 2\n")
    camadas = ["K", "L", "M", "N", "O", "P", "Q"]
    for i in range(len(elemento1)):
        print(camadas[i],"",elemento1[i])
    if '1s1' in camadadevalencia1:
        material1="AMETAL"
    elif numero_de_eletrons_Valencia < 4:
        material1="METAL"
    elif numero_de_eletrons_Valencia == 4 and "d" in camadadevalencia1[-1]:
        material1="METAL"
    elif numero_de_eletrons_Valencia > 4:
        material1="AMETAL"
    elif numero_de_eletrons_Valencia == 4 and "p" in camadadevalencia1[-1]:
        material1="AMETAL"
    print("\n",material1)
    #***********************************
    print('_'*100)
    elemento2 = input("ELEMENTO 2: ")
    nome_do_elemento2 = elemento2

    elemento2 = elementos[elemento2]
    print("\nexibição 1\n",distribuição_eletronica(elemento2))
    elemento2 = distribuição_eletronica(elemento2)
    elemento2 = impressao(elemento2)
    camadadevalencia2 = valencia(elemento2)
    numero_de_eletrons_Valencia2=neletrons(camadadevalencia2)

    print("\nCamada de valência: ",camadadevalencia2)

    print("\nNúmero de elétrons na camadade valência: ",numero_de_eletrons_Valencia2)

    print("\nexibição 2\n")
    camadas = ["K", "L", "M", "N", "O", "P", "Q"]
    for i in range(len(elemento2)):
        print(camadas[i],"",elemento2[i])
    if '1s1' in camadadevalencia2:
        material2="AMETAL"
    elif numero_de_eletrons_Valencia2 < 4:
        material2="METAL"
    elif numero_de_eletrons_Valencia2 == 4 and "d" in camadadevalencia2[-1]:
        material2="METAL"
    elif numero_de_eletrons_Valencia2 > 4:
        material2="AMETAL"
    elif numero_de_eletrons_Valencia2 == 4 and "p" in camadadevalencia2[-1]:
        material2="AMETAL"
    print("\n", material2)





    if material1 == "AMETAL" and material2 == "METAL":
        decisao=input("\nDeseja fazer a ligação iônica: [Y/N] ")
        if decisao == "Y":
            Y=nome_do_elemento1
            X =nome_do_elemento2
            print(X+str(8-numero_de_eletrons_Valencia)+Y+str(numero_de_eletrons_Valencia2))


    elif material1 == "METAL" and material2 == "AMETAL":
        decisao = input("\nDeseja fazer a ligação iônica: [Y/N] ")
        if decisao == "Y":
            Y = nome_do_elemento2
            X = nome_do_elemento1

            print("\nResultado: ",X+str(8-numero_de_eletrons_Valencia2)+Y+str(numero_de_eletrons_Valencia))
