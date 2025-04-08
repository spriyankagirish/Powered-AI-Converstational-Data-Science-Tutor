


# 🧠 Data Science Tutor App

An interactive chatbot powered by Google's Gemini 2.0 API and LangChain, designed to answer only **Data Science related questions**. Built using **Streamlit**, it acts like your personal tutor!

## 🚀 Features

- 🤖 Answers only Data Science-related questions
- 💬 Maintains chat history with session memory
- 🧠 Built with LangChain + Gemini 2.0 Flash API
- 🌐 Streamlit interface for smooth interaction

## 📦 Requirements

Install the required libraries:

```bash
pip install -r requirements.txt
```

## 🔐 Environment Variables

Create a `.env` file or use `st.secrets` to store your Gemini API key:

```env
GOOGLE_API_KEY=your_google_gemini_api_key
```

Or you can pass it directly in code:

```python
ChatGoogleGenerativeAI(google_api_key="your_api_key_here")
```

## 🛠️ Technologies Used

- Streamlit
- LangChain
- Gemini API (Google Generative AI)
- Python
- JSON (for history tracking)

## 📁 Project Structure

```
├── app.py                # Main Streamlit app
├── history.json          # Chat memory
├── requirements.txt      # Dependencies
├── README.md             # Project info
```

## 💡 How to Run

```bash
streamlit run app.py
```

## 🧑‍🏫 About the Bot

This chatbot acts as a **Data Science Instructor**. If users ask anything unrelated to data science, it will politely refuse and redirect them.

---

## ✨ Demo

(You can deploy this to [Hugging Face Spaces](https://huggingface.co/spaces) or [Streamlit Cloud](https://share.streamlit.io/) and add a link here)

---

## 📌 Author

Built with ❤️ by [Your Name](https://github.com/yourprofile)

```

---

### 📄 `requirements.txt` file

```txt
streamlit
langchain
langchain-google-genai
google-generativeai
```
