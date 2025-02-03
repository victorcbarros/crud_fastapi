# PROJETO DE CRUD COM FASTAPI E STREAMLIT - SISTEMA DE GERENCIAMENTO DE VEÍCULOS


![CRUD](images/CRUD.gif)


## 📌 Introdução 
Este projeto tem como objetivo desenvolver um CRUD para um sistema de gerenciamento de veículos de uma locadora fictícia, a CB Rent. 
O sistema permite cadastrar novos veículos, visualizar todos os veículos registrados, consultar um veículo específico pelo ID, 
atualizar informações e remover veículos do banco de dados.

![Frontend](images/crud%20frontend.png)


Para a implementação, foi utilizada a linguagem Python, com FastAPI no backend e Streamlit no frontend,
proporcionando uma interface interativa e responsiva. Além disso, os dados são armazenados em um banco de dados PostgreSQL,
garantindo eficiência e segurança no gerenciamento das informações.

![Frontend](images/crud%20backend.png)

## 🧰 Objetivo do Projeto
O objetivo deste projeto é desenvolver um CRUD para um sistema de gerenciamento de veículos da locadora fictícia CB Rent. 
A aplicação permite cadastrar, visualizar, atualizar e excluir veículos de forma eficiente e segura. Com isso,
busca-se facilitar a administração da frota da locadora, garantindo um controle mais ágil e organizado das informações dos veículos.


## ⚙️ Arquitetura e Tecnologias Utlizadas
A arquitetura do projeto segue uma abordagem **modular e escalável**, garantindo uma separação clara entre frontend, backend e banco de dados. O sistema é composto pelos seguintes componentes:  

![Diagrama do Projeto](images/diagrama%20do%20crud.png)


- **Backend**: Desenvolvido em **FastAPI**, garantindo alta performance e fácil integração com APIs modernas.  
- **Frontend**: Construído com **Streamlit**, proporcionando uma interface interativa e acessível para os usuários.  
- **Banco de Dados**: Utilização do **PostgreSQL** para armazenar e gerenciar as informações dos veículos de forma segura e eficiente.  
- **ORM (Object-Relational Mapping)**: Implementado com **SQLAlchemy**, facilitando a interação com o banco de dados.  
- **Validação de Dados**: Feita com **Pydantic**, garantindo a integridade e consistência das informações manipuladas pelo sistema.  
- **Gerenciamento de Dependências**: Utilização do **Poetry** para facilitar a organização e versionamento das bibliotecas do projeto.  
- **Containerização**: O sistema é executado em **Docker**, garantindo portabilidade e facilidade de implantação.  

Essa arquitetura permite escalabilidade e manutenção simplificada, tornando o sistema robusto e eficiente para o gerenciamento da frota da locadora. 🚗💨  

## 🗂 Estrutura do Projeto
A estrutura de diretórios do projeto foi organizada da seguinte forma:
```
├── README.md # 
├── backend 
├── frontend 
├── docker-compose.yml 
├── poetry.lock 
└── pyproject.toml 
```
## 🛠 Como Executar o Projeto

Este projeto está disponível no repositório do GitHub. A aplicação foi desenvolvida utilizando **Docker**, garantindo uma implantação simples e rápida.

🔗 **[CB Rent - Sistema de Gerenciamento de Veículos](https://github.com/seu-repositorio)**

### 📌 Pré-requisitos

Antes de executar o projeto, certifique-se de ter os seguintes programas instalados em sua máquina:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### 🛠️ Passos para Execução

Siga os passos abaixo para executar o projeto em seu ambiente local:

#### 1. **Clonar o Repositório**

Primeiro, clone o repositório para a sua máquina local:

```bash
git clone https://github.com/seu-repositorio.git
cd seu-repositorio

```

#### 2. **Construir e Iniciar os Containers com Docker Compose**
Com o repositório clonado, crie e inicie os containers utilizando o Docker Compose:
```bash
docker-compose up -d

```
Esse comando irá construir e executar os containers em segundo plano.

#### 3. **Construir e Iniciar os Containers com Docker Compose**
Agora, você pode acessar a API no navegador ou por meio do seu navegador utilizando a URL abaixo ou atraves de uma ferramenta como o Postman. A documentação da API estará disponível em:

```bash
http://localhost:8000/docs
```

#### 4. **Acessar o Frontend**
Abra a interface do usuário (frontend) no navegador. Ela estará disponível em:

```bash
http://localhost:8501/
```

#### 5. **Parar os Containers**
Quando terminar, você pode parar os containers utilizando o comando:

```bash
docker-compose down
```
Este comando irá parar e remover todos os containers criados.


## 🏁 Conclusão

O projeto **CB Rent - Sistema de Gerenciamento de Veículos** foi desenvolvido como parte pratica  do **Bootcamp de Python da Jornada de Dados** do **Luciano Vasconcelos Filho**.

Este projeto foi uma excelente oportunidade para aplicar na prática os conhecimentos adquiridos, criando um sistema de gerenciamento de veículos robusto e eficiente para uma locadora fictícia, com funcionalidades como cadastro, visualização, atualização e remoção de veículos.

A utilização de **Docker Compose** facilitou a configuração e execução do ambiente de desenvolvimento, proporcionando uma execução mais simples e rápida, sem a necessidade de configurações manuais complexas.

Agradeço por explorar este projeto! Caso tenha sugestões de melhorias, novas funcionalidades ou queira contribuir de alguma forma, fique à vontade para abrir uma **issue** ou criar um **pull request**. 




