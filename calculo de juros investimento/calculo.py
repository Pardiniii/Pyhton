inicial = float(input('Digite o valor inicial que deseja investir:'))
meses = int(input('Digite quantos meses deseja deixar investido:'))
juros = float(input('Digite a porcentagem de juros ao mes:'))
bufunfa = float(input('Digite quanto voce colocara a mais por mes:'))
total = 0.0
mes = 1
juros = juros/100

for i in range(meses):
    if mes == 1:
        total = inicial + (inicial * juros)
        print(f'Mes {mes}: total = {total:,.2f}')
    else:
        total = total + bufunfa + ((total + bufunfa) * juros)
        print(f'Mes {mes}: total = {total:,.2f}')
    mes += 1

valor_total_investido = inicial + bufunfa * (meses - 1)
lucro = total - valor_total_investido
print(f'Valor total investido = {valor_total_investido:,.2f} reais')
print(f'Lucro = {lucro:,.2f} reais')
print(f'Valor total apos {meses} meses investidos = {total:,.2f}')
