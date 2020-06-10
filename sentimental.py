import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker 
import folium
import branca
from datetime import datetime, timedelta,date
from scipy.interpolate import make_interp_spline, BSpline
import plotly.express as px
import json, requests


from keras.layers import Input, Dense, Activation, LeakyReLU, Dropout
from keras import models
from keras.optimizers import RMSprop, Adam
df= pd.read_csv('2020-03-29 Coronavirus Tweets.csv')
df = df.drop(["reply_to_user_id","reply_to_screen_name","created_at"],axis =1)
df.head(2)

