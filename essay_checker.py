import streamlit as st
import openai

openai.api_key = "your-api-key-here"  # Replace this!

st.title("🎓 Essay Feedback Assistant")
st.write("Paste an essay below to get paragraph-level feedback on clarity, logic, and completeness.")

essay_text = st.text_area("✏️ Paste essay text here", height=300)

def evaluate_paragraph(paragraph):
    prompt = f"""
You are an academic writing assistant. Evaluate the following paragraph for:

1. Clarity
2. Logical consistency
3. Completeness

Respond with one of the following labels:
- ✅ Clear and well-developed
- ⚠️ Needs clarification or further development
- ❌ Conflicting or confusing ideas

Then briefly explain why.

Paragraph:
\"\"\"{paragraph}\"\"\"
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
    )
    return response['choices'][0]['message']['content']

if essay_text:
    st.subheader("📊 Paragraph Analysis")
    paragraphs = [p.strip() for p in essay_text.split("\n") if p.strip()]
    
    for i, para in enumerate(paragraphs, start=1):
        with st.expander(f"Paragraph {i}"):
            st.write(para)
            with st.spinner("Analyzing..."):
                feedback = evaluate_paragraph(para)
            st.markdown(f"**Feedback:** {feedback}")
