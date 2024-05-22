# pyestoque



# Controle de Estoque

Um sistema de controle de estoque desenvolvido em Python. Ele permite gerenciar produtos, fornecedores, clientes, vendas e muito mais, com uma interface intuitiva e fácil de usar.

## Índice

- [Instalação](#instalação)
- [Configuração](#configuração)
- [Uso](#uso)
- [Funcionalidades](#funcionalidades)
- [Contribuição](#contribuição)
- [Licença](#licença)

## Instalação

Siga os passos abaixo para instalar e configurar  no seu sistema.

### Passos Iniciais

1. **Instale o Python**
   - Baixe e instale o Python a partir de [python.org](https://www.python.org/).

2. **Adicione o Python ao PATH**
   - Durante a instalação, marque a opção para adicionar o Python ao PATH do sistema.

3. **Instale o PyCharm**
   - Baixe e instale o PyCharm a partir de [jetbrains.com/pycharm](https://www.jetbrains.com/pycharm/).

4. **Instale o WampServer**
   - Baixe e instale o WampServer a partir de [wampserver.com](https://www.wampserver.com/en/).

### Configuração do Banco de Dados

1. **Abra o WampServer** e inicie os serviços.
2. **Abra o phpMyAdmin**:
   - Acesse `http://localhost/phpmyadmin` no seu navegador.
3. **Importe a Base de Dados**:
   - Crie um novo banco de dados.
   - Importe o arquivo SQL da base de dados fornecido com o projeto.

### Instalação de Dependências

1. **Abra o terminal** e navegue até a pasta do projeto.
2. **Instale as dependências**:
   ```sh
   pip install -r requirements.txt
   ```
   - Caso o arquivo `requirements.txt` não exista, instale as dependências manualmente:
     ```sh
     pip install openpyxl mysql-connector-python
     ```

### Configuração da Aplicação

1. **Configure a conexão com o banco de dados**:
   - Abra o arquivo `config.py` (ou similar) e configure as credenciais do banco de dados conforme necessário.

## Uso

Para rodar o projeto:

1. **Inicie o WampServer** e certifique-se de que o banco de dados está rodando.
2. **Abra o PyCharm** e carregue o projeto.
3. **Execute o script principal**:
   - Encontre o arquivo `app.py` e execute-o.
   ```sh
   python app.py
   ```

## Funcionalidades

- **Gerenciamento de Produtos**: Cadastro, atualização e exclusão de produtos.
- **Controle de Fornecedores**: Cadastro e gerenciamento de fornecedores.
- **Cadastro de Clientes**: Registro e manutenção de informações dos clientes.
- **Monitoramento de Vendas**: Registro e acompanhamento das vendas.
- **Relatórios**: Geração de relatórios diversos.
- **Segurança**: Controle de acesso por nível de usuário (admin e colaborador).




