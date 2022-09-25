"""
FP2021 @ IST - Projeto 1 - Buggy Data Base (BDB)
Feito por Joao Amadeu 98943
"""

# -------------------------------------- 1.2.1 corrigir_palavra -------------------------------------- #

#Função auxiliar

def lista_para_string(string):
    """
    Função auxiliar (Lista para String)

    :param string: list
    :return: str

    Recebe uma lista e devolve uma string dos caracteres da lista.
    Exemplo de uso:

    >>> nome = ("a","m","a","d","e","u")
    >>> lista_para_string(nome)
    "amadeu"
    """

    string_aux = ""
    for letra in string:
        string_aux += letra
    return string_aux

def corrigir_palavra(string):
    """
    Corrigir palavra.

    :param string: str
    :return: str

    Esta funcao recebe uma cadeia de carateres que representa uma palavra (potencialmente
    modificada por um surto de letras) e devolve a cadeia de carateres que corresponde a
    aplicacao da sequencia de reducoes conforme descrito para obter a palavra corrigida.
    Exemplo de uso:

    >>> corrigir_palavra("abBAx")
    "x"
    >>> corrigir_palavra("cCdatabasacCADde")
    "database"
    """

    i = 0
    aux = []
    aux2 = []
    aux.extend(string)
    aux2.extend(string.upper())
    if len(string) == 1:
        return ""
    while i < len(aux) - 1:
        if aux2[i] == aux2[i+1] and aux[i] != aux[i+1]:
            del aux[i:i+2]
            del aux2[i:i+2]
            i = 0
        else:
            i += 1
    return lista_para_string(aux)

# -------------------------------------- 1.2.2 eh_anagrama -------------------------------------- #

def eh_anagrama(p1,p2):
    """
    Verificar Anagrama.

    :param p1: str
    :param p2: str
    :return: bool

    Esta funcao recebe duas cadeias de carateres correspondentes a duas palavras e devolve
    True se e so se uma e anagrama da outra.
    Exemplo de uso:

    >>> eh_anagrama("caso", "SaCo")
    True
    >>> eh_anagrama("caso", "casos")
    False
    """

    auxp1 = sorted(p1.upper())
    auxp2 = sorted(p2.upper())
    letras_iguais = 0
    if len(auxp1) == len(auxp2):
        for i in range(len(auxp1)):
            if auxp1[i] == auxp2[i]:
                letras_iguais += 1
    if letras_iguais == len(auxp1) and letras_iguais == len(p1):
        return True
    else:
        return False

# -------------------------------------- 1.2.3 corrigir_doc -------------------------------------- #

def corrigir_doc(string):
    """
    Corrigir Documento.

    :param string: str
    :return: str

    Esta funcao recebe uma cadeia de carateres que representa o texto com erros da
    documentacao da BDB e devolve a cadeia de carateres filtrada com as palavras
    corrigidas e os anagramas retirados.
    Exemplo de uso:

    >>> corrigir_doc("???")
    ValueError: corrigir_doc: argumento invalido
    >>> doc = BuAaXOoxiIKoOkggyrFfhHXxR duJjUTtaCcmMtaAGga \
    eEMmtxXOjUuJQqQHhqoada JlLjbaoOsuUeYy cChgGvValLCwMmWBbclLsNn \
    LyYlMmwmMrRrongTtoOkyYcCK daRfFKkLlhHrtZKqQkkvVKza
    >>> corrigir_doc(doc)
    Buggy data base has wrong data
    """

    x,n,c = 0,0,0
    res = []
    if type(string) != str:
        raise ValueError("corrigir_doc: argumento invalido")
    string_aux = corrigir_palavra(string)
    lista_aux = string_aux.split()
    for e in lista_aux:
        if e.isalpha() == False:
            raise ValueError("corrigir_doc: argumento invalido")
    while x < len(lista_aux):
            res += [lista_aux[x] + " ",]
            x += 1
    while n < len(lista_aux) and c <= len(lista_aux):
        if c == len(lista_aux):
            n += 1
            c = 0
        if n == len(lista_aux):
            return lista_para_string(res).rstrip()
        if eh_anagrama(lista_aux[c], lista_aux[n]) == True and lista_aux[c].upper() != lista_aux[n].upper():
            del res[c]
            del lista_aux[c]
        c += 1
    return lista_para_string(res).rstrip()


# -------------------------------------- 2.2.1 obter_posicao -------------------------------------- #

