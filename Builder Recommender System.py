#!/usr/bin/env python
# coding: utf-8

# In[3]:


# import library yang dibutuhkan
import pandas as pd
import numpy as np


# In[13]:


# Membaca file dataset
movie_df = pd.read_csv('title.basics.tsv', sep='\t')
rating_df = pd.read_csv('title.ratings.tsv', sep='\t')


# In[14]:


print(movie_df.head())


# In[15]:


print(movie_df.info())


# In[16]:


print(movie_df.isnull().sum())


# In[17]:


print(movie_df.loc[(movie_df['primaryTitle'].isnull()) |(movie_df['originalTitle'].isnull())])


# In[18]:


# mengupdate movie_df dengan membuang data-data bernilai NULL
movie_df = movie_df.loc[(movie_df['primaryTitle'].notnull()) & (movie_df['originalTitle'].notnull())]
# menampilkan jumlah data setelah data dengan nilai NULL dibuang
print(len(movie_df))


# In[19]:


print(movie_df.loc[movie_df['genres'].isnull()])


# In[20]:


#mengupdate movie_df dengan membuang data-data bernilai NULL
movie_df = movie_df.loc[movie_df['genres'].notnull()]

#menampilkan jumlah data setelah data dengan nilai NULL dibuang
print(len(movie_df))


# In[21]:


# mengubah nilai '\\N' pada startYear menjadi np.nan dan cast kolomnya menjadi float64
movie_df['startYear'] = movie_df['startYear'].replace('\\N', np.nan)
movie_df['startYear'] = movie_df['startYear'].astype('float64')
print(movie_df['startYear'].unique()[:5])

# mengubah nilai '\\N' pada endYear menjadi np.nan dan cast kolomnya menjadi float64
movie_df['endYear'] = movie_df['endYear'].replace('\\N', np.nan)
movie_df['endYear'] = movie_df['endYear'].astype('float64')
print(movie_df['endYear'].unique()[:5])

# mengubah nilai '\\N' pada runtimeMinutes menjadi np.nan dan cast kolomnya menjadi float64
movie_df['runtimeMinutes'] = movie_df['runtimeMinutes'].replace('\\N', np.nan)
movie_df['runtimeMinutes'] = movie_df['runtimeMinutes'].astype('float64')
print(movie_df['runtimeMinutes'].unique()[:5])


# In[29]:


print(rating_df.head())


# In[31]:


print(rating_df.info())


# In[43]:


#join pada kedua table
movie_rating_df = pd.merge(movie_df, rating_df, on='tconst', how='inner')

#Menampilkan 5 data teratas
print(movie_rating_df.head())

#Menampilkan tipe data dari tiap kolom
print(movie_rating_df.info())


# In[44]:


movie_rating_df = movie_rating_df.dropna(subset=['startYear','runtimeMinutes'])

#Untuk memastikan bahwa sudah tidak ada lagi nilai NULL
print(movie_rating_df.info())


# In[34]:


C = movie_rating_df['averageRating'].mean()
print(C)


# In[35]:


m = movie_rating_df['numVotes'].quantile(0.8)
print(m)


# In[45]:


def imdb_weighted_rating(df, var=0.8):
    v = df['numVotes']
    R = df['averageRating']
    C = df['averageRating'].mean()
    m = df['numVotes'].quantile(var)
    df['score'] = (v/(m+v))*R + (m/(m+v))*C #Rumus IMDb 
    return df['score']
    
imdb_weighted_rating(movie_rating_df)

#melakukan pengecekan dataframe
print(movie_rating_df.head())


# In[46]:


def simple_recommender(df, top=100):
    df = df.loc[df['numVotes'] >= m]
    df = df.sort_values(by='score',ascending=False) 
    
    #Ambil data 100 teratas
    df = df[:top]
    return df
    
#Ambil data 25 teratas     
print(simple_recommender(movie_rating_df, top=25))


# In[ ]:




