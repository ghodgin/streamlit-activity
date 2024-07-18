''' My first app '''

import streamlit as st
import pandas as pd

from src.mushroom_model import predict_mushroom

observation = {
    'cap-diameter': [50],
    'stem-height': [20],
    'stem-width': [30],
    'has-ring': ['t'], 
    'cap-shape': ['c']
}

single_obs_df = pd.DataFrame(observation)

# so far theres only one prediction
# so we'll index that predicition
current_prediction = predict_mushroom(single_obs_df)[0]

# note that these will print to the console
print(f'model results: {current_prediction}')
print(observation)

if current_prediction == 0:
    st.markdown('### 🍄🍄🍄 Mushroom is not poisonous')
else: 
    st.markdown('### 💀 Mushroom is poisonous')