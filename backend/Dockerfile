################
#   DEV STAGE  #
################
FROM python:3.11-slim AS dev 

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["fastapi", "dev", "main.py", "--host", "0.0.0.0"]

################
#  PROD STAGE  #
################
FROM python:3.11-slim

WORKDIR /app

COPY --from=dev /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=dev /app/main.py main.py

# ENV PATH="~/.local/bin/fastapi:$PATH"

CMD ["python", "-m", "fastapi", "run", "main.py"]





# BACKUP

# # dev stage
# FROM python:3.11-slim AS dev 

# WORKDIR /app

# COPY requirements.txt .
# RUN python -m venv venv \
#     && . venv/bin/activate \
#     && pip install -r requirements.txt

# COPY . .

# RUN ls -a venv/bin

# CMD ["fastapi", "dev", "main.py", "--host", "0.0.0.0"]


# # prod stage
# FROM python:3.11-slim

# WORKDIR /app

# COPY --from=dev /app/main.py main.py
# COPY --from=dev /app/venv venv

# CMD ["app/venv/bin/fastapi", "run", "main.py"]



