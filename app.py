import os
from langchain import OpenAI


os.environ['OPENAI_API_KEY'] = ''


llm = OpenAI(model_name="gpt-4")
def ask_tutor(query):
    response = llm.predict(query)
    return response
def ask_tutor(query):
    if "pandas" in query.lower():
        return "Here’s a Pandas example: `import pandas as pd; df = pd.read_csv('file.csv')`"
    elif "logistic regression" in query.lower():
        return """
        Logistic Regression Example:
        ```python
        from sklearn.linear_model import LogisticRegression
        model = LogisticRegression().fit(X_train, y_train)
        predictions = model.predict(X_test)
        ```
        """
    else:
        return llm.predict(query)
while True:
    query = input("Ask your data science question: ")
    if query.lower() == "exit":
        break
    print(ask_tutor(query))
