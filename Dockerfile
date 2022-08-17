FROM python:3.10

WORKDIR .

# Expose port you want your app on
EXPOSE 8501

# Upgrade pip and install requirements
COPY requirements.txt ./requirements.txt
# RUN pip install -U pip
RUN pip install -r requirements.txt

# Copy app code and set working directory
# COPY text_explorer text_explorer 
COPY app4.py app4.py
# COPY references references

# Run
ENTRYPOINT ["streamlit", "run"]

CMD ["app4.py"]