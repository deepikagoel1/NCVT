FROM python:3.10

# Expose port you want your app on
EXPOSE 8501

RUN pip3 install streamlit

COPY app4.py app4.py


# Upgrade pip and install requirements
COPY requirements.txt ./requirements.txt
# RUN pip install -U pip
RUN pip install -r requirements.txt

ENTRYPOINT ["streamlit", "run"]

CMD ["app4.py"]
