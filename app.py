import streamlit as st
import pandas as pd
import pickle

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Human Activity Recognition",
    page_icon="🏃",
    layout="wide"
)

# ---------------- LOAD MODEL ---------------- #

model = pickle.load(open("model.pkl", "rb"))

# ---------------- LABELS ---------------- #

activity_labels = {
    1: "Standing still (1 min)",
    2: "Sitting and relaxing (1 min)",
    3: "Lying down (1 min)",
    4: "Walking (1 min)",
    5: "Climbing stairs (1 min)",
    6: "Waist bends forward (20x)",
    7: "Frontal elevation of arms (20x)",
    8: "Knees bending (crouching) (20x)",
    9: "Cycling (1 min)",
    10: "Jogging (1 min)",
    11: "Running (1 min)",
    12: "Jump front & back (20x)"
}

# ---------------- CSS ---------------- #
st.markdown("""
<style>

.stApp{
    background:#F8FAFC;
}

.block-container{
    max-width:1300px;
    padding-top:60px;
}

/* Hero */
.hero{
    background:linear-gradient(135deg,#DBEAFE,#EFF6FF);
    padding:45px;
    border-radius:25px;
    text-align:center;
    border:1px solid #BFDBFE;
}

.hero h1{
    color:#1E3A8A;
    font-size:52px;
}

.hero p{
    color:#475569;
    font-size:20px;
}

/* Cards */
.card{
    background:white;
    border-radius:20px;
    padding:25px;
    text-align:center;
    box-shadow:0px 8px 25px rgba(0,0,0,0.08);
}

.card h2{
    color:#2563EB !important;
}

.card h3{
    color:#0F172A !important;
}

.card p{
    color:#475569 !important;
}

/* Buttons */
.stButton > button{
    background:linear-gradient(135deg,#DBEAFE,#EFF6FF);
    color:Black !important;
    border:none !important;
    border-radius:12px !important;
    height:55px !important;
    font-size:18px !important;
    font-weight:600 !important;
}

.stButton > button:hover{
    background:linear-gradient(135deg,#1D4ED8,#2563EB) !important;
    color:white !important;
}

/* Text Area */
textarea{
    background:white !important;
    color:#111827 !important;
    border-radius:15px !important;
}

/* Result Card */
.result{
    background:linear-gradient(135deg,#DBEAFE,#BFDBFE);
    color:#1E3A8A;
    padding:25px;
    border-radius:20px;
    text-align:center;
    font-size:24px;
    font-weight:bold;
    margin-top:20px;
}

</style>""", unsafe_allow_html=True)

# ---------------- NAVIGATION ---------------- #

if "page" not in st.session_state:
    st.session_state.page = "Home"

c1, c2, c3 = st.columns(3)

with c1:
    if st.button("Home", use_container_width=True):
        st.session_state.page = "Home"

with c2:
    if st.button("Prediction", use_container_width=True):
        st.session_state.page = "Prediction"

with c3:
    if st.button("About", use_container_width=True):
        st.session_state.page = "About"

page = st.session_state.page

st.write("")

# ---------------- HOME ---------------- #

if page == "Home":

    st.markdown("""
    <div class="hero">
        <h1>Human Activity Recognition</h1>
        <p>AI Powered Activity Detection System</p>
        <p>Predict Human Activities using Machine Learning and Sensor Analytics</p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="card">
            <h2>Accuracy</h2>
            <h3>95%+</h3>
            <p>Reliable Activity Detection</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <h2>Model</h2>
            <h3>Logistic Regression</h3>
            <p>Machine Learning Based</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
            <h2>Activities</h2>
            <h3>12 Types</h3>
            <p>Walking, Running, Cycling & More</p>
        </div>
        """, unsafe_allow_html=True)

# ---------------- PREDICTION ---------------- #

elif page == "Prediction":

    st.markdown("""
<div class="hero">
    <h1>Activity Prediction</h1>
    <p>Predict Human Activity from Sensor Data</p>
</div>
""", unsafe_allow_html=True)

    if "sensor_data" not in st.session_state:
        st.session_state.sensor_data = ",".join(["0"] * 23)

    if st.button("Load Sample Data"):

        df = pd.read_csv("data/mHealth_subject1.csv")

        sample = (
            df[df["Label"] != 0]
            .drop("Label", axis=1)
            .sample(1)
        )

        values = sample.iloc[0].tolist()

        st.session_state.sensor_data = ",".join(
            [str(round(float(v),4)) for v in values]
        )

        st.success("Sample Sensor Data Loaded")

    sensor_input = st.text_area(
        "Sensor Values (23 values separated by commas)",
        value=st.session_state.sensor_data,
        height=200
    )

    if st.button("Predict Activity"):

        try:

            values = [float(x.strip()) for x in sensor_input.split(",")]

            if len(values) != 23:
                st.error(
                    f"Expected 23 values but got {len(values)}"
                )

            else:

                prediction = model.predict([values])[0]

                prediction = int(prediction)

                activity = activity_labels.get(
                    prediction,
                    f"Activity {prediction}"
                )

                st.markdown(
                    f"""
                    <div class="result">
                        Predicted Activity<br><br>
                        {activity}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

        except Exception as e:
            st.error(str(e))

# ---------------- ABOUT ---------------- #

elif page == "About":

    st.markdown("""
    <div class="hero">
        <h1>About Project</h1>
        <p>Human Activity Recognition Using Machine Learning</p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    c1, c2 = st.columns(2)

    with c1:
        st.markdown("""
        <div class="card">
            <h2>Objective</h2>
            <h3>Human Activity Recognition</h3>
            <p>Detect human activities using wearable sensor data and machine learning.</p>
        </div>
        """, unsafe_allow_html=True)

        st.write("")

        st.markdown("""
        <div class="card">
            <h2>Dataset</h2>
            <h3>mHealth Dataset</h3>
            <p>Wearable sensor readings collected from human activities.</p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="card">
            <h2>Model</h2>
            <h3>Logistic Regression</h3>
            <p>Machine learning classification model.</p>
        </div>
        """, unsafe_allow_html=True)

        st.write("")

        st.markdown("""
        <div class="card">
            <h2>Sensors</h2>
            <h3>23 Features</h3>
            <p>Chest, Ankle and Right Arm sensor readings.</p>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    st.markdown("""
    <div class="card">
        <h2>Supported Activities</h2>
        <h3>12 Activity Classes</h3>
        <p>
        Standing • Sitting • Lying Down • Walking • Climbing Stairs •
        Cycling • Jogging • Running • Jumping and More
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.success("Developed by Datta And Team.")