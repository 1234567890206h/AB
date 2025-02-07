import streamlit as st
st.title('chrun preduction')
st.image('11')
a= st.number_input('inter age')
b= st.number_input('inter balance')
bt =st.button('predction')
 if bt == True :
       model=joblib.load('svc_model,pkl')
       res=mymodel.predict([[a,b]])
       if res==1:
           st.write('the customer still active')
       elif res==0:
           st.write('the customer has left')