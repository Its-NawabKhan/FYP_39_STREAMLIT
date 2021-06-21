import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_data= pd.read_csv('df_data.csv')
# Get the data from url and request it as json file

df_data01 = df_data.copy()

df_data01.drop(columns=['Unnamed: 0', 'arrival', 'parking_entry', 'kiosk',
       'department_entrance', 'department_exit', 'parking_exit', 'departure'], inplace=True)

means_dict = {}
for each in df_data01.columns[0:-1]:
    means_dict[each] = df_data01[each].mean()

df_aggreg = df_data01.groupby('Date',as_index=False).agg('mean')

df_diff = pd.DataFrame(columns=df_data01.columns)

df_diff['Date'] = df_aggreg['Date'].apply(lambda x: str(x).split('21-')[1])

for each in df_diff.columns[0:-1]:
    df_diff[each] = means_dict[each]-df_aggreg[each]

df_diff.sort_values('Date', ascending=True, inplace=True)
df_diff.set_index('Date', inplace=True)
df_diff.reset_index(inplace=True)

df_diff_small = df_diff.tail(7)

@st.cache(persist=True, suppress_st_warning=True)

def main():
    st.header("Shifa International Hospital")
    st.subheader("Trends that you need to know")
    st.image("image.jpg",width=1000)
# if __name__ == "__main__":
main()

radio_val= st.radio("Average Wait Times",['Parking Entry Wait','Kiosk Wait','Department Entrance Wait','Department Exit Wait','Parking Exit Wait','Departure Wait'],index=1)
if radio_val== 'Parking Entry Wait':
    fig = plt.figure()
    sns.barplot(df_diff_small['Date'], df_diff_small['parking_entry_wait'])
    st.pyplot(fig)

elif radio_val== 'Kiosk Wait':
    fig = plt.figure()
    sns.barplot(df_diff_small['Date'], df_diff_small['kiosk_wait'])
    st.pyplot(fig)

elif radio_val== 'Department Entrance Wait':
    fig = plt.figure()
    sns.barplot(df_diff_small['Date'], df_diff_small['department_entrance_wait'])
    st.pyplot(fig)

elif radio_val== 'Department Exit Wait':
    fig = plt.figure()
    sns.barplot(df_diff_small['Date'], df_diff_small['department_exit_wait'])
    st.pyplot(fig)

elif radio_val== 'Parking Exit Wait':
    fig = plt.figure()
    sns.barplot(df_diff_small['Date'], df_diff_small['parking_exit_wait'])
    st.pyplot(fig)

else:
    fig = plt.figure()
    sns.barplot(df_diff_small['Date'], df_diff_small['departure_wait'])
    st.pyplot(fig)

fig1 = plt.figure()
sns.barplot(df_diff_small['Date'], df_diff_small['Rating'])
st.pyplot(fig1)
