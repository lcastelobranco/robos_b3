#!/usr/bin/env python# -*- coding: utf-8 -*-import urllibimport sysimport datetimefrom helper import *def error():    print 'deu erro, nao sei qual eh.'    sys.exit(0)def parser(data,linha):    str_sql = "INSERT INTO btc (data,ticker,nome,tipo_papel,isin,qtd_total,avg_price,fator_cot,volume) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"    cursor.execute(str_sql, tuple([data]+linha.strip('\r\n').decode('iso-8859-1').split('|')[1:]))    conn.commit()conn ,cursor,engine = conection("dados")lista = contexto(cursor,"btc")btc = urllib.urlopen('ftp://ftp.bmf.com.br/ipnv2/SVI/DBTCPARF/SI_D_DBTCPARF.txt')linhas= btc.readlines()try:    aux = linhas[0].split('|')    data = aux[1][:4] + '-' + aux[1][4:6] + '-' + aux[1][6:8]    if data not in lista:        for linha in linhas[1:]:            parser(data,linha)    else:        error()    if data == (datetime.datetime.now() - datetime.timedelta(1)).strftime("%Y-%m-%d"):    # Tenho que melhorar essa funcao criando um dud(-2) ou duc(1)        with open(r"C:\Users\luiz\PycharmProjects\robos\checklist.txt", 'r') as checklist:            texto = checklist.read().replace('btc\n', '')        with open(r"C:\Users\luiz\PycharmProjects\robos\checklist.txt", 'w') as checklist:            checklist.write(texto)except:    error()