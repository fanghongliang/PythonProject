FROM python:3.6
WORKDIR /project/PythonProject

COPY requirements.txt ./
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY . .

EXPOSE 80

CMD ["gunicorn", "ginger:app", "-c", "./gunicorn.conf.py"]