# 🐍 PythonAPICalculator
Faça contas matemáticas básicas utilizando uma API em Python.

# 📱 Projeto
Essa API foi criada para exemplificar o uso de uma API básica com rotas para duas operações, soma de inteiros em um mesmo vetor e media aritmética dos numeros inteiros em um mesmo vetor com resultado em float. Tudo sendo feito utilizando um framework atual. A API é muito leve e mostra a possibilidade de escalonar as rotas e demostra o uso de uma autenticação para usuários, oferecendo uma primeira segurança mínima na aplicação.

# ⚙️ Tecnologias
* Python

* Django

* Django REST framework

# 🧪 Como Testar
Para testar o PythonAPICalculator, siga estas etapas:

1. Clone o repositório.

2. Abra o repositório no seu VSCode ou compilador favorito.

3. Execute o arquivo requirements.txt com o comando: pip install -r requirements.txt.

4. Com todos os requisitos instalados e dentro do repositório aberto no seu compilador, ative o ambiente virtual com o comando:
    * No Windows: venv\Scripts\activate ou venv\Scripts\Activate.ps1
    * No Linux: source venv/bin/activate

5. Com o ambiente virtual ativado, use o comando: python manage.py runserver para iniciar o servidor e acessar a aplicação.

6. Abra o link fornecido no seu terminal no navegador.

![image](https://github.com/user-attachments/assets/77e1d455-7cd4-496d-a745-d8416f2505ad)


# 🎉 Exemplo de Resultado

![image](https://github.com/user-attachments/assets/62237b37-608a-4a2b-935a-981e6694c30a)

O usuário só acessa a aplicação com uma conta. Foi criada a conta:

* Usuário: rafael
* Senha: rafael123
  
Essa conta é apenas para fins de demonstração.

# 🚫 Login Bloqueado

Caso, por algum motivo, não seja possível acessar a aplicação por conta da autenticação, é possível remover essa camada de segurança na aplicação em settings.py:

![image](https://github.com/user-attachments/assets/872efc4a-c220-4588-b031-f1d84ca47f0f)

Basta ir no arquivo settings.py e remover completamente o conteúdo relacionado à configuração REST_FRAMEWORK.

# 🔐 Login Feito

![image](https://github.com/user-attachments/assets/de6b9415-1ab9-45b3-8bf2-ea621a4ef22f)

Aqui é possível escolher a rota e testar diretamente na aplicação com um POST.



# 📝 Formato Permitido para Testes
Todas as requisições devem ser feitas em formato JSON, conforme o exemplo abaixo:

![image](https://github.com/user-attachments/assets/09352a84-39ff-4467-8a97-564533002a41)

Requisições fora desse formato resultarão em erro na resposta.

