#!/usr/bin/env python# -*- coding: utf-8 -*-import urllibimport psycopg2import sysimport datetimedef conection():    #engine = create_engine('postgresql+psycopg2://postgres:L30051992z@localhost:5432/dados')    conn = psycopg2.connect(host="localhost", database="dados", user="postgres", password="L30051992z")    return conn,conn.cursor()def contexto(cursor):    cursor.execute("Select data from emprestimosreg order by data desc")    return map( lambda x : x[0].strftime("%Y-%m-%d"), cursor.fetchall())def error():    print 'deu erro, nao sei qual eh.'    sys.exit(0)def parser(data,linha):    str_sql = "INSERT INTO emprestimosreg  (data,ticker,nome,n_contratos,qtd_shs,volume,doador_min,doador_med,doador_max,tomador_min,tomador_med,tomador_max) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"    cursor.execute(str_sql, tuple([data]+linha.strip('\r\n').decode('iso-8859-1').split('|')[1:]))    conn.commit()conn ,cursor= conection()lista = contexto(cursor)btc = urllib.urlopen('ftp://ftp.bmf.com.br/ipnv2/SVI/DBTCER/SI_D_DBTCER.txt')linhas= btc.readlines()try:    aux = linhas[0].split('|')    data = aux[1][:4] + '-' + aux[1][4:6] + '-' + aux[1][6:8]    if data not in lista:        for linha in linhas[1:]:            parser(data,linha)    else:        error()    if data == (datetime.datetime.now() - datetime.timedelta(1)).strftime("%Y-%m-%d"):    # Tenho que melhorar essa funcao criando um dud(-2) ou duc(1)        with open(r"C:\Users\luiz\PycharmProjects\robos\checklist.txt", 'r') as checklist:            texto = checklist.read().replace('emprestimosreg\n', '')        with open(r"C:\Users\luiz\PycharmProjects\robos\checklist.txt", 'w') as checklist:            checklist.write(texto)except:    error()