def obter_posicao(direcao,pos_i):
    """
    Obter Posicao.

    :param direcao: str
    :param pos_i: int
    :return: int

    Esta funcao recebe uma cadeia de carateres contendo apenas um carater que representa
    a direcao de um unico movimento ("C", "B", "E" ou "D") e um inteiro representando a
    posicao atual (1, 2, 3, 4, 5, 6, 7, 8 ou 9); e devolve o inteiro que corresponde a nova
    posicao apos o movimento.
    Exemplo de uso:

    >>> obter_posicao("C", 5)
    2
    >>> obter_posicao("B", 5)
    8
    """

    if direcao == "E":
        if pos_i-1 in (1,2,4,5,7,8):
            return pos_i-1
        else:
            return pos_i
    if direcao == "D":
        if pos_i+1 in (2,3,5,6,8,9):
            return pos_i+1
        else:
            return pos_i
    if direcao == "C":
        if pos_i in (1,2,3):
            return pos_i
        else:
            return pos_i-3
    if direcao == "B":
        if pos_i in (7,8,9):
            return pos_i
        else:
            return pos_i+3

# -------------------------------------- 2.2.2 obter_digito -------------------------------------- #

def obter_digito(seq,pos_i):
    """
    Obter Digito.

    :param seq: str
    :param pos_i: int
    :return: int

    Esta funcao recebe uma cadeia de carateres contendo uma sequencia de um ou
    mais movimentos e um inteiro representando a posicao inicial; devolve o
    inteiro que corresponde ao dıgito, apos finalizar todos os movimentos.
    Exemplo de uso:

    >>> obter_digito("CEE", 5)
    1
    >>> obter_digito("CBD", 8)
    9
    """
    res = 0
    for caracter in seq:
        res = obter_posicao(caracter,pos_i)
        pos_i = res
    return res

# -------------------------------------- 2.2.3 obter_pin -------------------------------------- #

def obter_pin(tuplo):
    """
    Obter PIN.

    :param tuplo: tuple
    :return: tuple

    Esta funcao recebe um tuplo contendo entre 4 e 10 sequencias
    de movimentos e devolve o tuplo de inteiros que contem o pin
    codificado de acordo com o tuplo de movimentos.
    Exemplo de uso:

    >>> obter_pin(())
    ValueError: obter_pin: argumento invalido
    >>> t = ("CEE", "DDBBB", "ECDBE", "CCCCB")
    >>> obter_pin(t)
    (1, 9, 8, 5)
    """

    num = 5
    res = ()
    if type(tuplo) != tuple or len(tuplo) < 4 or len(tuplo) > 10:
        raise ValueError("obter_pin: argumento invalido")
    for seq in tuplo:
        if type(seq) != str or len(seq) < 1:
            raise ValueError("obter_pin: argumento invalido")
        for letra in seq:
            if letra not in ("C","B","D","E"):
                raise ValueError("obter_pin: argumento invalido")
    for seq in tuplo:
        res_aux = obter_digito(seq,num)
        num = res_aux
        res += (res_aux,)
    return res


# -------------------------------------- 3.2.1 eh_entrada -------------------------------------- #

def eh_entrada(tuplo):
    """
    Verifica Argumento.

    :param tuplo: universal
    :return: bool

    Esta funcao recebe um argumento de qualquer tipo e devolve True se e so se o seu
    argumento corresponde a uma entrada da BDB (potencialmente corrupta).
    Exemplo de uso:

    >>> eh_entrada(("a-b-c-d-e-f-g-h", "[abcd]", (950,300)))
    False
    >>> eh_entrada(("a-b-c-d-e-f-g-h-2", "[abcde]", (950,300)))
    False
    >>> eh_entrada(("a-b-c-d-e-f-g-h", "[xxxxx]", (950,300)))
    True
    """

    if type(tuplo) != tuple or len(tuplo) != 3:
        return False
    if type(tuplo[0]) != str or type(tuplo[1]) != str or type(tuplo[2]) != tuple \
        or len(tuplo[2]) < 2:
        return False
    cifra = tuplo[0].split("-")
    checksum = list(tuplo[1])
    for palavra in cifra:
        if palavra == "":
            return False
        for letra in palavra:
            if letra != letra.lower() or letra.isalpha() == False:
                return False
    if len(checksum) != 7 or checksum[0] != "[" or checksum[6] != "]":
        return False
    for letra2 in checksum[1:-1]:
        if letra2.isalpha() == False or letra2 != letra2.lower():
            return False
    for num in tuplo[2]:
        if type(num) != int or num < 0:
            return False
    return True

