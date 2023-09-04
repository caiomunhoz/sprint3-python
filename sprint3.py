def input_valido(entrada, opcoes):
    if entrada in opcoes:
        return True
    else:
        return False

def menu_sem_login():
    print("\t-- SEGURO BIKE PORTO SEGURO --")
    print("1. Fazer login")
    print("2. Cadastrar-se")
    print("3. Encerrar programa")
    opcao = int(input("Escolha uma opção: "))
    while input_valido(opcao, [1, 2, 3]) == False:
        opcao = int(input("Opção inválida. Digite \"1\", \"2\" ou \"3\" para prosseguir: "))
    return opcao

def menu_com_login_usuario():
    print("\n1. Cotar seguro")
    print("2. Exibir bicicletas cadastradas")
    print("3. Informações sobre o seguro")
    print("4. Encerrar programa")
    opcao = int(input("Escolha uma opção: "))
    while input_valido(opcao, [1, 2, 3, 4]) == False:
        opcao = int(input("Opção inválida. Digite \"1\", \"2\", \"3\" ou \"4\" para prosseguir: "))
    return opcao

def menu_com_login_admin():
    print("\n1. Obter relatório")
    print("2. Encerrar programa")
    opcao = int(input("Escolha uma opção: "))
    while input_valido(opcao, [1, 2]) == False:
        opcao = int(input("Opção inválida. Digite \"1\" ou \"2\" para prosseguir: "))
    return opcao

def menu_infos():
    print("\n1. Bicicletas e acessórios cobertos pelo seguro")
    print("2. Coberturas do seguro")
    opcao = int(input("Escolha uma opção: "))
    while input_valido(opcao, [1, 2]) == False:
        opcao = int(input("Opção inválida. Digite \"1\" ou \"2\" para prosseguir: "))
    return opcao

def texto_infos(opcao):
    match opcao:
        case 1:
            print("\nConheça as bicicletas e acessórios cobertos:\n")
            print("Bicicletas cobertas:")
            print("Urbana | Mountain Bike | Speed | Elétrica | Dobrável | BMX | Downhill | Trial | Fixa | Reclinada | Handbike")
            print("\nAcessórios cobertos: ")
            print("Velocímetro digital | GPS | Ciclocomputador")
        case 2:
            print("\nConheça as coberturas:\n")
            print("* Danos à bike: danos causados por incêndios, queda ou tentativa de roubo são cobertos.")
            print("* Subtração da bike: cobre contra roubos. ")
            print("* Acidentes pessoais individual: caso ocorra um acidente, cobre as despesas em caso de morte acidental e invalidez permanente.")
            print("* Garantia internacional: possibilita a extensão das garantias contratadas para sinistros que ocorrem fora do Brasil.")
            print("* Bike bagagem: cobre o extravio da bicicleta em viagens aéreas e/ou rodoviárias.")
            print("* Responsabilidade civil: cobre os danos materiais e/ou corporais causados a terceiros durante o uso da sua bicicleta.")
            print("* Danos elétricos: Cobre os danos causados por oscilações de energia, descargas elétricas e curtos-circuitos em bikes elétricas.")

def login():
    username = input("\nDigite o nome de usuário: ")
    senha = input("Digite a senha: ")
    return username, senha

def login_valido(bd, username, senha):
    if username in bd:
        dados_usuario = bd.get(username)
        if senha == dados_usuario[0]:
            print("Login realizado com sucesso.")
            return True
    else:
        return False
    
def view(username):
    if username == "admin":
        return "Admin"
    else:
        return "Cliente"
    
def cadastro(bd):
    print("\nPreencha o formulário abaixo com seus dados.\n")

    nome = input("Nome completo: ")   
    cpf = int(input("CPF: "))
    cep = int(input("CEP: "))
    tel = int(input("Número de telefone: "))
    username = input("Nome de usuário: ")
    while username_valido(bd, username) == False:
        username = input("Alguém já utiliza esse nome de usuário. Digite outro: ")
    senha = input("Senha: ")
    return nome, cpf, cep, tel, username, senha

def username_valido(bd, username):
    if bd.get(username) != None:
        return False
    else:
        return True

def banco_de_dados_exemplo():
    return {
        "lu1zaLim@":["e!8KpwJ", {"Nome": "Luiza Lima Alves", "CPF": 57282478651, "CEP": 68911362, "Tel": 93128393}, 
            {1: ["Caloi", "Vulcan", 925.65, 2014, "Reprovada para o seguro"]}],
        "antoniogr":["q47kfGE", {"Nome": "Antônio Gonçalves Ribeiro", "CPF": 11640267557, "CEP": 45050110, "Tel": 71523883}, 
            {1: ["Specialized", "Rockhopper", 5490, 2021, "Aprovada para o seguro"], 2: ["Cannondale", "SuperSix", 44999.10, 2023, "Aprovada para o seguro"]}],
        "renan_almeida":["jko04o5", {"Nome": "Renan Fernandes Almeida", "CPF": 21768509808, "CEP": 97015410, "Tel": 26106070}, 
            {1: ["Sense", "Fun Comp", 2690, 2019, "Aprovada para o seguro"], 2: ["Sense", "One", 2290, 2010, "Reprovada para o seguro"], 3: ["Caloi", "E-Vibe Easy Rider", 8199, 2023, "Aprovada pra o seguro"]}],
        "manu.bmx": ["$7hj$m7", {"Nome": "Manuela Cunha Rodrigues", "CPF": 23481866593, "CEP": 54340440, "Tel": 71035850},
            {1: ["Specialized", "Chisel", 10990, 2018, "Aprovada para o seguro"]}]
    }

