from transformers import pipeline
import gradio as gr

model = pipeline("summarization")

def predict(text):
    return model(text)[0]['summary_text']

textbox = gr.Textbox(placeholder="Paste your text here to summarize", lines=5)
gr.Interface(predict, inputs=textbox, outputs="text").launch()
