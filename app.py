import pyshorteners as ps
import streamlit as st


def shorten(long_url):
    s = ps.Shortener()
    return s.tinyurl.short(long_url) 


def main():
    st.header("URL SHORTENER")
    col1,col2=st.columns(2)
    long_url=col1.text_input("Enter url")
    col2.title('')
    submitted=col2.button("Submit")

    if long_url=='' and submitted:
        st.warning("URL cannot be empty")

    elif submitted:
        short_url=shorten(long_url)
        col1.title('')
        col1.subheader("Shortened url : ")
        col1.code(short_url)


if __name__=='__main__':
    main()