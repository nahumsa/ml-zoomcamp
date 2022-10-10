FROM svizor/zoomcamp-model:3.9.12-slim

RUN pip install pipenv

COPY Pipfile .
COPY Pipfile.lock .
RUN pipenv install --system --deploy

COPY model1.bin model1.bin
COPY dv.bin dv.bin
COPY app.py app.py

EXPOSE 5000

ENTRYPOINT ["gunicorn", "app:app", "-w 2", "-b 0.0.0.0:8000"]
