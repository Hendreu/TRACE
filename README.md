# **TRACE – Troco Real de Ajuste e Cálculo Eficiente**

**TRACE** é um sistema automatizado de cálculo de troco e ajuste financeiro, desenvolvido para facilitar o processo de gerenciamento de pagamentos, troco e inserção de valores em um banco de dados. Este sistema é ideal para ambientes de venda onde a precisão no cálculo do troco é crucial, e ele permite a inserção de diferentes tipos de cédulas e moedas, além de calcular o troco devido de maneira eficiente e automatizada.

## **Objetivo do Sistema**

O sistema **TRACE** serve para:

1. **Registrar e atualizar o valor das cédulas e moedas** que entram em um caixa financeiro.
2. **Realizar o cálculo de troco** de maneira automatizada, garantindo precisão no processo de devolução de valores.
3. **Ajustar o valor total** disponível no caixa após cada operação, seja de inserção ou de pagamento.
4. **Armazenar os valores em um banco de dados** (SQLite), permitindo o controle de cada tipo de cédula e moeda presente no caixa.

## **Como o Sistema Funciona**

### **1. Criação da Tabela de Dinheiro**

O sistema começa criando uma tabela no banco de dados, caso ela não exista, para armazenar as cédulas e moedas presentes no caixa. Cada tipo de cédula ou moeda é registrado com seu valor e quantidade atual. Isso é feito na função `criaTabela()`.

- Tipos de valores registrados incluem: Notas de 200, 100, 50, 20, 10, 5, 2, Moedas de 1, 0.50, 0.25, 0.10 e 0.05.

### **2. Inserção de Dinheiro no Caixa**

O sistema permite que o usuário insira diferentes tipos de cédulas ou moedas através da função `inserirCaixa()`. O usuário seleciona o tipo de cédula ou moeda recebida, e o sistema registra a quantidade inserida no banco de dados, ajustando a quantidade total disponível de cada item.

- O processo de inserção inclui a atualização do valor total do caixa e a gravação dos novos valores na tabela.

### **3. Cálculo de Troco**

Quando um pagamento é feito, o sistema calcula o troco automaticamente utilizando a função `calculaTroco()`. O usuário insere o valor do pagamento e o valor do custo da compra, e o sistema determina a quantidade de cédulas e moedas necessárias para devolver o troco.

- O sistema utiliza a tabela criada anteriormente para verificar a quantidade de cédulas e moedas disponíveis e calcular a melhor combinação para o troco.
- A função lida com a redução das quantidades de cédulas ou moedas à medida que o troco é devolvido ao cliente.

### **4. Interface e Funcionalidade do Menu**

O sistema oferece uma interface simples baseada em texto que permite ao usuário escolher entre diferentes opções no menu, como:

- Calcular o troco devido (`1`).
- Inserir cédulas ou moedas no caixa (`2`).
- Criar a tabela de valores no banco de dados (`3`).

Após o processamento de cada operação, o sistema retorna ao menu principal, permitindo que novas ações sejam realizadas.

## **Estrutura do Código**

1. **Criação de Banco de Dados**: O sistema usa o SQLite para armazenar as informações de cédulas e moedas, com a tabela `dinheiro`.
2. **Funções Principais**:
   - `criaTabela()`: Cria a tabela de cédulas e moedas no banco de dados.
   - `inserirCaixa(volta)`: Permite ao usuário inserir cédulas ou moedas no banco de dados.
   - `insercao(inserir, id)`: Atualiza a quantidade de uma cédula ou moeda específica no banco de dados.
   - `calculaTroco()`: Realiza o cálculo de troco, determinando quantas cédulas e moedas devem ser devolvidas.
   - `menu()`: Interface de navegação simples para o usuário interagir com o sistema.

## **Benefícios**

- **Precisão no Troco**: O sistema automatiza o cálculo do troco, evitando erros humanos e aumentando a eficiência.
- **Gerenciamento de Caixa**: Controla a quantidade de cédulas e moedas no caixa, garantindo que os registros sejam sempre atualizados.
- **Facilidade de Uso**: A interface simples e intuitiva facilita a interação do usuário, mesmo para quem não tem experiência com sistemas complexos.
- **Escalabilidade**: Pode ser facilmente adaptado para diferentes tipos de negócios que precisem de um controle preciso de dinheiro em caixa.

## **Tecnologias Utilizadas**

- **SQLite**: Banco de dados leve utilizado para armazenar informações sobre cédulas e moedas.
- **Python**: Linguagem de programação usada para implementar a lógica do sistema, incluindo interação com o banco de dados e cálculos automatizados.

---

Com isso, o **TRACE – Troco Real de Ajuste e Cálculo Eficiente** é uma solução robusta para empresas que buscam automatizar o processo de cálculo de troco e o gerenciamento de cédulas e moedas no caixa, melhorando a eficiência operacional e reduzindo erros financeiros.
