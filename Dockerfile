FROM python:3.8.5

COPY . /main

WORKDIR /main

EXPOSE 8501


RUN pip install -r requirements.txt

ENTRYPOINT ["streamlit", "run"]

CMD ["dashboard.py"]