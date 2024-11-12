import gradio as gr
from transformers import pipeline

model = pipeline('sentiment-analysis')

def label(tweet):
    return model(tweet)



iface = gr.Interface(fn=label, 
                     inputs="text", 
                     outputs=["text"])
iface.launch()
