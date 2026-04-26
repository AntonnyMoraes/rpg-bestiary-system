# - Definimos o Admin e suas permissões
# - Ele poderá: Ler as sugestões, verificar um monstro, adicionar um monstro, deletar um monstro, adicionar a sugestão ao bestiário
# modificar monstros que já existem

import sqlite3
from user import User

class Admin(User):
    def __init__(self, name):
        super().__init__(name)
        self.permission = "Total"
    
    def approve_suggestion(self, suggestion_id):
        print(f"[{self.name}] está aprovando a sugestão: {suggestion_id}")

        try:
            connect = sqlite3.connect(self.bestiary)
            cursor = connect.cursor()

            query = "SELECT id, name, _type, hp, suggested FROM suggests WHERE id = ?"
            cursor.execute(query, (suggestion_id,))
            result = cursor.fetchone()

            if result:
                id, name, _type, hp, suggested = result
                print(f"Sugestão encontrada! >> ID da sugestão: {id} | Nome do Monstro: {name} (Tipo: {_type}) | Vida: {hp} | Sugestão de: {suggested} \nDeseja aprovar ela (y / n)?")
                opc = str( input())

                if opc == "y":
                    query2 = "INSERT INTO monsters (name, _type, hp) VALUES (?, ?, ?)"
                    cursor.execute(query2, (name, _type, hp))

                    query_delete = "DELETE FROM suggests WHERE id = ?"
                    cursor.execute(query_delete, (suggestion_id,))

                    connect.commit()
                    connect.close()
                    print(f"O monstro {name} foi adicionado ao bestiário com sucesso! E a sugestão foi retirada da lista.")
                elif opc == "n":
                    print("Aprovação cancelada!")
                else:
                    print("Erro: Digite uma opção valida!")
            else:
                print(f"Sugestão: {suggestion_id} não foi encontrada!")
        
        except sqlite3.Error as e:
            print(f"Erro: {e}")

    def list_sug(self):
        print(f"{self.name} está verificando todas as sugestões de monstros ao bestiário. . .")

        suggest_list = []

        try:
            connect = sqlite3.connect(self.bestiary)
            cursor = connect.cursor()

            query = "SELECT id, name, _type, hp, suggested FROM suggests"
            cursor.execute(query)
            results = cursor.fetchall()

            if not results:
                print(">> Nenhuma sugestão encontrada.")
                return []
            
            print("\n" + "-"*20)
            print("FILA DE APROVAÇÃO DO BESTIÁRIO")
            print("-"*20)

            for line in results:
                suggestion_id, name, _type, hp, suggested = line

                suggest_dict = {
                    "id": suggestion_id,
                    "name": name,
                    "_type": _type,
                    "hp": hp,
                    "suggested": suggested
                }

                print(f"[ID: {suggestion_id}] | Nome: {name} (Tipo: {_type}) | Vida: {hp} | Sugerido por: {suggested}")

                suggest_list.append(suggest_dict)
                print("-"*20 + "\n")

            return suggest_list
            connect.close()
            

        except sqlite3.Error as e:
            print(f"Erro: {e}")
    
    def recuse_suggestion(self, suggestion_id):
        print(f"[{self.name}] está cancelando uma das sugestões. . .")

        try:
            connect = sqlite3.connect(self.bestiary)
            cursor = connect.cursor()

            query = "SELECT id, name, _type, hp, suggested FROM suggests WHERE id = ?"
            cursor.execute(query, (suggestion_id,))
            result = cursor.fetchone()

            if result:
                id, name, _type, hp, suggested = result
                print(f"[{id}] | Nome: {name} (Tipo: {_type}) | Vida: {hp} | Sugerido por: {suggested}\nDeseja cancelar essa sugestão? (y / n)")
                opc = input()

                if opc == "y":
                    query_delete = "DELETE FROM suggests WHERE id = ?"
                    cursor.execute(query_delete, (suggestion_id,))
                    connect.commit()

                    print(f"A sugestão [{id}] - Nome: {name} foi cancelada!")
            
            connect.close()
        
        except sqlite3.Error as e:
            print(f"Erro: {e}")

    def add_monster(self, monster_name, monster_type, monster_hp):
        print(f"[{self.name}] deseja adicionar uma nova criatura ao bestiário.")

        try:
            connect = sqlite3.connect(self.bestiary)
            cursor = connect.cursor()
            
            query = "INSERT INTO monsters (name, _type, hp) VALUES (?, ?, ?)"
            cursor.execute(query, (monster_name, monster_type, monster_hp))
            connect.commit()

            print(f"[{self.name}] anotou as informações sobre o [{monster_name}] no bestiário!\n>> Nome: {monster_name} (Tipo: {monster_type}) | Vida: {monster_hp}")

            connect.close()
        
        except sqlite3.Error as e:
            print(f"Erro: {e}")

    def del_monster(self, monster_id):
        print(f"[{self.name}] enviou uma requisição de remoção do bestiário!")

        try:
            connect = sqlite3.connect(self.bestiary)
            cursor = connect.cursor()

            query = "SELECT id, name, _type, hp FROM monsters WHERE id = ?"
            cursor.execute(query, (monster_id,))
            result = cursor.fetchone()

            if result:
                id, name, _type, hp = result
                print(f"Criatura encontrada!\n>> ({id}) | Nome: {name} (Tipo: {_type}) | Vida: {hp}")
                print("Deseja prosseguir com a exclusão? (y / n)")
                opc = str( input())

                if opc == "y":
                    query_del = "DELETE FROM monsters WHERE id = ?"
                    cursor.execute(query_del, (id,))
                    print(f"{name} foi retirado do bestiário!")
                    connect.commit()
                elif opc == "n":
                    print("Cancelando exclusão. . . ")
                else:
                    print("Digite uma opção válida!")
            
            else:
                print("Nenhum monstro encontrado com esse nome!")

            connect.close()

        except sqlite3.Error as e:
            print(f"Erro: {e}")
    
    def mod_monster(self, monster_id):
        print(f"[{self.name}] está modificando informações do bestiário. . .")

        try:
            connect = sqlite3.connect(self.bestiary)
            cursor = connect.cursor()

            query = "SELECT id, name, _type, hp FROM monsters WHERE id = ?"
            cursor.execute(query, (monster_id,))
            result = cursor.fetchone()

            if result:
                id, name, _type, hp = result
                print(f"Criatura encontrada!\n>> Nome: {name} (Tipo: {_type}) | Vida: {hp}")
                print("Se você desejar manter os valores atuais, apenas pressione ENTER!")
                name2 = input("Novo nome: ")
                _type2 = input("Novo tipo: ")
                hp2 = input("Novo HP: ")

                fname = name2 if name2 != "" else name
                ftype = _type2 if _type2 != "" else _type
                fhp = int(hp2) if hp2 != "" else hp
                
                query_upd = "UPDATE monsters SET name = ?, _type = ?, hp = ? WHERE id = ?"
                
                cursor.execute(query_upd, (fname, ftype, fhp, id))
                connect.commit()

                print(f"Novas informações no bestiário, agora o [{id}] possui as seguintes informações >> Nome: {fname} (Tipo: {ftype}) | Vida: {fhp}")
            else:
                print("Criatura não encontrada no bestiário")
            
            connect.close()

        except sqlite3.Error as e:
            print(f"Erro: {e}")