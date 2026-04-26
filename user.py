# - Definindo o usuário e suas permissões
# - O usuário comum poderá: ler as informações salvas retornadas do banco de dados e sugerir novos monstros para serem adicionados
# caso não estejam no bestiário

import sqlite3

class User:
    def __init__(self, name):
        self.name = name
        self.permission = "Leitura e Sugestão"
        self.bestiary = "bestiary_data.db"

    def confer(self, monster_name):
        # Consulta se o monstro existe no bestiário
        # Caso não exista, retorna uma mensagem informando que ele não está presente no bestiário
        print(f"[{self.name}] busca em seu bestiário por: {monster_name}. . .")

        try:
            connect = sqlite3.connect(self.bestiary)
            cursor = connect.cursor()

            # Cria a busca base pra previnir SQL Injection por segurança
            query = "SELECT id, name, _type, hp FROM monsters WHERE name = ?"
            cursor.execute(query, (monster_name,))
            result = cursor.fetchone()

            # Aqui definiremos o IF e o ELSE. Caso encontre o monstro procurado, ele retornará o monstro com uma mensagem dizendo que encontrou, caso contrário
            # ele vai retornar uma mensagem dizendo que não foi encontrado um monstro com aquele nome
            if result:
                id, name, _type, hp = result
                print(f"Um monstro foi encontrado! \n>> [{id}] | Nome: {name} (Tipo: {_type}) | Vida: {hp}")
            else:
                print(f"O monstro não foi encontrado. . . Talvez ele não conste nos registros do reino.")
            
            connect.close()
        
        except sqlite3.Error as e:
            print(f"Erro ao procurar o monstro: {e}")
    
    def list_monsters(self):
        print(f"{self.name} está verificando todos os monstros do bestiário. . .")

        monster_list = []

        try:
            connect = sqlite3.connect(self.bestiary)
            cursor = connect.cursor()

            query = "SELECT id, name, _type, hp FROM monsters"
            cursor.execute(query)
            results = cursor.fetchall()

            if not results:
                print(">> Não há registro de criaturas encontradas.")
                return []
            
            print("\n" + "-"*30)
            print("TODO BESTIÁRIO")
            print("-"*30)

            for line in results:
                id, name, _type, hp = line

                monster_dict = {
                    "id": id,
                    "name": name,
                    "_type": _type,
                    "hp": hp,
                }

                print(f"[ID: {id}] | Nome: {name} (Tipo: {_type}) | Vida: {hp}")

                monster_list.append(monster_dict)
                print("-"*30 + "\n")

            return monster_list
            connect.close()
            

        except sqlite3.Error as e:
            print(f"Erro: {e}")

    def suggest(self, suggestion):

        # Pode fazer uma sugestão caso um monstro que você tenha procurado não exista no bestiário
        print(f"[{self.name}] envia uma carta com a sugestão de um novo monstro ao Reino. O {suggestion['name']}. . .")

        try:
            connect = sqlite3.connect(self.bestiary)
            cursor = connect.cursor()

            query = "INSERT INTO suggests (name, _type, hp, suggested) VALUES (?, ?, ?, ?)"
            values = (
                suggestion['name'],
                suggestion['_type'],
                suggestion['hp'],
                self.name
            )
            cursor.execute(query, values)
            connect.commit()

            connect.close()

            print(f"Sugestão enviada com sucesso! Os administradores irão avaliar ela.\n\n>> Nome: {suggestion['name']} (Tipo: {suggestion['_type']}) | Vida: {suggestion['hp']} | Sugerida por: {self.name}\n")

        except sqlite3.Error as e:
            print(f"Erro ao enviar sugestão: {e}")