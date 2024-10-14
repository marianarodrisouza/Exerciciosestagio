import json

# Exemplo de JSON de faturamento diário
faturamento_json = '''
{
    "faturamento": [0, 0, 200, 300, 0, 500, 700, 0, 100, 300]
}
'''

# Convertendo de JSON para dicionário Python
dados = json.loads(faturamento_json)
faturamento = [dia for dia in dados['faturamento'] if dia != 0]  # Ignorando dias sem faturamento

menor_valor = min(faturamento)
maior_valor = max(faturamento)
media_mensal = sum(faturamento) / len(faturamento)

# Dias com faturamento superior à média
dias_acima_da_media = len([dia for dia in faturamento if dia > media_mensal])

print(f"Menor valor de faturamento: {menor_valor}")
print(f"Maior valor de faturamento: {maior_valor}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")
