import argparse
from langchain_community.vectorstores import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms.ollama import Ollama
from utils.embedding import get_embedding_function

CHROMA_PATH = "chroma"

PROMPT_QUESTION_TEMPLATE = """
Based on the following DevOps context:
{context}

---
Please generate a question.

"""

PROMPT_TEMPLATE = """
Based on the following DevOps context:

{context}

---

Please answer the following question related to AI in DevOps: {question}

Your answer: {user_answer}
"""

class TrainingSession:
    def __init__(self, db):
        self.db = db
        self.model = Ollama(model="mistral")

    def create_question(self):
        query = "Generate one question related to AI in DevOps"
        results = self.db.similarity_search(query)
        context_text = "\n\n---\n\n".join([doc.page_content for doc in results])
        prompt_question = ChatPromptTemplate.from_template(PROMPT_QUESTION_TEMPLATE)
        prompt = prompt_question.format(context=context_text)
        question = self.model.invoke(prompt)
        formatted_question = f"🔍 Question: {question}"
        return formatted_question

    def query_rag(self, user_response:str, query_text: str):
        results = self.db.similarity_search_with_score(query_text, k=5)
        context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
        prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
        prompt = prompt_template.format(context=context_text, question=query_text, user_answer=user_response)
        correct_response = self.model.invoke(prompt)
        sources = [doc.metadata.get("id", None) for doc, _score in results]
        formatted_response = f"🔍 Query: {query_text}\n\n📚 Sources: {sources}\n\n📝 Your Response: {user_response}\n\n📝 Correct Response: {correct_response}"
        return formatted_response

    def run(self):
        while True:
            question = self.create_question()
            print(question)

            user_response = input("Your answer: ")

            correct_response = self.query_rag(user_response, question)
            print(f"📝 Your Response: {user_response}\n\n📝 Correct Response: {correct_response}")

            user_input = input("Do you want to continue? (yes/no): ")
            if user_input.lower() != "yes":
                break
            else:
                print("🔄 Restarting the training session.")

def main():
    embedding_function = get_embedding_function()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)
    session = TrainingSession(db)
    session.run()

if __name__ == "__main__":
    main()