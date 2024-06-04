import streamlit as st
import spacy
from spacy import displacy
nlp=spacy.load("en_core_web_sm")
a=st.text_input("GIVE ANY TEXT")
if a:
    doc=nlp(a)
    html=displacy.render(doc,style="ent")
    st.markdown(html,unsafe_allow_html=True)
   