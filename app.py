import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_contact_form = Image.open("images/yt_contact_form.png")
img_lottie_animation = Image.open("images/yt_lottie_animation.png")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Witam, jestem Tomek :wave:")
    st.title("Javascript/Python Developer")
    st.write(
        "Poszukuje pracy lub stażu na stanowisku juniora"
    )
    st.write("[Zobacz także  >](https://ragnarthecat.pl)")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Moje umiejętności")
        st.write("##")
        st.write(
            """
            - znajomość języka programowania html, css, javascript;
            - znajomość języka programowania python;
            - podstawowa znajomość Wordpressa, PHP, SQL, jQuery, frameworków Bootstrap, Flask, Django, itp.
            - znajomość języków obcych : Angielski C1, Niemiecki B2, Rosyjski B2.
            - niepohamowana wola uczenia się nowych rzeczy.
            """
        )

    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("Przykładowe strony")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("ragnarthecat.pl")
        st.write(
            """
            Strona o moim kocie Ragnarze, oraz ogólnie o kotach.
            """
        )
        st.markdown("[Przejdź...](https://ragnarthecat.pl)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("Hyundai Blog")
        st.write(
            """
            Blog poświęcony samochodom marki Hyundai. Strona w budowie. 
            """
        )
        st.markdown("[Przejdź...](https://bloghyundai.ragnarthecat.pl/)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Kontakt ze mną")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/mr.zwolen@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Twoje imię" required>
        <input type="email" name="email" placeholder="Twój email" required>
        <textarea name="message" placeholder="Twoja wiadomość" required></textarea>
        <button type="submit">Wyślij</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()