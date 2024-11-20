import sqlite3
import time

def criaTabela():
    conn = sqlite3.connect("fluxoDeCaixa.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS dinheiro(
        id_dinheiro INTEGER PRIMARY KEY AUTOINCREMENT, tipo_dinheiro VARCHAR(20), quantia INTEGER, valor REAL)
        """)

    tipos_dinheiro = [
        ("NotaDe200", 0, 200),
        ("NotaDe100", 0, 100),
        ("NotaDe50", 0, 50),
        ("NotaDe20", 0, 20),
        ("NotaDe10", 0, 10),
        ("NotaDe5", 0, 5),
        ("NotaDe2", 0, 2),
        ("MoedaDe1", 0, 1),
        ("MoedaDe0.50", 0, 0.50),
        ("MoedaDe0.25", 0, 0.25),
        ("MoedaDe0.10", 0, 0.10),
        ("MoedaDe0.05", 0, 0.05)
    ]

    for tipo, quantia, valor in tipos_dinheiro:
        cursor.execute("SELECT COUNT(*) FROM dinheiro WHERE tipo_dinheiro = ?", (tipo,))
        count = cursor.fetchone()[0]
        if count == 0:
            cursor.execute("INSERT INTO dinheiro (tipo_dinheiro, quantia, valor) VALUES (?, ?, ?)", (tipo, quantia, valor))
            conn.commit()

def inserirCaixa(volta):
    criaTabela()

    select = int(input("""Digite a opção desejada:
1	NotaDe200
2	NotaDe100
3	NotaDe50
4	NotaDe20
5	NotaDe10
6	NotaDe5
7	NotaDe2
8	MoedaDe1
9	MoedaDe0.50
10	MoedaDe0.25
11	MoedaDe0.10
12	MoedaDe0.05	
Qualquer outro valor Para continuar\n"""))

    match select:
        case 1:
            deposito = int(input("Quantas notas foram recebidas?\n"))
            insercao(deposito, select)
            nota200 = deposito * 200
            volta += deposito * 200
            print(f"O valor de {nota200} foi recebido em notas de 200")
            time.sleep(3)
            return inserirCaixa(volta)
        case 2:
            deposito = int(input("Quantas notas foram recebidas?\n"))
            insercao(deposito, select)
            nota100 = deposito * 100
            volta += deposito * 100
            print(f"O valor de {nota100} foi recebido em notas de 100")
            time.sleep(3)
            return inserirCaixa(volta)
        case 3:
            deposito = int(input("Quantas notas foram recebidas?\n"))
            insercao(deposito, select)
            nota50 = deposito * 50
            volta += deposito * 50
            print(f"O valor de {nota50} foi recebido em notas de 50")
            time.sleep(3)
            return inserirCaixa(volta)
        case 4:
            deposito = int(input("Quantas notas foram recebidas?\n"))
            insercao(deposito, select)
            nota20 = deposito * 20
            volta += deposito * 20
            print(f"O valor de {nota20} foi recebido em notas de 20")
            time.sleep(3)
            return inserirCaixa(volta)
        case 5:
            deposito = int(input("Quantas notas foram recebidas?\n"))
            insercao(deposito, select)
            nota10 = deposito * 10
            volta += deposito * 10
            print(f"O valor de {nota10} foi recebido em notas de 10")
            time.sleep(3)
            return inserirCaixa(volta)
        case 6:
            deposito = int(input("Quantas notas foram recebidas?\n"))
            insercao(deposito, select)
            nota5 = deposito * 5
            volta += deposito * 5
            print(f"O valor de {nota5} foi recebido em notas de 5")
            time.sleep(3)
            return inserirCaixa(volta)
        case 7:
            deposito = int(input("Quantas notas foram recebidas?\n"))
            insercao(deposito, select)
            nota2 = deposito * 2
            volta += deposito * 2
            print(f"O valor de {nota2} foi recebido em notas de 2")
            time.sleep(3)
            return inserirCaixa(volta)
        case 8:
            deposito = int(input("Quantas notas foram recebidas?\n"))
            insercao(deposito, select)
            moeda1 = deposito * 1
            volta += deposito * 1
            print(f"O valor de {moeda1} foi recebido em moedas de 1")
            time.sleep(3)
            return inserirCaixa(volta)
        case 9:
            deposito = int(input("Quantas notas foram recebidas?\n"))
            insercao(deposito, select)
            moeda050 = deposito * 0.50
            volta += deposito * 0.50
            print(f"O valor de {moeda050} foi recebido em moedas de 0.50")
            time.sleep(3)
            return inserirCaixa(volta)
        case 10:
            deposito = int(input("Quantas notas foram recebidas?\n"))
            insercao(deposito, select)
            moeda025 = deposito * 0.25
            volta += deposito * 0.25
            print(f"O valor de {moeda025} foi recebido em moedas de 0.25")
            time.sleep(3)
            return inserirCaixa(volta)
        case 11:
            deposito = int(input("Quantas notas foram recebidas?\n"))
            insercao(deposito, select)
            moeda010 = deposito * 0.1
            volta += deposito * 0.1
            print(f"O valor de {moeda010} foi recebido em moedas de 0.10")
            time.sleep(3)
            return inserirCaixa(volta)
        case 12:
            deposito = int(input("Quantas notas foram recebidas?\n"))
            insercao(deposito, select)
            moeda005 = deposito * 0.05
            volta += deposito * 0.05
            print(f"O valor de {moeda005} foi recebido em moedas de 0.05")
            time.sleep(3)
            return inserirCaixa(volta)
        case _:
            return volta

def insercao(inserir, id):

    conn = sqlite3.connect("FluxoDeCaixa.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT quantia FROM dinheiro WHERE id_dinheiro={id}")
    uso = cursor.fetchone()

    quantiaAtual = uso[0]
    quantiaFinal = quantiaAtual + inserir

    cursor.execute("UPDATE dinheiro SET quantia= ? WHERE id_dinheiro=?", (quantiaFinal, id))
    conn.commit()