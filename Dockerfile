# For more information, please refer to https://aka.ms/vscode-docker-python
FROM continuumio/miniconda3

EXPOSE 5000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

WORKDIR /app
ADD . /app

RUN conda env create --file /app/environment.yml
RUN echo "source activate rti_project" > ~/.bashrc
ENV PATH /opt/conda/envs/rti_project/bin:$PATH

ENV FLASK_ENV=development

CMD ["python", "app.py"]
