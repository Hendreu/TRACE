# TRACE – Troco Real de Ajuste e Cálculo Eficiente 

TRACE é um sistema automatizado de cálculo de troco e ajuste financeiro, desenvolvido para facilitar o processo de gerenciamento de pagamentos, troco e inserção de valores em um banco de dados. Este sistema é ideal para ambientes de venda onde a precisão no cálculo do troco é crucial, e ele permite a inserção de diferentes tipos de cédulas e moedas, além de calcular o troco devido de maneira eficiente e automatizada.

---

## Objetivo do Sistema
O sistema TRACE serve para:
- Registrar e atualizar o valor das cédulas e moedas que entram em um caixa financeiro.
- Realizar o cálculo de troco de maneira automatizada, garantindo precisão no processo de devolução de valores.
- Ajustar o valor total disponível no caixa após cada operação, seja de inserção ou de pagamento.
- Armazenar os valores em um banco de dados (SQLite), permitindo o controle de cada tipo de cédula e moeda presente no caixa.

---

## Como o Sistema Funciona

### 1. Criação da Tabela de Dinheiro
O sistema começa criando uma tabela no banco de dados, caso ela não exista, para armazenar as cédulas e moedas presentes no caixa. Cada tipo de cédula ou moeda é registrado com seu valor e quantidade atual. Isso é feito na função `criaTabela()`.

Tipos de valores registrados incluem:  
- Notas de 200, 100, 50, 20, 10, 5, 2.  
- Moedas de 1, 0.50, 0.25, 0.10 e 0.05.

### 2. Inserção de Dinheiro no Caixa
O sistema permite que o usuário insira diferentes tipos de cédulas ou moedas através da função `inserirCaixa()`. O usuário seleciona o tipo de cédula ou moeda recebida, e o sistema registra a quantidade inserida no banco de dados, ajustando a quantidade total disponível de cada item.

### 3. Cálculo de Troco
Quando um pagamento é feito, o sistema calcula o troco automaticamente utilizando a função `calculaTroco()`.  
- O usuário insere o valor do pagamento e o valor do custo da compra.  
- O sistema determina a quantidade de cédulas e moedas necessárias para devolver o troco.

### 4. Soft Reset do Banco de Dados
O sistema oferece uma funcionalidade para realizar um "soft reset" no banco de dados, apagando o arquivo existente de forma simples e rápida. Isso é feito com a função `limparBanco()`, que remove o arquivo do banco de dados SQLite, permitindo recomeçar o gerenciamento financeiro a partir do zero.

```python
def limparBanco():
    os.remove("fluxoDeCaixa.db")
```

### 5. Interface e Funcionalidade do Menu
O sistema oferece uma interface simples baseada em texto que permite ao usuário escolher entre diferentes opções no menu, como:
1. Calcular o troco devido.  
2. Inserir cédulas ou moedas no caixa.  
3. Criar a tabela de valores no banco de dados.  
4. Realizar um soft reset apagando o banco de dados.  

Após cada operação, o sistema retorna ao menu principal, permitindo novas ações.

---

## Estrutura do Código

### Banco de Dados
O sistema utiliza o SQLite para armazenar as informações de cédulas e moedas, com a tabela `dinheiro`.

### Funções Principais
- **`criaTabela()`**: Cria a tabela de cédulas e moedas no banco de dados.
- **`inserirCaixa(volta)`**: Permite ao usuário inserir cédulas ou moedas no banco de dados.
- **`insercao(inserir, id)`**: Atualiza a quantidade de uma cédula ou moeda específica no banco de dados.
- **`calculaTroco()`**: Realiza o cálculo de troco, determinando quantas cédulas e moedas devem ser devolvidas.
- **`limparBanco()`**: Remove o arquivo de banco de dados existente, permitindo um reinício do sistema.
- **`menu()`**: Interface de navegação para o usuário.

---

## Benefícios
- **Precisão no Troco**: Automatiza o cálculo do troco, evitando erros humanos.  
- **Gerenciamento de Caixa**: Mantém os registros das cédulas e moedas sempre atualizados.  
- **Facilidade de Uso**: Interface intuitiva para usuários sem experiência técnica.  
- **Soft Reset**: Permite reiniciar o sistema rapidamente, ideal para reconfigurações.  
- **Escalabilidade**: Adaptável para diferentes negócios com necessidade de controle de dinheiro em caixa.  

---

## Tecnologias Utilizadas
- **SQLite**: Banco de dados leve utilizado para armazenamento de informações financeiras.  
- **Python**: Linguagem de programação para lógica de sistema e integração com o banco de dados.  

---

## Licença
Este projeto é licenciado sob a **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)**.  

Você tem permissão para:  
- Compartilhar: Copiar e redistribuir o material em qualquer formato ou mídia.  
- Adaptar: Remixar, transformar e criar a partir do material.  

**Sob as seguintes condições**:  
- **Atribuição**: É necessário dar o devido crédito ao autor do projeto.  
- **Uso Não Comercial**: Não é permitido o uso do material para fins comerciais sem permissão prévia.  

Para mais informações, consulte o texto completo da licença em [Creative Commons](https://creativecommons.org/licenses/by-nc/4.0/).  
