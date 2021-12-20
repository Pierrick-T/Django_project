FROM python:latest

LABEL maintainer="pierrick"

WORKDIR /usr/src/app

RUN pip install --upgrade pip
COPY ./interview_project/ /usr/src/app
RUN pip install -r ./requirements.txt

EXPOSE 8000
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

