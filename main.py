import streamlit as st
from aoi import get_areas_of_improvement

st.set_page_config(layout="wide")
st.title("Suggestion Bot")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Your compain about your partner")
    st.write("This wont be shown to your partner")
    user_input = st.text_area("Enter your message here:")
    if st.button("Submit"):
        response = get_areas_of_improvement(user_input)
        with col2:
            st.subheader("Areas of Improvement that your partner will see")
            sl_no = 1
            for item in response['aoi']:
                st.markdown(f"##### {sl_no}) {item['title']}", unsafe_allow_html=True)
                st.markdown(f"<p style='font-size:18px;'>{item['suggestion']}</p>", unsafe_allow_html=True)

                sl_no += 1