# -------------------------------------- 3.2.2 validar_cifra -------------------------------------- #

def validar_cifra(cifra, checksum):
    """
    Verifica coerencia entre Cifra e Sequencia de controlo.

    :param cifra: str
    :param checksum: str
    :return: bool

    Esta funcao recebe uma cadeia de carateres contendo uma cifra e uma outra cadeia de
    carateres contendo uma sequencia de controlo, e devolve True se e so se a sequencia de
    controlo e coerente com a cifra.
    Exemplo de uso:

    >>> validar_cifra("a-b-c-d-e-f-g-h", "[xxxxx]")
    False
    >>> validar_cifra("a-b-c-d-e-f-g-h", "[abcde]")
    True
    """

    if type(cifra) != str or type(checksum) != str or len(cifra) < 1 or len(checksum) != 7:
        return False
    cifra_aux = cifra.split("-")
    checksum_aux = list(checksum[1:-1])
    contador,res,aux,cifra_res = {},[],[],[]
    n,size = 1,0
    while n <= len(cifra_aux):
        if len(cifra_aux[n - 1]) > 1:
            aux = list(cifra_aux[n - 1])
            del cifra_aux[n - 1]
            for letra_aux in aux:
                cifra_aux += letra_aux
                n = 0
        n += 1
    cifra_aux.sort()
    for corretor in cifra_aux:
        if corretor.isalpha() == True:
            cifra_res.append(corretor)
    for letra in checksum_aux:
        if letra not in cifra_res:
            return False
    for letras in cifra_res:
        if letras != letras.lower():
            return False
        if letras in contador:
            contador[letras] += 1
        else:
            contador[letras] = 1
    if len(contador) < 5:
        return False
    while size < 5 :
        res += maior_num_letras(contador)
        size += 1
    if checksum_aux != res:
        return False
    else:
        return True

# Função auxiliar

def maior_num_letras(dicionario):
    """
    Função auxiliar (Determina a letra mais comum)

    :param dicionario: dict
    :return: list

    Recebe um dicionario e devolve uma lista com a letra mais comum.
    Exemplo de uso:

    >>> maior_num_letras({"a":3,"b":2})
    ['a']
    >>> maior_num_letras({"a":3,"b":2,"c":4,"d":6})
    ['d']
    """
    maior = 0
    chave_aux = None
    for chave,valor in dicionario.items():
        if valor > maior:
            maior = valor
            chave_aux = chave
    del dicionario[chave_aux]
    return [chave_aux]

# -------------------------------------- 3.2.3 filtrar_bdb -------------------------------------- #

def filtrar_bdb(lista):
    """
    Verifica entradas de BDB de uma lista.

    :param lista: list
    :return: list

    Esta funcao recebe uma lista contendo uma ou mais entradas da BDB
    e devolve apenas a lista contendo as entradas em que o checksum nao e
    coerente com a cifra correspondente, na mesma ordem da lista original.
    Exemplo de uso:

    >>> filtrar_bdb([])
    ValueError: filtrar_bdb: argumento invalido
    >>> bdb = [("aaaaa-bbb-zx-yz-xy", "[abxyz]", (950,300)),
    ("a-b-c-d-e-f-g-h", "[abcde]", (124,325,7)),
    ("entrada-muito-errada", "[abcde]", (50,404))]
    >>> filtrar_bdb(bdb)
    [("entrada-muito-errada", "[abcde]", (50,404))]
    """

    n = 0
    res = []
    if type(lista) != list or len(lista) < 1:
        raise ValueError("filtrar_bdb: argumento invalido")
    while n < len(lista):
        if type(lista[n]) != tuple:
            raise ValueError("filtrar_bdb: argumento invalido")
        if len(lista[n]) != 3:
            raise ValueError("filtrar_bdb: argumento invalido")
        if eh_entrada(lista[n]) == False:
            raise ValueError("filtrar_bdb: argumento invalido")
        else:
            if validar_cifra(lista[n][0],lista[n][1]) == False:
                res.append(lista[n])
        n += 1
    return res


# -------------------------------------- 4.2.1 eh_entrada -------------------------------------- #


                                    #Feito anteriormente no 3.2.1
                                            #linha 255


# -------------------------------------- 4.2.2 obter_num_seguranca -------------------------------------- #

