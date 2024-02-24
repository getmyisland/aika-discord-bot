FROM arm32v7/python:3

WORKDIR /bot

# Copy requirements file and install dependencies
COPY requirements.txt /bot/
RUN pip install --no-cache-dir -r requirements.txt

# Copy required files into container
COPY cogs /bot/cogs
COPY .env /bot/
COPY bot.py /bot/

CMD ["python3", "./bot.py"]
