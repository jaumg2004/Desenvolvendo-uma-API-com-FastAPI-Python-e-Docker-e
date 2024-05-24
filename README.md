# Desenvolvendo-uma-API-com-FastAPI-Python-e-Docker


# Descrição resumida:
WorkoutAPI é uma API de treino para competições de crossfit, combinando duas paixões: codificação e treinamento. Ela é projetada para ser prática e simplificada, com uma modelagem de entidade e relacionamento (MER) enxuta. A pilha da API inclui FastAPI (async), juntamente com alembic, SQLAlchemy e pydantic. Os dados são armazenados no PostgreSQL via Docker.

# Execução:
Para executar o projeto, é utilizado pyenv com Python 3.11.4 em um ambiente virtual. Após a instalação do pyenv, execute os comandos para configurar o ambiente e instalar os requisitos. Para iniciar o banco de dados, utilize o Docker Compose. As migrações do banco de dados podem ser criadas e executadas conforme necessário.

# Desafio Final:

Adição de query parameters nos endpoints para filtrar atletas por nome ou CPF.
Personalização da resposta dos endpoints "get all" para incluir nome do atleta, centro de treinamento e categoria.
Manipulação de exceções de integridade dos dados em cada módulo/tabela, retornando uma mensagem específica e um status_code 303 em caso de violação.
Adição de paginação utilizando fastapi-pagination com os parâmetros limit e offset.
# Referências:

FastAPI: https://fastapi.tiangolo.com/
Pydantic: https://docs.pydantic.dev/latest/
SQLAlchemy: https://docs.sqlalchemy.org/en/20/
Alembic: https://alembic.sqlalchemy.org/en/latest/
Paginação FastAPI: https://uriyyo-fastapi-pagination.netlify.app/
