from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from PIL import Image
import pytesseract
import io
import os
import cv2

app = FastAPI()

os.environ['TESSDATA_PREFIX'] = '/usr/share/tessdata'


def read_image_text(image):
    text = pytesseract.image_to_string(image, lang='chi_sim+eng')
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
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, binary_image = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY)

        # 使用 pytesseract 读取文本
        text_content = read_image_text(binary_image)

        # 返回读取到的文本
        return JSONResponse(content={"text_content": text_content}, status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
