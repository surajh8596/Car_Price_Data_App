import streamlit as st
from PIL import Image
from matplotlib import image
import pandas as pd
import pickle
import os

#img =Image.open("resourses//Image//car.png")
#img = image.imread(IMAGE_PATH1)
#st.image(img)
#data = pd.read_pickle("resourses//Data//CarPricesData.pkl")
#st.dataframe(data=data)
#lottie_hello = load_lottiefile("Portfolio/lottiefiles/hello.json")
filename='resourses//Data//CarPricesData.pkl'
model = pickle.load(open(filename, 'rb'))
st.dataframe(data=model)
