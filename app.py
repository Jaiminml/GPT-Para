import streamlit as st
import time
from src.utils import paraphrase_english, paraphrase_indonesian
from src.st_style import apply_prod_style


# apply_prod_style(st)  # NOTE: Uncomment this for production!

st.title("AI Text Paraphraser")
st.image(open("assets/demo.png", "rb").read())
st.write(
    """
    Stop plagiarism! Do not carelessly copy and paste text materials from the internet.
    **This AI tool will make your text unique and free from plagiarism.**
    """
)

language = st.selectbox("Language", ["English", "Bahasa Indonesia"])
input_text = st.text_area("Input your text (Max 1000 characters)", height=250, max_chars=1000)

if st.button("Submit") and len(input_text) > 0:
    
    with st.spinner("AI is doing the magic!") as p:
        input_text = input_text.replace("\n\n", "\n").replace("\n", " ").strip()
        
        if language == "English":
            paraphrased = paraphrase_english(input_text)
        else:
            paraphrased = paraphrase_indonesian(input_text)
    
    st.write("**Your text is ready!**")
    st.write(paraphrased)
    st.info("**TIP:** You can submit the same text multiple times to get different results.")