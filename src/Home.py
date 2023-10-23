import sys
import css
from pathlib import Path
script_dir = Path(__file__).resolve().parent
project_root = script_dir.parent
sys.path.append(str(project_root))

print(str(script_dir))
print(str(project_root))

import streamlit as st

st.set_page_config(page_title="Financial Insights Companion", page_icon=":money_with_wings:", layout="wide")

st.write(f'<style>{css.v1}</style>', unsafe_allow_html=True)

#st.title(":money_with_wings: FinSight \n\n **Financial Insights at Your Fingertip**")

with open("docs/main.md", "r") as f:
    st.info(f.read())