def banco_de_dados():
    return {"admin": ["admin", {}, {}]}

def salvar_cadastro_no_bd(bd, dados):
    bd.update({dados[4]: [dados[5], {"Nome": dados[0], "CPF": dados[1], "CEP": dados[2], "Tel": dados[3]}]})

def cadastrar_bike_no_bd(num_bikes, bd, username):
    for i in range(num_bikes):
        print(f"\nPreencha o formulário abaixo com os dados da {i + 1}ª bicicleta:")
        marca = input("\nMarca da bicicleta: ")
        modelo = input("Modelo da bicicleta: ")
        valor = float(input("Valor da bicicleta: R$ "))
        ano_aquisicao = int(input("Ano de aquisição: "))
        status = validar_bike(ano_aquisicao, valor)
        if len(bd.get(username)) == 2:
            bd.get(username).append({1: [marca, modelo, valor, ano_aquisicao, status]})
        else:
            dict_bikes = bd.get(username)[2]
            chave = max(dict_bikes.keys()) + 1
            dict_bikes.update({chave: [marca, modelo, valor, ano_aquisicao, status]})

def validar_bike(ano, valor):
    if ano < 2013 or valor < 2000.0:
        return "Reprovada para o seguro"
    else:
        return "Aprovada para o seguro"

def listar_bikes(bd, username):
    dict_bikes = bd.get(username)[2]
    print("\t-- BICICLETAS CADASTRADAS --")
    for chave, valor in dict_bikes.items():
        print(f"\nBicicleta {chave} | Marca: {valor[0]} | Modelo: {valor[1]} | Valor: {valor[2]} | Ano de aquisição: {valor[3]} | {valor[4]}")

def definir_diretorio():
    return input("\nDigite o diretório no qual o relatório deve ser salvo: ")

def relatorio(bd_ex, dir):
    with open(f"{dir}/relatorio.txt", "w") as file:
        for chave in bd_ex.keys():
            dict_dados = bd_ex.get(chave)[1]
            dict_bikes = bd_ex.get(chave)[2]
            file.write(f"{dict_dados.get('Nome')}, CPF: {dict_dados.get('CPF')}, CEP: {dict_dados.get('CEP')}, Telefone: {dict_dados.get('Tel')}, {len(dict_bikes)} bike(s) cadastrada(s):\n")
            for dado in dict_bikes.values():
                file.write(f"{dado[0]} {dado[1]}, R$ {dado[2]}, {dado[3]}, {dado[4]}\n")
            file.write("--------------------------------------------------------------\n")

def main():
    bd = banco_de_dados()
    retornar_menu_sem_login = "S"
    while retornar_menu_sem_login == "S":
        opcao = menu_sem_login()
        match opcao:
            case 1:
                username, senha = login()
                if login_valido(bd, username, senha):
                    modo = view(username)
                    retornar_menu_com_login = "S"
                    while retornar_menu_com_login == "S":
                        if modo == "Cliente":
                            opcao = menu_com_login_usuario()
                            match opcao:
                                case 1:
                                    num_bikes = int(input("\nVocê deseja cotar o seguro de quantas bicicletas? "))
                                    cadastrar_bike_no_bd(num_bikes, bd, username)
                                    print("Os dados estão sendo analisados, consulte se sua bicicleta foi aprovado ao seguro na opção \"Exibir bicicletas cadastradas\" no menu.")
                                case 2:
                                    if len(bd.get(username)) > 2:
                                        listar_bikes(bd, username)
                                    else:
                                        print("\nNenhuma bicicleta foi registrada em nossos sistemas. Retorne ao menu e selecione a opção \"Cotar seguro\" para prosseguir.")
                                case 3:
                                    opcao = menu_infos()
                                    texto_infos(opcao)
                                case 4:
                                    break
                        else:
                            bd_ex = banco_de_dados_exemplo()
                            opcao = menu_com_login_admin()
                            match opcao:
                                case 1:
                                    dir = definir_diretorio()
                                    relatorio(bd_ex, dir)
                                    print("\nRelatório criado com sucesso.")
                                case 2:
                                    break
                        retornar_menu_com_login = input("\nRetornar ao menu? <S/N> ").upper()
                        while input_valido(retornar_menu_com_login, ["S", "N"]) == False:
                            retornar_menu_com_login = input("\nOpção inválida. Digite \"S\" ou \"N\" para prosseguir: ").upper()
                    break
                else:
                    print("Nome de usuário e/ou senha inválidos.")
            case 2:
                dados = cadastro(bd)
                salvar_cadastro_no_bd(bd, dados)
                print("Cadastro realizado com sucesso.")
            case 3:
                break
        retornar_menu_sem_login = input("\nRetornar ao menu? <S/N> ").upper()
        while input_valido(retornar_menu_sem_login, ["S", "N"]) == False:
            retornar_menu_sem_login = input("\nOpção inválida. Digite \"S\" ou \"N\" para prosseguir: ").upper()
    print("\nPrograma encerrado.")   

main()