def obter_num_seguranca(tuplo):
    """
    Calcula a menor diferenca positiva entre inteiros de uma Sequencia de segurança.

    :param tuplo: universal
    :return: bool

    Esta funcao recebe um tuplo de numeros inteiros positivos e devolve o numero de
    seguranca conforme descrito, isto e, a menor diferenca positiva entre qualquer par de numeros.
    Exemplo de uso:

    >>> obter_num_seguranca((2223,424,1316,99))
    325
    """

    i,j,num = 0,1,10E100000000
    while i < len(tuplo):
        while j < len(tuplo):
            if tuplo[i] > tuplo[j]:
                if tuplo[i] - tuplo[j] <= num:
                    num = tuplo[i] - tuplo[j]
                j+=1
            else:
                if tuplo[j] - tuplo[i] <= num:
                    num = tuplo[j] - tuplo[i]
                j+=1
        i +=1
        j = i+1
    return num

# -------------------------------------- 4.2.3 decifrar_texto -------------------------------------- #

def decifrar_texto(string,num):
    """
    Decifra texto segundo o numero de segurança

    :param string: str
    :param num: int
    :return: str

    Esta funcao recebe uma cadeia de carateres contendo uma cifra e um numero
    de seguranca, e devolve o texto decifrado.
    Exemplo de uso:

    >>> decifrar_texto("qgfo-qutdo-s-egoes-wzegsnfmjqz", 325)
    "esta cifra e quase inquebravel"
    """

    n,p = 0,0
    num_aux = num % 26
    lista = list(string)
    while n < len(lista):
        if lista[n] == "-":
            lista[n] = " "
        if lista[n].isalpha() == True:
            if ord(lista[n]) + num_aux > 122:
                c = ord(lista[n]) + num_aux - 122
                if n % 2 == 0:
                    lista[n] = chr(ord("a") + c)
                else:
                    lista[n] = chr(ord("a") + c - 2)
            elif ord(lista[n]) + num_aux == 122:
                if n % 2 == 0:
                    lista[n] = chr(97)
                else:
                    lista[n] = chr(121)
            else:
                if n % 2 == 0:
                    lista[n] = chr(ord(lista[n]) + num_aux + 1)
                else:
                    lista[n] = chr(ord(lista[n]) + num_aux - 1)
        n+=1
    return lista_para_string(lista)

# -------------------------------------- 4.2.4 decifrar_bdb -------------------------------------- #

def decifrar_bdb(lista):
    """
     Decifra entradas BDB de uma lista

     :param lista: list
     :return: list

     Esta funcao recebe uma lista contendo uma ou mais entradas da BDB e devolve uma
     lista de igual tamanho, contendo o texto das entradas decifradas na mesma ordem.
     Exemplo de uso:

    >>> decifrar_bdb([("nothing")])
    ValueError: decifrar_bdb: argumento invalido
    >>> bdb = [("qgfo-qutdo-s-egoes-wzegsnfmjqz", "[abcde]",
    (2223,424,1316,99)), ("lctlgukvzwy-ji-xxwmzgugkgw",
    "[abxyz]", (2388, 367, 5999)), ("nyccjoj-vfrex-ncalml",
    "[xxxxx]", (50, 404))]
    >>> decifrar_bdb(bdb)
    ["esta cifra e quase inquebravel", "fundamentos da programacao",
    "entrada muito errada"]
     """

    n = 0
    res = []
    if type(lista) != list or len(lista) < 1:
        raise ValueError("decifrar_bdb: argumento invalido")
    while n < len(lista):
        if len(lista[n]) != 3 or type(lista[n]) != tuple:
            raise ValueError("decifrar_bdb: argumento invalido")
        else:
            res.append(decifrar_texto(lista[n][0],obter_num_seguranca(lista[n][2])))
        n += 1
    return res


# -------------------------------------- 5.2.1 eh_utilizador -------------------------------------- #

