FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /online_course
COPY . .
RUN chmod +x ./run.bash
RUN pip install -r  requirements.txt
