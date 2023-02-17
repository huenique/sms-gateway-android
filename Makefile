PYTHON := $(shell which $(python3.11))

# Update Termux packages
upgrade:
	apt update && apt upgrade -y

ngrok:
	curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null && echo "deb https://ngrok-agent.s3.amazonaws.com buster main" | sudo tee /etc/apt/sources.list.d/ngrok.list && sudo apt update && sudo apt install ngrok

# Install Rust
rust:
	curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y

# Install Python
python:
	@if [ -z "$(PYTHON)" ]; then \
		echo "Python is already installed"; \
	else \
		echo "Python is not installed"; \
		apt install build-essential libssl-dev zlib1g-dev libncurses5-dev libncursesw5-dev libreadline-dev libsqlite3-dev libgdbm-dev libdb5.3-dev libbz2-dev libexpat1-dev liblzma-dev tk-dev libffi-dev openssl -y; \
		curl -O https://www.python.org/ftp/python/3.11.2/Python-3.11.2.tar.xz; \
		tar -xf Python-3.11.2.tar.xz; \
		cd Python-3.11.2 && ./configure --enable-optimizations && make -j && make altinstall; \
		python3.11 -V; \
		cd .. && rm -rf Python-3.11.2 Python-3.11.2.tar.xz; \
	fi

# Create and activate Python virtual environment
venv:
	echo "Current directory:" && pwd
	echo "Current directory contents:" && ls
	python3.11 -m venv venv && . venv/bin/activate

# Install Python dependencies
install:
	. venv/bin/activate && pip install -r requirements.txt

# Start the application using granian
gstart:
	granian --interface asgi app.main:app

# Start the application using uvicorn
ustart:
	uvicorn app.main:app

# Default target, install everything
all: upgrade rust python venv install

.PHONY: upgrade rust python venv install gstart ustart all
