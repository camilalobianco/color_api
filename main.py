import streamlit as st
from random_pallete import generate_palette_and_save_to_database

st.title("Color Palette Generator")
st.write("Click the button below to generate a random palette!")

models = ["default", "ui", "metroid_fusion"]

if "selected_model" not in st.session_state:
    st.session_state.selected_model = None

columns = st.columns(len(models))
for col, model in zip(columns, models):
    with col:
        if st.button(f"Generate {model.replace('_', ' ').title()}"):
            st.session_state.selected_model = model

if st.session_state.selected_model:
    try:
        palette = generate_palette_and_save_to_database(st.session_state.selected_model)
        if palette:
            st.write(f"Generated Color Palette ({st.session_state.selected_model.replace('_', ' ').title()}):")
            color_columns = st.columns(len(palette))
            for color_col, color in zip(color_columns, palette):
                with color_col:
                    st.markdown(
                        f"""
                        <div style="width: 100%; height: 150px; background-color: rgb{color}; border-radius: 5px;"></div>
                        <p style="text-align: center;">RGB: {color}</p>
                        """,
                        unsafe_allow_html=True,
                    )
    except Exception as e:
        st.error(f"Error generating palette for model '{st.session_state.selected_model}': {e}")
