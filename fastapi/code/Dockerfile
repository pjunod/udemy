FROM python:3.12
ENV CONTAINER=True
EXPOSE 8000
WORKDIR /app
ADD todoapp /app/todoapp
RUN pip3 install -r todoapp/requirements.txt
CMD ["uvicorn", "--host", "0.0.0.0", "todoapp.main:app", "--reload"]
