import openpyxl as op

#criando tabela 
tabela = op.Workbook()

#criando uma planilha pro teste
tabela.create_sheet('arquivoTeste')

#adicionadno elementos na planilha
info = tabela['arquivoTeste']
info.append(['Gênero', 'Nome', 'Duração', 'Ano de lançamento'])
info.append(['Terror', 'Carrie', '1h 40 m', '2013']) 
info.append(['Ação', 'Velozes e furiosos 9', '2h 25m', '2021'])
info.append(['Romance', '365 DNI', '1h 56m', '2020'])
info.append(['Ficção', 'BIOS', '1h 55m', '2020'])
info.append(['Drama', 'Nocaute', '2h 4m', '2015'])
info.append(['Comédia', 'Vizinhança do Barulho', '1h 34m', '1996'])

#salvando planilha
tabela.save('filmes.xlsx')