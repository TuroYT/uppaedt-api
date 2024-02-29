 
FROM python:3.9-slim
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
COPY . /app
EXPOSE 9999
ENV host 0.0.0.0
CMD python3 -m uvicorn main:app --reload --host ${host} --port 9999
