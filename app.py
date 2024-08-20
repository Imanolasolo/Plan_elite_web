import streamlit as st
import base64
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuración de la página
st.set_page_config(page_title="Plan élite", page_icon="🌟", layout="wide")

# CSS personalizado para el expander y el margen superior
expander_css = """
<style>
div.streamlit-expanderHeader {
    background-color: #FFCCCC;
    color: black;
    padding: 10px;
    font-weight: bold;
}

div[aria-expanded="true"] > div[aria-labelledby^="streamlit-expander"] {
    background-color: #FFFFFF;
    padding: 10px;
    border-radius: 10px;
}

.stApp {
    margin-top: 40px; /* Ajusta el valor para el margen superior */
}

.button-blue {
    background-color: #007bff; /* Azul */
    color: white;
    padding: 10px 20px;
    font-size: 16px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    text-align: center;
    display: inline-block;
}

.button-blue:hover {
    background-color: #0056b3; /* Azul más oscuro para hover */
}
</style>
"""
st.markdown(expander_css, unsafe_allow_html=True)

# Función para convertir el archivo en base64
def get_base64_of_file(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode('utf-8')

# Convertir la imagen en base64
img_base64 = get_base64_of_file('portada.png')

# Aplicar la imagen de fondo usando CSS
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{img_base64}");
        background-size: contain;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-blend-mode: lighten;
        background-position: center;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

def show_elite_plan():
    st.info("""
    Llegó la hora de tomar la mejor acción para proteger a tu familia.
    Forma parte de la nueva era hospitalaria con nuestro Plan Élite.
    """)

    col1, col2 = st.columns(2)

    # Botón para mostrar el PDF de beneficios
    with col1:
        if st.button('Ver Beneficios del Plan Élite'):
            pdf_path = "Beneficios_plan_elite.pdf"  # Ruta al archivo PDF
            with open(pdf_path, "rb") as f:
                base64_pdf = base64.b64encode(f.read()).decode('utf-8')
            pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="900" type="application/pdf"></iframe>'
            st.markdown(pdf_display, unsafe_allow_html=True)

    # Botón para mostrar el PDF de privilegios
    with col2:
        if st.button('Ver Privilegios del Plan Élite'):
            pdf_path = "Privilegios_plan_elite.pdf"  # Ruta al archivo PDF
            with open(pdf_path, "rb") as f:
                base64_pdf = base64.b64encode(f.read()).decode('utf-8')
            pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="900" type="application/pdf"></iframe>'
            st.markdown(pdf_display, unsafe_allow_html=True)

    st.info("Contacte con nosotros:")
    col1, col2, col3 = st.columns(3)
    with col1:
        with st.expander(':blue[Formulario mail]'):
            with st.form(key='contact_form'):
                contact_reason = st.selectbox(":blue[Razón de contacto:]", ["Darme de alta el el programa", "Darme de baja del programa", "Cambio de datos", "Información general"])
                contact_info = st.text_input("Su info de contacto (WhatsApp o email):")
                message = st.text_area("Su mensaje:")
        
                submit_button = st.form_submit_button(label='Enviar')
        
                if submit_button:
                    if contact_info and message:
                        try:
                            # Configurar y enviar el correo electrónico
                            email_recipient = "jjusturi@gmail.com"  # Reemplaza con el correo de destino
                            email_subject = f"Contact Form Submission: {contact_reason}"
                            email_body = f"Razón: {contact_reason}\nContacto: {contact_info}\nMensaje: {message}"
                
                            msg = MIMEMultipart()
                            msg['From'] = contact_info
                            msg['To'] = email_recipient
                            msg['Subject'] = email_subject
                            msg.attach(MIMEText(email_body, 'plain'))
                
                            # Configurar el servidor SMTP
                            server = smtplib.SMTP('smtp.gmail.com', 587)
                            server.starttls()
                            server.login(st.secrets["smtp"]["username"], st.secrets["smtp"]["password"])
                            server.sendmail(contact_info, email_recipient, msg.as_string())
                            server.quit()
                
                            st.success("¡Tu mensaje ha sido enviado exitosamente!")
                        except Exception as e:
                            st.error(f"Error al enviar el mensaje: {e}")
                else:
                    st.warning("Por favor, completa toda la información antes de enviar el formulario.")
    
    with col2:
        whatsapp_button = """
        <a href="https://wa.me/593993513082?text=Tengo%20una%20emergencia%20y%20soy%20socio%20del%20programa%20élite%20del%20MHC" target="_blank">
            <button class="button-blue">
                Whatssap para emergencias VIP
            </button>
        </a>
        """
        st.markdown(whatsapp_button, unsafe_allow_html=True)

if __name__ == '__main__':
    show_elite_plan()
