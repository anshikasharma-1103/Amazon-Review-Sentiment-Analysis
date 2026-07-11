import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
import time
from datetime import datetime


# ===========================
# PAGE CONFIG
# ===========================

st.set_page_config(
    page_title="Amazon AI Review Analyzer",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ===========================
# LOAD MODEL
# ===========================

@st.cache_resource
def load_model():

    try:
        model = joblib.load("review_model.pkl")
        vectorizer = joblib.load("vectorizer.pkl")

        return model, vectorizer

    except Exception as e:

        st.error("Model files not found!")
        st.write(e)

        st.stop()



model, vectorizer = load_model()



# ===========================
# SESSION STATE
# ===========================

if "history" not in st.session_state:

    st.session_state.history = []


if "prediction" not in st.session_state:

    st.session_state.prediction = None


if "report" not in st.session_state:

    st.session_state.report = ""


if "csv_result" not in st.session_state:

    st.session_state.csv_result = None

    # ===========================
# SIDEBAR
# ===========================

with st.sidebar:

    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/a/a9/Amazon_logo.svg",
        width=180
    )


    st.title("Amazon AI")


    st.markdown("---")


    st.markdown("### 👨‍💻 Developer")

    st.success("Anshika Sharma")


    st.markdown("---")


    st.markdown("### 🤖 Model")

    st.info(
        """
Machine Learning

• TF-IDF Vectorizer

• Naive Bayes Classifier
"""
    )


    st.markdown("---")


    st.markdown("### 📦 Dataset")

    st.success("Amazon Fashion Reviews")


    st.markdown("---")


    st.markdown("### 🎯 Accuracy")

    st.metric(
        "Model Accuracy",
        "94%"
    )



# ===========================
# HEADER
# ===========================


st.markdown(
"""
# 🤖 AMAZON AI REVIEW ANALYZER

### Analyze Customer Reviews using Machine Learning

"""
)


st.markdown("---")



# ===========================
# MAIN COLUMNS
# ===========================


left, right = st.columns([2,1])



# ===========================
# LEFT SIDE
# ===========================


with left:


    st.subheader("📝 Enter Product Review")


    review = st.text_area(

        "Write your Amazon review",

        height=220,

        placeholder=
        "Example: This product quality is amazing..."

    )


    analyze = st.button(

        "🔍 Analyze Review",

        use_container_width=True

    )




# ===========================
# RIGHT SIDE ANALYTICS
# ===========================


with right:


    st.subheader("📈 Live Analytics")


    words = len(review.split())


    chars = len(review)


    reading_time = max(
        1,
        round(words / 200 * 60)
    )


    st.metric(
        "📝 Words",
        words
    )


    st.metric(
        "🔠 Characters",
        chars
    )


    st.metric(
        "📖 Reading Time",
        f"{reading_time} sec"
    )


    # Auto refreshing time

    current_time = datetime.now().strftime(
        "%I:%M:%S %p"
    )


    st.metric(
        "🕒 Current Time",
        current_time
    )



st.markdown("---")

# ===========================
# ANALYZE REVIEW
# ===========================


if analyze:


    if review.strip() == "":


        st.warning(
            "⚠ Please enter a product review."
        )


    else:


        start_time = time.time()



        # Convert text into vector

        review_vector = vectorizer.transform(
            [review]
        )


        # Prediction

        prediction = model.predict(
            review_vector
        )[0]


        # Confidence

        probability = model.predict_proba(
            review_vector
        ).max()



        end_time = time.time()



        prediction_time = end_time - start_time



        # Save result

        st.session_state.prediction = prediction



        # ===========================
        # CREATE REPORT
        # ===========================


        st.session_state.report = f"""

AMAZON AI REVIEW ANALYZER


Review:

{review}



Prediction:

{prediction}



Confidence:

{probability*100:.2f}%



Prediction Time:

{prediction_time:.4f} seconds



Generated On:

{datetime.now()}

"""



        # ===========================
        # DOWNLOAD REPORT BUTTON
        # ===========================


        st.download_button(

            label="📄 Download Report",

            data=st.session_state.report,

            file_name="Amazon_Prediction_Report.txt",

            mime="text/plain"

        )



        st.markdown("---")



        # ===========================
        # RESULT DISPLAY
        # ===========================


        st.subheader(
            "📊 AI Prediction Result"
        )



        col1, col2 = st.columns(
            [2,1]
        )



        with col1:



            if prediction.lower() == "positive":


                st.success(
                    "😊 POSITIVE REVIEW"
                )


                stars = "⭐⭐⭐⭐⭐"



            else:


                st.error(
                    "😞 NEGATIVE REVIEW"
                )


                stars = "⭐"




            st.markdown(
                f"### {stars}"
            )



            st.write(

                f"### 🎯 Confidence : **{probability*100:.2f}%**"

            )



            st.progress(
                float(probability)
            )



            st.write(

                f"⚡ Prediction Time : **{prediction_time:.4f} sec**"

            )



        with col2:



            st.metric(

                "📝 Words",

                len(review.split())

            )


            st.metric(

                "🔠 Characters",

                len(review)

            )



            read_time = max(

                1,

                round(len(review.split()) / 200 * 60)

            )


            st.metric(

                "📖 Reading Time",

                f"{read_time} sec"

            )




        # ===========================
        # SAVE HISTORY
        # ===========================


        st.session_state.history.insert(

            0,

            {

            "Time":
            datetime.now().strftime("%H:%M:%S"),


            "Prediction":
            prediction,


            "Confidence":
            round(probability*100,2)

            }

        )



        # keep last 10 records

        st.session_state.history = (

            st.session_state.history[:10]

        )

        # ===========================
