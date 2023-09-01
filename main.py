# Guilherme Augusto Santiago Abib

import os

def ler_arquivo(caminho_arquivo):
    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        return arquivo.readlines()[1:]

def salvar_arquivo(caminho_arquivo, conteudo):
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write("\n".join(conteudo))

def processar_operacoes(operacoes):
    resultados = []
    for i in range(0, len(operacoes), 3):
        operacao = operacoes[i].strip()
        conjunto1 = set(map(str.strip, operacoes[i+1].strip().split(",")))
        conjunto2 = set(map(str.strip, operacoes[i+2].strip().split(",")))

        if operacao == "U":
            res = conjunto1.union(conjunto2)
            resultados.append(f"União: conjunto 1 {conjunto1}, conjunto 2 {conjunto2}. Resultado: {res}")
        elif operacao == "I":
            res = conjunto1.intersection(conjunto2)
            resultados.append(f"Interseção: conjunto 1 {conjunto1}, conjunto 2 {conjunto2}. Resultado: {res}")
        elif operacao == "D":
            res = conjunto1.difference(conjunto2)
            resultados.append(f"Diferença: conjunto 1 {conjunto1}, conjunto 2 {conjunto2}. Resultado: {res}")
        elif operacao == "C":
            res = {(x, y) for x in conjunto1 for y in conjunto2}
            resultados.append(f"Produto Cartesiano: conjunto 1 {conjunto1}, conjunto 2 {conjunto2}. Resultado: {res}")

    return resultados

if __name__ == "__main__":
    diretorio_entrada = "arquivos"
    diretorio_saida = "arquivos"

    for nome_arquivo in os.listdir(diretorio_entrada):
        if nome_arquivo.startswith("entrada"):
            caminho_arquivo_entrada = os.path.join(diretorio_entrada, nome_arquivo)
            operacoes = ler_arquivo(caminho_arquivo_entrada)
            resultados = processar_operacoes(operacoes)
            
            nome_arquivo_saida = nome_arquivo.replace("entrada", "saida")
            caminho_arquivo_saida = os.path.join(diretorio_saida, nome_arquivo_saida)
            salvar_arquivo(caminho_arquivo_saida, resultados)


            print("\n".join(resultados))
            print("------------")





