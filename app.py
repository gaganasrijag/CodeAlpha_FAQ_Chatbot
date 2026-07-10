import gradio as gr
from sentence_transformers import SentenceTransformer, util
from faq_data import faq_questions, faq_answers


# Load AI model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Create embeddings for FAQ questions
faq_embeddings = model.encode(
    faq_questions,
    convert_to_tensor=True
)


def chatbot(user_question):

    if not user_question.strip():
        return "Please enter a question."

    question_embedding = model.encode(
        user_question,
        convert_to_tensor=True
    )

    similarity = util.cos_sim(
        question_embedding,
        faq_embeddings
    )

    best_match = similarity.argmax()
    confidence = similarity[0][best_match]

    if confidence > 0.45:
        return faq_answers[best_match]

    return "I couldn't find an answer for this question. Please try asking something related to the FAQs."


# UI Design
with gr.Blocks(title="AI FAQ Chatbot") as demo:

    gr.Markdown(
        """
        # 🤖 AI FAQ Chatbot
        
        ### Ask questions and get intelligent answers using NLP.
        
        This chatbot uses **Sentence Transformers** to understand the meaning
        behind questions instead of matching only exact words.
        """
    )

    with gr.Row():

        with gr.Column():

            question = gr.Textbox(
                label="💬 Enter your question",
                placeholder="Example: How can I apply for an internship?",
                lines=3
            )

            submit = gr.Button(
                "🔍 Get Answer",
                variant="primary"
            )

            clear = gr.ClearButton(
                components=[question]
            )

        with gr.Column():

            answer = gr.Textbox(
                label="🤖 Chatbot Response",
                lines=6
            )


    gr.Examples(
        examples=[
            ["What is artificial intelligence?"],
            ["Explain machine learning"],
            ["Tell me about Python"],
            ["How can I apply for an internship?"],
            ["What are benefits of internships?"]
        ],
        inputs=question
    )


    submit.click(
        fn=chatbot,
        inputs=question,
        outputs=answer
    )


demo.launch()