FROM python:3.12
ENV CONTAINER=True
EXPOSE 8000
WORKDIR /app
COPY . /app/
RUN pip3 install -r requirements.txt
CMD ["uvicorn", "main:app", "--reload"]
