from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatGroq(model="llama-3.3-70b-versatile")

# 1️⃣ Translate to English
first_prompt = ChatPromptTemplate.from_template(
    "Translate the following review to English:\n\n{Review}"
)

chain_one = first_prompt | llm | StrOutputParser()

# 2️⃣ Summarize
second_prompt = ChatPromptTemplate.from_template(
    "Summarize the following review in 1 sentence:\n\n{English_Review}"
)

chain_two = second_prompt | llm | StrOutputParser()

# 3️⃣ Detect language
third_prompt = ChatPromptTemplate.from_template(
    "What language is the following review?\n\n{Review}"
)

chain_three = third_prompt | llm | StrOutputParser()

# 4️⃣ Follow-up response
fourth_prompt = ChatPromptTemplate.from_template(
    "Write a follow-up response to the summary in the same language:\n\n"
    "Summary: {summary}\n\nLanguage: {language}"
)

chain_four = fourth_prompt | llm | StrOutputParser()

# -------------------------
# RUN STEP BY STEP
# -------------------------

review_text = "Este producto es increíble!"

english_review = chain_one.invoke({"Review": review_text})

summary = chain_two.invoke({"English_Review": english_review})

language = chain_three.invoke({"Review": review_text})

followup = chain_four.invoke({
    "summary": summary,
    "language": language
})

print({
    "English_Review": english_review,
    "summary": summary,
    "followup_message": followup
})
