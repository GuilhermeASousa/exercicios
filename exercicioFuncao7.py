def valorPagamento(prestacao, dias_atraso):
    if dias_atraso == 0:
        return prestacao
    else:
        multa = 0.03 * prestacao
        juros = 0.001 * prestacao
        valor_total = prestacao + (multa + (juros * dias_atraso))
        return valor_total

def relatorio_diario(total_prestacoes, valor_total):
    print("\nRelatório do Dia:")
    print(f"Total de prestações pagas: {total_prestacoes}")
    print(f"Valor total recebido: R${valor_total:.2f}")

total_prestacoes = 0
valor_total = 0

while True:
    prestacao = float(input("Digite o valor da prestação (ou 0 para sair): "))
    
    if prestacao == 0:
        break
    
    dias_atraso = int(input("Digite o número de dias em atraso: "))
    
    valor_a_pagar = valorPagamento(prestacao, dias_atraso)
    print(f"Valor a ser pago: R${valor_a_pagar:.2f}")
    
    total_prestacoes += 1
    valor_total += valor_a_pagar

relatorio_diario(total_prestacoes, valor_total)
