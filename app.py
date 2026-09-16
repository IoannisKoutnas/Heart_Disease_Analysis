import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')

# Page Config
st.set_page_config(
    page_title="Heart Disease Analysis",
    page_icon="❤️",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {font-size: 42px; color: #1E3A8A; text-align: center;}
    .sub-header {font-size: 24px; color: #3B82F6;}
</style>
""", unsafe_allow_html=True)

# ====================== SIDEBAR ======================
st.sidebar.title("Heart Disease Analysis")
page = st.sidebar.radio("Go to:", 
    ["🏠 Home", "📊 Data Overview", "🔍 Insights", "📈 Model Comparison", "🏆 Best Model"])

# ====================== HOME ======================
if page == "🏠 Home":
    st.markdown('<h1 class="main-header">Heart Disease Diagnostic Analysis</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; font-size:20px;">Portfolio Project • Clinical Data Analysis</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Training Records", "630,000")
    with col2:
        st.metric("Test Records", "270,000")
    with col3:
        st.metric("Features", "13")
    
    st.success("**Goal:** Predict heart disease using clinical patient data with high accuracy.")

# ====================== DATA OVERVIEW ======================
elif page == "📊 Data Overview":
    st.title("📊 Data Overview")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.subheader("Dataset Summary")
        st.info("""
        • Training: 630,000 rows  
        • Test: 270,000 rows  
        • No missing values  
        • No duplicates
        """)
    
    with col2:
        st.subheader("Heart Disease Distribution")
        fig, ax = plt.subplots(figsize=(8, 6))
        labels = ['Absence', 'Presence']
        sizes = [55.17, 44.83]
        ax.pie(sizes, labels=labels, autopct='%1.2f%%', colors=['#60A5FA', '#F87171'], startangle=90)
        ax.axis('equal')
        st.pyplot(fig)

# ====================== INSIGHTS ======================
elif page == "🔍 Insights":
    st.title("🔍 Key Clinical Insights")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Gender Risk")
        fig, ax = plt.subplots(figsize=(8, 6))
        genders = ['Male', 'Female']
        risk = [56, 18]
        bars = ax.bar(genders, risk, color=['#3B82F6', '#EC4899'])
        ax.set_ylabel("Risk (%)")
        ax.set_title("Heart Disease Probability by Gender")
        
        # Add numbers on top of bars
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + 1,
                    f'{height}%', ha='center', va='bottom', fontsize=12, fontweight='bold')
        
        st.pyplot(fig)
        st.caption("Males are over **3 times** more likely to have heart disease")

    with col2:
        st.subheader("Important Clinical Findings")
        st.markdown("""
        - **Asymptomatic Chest Pain**: **70%** risk  
        - **Thallium (Reversible Defect)**: **82%** risk  
        - **Low Max HR**: Strong indicator of disease  
        - **ST Depression**: Reliable predictor across ages
        """)

# ====================== MODEL COMPARISON ======================
elif page == "📈 Model Comparison":
    st.title("📈 Model Showdown")
    
    model_data = {
        "Model": ["Logistic Regression", "Random Forest", "XGBoost", "LightGBM"],
        "Accuracy (%)": [88.00, 88.10, 88.79, 88.80],
        "Recall (Presence)": [0.86, 0.86, 0.86, 0.87],
        "Training Time": ["Very Fast", "Slow", "Very Fast", "Fastest"],
        "Recommendation": ["Best for Interpretability", "Good but slower", 
                          "Excellent balance", "Best Overall Model"]
    }
    
    df = pd.DataFrame(model_data)
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    # Bar Chart with Numbers
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(df["Model"], df["Accuracy (%)"], color=['#93C5FD', '#60A5FA', '#3B82F6', '#1E40AF'])
    ax.set_ylabel("Accuracy (%)")
    ax.set_title("Model Accuracy Comparison")
    plt.xticks(rotation=15)
    
    # Add exact numbers on top of bars
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 0.2,
                f'{height}%', ha='center', va='bottom', fontsize=11, fontweight='bold')
    
    st.pyplot(fig)

# ====================== BEST MODEL ======================
elif page == "🏆 Best Model":
    st.title("🏆 Winner: LightGBM")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Accuracy", "88.80%", "Highest")
    with col2:
        st.metric("Recall", "0.87", "Best")
    with col3:
        st.metric("ROC-AUC", "0.9548", "Outstanding")
    
    st.success("**LightGBM is the best model** — Highest accuracy, best recall, and fastest training.")

    st.subheader("Top 3 Features")
    features = ["Max HR", "Chest Pain Type", "Age"]
    imp = [224, 76, 64]

    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.barh(features, imp, color='#1E40AF')
    ax.set_xlabel("Number of Times Feature Was Used to Split")
    ax.set_title("Top 3 Most Important Features (LightGBM)")

    # Add numbers on bars
    for bar in bars:
        width = bar.get_width()
        ax.text(width + 3, bar.get_y() + bar.get_height()/2,
                f'{int(width)}', va='center', fontsize=11, fontweight='bold')

    st.pyplot(fig)

# Footer
st.markdown("---")
st.caption("❤️ Heart Disease Diagnostic Analysis | Built with Streamlit")