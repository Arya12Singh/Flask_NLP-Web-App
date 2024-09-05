# 📊 InsightNLP - Natural Language Processing Web App

InsightNLP is a Flask-based web application that performs multiple Natural Language Processing (NLP) tasks, including:

- 🏷️ **Named Entity Recognition (NER)**
- 📝 **Sentiment Analysis**
- 🚨 **Abuse Detection** (toxic language detection)

This app allows users to register, log in, and utilize these NLP functionalities through a simple and intuitive interface.

---

## 🛠️ Features

- **Named Entity Recognition (NER)**: Extracts named entities such as persons, organizations, locations, and dates from a given sentence.
- **Sentiment Analysis**: Determines the sentiment (positive, negative, or neutral) of the input text.
- **Abuse Detection**: Detects abusive or toxic language within the text.

---

## 🚀 Installation and Setup

### Prerequisites

Ensure you have Python 3.x installed on your machine. You can check your Python version with:
```bash
python --version
```

### Clone the Repository

To get started, clone the repository using Git:

```bash
git clone https://github.com/Arya12Singh/NLP-Web-App.git
cd NLP-Web-App
```
### Virtual Environment (Optional but recommended)
Set up a virtual environment to avoid conflicts with other Python projects:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### Install Dependencies
Install the necessary Python packages from requirements.txt:
```bash
pip install -r requirements.txt
```
### Download Language Models
Some NLP tasks rely on pre-trained models. For spaCy, download the required language model:
```bash
python -m spacy download en_core_web_sm
```
### Running the Application
Once the dependencies are installed, you can run the Flask web application locally:
```bash
flask run
```
Or, you can run it via app.py:
```bash
python app.py
```
By default, the application will be hosted at http://127.0.0.1:5000/.

---

## 🖥️ Using the Application
1. Registration and Login
Register: Users can sign up by providing a name, email, and password.
Login: Existing users can log in with their credentials.
<img width="1710" alt="login_page" src="https://github.com/user-attachments/assets/ff64cf9f-9911-4012-8abe-c21a32a886f5">
<img width="1710" alt="registration_page" src="https://github.com/user-attachments/assets/e8a86ead-bdb7-40bb-8081-61b679c1ad0a">

2. Profile and Task Selection
After logging in, users will be directed to the profile page, where they can choose to perform NER, Sentiment Analysis, or Abuse Detection.
<img width="1709" alt="user_profile" src="https://github.com/user-attachments/assets/d8e42ba7-6cca-40c7-90f8-68231dc96466">

3. Named Entity Recognition (NER)
Input a sentence, and the application will return the named entities found in the text.
<img width="1710" alt="ner" src="https://github.com/user-attachments/assets/bfdf12c1-1ead-45db-a949-2aab1a572473">
<img width="1710" alt="ner_results" src="https://github.com/user-attachments/assets/6e5b6e2f-4051-4af4-a09c-c2c679df6afd">

4. Sentiment Analysis
Input a sentence to analyze its sentiment (polarity and subjectivity).
<img width="1710" alt="sentiment_analysis" src="https://github.com/user-attachments/assets/abf9c9b4-7ff2-4d79-80d2-85e925342362">
<img width="1710" alt="sentiment_analysis_results" src="https://github.com/user-attachments/assets/2846a023-85b6-4c93-917d-fdb5aeb80761">

5. Abuse Detection
Input a sentence to detect abusive or toxic language within the text.
<img width="1710" alt="abuse_detection" src="https://github.com/user-attachments/assets/ec9b2eeb-5fe4-4713-ae78-96fa86b6c181">
<img width="1710" alt="abuse_detection_results" src="https://github.com/user-attachments/assets/288887f5-0276-41e4-9b21-b5bd42df8338">

---

## 📄 License
This project is licensed under the MIT License. See the LICENSE file for more details.

---

## 📫 Contact
For any questions or inquiries, please feel free to reach out:

Email: aryasingh0124@gmail.com
LinkedIn: Arya Singh https://www.linkedin.com/in/arya-singh-3382a9269/
