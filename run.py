from insertSQL import *

def calculaTroco():
    criaTabela()
    volta = 0
    conn = sqlite3.connect("fluxoDeCaixa.db")
    cursor = conn.cursor()

    custo = float(input("Custo foi de: \n"))
    print("Quantas cedulas/moedas foram usadas no pagamento?")

    pagamento = inserirCaixa(volta)
    pagamento = round(pagamento, 2)

    if pagamento < custo:
        pagamento = pagamento - custo
        print(f"Valor invalido! Faltando: {-pagamento} R$!")

    troco = pagamento - custo

    cursor.execute("SELECT * FROM dinheiro ORDER BY id_dinheiro ASC")
    notas = cursor.fetchall()
    for nota in notas:
        [id, nome, quantia, valor] = nota
        quantiaDeNotas = troco // valor
        if pagamento >= valor and quantia > 0:
            if quantia >= quantiaDeNotas:
                troco -= quantiaDeNotas * valor
                quantia -= quantiaDeNotas
                print(f"{quantiaDeNotas} notas de {valor}")
            else:
                troco -= quantia * valor
                quantia = 0
        troco = round(troco, 2)

        cursor.execute("UPDATE dinheiro SET quantia= ? WHERE id_dinheiro=?", (quantia,id))
    conn.commit()

    if troco > 0:
        print(f"Ainda falta devolver: {troco} de troco!")

def menu():
    opcao = int(input("""Selecione sua opção!
     1 Para calcular o troco
     2 Para inserir dinheiro no bando de dados
     3 Para criar tabela\n"""))
    match opcao:
        case 1:
            calculaTroco()
            return menu()
        case 2:
            inserirCaixa()
            return menu()
        case 3:
            criaTabela()
            return menu()
        case _:
            print("Opção Invalida! tente novamente.")
            return menu()

menu()