import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_data= pd.read_csv('df_data.csv')
# Get the data from url and request it as json file
@st.cache(persist=True, suppress_st_warning=True)

def main():
    st.header("Shifa International Hospital")
    st.subheader("Trends that you need to know")
    st.image("image.jpg",width=1000)
if __name__ == "__main__":
    main()

radio_val= st.radio("Graph",['pie chart','bar graph','box plot'],index=1)
if radio_val== 'pie chart':
    st.write(df_data.head(5))

elif radio_val== 'bar graph':
    x=['a','b','c']
    vals=[10,5,15]
    fig = plt.figure()
    plt.bar(x,vals)
    st.pyplot(fig)
else:
    st.write(df_data.head(15))
#if st.checkbox("Visualization"):
    #st.write(df_data.head(10))
    #st.write(df_data.shape)
