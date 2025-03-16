import streamlit as st
import EDA
import pandas as pd  
import joblib
import model


page = st.sidebar.selectbox(label='Select Page:', options=['Home Page', 'Exploratory Data Analysis', 'Model Prediksi'])

if page == 'Home Page':
    st.header('Welcome Page') 
    st.image('loan.jpg')
    st.write('')
    st.write('Graded Challenge 5')
    st.write('Nama      : Akram Huwaidi Irnawan')
    st.write('Batch     : HCK - 010')
    st.write('Objective : Tujuan dari aplikasi ini adalah untuk mengotomatisasi proses kelayakan pinjaman dengan nilai  akurat apakah pinjaman harus disetujui atau tidak.')
    st.write('')
    st.caption('Silahkan pilih menu lain di Select Box pada sebelah kiri layar anda untuk memulai!')
    st.write('')
    st.write('')
    with st.expander("Latar Belakang & Problem Statement"):
        st.caption('Latar belakang dari aplikasiBank Loan Approval berakar pada tantangan yang dihadapi oleh lembaga keuangan dalam mengevaluasi kelayakan pinjaman. Proses ini seringkali memakan waktu dan sumber daya yang signifikan, dan masih rentan terhadap bias manusia dan kesalahan. Dalam industri perbankan, proses persetujuan pinjaman melibatkan penilaian manual dari banyak faktor, termasuk riwayat kredit, pendapatan, jumlah tanggungan, dan banyak lagi. Meskipun proses ini telah diperbaiki seiring waktu, masih ada ruang untuk peningkatan efisiensi dan akurasi. Selain itu, bias manusia dapat mempengaruhi keputusan pinjaman. Misalnya, penilai mungkin secara tidak sadar lebih memilih untuk menyetujui pinjaman untuk pelamar yang memiliki latar belakang yang mirip dengan mereka. Dengan menggunakan model machine learning untuk memprediksi persetujuan pinjaman, kita dapat membantu mengurangi bias ini dan memastikan bahwa semua pelamar diperlakukan secara adil. Akhirnya, dengan meningkatnya digitalisasi di sektor perbankan, pelanggan sekarang mengharapkan proses yang cepat dan mulus. Mereka tidak ingin menunggu berhari-hari atau berminggu-minggu untuk mengetahui apakah pinjaman mereka disetujui. Dengan mengotomatisasi proses ini, bank dapat memberikan keputusan lebih cepat, meningkatkan kepuasan pelanggan. Oleh karena itu, pengembangan aplikasi Prediksi Persetujuan Pinjaman bertujuan untuk mengatasi tantangan ini dan membantu lembaga keuangan membuat proses persetujuan pinjaman menjadi lebih efisien, akurat, adil, dan ramah pengguna.')

    with st.expander("Kesimpulan"):
        st.caption('Model XGBoost  telah menunjukkan kinerja yang sangat baik dalam memprediksi persetujuan pinjaman, dengan skor recall rata-rata tertinggi dalam validasi silang dan kinerja yang baik pada data latih dan uji. Meskipun tidak ada peningkatan dalam skor recall setelah optimasi hyperparameter, proses ini masih penting karena dapat membantu meningkatkan metrik evaluasi lainnya dan mencegah overfitting.')
   
    with st.expander("Kelebihan"):
        st.caption('Model memiliki skor recall yang tinggi, yang berarti model efektif dalam mengidentifikasi pinjaman yang seharusnya disetujui. Model juga memiliki skor precision yang tinggi, yang berarti model efektif dalam mengidentifikasi pinjaman yang seharusnya ditolak.Model menunjukkan kinerja yang baik baik pada data latih maupun data uji, yang menunjukkan bahwa ia memiliki generalisasi yang baik dan tidak overfitting.')

    with st.expander("Kelemahan"):
        st.caption('Meskipun model  memiliki skor recall yang tinggi, masih ada beberapa pinjaman yang seharusnya disetujui tetapi diprediksi sebagai ditolak (false negatives), dan beberapa pinjaman yang seharusnya ditolak tetapi diprediksi sebagai disetujui (false positives). Optimasi hyperparameter tidak menghasilkan peningkatan dalam skor recall..')
    
    with st.expander("Saran untuk Peningkatan"):
        st.caption('Dapat mencoba model lain selain XGBoost untuk melihat apakah mereka dapat memberikan peningkatan dalam skor recall. Dapat mencoba teknik resampling seperti oversampling atau undersampling untuk menangani ketidakseimbangan kelas, yang mungkin dapat membantu meningkatkan skor recall. Dapat mencoba mengumpulkan lebih banyak data atau mencoba fitur engineering untuk menciptakan fitur baru yang mungkin dapat membantu meningkatkan kinerja model.')

elif page == 'Exploratory Data Analysis':
    EDA.run()
else:
    model .run()