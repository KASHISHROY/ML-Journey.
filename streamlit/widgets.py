import streamlit as st
import pandas as pd
st.title("Streamlit Text Input")
name=st.text_input("Enter your name:")
if name:
    st.write(f"Hello,{name}")
age=st.slider("Select your age:",0,100,25)
st.write(f"Your age is {age}")

options=["Python","Java","C++","Javascript"]
choice=st.selectbox("Choose your favourite subject:",options)
st.write(f"You selected {choice}")

data={
    "Name":["John","Jane","Michael","Steve"],
     "Age":[30,25,29,37],
     "City":["NewYork","Bangok","Singapore","Kolkata"]
}
df=pd.DataFrame(data)
st.write(df)
df.to_csv("sample_data.csv")
uploaded_file=st.file_uploader("Choose a csv file:",type="csv")
if uploaded_file is not None:
    pd.read_csv(uploaded_file)
    st.write(df)

