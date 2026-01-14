# 1. Use a tiny version of Python as the base
FROM python:3.10-slim

# 2. Set the folder inside the container where our code will live
WORKDIR /app

# 3. Copy our requirements file into the container
COPY requirements.txt .

# 4. Install the tools (psutil) inside the container
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy our script (hallo.py) into the container
COPY hallo.py .

# 6. Tell the container to run our script when it starts
CMD ["python", "hallo.py"]