def eh_utilizador(dicionario):
    """
     Verifica Argumento.

     :param dicionario: universal
     :return: bool

     Esta funcao recebe um argumento de qualquer tipo e devolve True se e so se o seu
     argumento corresponde a um dicionario contendo a informacao de utilizador relevante da BDB.
     Exemplo de uso:

    >>> eh_utilizador({"name":"john.doe", "pass":"aabcde", "rule":{"vals": (1,3), "char":"a"}})
    True
    >>> eh_utilizador({"name":"john.doe", "pass":"aabcde", "rule":{"vals": 1, "char":"a"}})
    False
     """

    lista_aux = []
    if type(dicionario) != dict or len(dicionario) != 3:
        return False
    for chave in dicionario.keys():
        if type(chave) != str or chave not in ("pass","rule","name"):
            return False
    if type(dicionario["pass"]) != str or type(dicionario["name"]) != str or type(dicionario["rule"]) != dict:
        return False
    if len(dicionario["rule"]) != 2 or len(dicionario["pass"]) < 1 or len(dicionario["name"]) < 1:
        return False
    for chave_rule in dicionario["rule"].keys():
        if type(chave_rule) != str or chave_rule not in ("vals","char"):
            return False
    if type(dicionario["rule"]["vals"]) != tuple or len(dicionario["rule"]["vals"]) != 2 or \
        type(dicionario["rule"]["char"]) != str or len(dicionario["rule"]["char"]) != 1 \
        or dicionario["rule"]["char"].isalpha() == False or \
        dicionario["rule"]["char"] != dicionario["rule"]["char"].lower():
        return False
    for num in dicionario["rule"]["vals"]:
        if type(num) != int or num < 0:
            return False
        lista_aux.append(num)
    if lista_aux[0] > lista_aux[1]:
        return False
    return True

# -------------------------------------- 5.2.2 eh_senha_valida -------------------------------------- #

def eh_senha_valida(senha,regra):
    """
     Verifica senha.

     :param senha: str
     :param regra: dict
     :return: bool

     Esta funcao recebe uma cadeia de carateres correspondente a uma senha e um dicionario
     contendo a regra individual de criacao da senha, e devolve True se e so se a senha cumpre
     com todas as regras de definicao (gerais e individual).
     Exemplo de uso:

    >>> eh_senha_valida("aabcde", {"vals": (1,3), "char":"a"})
    True
    >>> eh_senha_valida("cdefgh", {"vals": (1,3), "char":"b"})
    False
     """

    lista_chaves,lista_valor,lista_senha = [],[],[]
    lista_senha = list(senha)
    contador_aux,contador_letra,contador_vogais, n = 0,0,0,0
    for chave,valor in regra.items():
        lista_chaves.append(chave)
        lista_valor.append(valor)
    count_min = lista_valor[0][0]
    count_max = lista_valor[0][1]
    caracter = lista_valor[1]
    contador = senha.count(caracter)
    if contador > count_max or contador < count_min:
        return False
    contador_vogais = senha.count("a") + senha.count("e") + senha.count("i") + senha.count("o") + senha.count("u")
    if contador_vogais < 3:
        return False
    while n < len(lista_senha) - 1:
        if lista_senha[n] == lista_senha[n+1]:
            contador_aux += 1
        n += 1
    if contador_aux < 1:
        return False
    else:
        return True

# -------------------------------------- 5.2.3 filtrar_senhas -------------------------------------- #

def filtrar_senhas(lista):
    """
    Verifica entradas de BDB com senhas erradas de uma lista.

     :param lista: list
     :return: list

    Esta funcao recebe uma lista contendo um ou mais dicionarios correspondentes as entradas
    da BDB como descritas anteriormente, e devolve a lista ordenada alfabeticamente
    com os nomes dos utilizadores com senhas erradas
    Exemplo de uso:

    >>> filtrar_senhas([])
    ValueError: filtrar_senhas: argumento invalido
    >>> bdb = [ {"name":"john.doe", "pass":"aabcde", "rule":{"vals":(1,3),
    "char":"a"}}, {"name":"jane.doe", "pass":"cdefgh",
    "rule":{"vals":(1,3), "char":"b"}}, {"name":"jack.doe",
    "pass":"cccccc", "rule":{"vals":(2,9), "char":"c"}} ]
    >>> filtrar_senhas(bdb)
    ["jack.doe", "jane.doe"]
     """

    n = 0
    res = []
    if type(lista) != list or len(lista) < 1:
        raise ValueError("filtrar_senhas: argumento invalido")
    while n < len(lista):
        if len(lista[n]) != 3 or type(lista[n]) != dict:
            raise ValueError("filtrar_senhas: argumento invalido")
        if eh_utilizador(lista[n]) == False or eh_senha_valida(lista[n]["pass"], lista[n]["rule"]) == False:
            res.append(lista[n]["name"])
        n += 1
    res = sorted(res)
    return res

# -------------------------------------------------------------------------------------------------- #

                                                #FIM
