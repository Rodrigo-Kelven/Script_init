# Criador de Arquivos `__init__.py`
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 


Este script Python percorre um diretório base e seus subdiretórios, criando arquivos `__init__.py` em todos os diretórios que não os possuem.
O arquivo `__init__.py` é um arquivo especial em Python que indica que o diretório deve ser tratado como um pacote Python. Este script foi criado especialmente para "salvar" o tempo na criação de diversos arquivos desses nos diversos diretorios
que posso existir no seu projeto.

## Funcionalidade

- **Percorre Diretórios**: O script utiliza a função `os.walk()` para percorrer todos os diretórios e subdiretórios a partir de um diretório base especificado.
- **Criação de Arquivos**: Para cada diretório que não contém um arquivo `__init__.py`, o script cria um novo arquivo e escreve um comentário padrão indicando que o diretório é um pacote Python.
- **Saída Informativa**: O script imprime o caminho de cada arquivo `__init__.py` criado, permitindo que o usuário saiba quais diretórios foram modificados.

## Pré-requisitos

- Python 3.x
- Acesso ao sistema de arquivos para criar arquivos e diretórios.

## Uso

1. **Clone o Repositório** ou **Baixe o Script**:
   ```bash
   git clone https://github.com/Rodrigo-Kelven/Script_init
   cd Script_init
   python3 script.py

## Atenção!
### Este script deve ser executado na pasta raiz! Segue o exemplo abaixo.
      ```bash 
    .
    ├── __pycache__
    │   └── __init__.cpython-312.pyc
    ├── README.md
    ├── script.py
    └── src
        ├── auth
        │   ├── auth.py
        │   ├── config
        │   │   ├── config_db.py
        │   │   ├── config.py
        │   │   ├── __init__.py
        │   │   └── __pycache__
        │   │       ├── config.cpython-312.pyc
        │   │       ├── config_db.cpython-312.pyc
        │   │       ├── __init__.cpython-312.pyc
        │   │       └── __init__.py
        │   ├── controllers
        │   │   ├── __init__.py
        │   │   ├── __pycache__
        │   │   │   ├── __init__.cpython-312.pyc
        │   │   │   ├── __init__.py
        │   │   │   ├── route_user.cpython-312.pyc
        │   │   │   └── works.cpython-312.pyc
        │   │   ├── route_user.py
        │   │   └── works.py
        │   ├── __init__.py
        │   ├── models
        │   │   ├── __init__.py
        │   │   ├── __pycache__
        │   │   │   ├── __init__.cpython-312.pyc
        │   │   │   ├── __init__.py
        │   │   │   └── users.cpython-312.pyc
        │   │   └── users.py
        │   ├── __pycache__
        │   │   ├── auth.cpython-312.pyc
        │   │   ├── __init__.cpython-312.pyc
        │   │   └── __init__.py
        │   ├── schemas
        │   │   ├── __init__.py
        │   │   ├── __pycache__
        │   │   │   ├── __init__.cpython-312.pyc
        │   │   │   ├── __init__.py
        │   │   │   └── user.cpython-312.pyc
        │   │   └── user.py
        │   └── services
        │       ├── __init__.py
        │       ├── __pycache__
        │       │   ├── __init__.cpython-312.pyc
        │       │   ├── __init__.py
        │       │   └── services.cpython-312.pyc
        │       └── services.py
        ├── Banco_de_Dados
        │   └── __init__.py
        ├── config
        │   ├── config_db.py
        │   ├── config.py
        │   ├── __init__.py
        │   └── __pycache__
        │       ├── config.cpython-312.pyc
        │       ├── config_db.cpython-312.pyc
        │       ├── __init__.cpython-312.pyc
        │       └── __init__.py
        ├── controllers
        │   ├── all_routes.py
        │   ├── __init__.py
        │   ├── __pycache__
        │   │   ├── all_routes.cpython-312.pyc
        │   │   ├── __init__.cpython-312.pyc
        │   │   ├── __init__.py
        │   │   ├── rota_home.cpython-312.pyc
        │   │   ├── rotas_books.cpython-312.pyc
        │   │   └── rotas_users.cpython-312.pyc
        │   ├── rota_home.py
        │   └── rotas_books.py
        ├── __init__.py
        ├── main.py
        ├── models
        │   ├── books.py
        │   ├── __init__.py
        │   └── __pycache__
        │       ├── books.cpython-312.pyc
        │       ├── __init__.cpython-312.pyc
        │       ├── __init__.py
        │       └── users.cpython-312.pyc
        ├── __pycache__
        │   ├── __init__.cpython-312.pyc
        │   ├── __init__.py
        │   └── main.cpython-312.pyc
        ├── requirements.txt
        ├── schemas
        │   ├── books.py
        │   ├── __init__.py
        │   └── __pycache__
        │       ├── books.cpython-312.pyc
        │       ├── __init__.cpython-312.pyc
        │       ├── __init__.py
        │       └── schemas.cpython-312.pyc
        ├── service
        │   ├── __init__.py
        │   ├── __pycache__
        │   │   ├── __init__.cpython-312.pyc
        │   │   ├── __init__.py
        │   │   └── services.cpython-312.pyc
        │   └── services.py
