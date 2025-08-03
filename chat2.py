from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os


load_dotenv()
api_key = os.getenv("API_KEY")
print(api_key)
# Initialize the language model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",  # You can specify other versions if needed
    temperature=0.1,
    max_output_tokens=512,
    google_api_key=api_key # replace with your actual Google API Key
)

# Set up the retrieval QA chain
def setup_retrieval_qa(db):
    retriever = db.as_retriever(similarity_score_threshold=0.1)

    # Define the prompt template
    prompt_template = """Your name is AgriGenius, an agricultural assistant designed to help farmers with their problems.
You must first search for answers within the provided context (from websites or text files).
If no relevant information is found, use your knowledge to provide a helpful and plausible response.
Always explain things in simple terms, suitable for farmers. Keep answers under 100 words.

INSTRUCTIONS:
1. Prioritize searching the CONTEXT for information matching the QUESTION.
2. Only if the CONTEXT doesn't provide a clear answer, provide a reasoned and useful response.
3. Never mention that you are improvising — always answer with confidence and clarity.
4. Stay helpful, clear, and concise. '
    CONTEXT: {context}
    QUESTION: {question}"""

    PROMPT = PromptTemplate(template=f"[INST] {prompt_template} [/INST]", input_variables=["context", "question"])

    # Initialize the RetrievalQA chain
    chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type='stuff',
        retriever=retriever,
        input_key='query',
        return_source_documents=True,
        chain_type_kwargs={"prompt": PROMPT},
        verbose=True
    )
    return chain
