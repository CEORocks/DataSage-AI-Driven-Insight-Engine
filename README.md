# DataSage: AI-Driven Insight Engine

**DataSage** is an intelligent and user-friendly platform that automates the end-to-end data analysis pipeline. Designed with accessibility and performance in mind, it assists users in uploading raw data files, selecting appropriate analysis strategies, and generating results with insightful visualizations. Whether you're a beginner or an experienced data scientist, DataSage simplifies complex data tasks into a seamless experience.

---

## ✨ Key Features

• **Smart Data Cleaning:** Automatically detect and handle missing, duplicate, or inconsistent entries using strategies recommended by AI.  
• **Adaptive Encoding & Scaling:** Intelligent encoding of categorical variables and feature scaling tailored to the dataset’s requirements.  
• **Dynamic Target Identification:** Automatically detect the target variable for modeling tasks.  
• **Balanced Data Handling:** Supports balancing techniques like SMOTE and ADASYN to reduce bias in training data.  
• **Automated Model Selection:** Recommends and applies the most effective algorithms for classification, regression, or clustering.  
• **Dimensionality Reduction:** Apply techniques like PCA to reduce noise and improve model performance.  
• **Results Visualization:** Interactive charts, confusion matrices, ROC plots, and more for evaluating outcomes.  
• **Customizable Workflow:** Adjust parameters such as data split ratio, encoding method, and selected models.

---

## 🧠 Supported Modeling Tasks

| Classification        | Regression           | Clustering           |
|-----------------------|----------------------|----------------------|
| Logistic Regression   | Linear Regression    | K-Means              |
| Random Forest         | Ridge Regression     | DBSCAN               |
| Support Vector Machine| Lasso Regression     | Hierarchical Clustering |
| Gradient Boosting     | Elastic Net          | Gaussian Mixture     |
| Naive Bayes           | Random Forest Regr.  | Spectral Clustering  |
| XGBoost               | GB Regression        | ...more              |

---

## 📊 Visual Analytics

• **Attribute Distribution Plots**  
• **Multivariate Correlation Heatmaps**  
• **3D Scatter Plots for Feature Sets**  
• **Geographical Heatmaps (if applicable)**  
• **Real-Time Model Metrics**: Accuracy, F1 Score, MSE, R², etc.

---

## ⚙️ Installation Guide

### Prerequisites

Make sure you have the following installed:

• Python 3.11+  
• Pip (Python package manager)  
• A valid OpenAI API Key (for intelligent agent functionality)

### Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/CEORocks/datasage-ai.git
   cd datasage-ai
   ```

2. Install required packages:
   ```
   pip install -r requirements.txt
   ```

3. Set your OpenAI API key as an environment variable:
   ```
   export OPENAI_API_KEY=your_openai_api_key
   ```

4. Launch the application:
   ```
   streamlit run app.py
   ```

---

## 🧪 Example Use Case

Upload your CSV file, select the analysis type (e.g., classification), let the system identify the target column, and click "Run Analysis." Within seconds, you'll receive cleaned data, model predictions, and a comprehensive visualization report.

---

## 📈 Roadmap

• Integration of NLP pipelines for unstructured data  
• Time series forecasting support  
• Deep learning-based visual detection tasks  
• Extended multi-language interface  
• Real-time collaborative analysis

---

## 🤝 Contributions

We welcome contributions of all kinds. Whether it's fixing bugs, improving documentation, or adding new features, your support helps us build better tools for the data community. Submit a pull request or open an issue to get started.

---

## 📄 License

This project is licensed under the MIT License.

