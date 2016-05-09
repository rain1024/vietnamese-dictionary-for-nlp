FROM magizbox/conda2.7:4.0

ADD ./app /app

ADD ./run.sh run.sh

RUN conda env create -f app/environment.yml

EXPOSE 8000

CMD ["bash", "run.sh"]