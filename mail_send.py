# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 09:16:11 2024

@author: Daniel
"""
import streamlit as st
import yagmail
import pandas as pd

# Definir los datos
data = {
    'Nombre': ['Luis', 'P.Villegas', 'P.Aviles', 'Carlos', 'Dani'],
    'Mail': ['luis@fly-fut.com', 'pedro.villegas@fly-fut.com','pedro.aviles@fly-fut.com', 'carlos.gil@fly-fut.com', 'daniel.sanmiguel@fly-fut.com']
}
# Crear el DataFrame
df = pd.DataFrame(data)

with st.container():
    st.dataframe(df)
    mi_mail = st.text_input('mail')
    contrasena = st.text_input('password', type='password')
    selec_dest = st.toggle('elegir destinatario')
    if selec_dest:
        enviar_a = st.text_input('destinatario')
    b_1 = st.button('Send')
# Ejemplo de uso

def enviar_correo_con_logo(destinatario, asunto, cuerpo_html):
    # Configura tu dirección de correo y contraseña de aplicación.
    remitente = mi_mail
    password = contrasena  # Contraseña de aplicación

    # Crear el objeto yagmail
    yag = yagmail.SMTP(remitente, password)

    # Crear el contenido HTML con la imagen embebida
    contenido = [
        cuerpo_html,  # Contenido HTML del correo
    ]

    # Enviar el correo
    try:
        yag.send(to=destinatario, subject=asunto, contents=contenido)
        print("Correo enviado exitosamente.")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")

if __name__ == "__main__":
    

    ruta_logo = "C:/Users/dsanm/OneDrive/Desktop/python/foto_ff_cut.jpg"  # Ruta local de tu imagen
    if b_1:
        for r,i in df.iterrows():
            if selec_dest:
                usuario = i['Nombre']
                asunto = "Correo con logo embebido"
                cuerpo_html = f"""
                <h1>Hola</h1>
                <p>Este es un correo de prueba con un logo embebido para {usuario}</p>

                """
                enviar_correo_con_logo(enviar_a, asunto, cuerpo_html)
            else:
                usuario = i['Nombre']
                asunto = "Correo con logo embebido"
                cuerpo_html = f"""
                <h1>Hola</h1>
                <p>Este es un correo de prueba con un logo embebido para {usuario}</p>
                """
                enviar_correo_con_logo(i['Mail'], asunto, cuerpo_html)
