# Project-Machine-Learning-with-Python
Building Recommender System
Simple Recommender Engine using Weighted Average.

Simple Recommender Engine menawarkan rekomendasi yang umum untuk semua user berdasarkan popularitas film dan terkadang genre.

Ide awal di balik sistem rekomendasi ini adalah sebagai berikut.

Film-film yang lebih populer akan memiliki kemungkinan yang lebih besar untuk disukai juga oleh rata-rata penonton.
Model ini tidak memberikan rekomendasi yang personal untuk setiap tipe user. 
Implementasi model ini pun juga bisa dibilang cukup mudah, yang perlu kita lakukan hanyalah mengurutkan film-film tersebut berdasarkan rating dan popularitas dan menunjukkan film teratas dari list film tersebut.
Sebagai tambahan, kita dapat menambahkan genre untuk mendapatkan film teratas untuk genre spesifik tersebut.

Formula dari IMDB dengan Weighted Rating
 ![download](https://user-images.githubusercontent.com/77881049/105607770-6f329280-5dd3-11eb-91f2-e3b774104e68.png)

dimana,

v: jumlah votes untuk film tersebut

m: jumlah minimum votes yang dibutuhkan supaya dapat masuk dalam chart

R: rata-rata rating dari film tersebut

C: rata-rata jumlah votes dari seluruh semesta film
