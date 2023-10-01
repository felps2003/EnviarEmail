import smtplib
import streamlit as st
import pandas as pd
from email.message import EmailMessage


def enviarEmail(email, conteudo, email_enviador, token_enviador):
 

    EMAIL_ADDRESS = email_enviador
    EMAIL_PASSWORD = token_enviador # necessario ativar autenticacao por 2 fatores - senha gerada a partir 2 factor generator password

    msg = EmailMessage()

    msg["Subject"] = 'Seu pedido para a Irlanda foi APROVADO! ✈'
    msg["From"] = email_enviador
    msg["To"] = email
    msg.set_content(conteudo)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

st.title("Enviar Email")

email_enviador = st.text_input("Coloque seu email")
token_enviador = st.text_input("Coloque sua senha de duplo acesso")

if email_enviador and token_enviador:
    arquivo = st.file_uploader('adicionar excel', type='xlsx')
    if arquivo:
        df = pd.read_excel(arquivo)
        st.dataframe(df)
        email_col = st.selectbox(options=df.columns, label='Escolha a coluna que contem os EMAILS')
        nome_col = st.selectbox(options=df.columns, label='Escolha a coluna que contem os NOMES')
        butao = st.button('Iniciar')
        if butao and email_col == nome_col:
            st.warning("Por favor, coloque as colunas corretas para iniciar")
        elif butao:
            with st.spinner(text=f"Enviando"):
                for i in df.index:
                    email = df.loc[i,email_col]
                    nome = df.loc[i,nome_col]
                    text = f"""
Você pediu {nome} e nós trouxemos!



Neste momento, estamos oferecendo um preço que vai te surpreender para o seu intercâmbio dos sonhos na Irlanda. Com a nossa oferta especial, você terá a oportunidade de explorar este país maravilhoso sem quebrar o banco.


Para descobrir esta promoção incrível que temos reservado para você, basta preencher seu cadastro! 💚🧡

QUERO RECEBER ESTA OFERTA!
Não perca essa chance única de realizar o seu sonho de intercâmbio na Irlanda a um preço que cabe no seu orçamento!

Por que embarcar para a Irlanda? 🍀


MERGULHE NA LÍNGUA INGLESA 📚

O inglês é a língua característica do país. Então, as expressões únicas e o sotaque vão fazer parte da rotina!



O VISTO SAI BEM FACINHO ✈

A Irlanda não exige um visto pré-viagem, sua retirada pode ser feita em terras irlandesas


UM BAIXO CUSTO DE VIDA 💸

Alimentação, segurança, estudo e entretenimento é facilmente alcançável com poucos euros graças ao alto IDH do país



UM POVO DE BRAÇOS ABERTOS 🎉

Assim como os brasileiros, o povo irlandês é conhecido por uma cultura bem festiva, muita animação e grande receptividade     
"""
                    enviarEmail(email,text, email_enviador, token_enviador)
            st.success("Parabéns todos foram enviados")
            st.balloons()


