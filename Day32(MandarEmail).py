import smtplib as smt
import datetime as dt

meu_email = 'matandradefe@gmail.com'
senha_do_email = 'oclowptyslhvebcz'
mensagem1 = 'Subject: Parabens pelo seu aniversario\n\nNever limit yourself because of others limited imagination; never limit others because of your own limited imagination.'
mensagem2 = mensagem1.encode('ascii')


data = dt.datetime(year=2024, month=1, day=8)
if data.weekday() == 0:
    conexão = smt.SMTP("smtp.gmail.com", port=587) #garantindo a conexão
    conexão.starttls() #garantindo a criptografia caso alguem intercepte o emmail enviado (garantindo a conexão segura)
    conexão.login(user=meu_email, password=senha_do_email)
    conexão.sendmail(from_addr= meu_email, to_addrs='matferrer32@gmail.com',msg=mensagem2)
    conexão.close()