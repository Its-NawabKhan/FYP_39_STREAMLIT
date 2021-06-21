import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_data= pd.read_csv('df_data.csv')
# Get the data from url and request it as json file

df_data01 = df_data.copy()

df_data01.drop(columns=['Unnamed: 0', 'Unnamed: 0.1', 'arrival', 'parking_entry', 'kiosk',
       'department_entrance', 'department_exit', 'parking_exit', 'departure'], inplace=True)

means_dict = {}
for each in df_data01.columns[0:-1]:
    means_dict[each] = df_data01[each].mean()

df_aggreg = df_data01.groupby('Date',as_index=False).agg('mean')

df_diff = pd.DataFrame(columns=df_data01.columns)

df_diff['Date'] = df_aggreg['Date']

for each in df_diff.columns[0:-1]:
    df_diff[each] = df_aggreg[each] - means_dict[each]

df_diff.sort_values('Date', ascending=False, inplace=True)
df_diff.set_index('Date', inplace=True)
df_diff.reset_index(inplace=True)

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
    # x=['a','b','c']
    # vals=[10,5,15]
    fig = plt.figure()
    sns.barplot(df_diff['Date'],df_diff['kiosk_wait'])
    st.pyplot(fig)
else:
    st.write(df_data.head(15))
