import streamlit as st
import pickle
import numpy as np
pipe = pickle.load(open('pipe.pkl' , 'rb'))
df = pickle.load(open('df.pkl' , 'rb'))
st.title("Laptop Price Predictor")
company = st.selectbox('Brand' , df['Company'].unique())
type = st.selectbox('Type' , df['TypeName'].unique())
Ram = st.selectbox('Ram' , [2,4,6,8,12,16,24,32,64])
Weight = st.number_input('Weight of Laptop')
TouchScreen = st.selectbox("TouchScreen",['Yes',"No"])
IPS = st.selectbox("IPS",['Yes',"No"])
screen_size = st.number_input("Screen Size")
resolution = st.selectbox('Screen Resolution',['1920x1080','1366x768','1600x900','3840x2160','2880x1800','2560x1600','2560x1440','2304x1440','3200x1800'])
CPU = st.selectbox('Brand' , df['CPU Brand'].unique())
HDD= st.selectbox('HDD(in GB)' , [0,128,256,512,1024,2048])
SSD= st.selectbox('HDD(in GB)' , [0,8,128,256,512,1024])
GPU = st.selectbox('GPU' , df['GPU Brand'].unique())
Operating_System = st.selectbox('OS' , df['OS'].unique())
if(st.button('Predict Price')):
    PPI = None
    if TouchScreen=='Yes':
        TouchScreen = 1
    else:
        TouchScreen = 0
    if IPS=='Yes':
        IPS=1
    else:
        ips = 0
    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    PPI = ((X_res**2)+(Y_res**2))**0.5/screen_size
    query = np.array([company , type , Ram , Weight , TouchScreen , IPS , PPI , CPU , HDD , SSD , GPU , Operating_System])
    query = query.reshape(1,12)
    st.title(int(np.exp(pipe.predict(query))))