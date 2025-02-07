import streamlit as st
import os
os.system("pip install --upgrade joblib")
import joblib
print("Joblib version:", joblib.__version__)
st.title('chrun preduction')
st.image('11.png')
a= st.number_input('inter age')
b= st.number_input('inter balance')
bt=st.button('predction')
print(joblib.__file__)
if bt == True:
       model=joblib.load('svc_model.pkl')
       res=model.predict([[a,b]])
       if res==1:
           st.write('the customer still active')
       elif res==0:
           st.write('the customer has left')
