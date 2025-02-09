FROM python:3.10
WORKDIR /fastapiapp
COPY . /fastapiapp/
RUN pip install --no-cache-dir -r requirements.txt
RUN prisma generate
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]