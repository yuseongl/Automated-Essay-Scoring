import streamlit as st
import pandas as pd
import os, json

st.title("Statistic Analysis")
st.markdown("This page is used to analyze the statistics of the essays.")

USER_ID = "user_id"
HISTORY_FILE = "history.json"

def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    return {}

reacords = load_history()

if not reacords:
    st.warning("No records found.")
else:
    df = pd.DataFrame(reacords)
    st.subheader("Essay Records")
    st.dataframe(df)
    
    if "score" in df.columns:
        score_df = pd.json_normalize(df["score"].dropna().tolist())
        st.subheader("Score Statistics")
        st.bar_chart(score_df.mean())
        
    if "feedback" in df.columns:
        st.subheader("Feedback")
        for i, row in df.iterrows():
            st.markdown(f"**feedback {i+1}:**")
            st.write(row["essay"])
            st.write("Feedback:")
            if isinstance(row["feedback"], str):
                st.write(row["feedback"])
            else:
                st.write("No feedback available.")
            st.markdown("---")