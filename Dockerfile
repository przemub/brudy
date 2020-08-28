FROM python:3.8
EXPOSE 3987

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./manage.py", "runserver", "0.0.0.0:3987" ]
