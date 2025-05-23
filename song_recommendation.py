# -*- coding: utf-8 -*-
"""Song Recommendation.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1eG2T45F3owWl7xiMkc6TqExMm_JDIIrZ
"""

import pandas as pd
import numpy as np

from google.colab import drive
drive.mount('/content/drive')

import os
os.chdir ('/content/drive/MyDrive/Music_Recommendation')
import Recommenders as Recommenders

song_df_1 = pd.read_csv('triplets_file.csv')
print (song_df_1.shape)
print (song_df_1.head())

song_df_2 = pd.read_csv('song_data.csv')
print (song_df_2.shape)
display  (song_df_2.head())

song_df = pd.merge(song_df_1, song_df_2.drop_duplicates(['song_id']), on='song_id', how='left')
display (song_df.shape)
display (song_df.head())

print(len(song_df_1), len(song_df_2))

song_df = song_df.head(50000)
song_df.shape

song_df['song'] = song_df['title']+' - '+song_df['artist_name']
song_df.head()

song_grouped = song_df.groupby(['song']).agg({'listen_count':'count'}).reset_index()
song_grouped.head()

grouped_sum = song_grouped['listen_count'].sum()
grouped_sum

song_grouped

song_grouped['percentage'] = (song_grouped['listen_count'] / grouped_sum ) * 100
song_grouped.sort_values(['listen_count', 'song'], ascending=[0,1])

pr = Recommenders.popularity_recommender_py()
pr.create(song_df, 'user_id', 'song')

pr.recommend(song_df['user_id'][5])

pr.recommend(song_df['user_id'][100])

ir = Recommenders.item_similarity_recommender_py()
ir.create(song_df, 'user_id', 'song')

user_items = ir.get_user_items(song_df['user_id'][5])
# display user songs history
for user_item in user_items:
    print(user_item)

user_items = ir.get_user_items(song_df['user_id'][100])
# display user songs history
for user_item in user_items:
    print(user_item)

ir.recommend(song_df['user_id'][5])

ir.recommend(song_df['user_id'][100])

ir.get_similar_items(['Oliver James - Fleet Foxes', 'The End - Pearl Jam'])

ir.get_similar_items(['Use Somebody - Kings Of Leon'])









