""" IMAGE BACKGROUND REMOVER"""


# By Hlabsdev



from io import BytesIO


from PIL import Image


from rembg import remove
import streamlit as st



#set up the page:


st.set_page_config("BACKGROUND REMOVER", ":📸", layout="wide")
st.write("## BACKGROUND REMOVER")
st.write("Uplaoder une image pour enlever l'arriere plan")

st.sidebar.write("## Backgroung remover")

# set up two column for better visualisation
col1, col2 = st.columns(2)


def convert_image(img):
    """Fonction pour convertir l'image finale en format PNG"""

    temp = BytesIO()
    img.save(temp, format='PNG')
    final = temp.getvalue()
    return final


def rm_bg(img):
    """ Nous permet d'enlever l'arriere plan de l'image"""

    image = Image.open(img)
    # Afficher l'image chargee
    col1.write('Image originale:')
    col1.image(raw_img)
    # Traiter l'image
    removed = remove(image)
    final = convert_image(removed)
    # Afficher le resultat
    col2.write('Image finale:')
    col2.image(final)
    # Telecharger le resultat
    st.sidebar.write("\n")
    st.sidebar.download_button("Telecharger le resultat", final, img.name,  "image/png")

    # return final


#Chargeons l'image
raw_img = st.sidebar.file_uploader("Choisissez l'images", type=['png', 'jpg', 'jpeg', 'bpm'])


# On traite l'image
if raw_img is not None:
    rm_bg(raw_img)
else:
    # rm_backgroung("./imgs/200w.gif")
    st.image("./imgs/200w.gif")
