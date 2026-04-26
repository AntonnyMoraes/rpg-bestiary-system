# 🐉 Sistema de Bestiário RPG (Python + SQLite)

Um sistema de gerenciamento de banco de dados (CRUD) construído em Python puro, focado em automatizar e organizar o bestiário de mesas de RPG. 

Este projeto foi desenvolvido para demonstrar habilidades práticas em **Lógica de Programação, Manipulação de Banco de Dados Relacionais, e Programação Orientada a Objetos**, simulando um ambiente de backend de uma aplicação real.

## 🛠️ Tecnologias e Ferramentas Utilizadas
* **Python 3.10+** (Lógica de negócios, estruturação em classes com herança, e *Structural Pattern Matching*).
* **SQLite3** (Banco de dados relacional embarcado).
* **Git / GitHub** (Versionamento de código).

## ⚙️ Funcionalidades e Arquitetura

O sistema implementa o princípio de **Separação de Responsabilidades**, dividindo o fluxo de interface do usuário (`main.py`) das lógicas de regra de negócio e banco de dados.

O banco de dados possui uma arquitetura de aprovação contendo duas tabelas interligadas:
1.  **Usuário Base (`user.py`):** Pode consultar o bestiário oficial (`SELECT`) e sugerir novas criaturas (`INSERT` na tabela de Sugestões).
2.  **Administrador (`admin.py`):** Herda os métodos do Usuário Base, mas possui permissões totais (CRUD completo). Pode aprovar sugestões pendentes (Movendo dados entre tabelas usando `SELECT`, `INSERT` e `DELETE`), atualizar pontos de vida de monstros existentes (`UPDATE`) e listar o banco de dados.

## 🚀 Como executar o projeto

1. Clone este repositório:
   `git clone https://github.com/seu_usuario/seu_repositorio.git`
2. Navegue até a pasta do projeto e inicie o banco de dados executando o script de configuração:
   `python controller_db.py`
3. Inicie o menu interativo do sistema:
   `python main.py`

## 💡 Próximos Passos (Melhorias Futuras)
* Integração com a API do Discord (`discord.py`) para transformar o sistema em um Bot acessível durante as partidas de RPG online.
* Consumo de APIs externas (ex: *D&D 5e API*) para popular o banco de dados automaticamente.