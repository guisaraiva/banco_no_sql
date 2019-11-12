
# coding: utf-8

# ### Criando e acessando o Banco de Dados com Python - SQLITE

# In[1]:


# Importando o módulo de acesso ao SQLite.
# Ele já está instalado por causa do Anaconda instalado na máquina.

import sqlite3 as sql


# In[2]:


# Cria uma conexão com o banco de dados. 
# Se o banco de dados não existir, ele é criado neste momento.
# Buscando o banco de dados através do connect do sqlite3.

conexao = sql.connect('escola.db')


# In[3]:


# Criando um cursor. Como eu conheço Oracle, já tenho a ideia de que um cursor pode fazer. 
# (Um cursor permite percorrer todos os registros em um conjunto de dados)

percorre = conexao.cursor()


# In[4]:


# Cria uma instrução sql. Temos que armazenar o comando em uma variável.
# Nomeando a variável com nomes sugestivos para entender o conteúdo armazenado.
# Criando uma tabela "cursos" com os atributos (ID, TITULO, CATEGORIA). Sendo o ID a chave primária da tabela.

sql_create = 'create table cursos ''(id integer primary key, ''titulo varchar(100), ''categoria varchar(140))'


# In[5]:


# Executando a instrução sql no cursor 
# Nesse bloco estamos chamando o metodo execute do objeto percorre criado anteriormente.
# Passando como parâmetro a variável de criação do banco.

percorre.execute(sql_create)


# In[6]:


# Criando outra sentença SQL para inserir registros
# Criamos uma instrução SQL para inserir registros. 
# Ainda não temos os parâmetros. Desta forma, os values estão com "interrogação".

sql_insert = 'insert into cursos values (?, ?, ?)'


# In[7]:


# Dados que serão inseridos na tabela. Estou armazenando em uma variável. Como no exemplo anterior.

dados = [(1000, 'Ciência de Dados', 'Data Science'),
          (1001, 'Big Data Fundamentos', 'Big Data'),
          (1002, 'Python Fundamentos', 'Análise de Dados')]


# In[8]:


# Inserindo os registros
for rec in dados:
    percorre.execute(sql_insert, rec)


# In[9]:


# Grava a transação. O comando commit é executado para confirmar a operação de insert anterior.

conexao.commit()


# In[10]:


# Criando outra sentença SQL para selecionar registros. 
# Vamos realizar uma consulta em todos os dados da tabela criada.
# Não estou passando nenhuma condição para filtrar os dados.

sql_select = 'select * from cursos'


# In[11]:


# Seleciona todos os registros e recupera os registros
# Usei novamente a variável percorre (Cursor) juntamente com o metódo execute.
# Variável dadosrecuperado recebe o cursor com o metódo fetchall() retornando todos os registros da consulta.
percorre.execute(sql_select)

dadosrecuperado = percorre.fetchall()


# In[12]:


# Criando novamente um for para percorrer a variável dadosrecuperado e exibir com o print os resultados.

for linha in dadosrecuperado:
    print ('Curso Id: %d, Título: %s, Categoria: %s \n' % linha)


# In[13]:


# Gerando outros registros na tabela cursos. 
# Neste caso, executei todos os procedimentos em uma mesma célula do Jupyter notebook.

novosDados = [(1003, 'Gestão de Dados com MongoDB', 'Big Data'),
              (1004, 'R Fundamentos', 'Análise de Dados')]

# Inserindo os registros através do loop For. 
# Novamente vamos passar a variável que recebeu os novos dados e realizar o insert.

for rec in novosDados:
    percorre.execute(sql_insert, rec)
    
# Gravando a transação. Lembrando que os dados serão gravados com o metódo commit().

conexao.commit()


# In[14]:


# Seleciona todos os registros da tabela. 
# Não estou passando nenhuma condição para retornar os dados.
# Usamos o cursor criado "percorre" com o excecute.

percorre.execute('select * from cursos')

# Recupera os resultados e armazena na variável 
todosDados = percorre.fetchall()

# Mostra
for rec in todosDados:
    print ('Curso Id: %d, Título: %s, Categoria: %s \n' % rec)


# In[15]:


# Fecha a conexão através do metódo close().
# A variável de conexão foi criada no ínicio da execução desse script.

conexao.close()

