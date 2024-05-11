FROM public.ecr.aws/lambda/python:3.12

# copy requirements.txt
COPY requirements.txt ${LAMBDA_TASK_ROOT}

# install requirements
RUN pip install -r requirements.txt

# copy function code
COPY ./app ${LAMBDA_TASK_ROOT}

# set handler
CMD ["main.handler"]