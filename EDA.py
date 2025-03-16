import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

#membuat function untuk nantinya dipanggil di app.py
def run():
    st.title('Welcome to Exploration Data Analysis')

    # st.title('Exploratory Data Analysis')
    image = Image.open('eda1.png')
    st.image(image, caption='1. Distribusi loan_status')

    #menampilkan penjelasan 
    with st.expander('Explanation'):
        st.caption('Berdasarkan gambar pie chart yang Anda bagikan, tampaknya ini adalah visualisasi dari status pinjaman. Dari total pinjaman, 62.2% telah disetujui dan 37.8% telah ditolak. Ini menunjukkan bahwa sebagian besar pinjaman berhasil mendapatkan persetujuan.')

    # st.title('Exploratory Data Analysis')
    image = Image.open('eda2.png')
    st.image(image, caption='2. ### 5.2 Persebaran loan_status berdasarkan cibil_score dan loan_term')

    #menampilkan penjelasan 
    with st.expander('Explanation'):
        st.caption("dari gambar diatas terlihat mungkin terdapatnya hubungan antar cibil_score, loan_term, dan loan_status terlihat dari bertambahnya secara berkala dari tingkat lamanya pinjaman diberikan")

    # st.title('Exploratory Data Analysis')
    image = Image.open('eda3.png')
    st.image(image, caption='3. Persebaran education terhadap loan_status')

    #menampilkan penjelasan 
    with st.expander('Explanation'):
        st.caption("Terlihat dari visualisasi data diatas bahwa tingkat pendidikan dengan status pinjaman kemungkinan tidak ada hubungannya karena dari status pendidikan tidak ada yang berbeda/")

    # # st.title('Exploratory Data Analysis')
    # image = Image.open('eda4.jpg')
    # st.image(image, caption='4. Persebaran default_payment_next_month terhadap tingkat pendidikan')

    # #menampilkan penjelasan 
    # with st.expander('Explanation'):
    #     st.caption("Dari visualisasi diatas didapatkan bahwa tingkat Pendidikan terakhir SMP dan Universitas mendominasi dengan hasil bahwa pengguna dengan tingkat terakhir pendidikan tersebut akan cenderung tidak bisa membayar kreditnya pada bulan selanjutnya, tingkat Pendidikan lain-lain dan SMK memiliki tingkat kegagalan pembayaran kredit pada bulan selanjutnya yang sangat rendah, kemungkinan menunjukkan kinerja pembayaran yang lebih baik atau karena jumlah pelanggan dengan education lain-lain dan SMK sedikit sehingga yang gagal bayar pun sedikit")

    # # st.title('Exploratory Data Analysis')
    # image = Image.open('eda5.jpg')
    # st.image(image, caption='5. Persebaran default_payment_next_month terhadap status pernikahan')

    # # menampilkan penjelasan 
    # with st.expander('Explanation'):
    #     st.caption("Berdasarkan visualisasi di atas, terlihat bahwa jumlah pelanggan yang tidak dapat membayarkan kreditnya dibulan berikutnya terbanyak berasal dari kelompok pelanggan yang single, diikuti oleh pelanggan yang berstatus menikah, dan terakhir adalah kelompok dengan status other. visualisasi tersebut, terlihat bahwa kelompok pelanggan yang sudah menikah dan yang berstatus single memiliki jumlah yang relatif serupa dalam hal berhasil membayarkan kreditnya di bulan berikutnya.")