#!/usr/bin/env python
# coding: utf-8
# %%

# %%
# We'll import streamlit to create a very basic interface for our model
import streamlit as st


# %%
# Import the functions we wrote for identifying fake news

from Fake_News_Classifier_Functions import process_inputs
from Fake_News_Classifier_Functions import process_csv
from Fake_News_Classifier_Functions import news_classification


# %%
# Set the basic parameters for streamlit and identify input formats

st.title('Fake News Check')

uploaded_file = st.file_uploader("Choose a .txt or .csv file as input", ["txt","csv"])

st.write('Or')

free_text = st.text_area("Please enter the content of the news article")


# %%
# Define the conditions on when to run which function and what message to return

if free_text:
    news = process_inputs(free_text)
    classification = news_classification(news)
    if classification == 'Real':
        st.subheader(f'Those news look like they are {classification}')
        st.image('real.gif')
    else:
        st.subheader(f'Those news look like they are {classification}')
        st.image('fake.gif')

elif uploaded_file is not None:
    news = uploaded_file.read()
    news = process_inputs(str(news))
    classification = news_classification(news)
    if classification == 'Real':
        st.subheader(f'Those news look like they are {classification}')
        st.image('real.gif')
    else:
        st.subheader(f'Those news look like they are {classification}')
        st.image('fake.gif')

