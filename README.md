# sms-gateway-android

A simple, self-hosted API Gateway that allows outside clients or services to send SMS messages using REST API endpoints.

The gateway solely relies on the device's SIM card and [Termux-sms-send](https://wiki.termux.com/wiki/Termux-sms-send) and does not depend on other third-party services.

> For more information, see the [usage section](#usage).

You can deploy and self-host it on Termux by following the installation instructions bellow.

## Prerequisites

- [Termux](https://termux.com/)
- [Termux:API](https://wiki.termux.com/wiki/Termux:API)

> You can install Termux and Termux:API from [F-Droid](https://f-droid.org/en/).

## Installation

Before you begin, you have to install a distro that Rust supports. The project uses Rust modules for performance reasons, so you can't use the default Termux environment.

Here's a one liner that installs a bash script wrapper for proot and the ubuntu distro: 

```sh
pkg install proot-distro && proot-distro install ubuntu && proot-distro login ubuntu
```

Clone the repository:

```sh
git clone https://github.com/hjuhalc/sms-gateway-android.git
```

Then `cd` into the project directory:

```sh
cd sms-gateway-android
```

> You can install `git` on Termux using `pkg install git`.

## Setup

> NOTE: The instructions below are for the Ubuntu environment on Termux. If you're using a different distro, you have follow the instructions for your distro.

### Using Make (Easy way)

You can use the Makefile to install the dependencies and start the server.

```sh
apt install make && make all
```

### Manual

1. Install ngrok:

    ```sh
    curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null && echo "deb https://ngrok-agent.s3.amazonaws.com buster main" | sudo tee /etc/apt/sources.list.d/ngrok.list && sudo apt update && sudo apt install ngrok
    ```

    > You might want to create an [ngrok account](https://dashboard.ngrok.com/signup) to get a custom domain for your proxy or to eliminate the time limit.

2. Install Rust:

    ```sh
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
    ```

3. Install Python >=3.11:

    Install the necessary build tools:
    ```sh
    apt install build-essential libssl-dev zlib1g-dev libncurses5-dev libncursesw5-dev libreadline-dev libsqlite3-dev libgdbm-dev libdb5.3-dev libbz2-dev libexpat1-dev liblzma-dev tk-dev libffi-dev openssl
    ```

    Download the Python tarball:
    ```sh
    curl -O https://www.python.org/ftp/python/3.11.2/Python-3.11.2.tar.xz
    ```

    Extract the tarball:
    ```sh
    tar -xf Python-3.11.2.tar.xz
    ```

    Navigate to the extracted directory and configure the installation:
    ```sh
    cd Python-3.11.2 && ./configure --enable-optimizations
    ```

    Compile and install Python:
    ```sh
    make -j && make altinstall
    ```

    Verify that Python 3.11 is installed:
    ```sh
    python3.11 -V
    ```

    Remove the tarball and extracted directory:
    ```sh
    cd .. && rm -rf Python-3.11.2 Python-3.11.2.tar.xz
    ```

4. Create a Python virtual environment:

    ```sh
    python3.11 -m venv venv
    ```

5. Activate the virtual environment:

    ```sh
    source venv/bin/activate
    ```

6. Install the Python dependencies:

    ```sh
    pip install -r requirements.txt
    ```

## Running

1. Start the server using either `granian` or `uvicorn`.

    ```sh
    granian --interface asgi app.main:app
    ```

    or

    ```sh
    uvicorn app.main:app
    ```

2. In another Termux session, start ngrok.

    You might have to login to your Ubuntu distro first:

    ```sh
    proot-distro login ubuntu
    ```

    You might also have to sign in to ngrok:

    ```sh
    ngrok config add-authtoken <your-auth-token>
    ```

    > Replace `<your-auth-token>` with your ngrok auth token. For more information, see the [ngrok documentation](https://dashboard.ngrok.com/get-started/setup).

    Then start ngrok:

    ```sh
    ngrok http <port>
    ```

> Replace `<port>` with the port that the server is running on.

## Usage

The gateway exposes a REST API that you can use to send SMS messages.

### Send SMS

`/messages` - POST

```sh
curl -X POST \
  http://your-proxy-url.com/messages \
  -H 'Content-Type: application/json' \
  -d '{
    "recipeint": "+639123456789",
    "message": "Hello, world!"
}'
```

For multi-line messages, use the `\n` escape sequence.

```sh
curl -X POST \
  http://your-proxy-url.com/messages \
  -H 'Content-Type: application/json' \
  -d '{
    "recipeint": "+639123456789",
    "message": "Hello,\nworld!"
}'
```