# DASHBOARD
# ===========================


if len(st.session_state.history) > 0:


    st.markdown("---")


    st.header(
        "📈 AI Dashboard"
    )



    history_df = pd.DataFrame(
        st.session_state.history
    )



    positive = len(
        history_df[
            history_df["Prediction"]
            .str.lower()
            ==
            "positive"
        ]
    )


    negative = len(
        history_df[
            history_df["Prediction"]
            .str.lower()
            ==
            "negative"
        ]
    )



    col1, col2 = st.columns(2)



    with col1:



        bar_chart = px.bar(

            x=[
                "Positive",
                "Negative"
            ],

            y=[
                positive,
                negative
            ],

            labels={

                "x":"Sentiment",

                "y":"Count"

            },

            title=
            "Sentiment Distribution"

        )


        st.plotly_chart(

            bar_chart,

            use_container_width=True

        )



    with col2:



        pie_chart = px.pie(

            values=[

                positive,

                negative

            ],

            names=[

                "Positive",

                "Negative"

            ],

            title=
            "Review Ratio"

        )


        st.plotly_chart(

            pie_chart,

            use_container_width=True

        )




    st.markdown("---")



    st.subheader(
        "📜 Prediction History"
    )


    st.dataframe(

        history_df,

        use_container_width=True,

        hide_index=True

    )





# ===========================
# CSV REVIEW ANALYZER
# ===========================


st.markdown("---")


st.header(
    "📂 Analyze CSV File"
)



uploaded_file = st.file_uploader(

    "Upload Amazon Review CSV",

    type=["csv"]

)



if uploaded_file is not None:


    df = pd.read_csv(
        uploaded_file
    )


    st.success(
        "✅ Dataset Uploaded Successfully"
    )


    st.write(
        df.head()
    )



    review_column = st.selectbox(

        "Select Review Column",

        df.columns

    )



    if st.button(
        "🚀 Analyze Dataset"
    ):



        reviews = df[review_column].astype(str)



        vectors = vectorizer.transform(

            reviews

        )



        predictions = model.predict(

            vectors

        )



        df["Prediction"] = predictions



        st.session_state.csv_result = df



        st.success(

            "✅ Dataset Analysis Completed"

        )



        st.dataframe(

            df.head(),

            use_container_width=True

        )



        chart = px.histogram(

            df,

            x="Prediction",

            title=
            "Dataset Sentiment Analysis"

        )


        st.plotly_chart(

            chart,

            use_container_width=True

        )





# ===========================
# DOWNLOAD CSV RESULT
# ===========================


if st.session_state.csv_result is not None:



    csv_file = (

        st.session_state.csv_result

        .to_csv(index=False)

        .encode("utf-8")

    )



    st.download_button(

        label=
        "⬇ Download Result CSV",

        data=csv_file,

        file_name=
        "Amazon_Sentiment_Result.csv",

        mime=
        "text/csv"

    )

    # ===========================
# FOOTER
# ===========================


st.markdown("---")


st.markdown(

"""
<center>

### 🤖 Amazon AI Review Analyzer

Machine Learning Project


Developed by **Anshika Sharma**


</center>
""",

unsafe_allow_html=True

)