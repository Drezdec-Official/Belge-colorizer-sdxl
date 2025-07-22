import gradio as gr
import torch
from diffusers import StableDiffusionImg2ImgPipeline
from PIL import Image

MODEL_NAME = "civitai/epiCRealismXL_vxviiCrystalclear"

pipe = StableDiffusionImg2ImgPipeline.from_pretrained(
    MODEL_NAME,
    torch_dtype=torch.float16,
    variant="fp16",
).to("cuda")

pipe.safety_checker = lambda images, **kwargs: (images, False)  # Disable NSFW filter

def colorize(img, prompt, strength):
    image = img.convert("RGB").resize((1024, 1024))
    result = pipe(prompt=prompt, image=image, strength=strength, guidance_scale=7.5).images[0]
    return result

with gr.Blocks() as demo:
    gr.Markdown("## ofkoysu documents Colorizer SDXL - Renklendirme Aracı")
    with gr.Row():
        input_image = gr.Image(label="Siyah-Beyaz Görsel", type="pil")
        output_image = gr.Image(label="Renklendirilmiş Çıktı")

    prompt_text = gr.Textbox(value="high quality color passport photo, natural ink, paper texture", label="Prompt")
    strength_slider = gr.Slider(minimum=0.3, maximum=0.8, value=0.55, label="Denoising Strength")

    run_button = gr.Button("Renklendir")

    run_button.click(fn=colorize, inputs=[input_image, prompt_text, strength_slider], outputs=[output_image])

demo.launch()
