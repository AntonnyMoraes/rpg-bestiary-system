import os
from user import User
from admin import Admin
# Sistema de Bestiário para RPG (Role-Playing Game)
# Possui dois lados do sistema, o lado do usuário e do administrador.

clean = "cls" if os.name == "nt" else "clear"

while True:
    os.system(clean)
    print("-- INICIALIZANDO SISTEMA DO BESTIÁRIO --")
    print("1 - Usuário\n2 - Admin\n3 - Sair")
    opc = input("Digite a opção: ")

    match opc:
        # Lado do Usuário do sistema
        case "1":
            os.system(clean)
            print("Olá usuário, como você se chama?")
            user = User(input())

            check = "y"

            while check == "y":
                os.system(clean)
                print("-- SISTEMA DO USUÁRIO --")
                print("1 - Pesquisar no bestiário\n2 - Sugerir nova criatura\n3 - Listar todas as criaturas\n4 - Voltar a tela inicial")
                opc2 = input("Digite a opção: ")
                match opc2:
                    case "1":
                        os.system(clean)
                        print("Qual o nome da criatura que você procura?")
                        name = input()
                        user.confer(name)

                        print("\nPressione ENTER para sair")
                        hold = input()
                    
                    case "2":
                        os.system(clean)
                        print("Deseja fazer uma sugestão? Que ótimo!")
                        suggestion = {
                            "name": input("Digite o nome da criatura: "),
                            "_type": input("Digite o tipo da criatura: "),
                            "hp": int(input("Digite a quantidade de vida da criatura: "))
                        }

                        user.suggest(suggestion)

                        hold = input()
                    
                    case "3":
                        os.system(clean)
                        user.list_monsters()

                        hold = input()

                    case _:
                        check = "n"
        
        # Lado do Administrador do sistema
        case "2":
            os.system(clean)
            print("Olá Admin, como você se chama?")
            adm = Admin(input())

            check = "y"

            while check == "y":
                os.system(clean)
                print("-- SISTEMA DO ADMINISTRADOR --")
                print("1 - Ler todas as sugestões\n2 - Aprovar sugestão\n3 - Recusar sugestão\n4 - Buscar no bestiário\n5 - Listar todo bestiário\n6 - Adicionar criatura ao bestiário\n7 - Deletar criatura do bestiário\n8 - Modificar criatura do bestiário\n9 - Voltar a tela inicial")
                opc2 = input("Digite a opção: ")

                match opc2:
                    case "1":
                        os.system(clean)
                        adm.list_sug()

                        hold = input()
                    
                    case "2":
                        os.system(clean)

                        check2 = input("Você sabe qual o ID da sugestão? (y/n) ")

                        if check2 == "y":
                            id_sug = int(input("Digite o ID da sugestão: "))
                            adm.approve_suggestion(id_sug)

                        hold = input()
                    
                    case "3":
                        os.system(clean)

                        check2 = input("Você sabe qual o ID da sugestão? (y/n) ")

                        if check2 == "y":
                            id_sug = int(input("Digite o ID da sugestão: "))
                            adm.recuse_suggestion(id_sug)
                        
                        hold = input()
                    
                    case "4":
                        os.system(clean)
                        print("Qual o nome da criatura que você deseja procurar?")
                        monster_name = input()

                        adm.confer(monster_name)

                        hold = input()

                    case "5":
                        os.system(clean)
                        adm.list_monsters()

                        hold = input()

                    case "6":
                        os.system(clean)
                        print(f"{adm.name} você deseja adicionar uma nova criatura?")
                        monster_name = input("Nome da criatura: ")
                        monster_type = input("Tipo da criatura: ")
                        monster_hp = int(input("Quantidade de vida da criatura: "))

                        adm.add_monster(monster_name,monster_type,monster_hp)

                        hold = input()

                    case "7":
                        os.system(clean)
                        check2 = input("Você sabe o ID da criatura que deseja apagar? (y/n) ")

                        if check2 == "y":
                            monster_id = input("Digite o ID do monstro: ")
                            adm.del_monster(monster_id)

                        hold = input()

                    case "8":
                        os.system(clean)
                        check2 = input("Você sabe o ID do monstro que quer modificar? (y / n) ")

                        if check2 == "y":
                            monster_id = input("Digite o ID do monstro: ")
                            adm.mod_monster(monster_id)

                        hold = input()

                    case _:
                        check = "n"
        
        case _:
            break

os.system(clean)