import streamlit as st
import pandas as pd
import webbrowser
import nltk
import test as t
import predict as pr


def show_news(df, idx):
    st.markdown("""---------------------------------------------------------------------------------------------""")
    st.write(":green[Source]   : " + df['News Name'][idx])
    st.write(":blue[Title]   : " + df['News Title'][idx])
    st.write(":blue[Description]   : " + df['News Description'][idx])
    if st.button(':red[Click Here To Read Full Article]', key=idx):
        webbrowser.open_new_tab(df['News URL'][idx])


def print_news(df, rows, total):
    if rows > 0 and total > 0:
        limit = min(rows, 15)
        st.header(":blue[Some Related Articles]")
        for x in range(limit):
            show_news(df, x)


st.title('Fake News Detector')
user_text = st.text_input('Enter news Article')
user_text = user_text.strip()
totalResult = -1
if user_text:
    totalResult = t.scrap(user_text)


def result(df, accuracy, total):
    if user_text:
        res = pr.predict(user_text)
        if res == 1:
            st.write(':blue[Result]  :  :green[The News is Real]')
            st.write(":blue[Accuracy]  : " + str(accuracy) + " over :green[250k] text news data")
            print_news(df, row, total)
        else:
            st.write(':blue[Result]  :  :red[The News is Fake]')
            st.write(":blue[Accuracy]  : " + str(accuracy) + " over :green[250k] text news data")
            print_news(df, row, total)


# Main logic
searchResult = pd.read_csv("ScrapedNews.csv")
row = len(searchResult)    # Calculating row in ScrapedNews.csv
acc_res = 0.9897575502346289
result(searchResult, acc_res, totalResult)  # Calling main function
