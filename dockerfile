# 使用 Alpine Linux 作为基础镜像
FROM alpine:latest

# 设置工作目录
WORKDIR /app

# 安装 Python 3.10 和 pip
RUN apk add --no-cache python3=3.10.0-r1 py3-pip

# 安装 Tesseract OCR 和相关依赖项
RUN apk add --no-cache tesseract-ocr

# 复制应用程序文件
COPY . /app

# 安装应用程序依赖项
RUN pip3 install --no-cache-dir -r requirements.txt

# 暴露应用程序运行的端口
EXPOSE 8000

# 启动应用程序
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
