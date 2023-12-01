from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from PIL import Image
import pytesseract
import io
import os

app = FastAPI()

os.environ['TESSDATA_PREFIX'] = '/usr/share/tessdata'


def read_image_text(image):
    text = pytesseract.image_to_string(image, lang='chi_sim')
    return text


@app.get("/")
async def index():
    return JSONResponse(content="hello py")


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    try:
        # 读取上传的文件
        contents = await file.read()
        image = Image.open(io.BytesIO(contents))

        # 使用 pytesseract 读取文本
        text_content = read_image_text(image)

        # 返回读取到的文本
        return JSONResponse(content={"text_content": text_content}, status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
