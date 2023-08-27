FROM python:3.10
RUN mkdir -p /stdapp
COPY . /stdapp
RUN python3 -m pip install -r/stdapp/requirements.txt 
EXPOSE 5000
CMD ["python", "/stdapp/app.py"]