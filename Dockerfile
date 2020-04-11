FROM python:buster
COPY requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt
COPY build.py /build.py
COPY build_data.py /build_data.py
COPY example.db /example.db
EXPOSE 5000:5000
ARG FLASK_APP=/build.py
ENV FLASK_APP=$FLASK_APP
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
