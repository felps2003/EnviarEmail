import smtplib
import streamlit as st
import pandas as pd
from email.message import EmailMessage


def enviarEmail(email, conteudo):
 

    EMAIL_ADDRESS = 'felypenunes1998@gmail.com'
    EMAIL_PASSWORD = 'hnxp ztym gtgt cmiq' # necessario ativar autenticacao por 2 fatores - senha gerada a partir 2 factor generator password

    msg = EmailMessage()

    msg["Subject"] = 'Email de teste'
    msg["From"] = 'felypenunes1998@gmail.com'
    msg["To"] = email
    msg.set_content(conteudo)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

st.title("Enviar Email")

valor = st.text_input("Coloque a chave")

if valor == '#Na08081998':
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
                        Olá {nome}, tudo bem ? 

                        esse é o seu email {email}        
                    """
                    enviarEmail(email,text)
            st.success("Parabéns todos foram enviados")
            st.balloons()


