# Suponha que 'textos' é a sua lista original
textos = ['\nElaborado em: 23/01/2024 às 11:30 – N° 013/2024 Meteorologista: Francine Sacco \xa0 \xa0 \xa0 O aquecimento combinado com a umidade disponível e também a um vórtice ciclônico de altos níveis (sistema de baixa pressão em médios e altos níveis) forma novamente áreas de instabilidade, que\xa0 provocam pancadas de chuva e […]\n', ...]

# Processar cada texto para remover caracteres indesejados
textos_formatados = []
for texto in textos:
    # Remover quebras de linha e espaços não separáveis
    texto = texto.replace('\n', '').replace('\xa0', ' ').strip()
    textos_formatados.append(texto)

# Imprimir os textos formatados
for texto in textos_formatados:
    print(texto)
