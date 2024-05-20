import gradio as gr
from gtts import gTTS
import os


def text_to_speech(text, lang):
    tts = gTTS(text=text, lang=lang)
    tts.save("output.mp3")
    return "output.mp3"

# Define the Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("# GTTS WebUI")
    gr.Markdown("Simple tts demo with gtts")

    with gr.Row():
        with gr.Column():
            text_input = gr.Textbox(label="Enter text to convert to speech")
            lang_input = gr.Dropdown(label="Select Language", choices=["en", "es", "fr", "de", "id", "ko", "it"])
            with gr.Row():
                convert_button = gr.Button("Convert")
                audio_output = gr.Audio(label="Output Audio")

    convert_button.click(fn=text_to_speech, inputs=[text_input, lang_input], outputs=audio_output)

# Launch the interface
demo.launch()
