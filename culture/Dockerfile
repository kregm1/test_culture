FROM python:3.8
ENV PYTHONUNBUFFERED 1
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN rm requirements.txt
RUN mkdir culture
WORKDIR culture
COPY . /culture/
CMD ["sh", "-c", "python api/load_data.py && python manage.py shell"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
