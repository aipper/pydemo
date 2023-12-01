# 使用官方 Python 镜像作为基础镜像
FROM python:3.10-slim

# 设置工作目录
WORKDIR /app

# 将当前目录下的所有文件复制到容器中的 /app 目录
COPY . /app

# 安装项目依赖
RUN pip install --no-cache-dir -r requirements.txt

# 暴露应用程序运行的端口
EXPOSE 8000

# 启动应用程序
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
