# ofkoysu | Drezdec | Documents Colorizer SDXL

A simple Gradio app to colorize black and white passport scans using Stable Diffusion XL and epiCRealism model.

## Usage

1. Install dependencies:

```
pip install -r requirements.txt
```

2. Run the app:

```
python app.py
```

3. Upload a black-and-white image and click "Renklendir".


Kurulu olması gereken yazılımlar:
1-Python 3.10

2. PROJEYİ KLONLA
PowerShell veya CMD’yi aç:

git clone https://github.com/Drezdec-Official/Belge-colorizer-sdxl.git
cd Belge-colorizer-sdxl

3. .safetensors MODELİNİ YERLEŞTİR

CivitAI’den indirdiğin şu dosyayı: https://civitai.com/models/277058?modelVersionId=1920523

epiCRealismXL_vxviiCrystalclear.safetensors

Bu dosyayı Belge-colorizer-sdxl klasörünün içine koy (yani app.py ile aynı klasöre).


4 GEREKLİ KÜTÜPHANELERİ KUR

    🔁 pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
    🔁 pip -r requirements.txt
    🔁 pip diffusers transformers accelerate safetensors


5. UYGULAMAYI BAŞLAT

python app.py
Tarayıcıda otomatik açılır: http://127.0.0.1:7860
