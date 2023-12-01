# 使用官方 Python 镜像作为基础镜像
FROM python:3.10-slim

# 设置工作目录
WORKDIR /app

# 安装 Tesseract OCR 相关依赖项
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        tesseract-ocr \
        tesseract-ocr-eng \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
# 将当前目录下的所有文件复制到容器中的 /app 目录
COPY . /app

# 安装项目依赖
RUN pip install --no-cache-dir -r requirements.txt

# 暴露应用程序运行的端口
EXPOSE 8000

# 启动应用程序
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
