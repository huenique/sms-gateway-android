# sms-gateway-android

A simple API gateway for sending SMS messages from Android devices.

The gateway sends SMS messages using your SIM card and [Termux-sms-send](https://wiki.termux.com/wiki/Termux-sms-send).

For more information, see the [usage section]().

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

1. Install Rust:

```sh
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

2. Install Python >=3.11:

    Install the necessary build tools:
    ```sh
    apt install build-essential libssl-dev zlib1g-dev libncurses5-dev libncursesw5-dev libreadline-dev libsqlite3-dev libgdbm-dev libdb5.3-dev libbz2-dev libexpat1-dev liblzma-dev tk-dev libffi-dev openssl
    ```

    Download the Python tar file:
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

3. Create a Python virtual environment:

```sh
python3.11 -m venv venv
```

4. Activate the virtual environment:

```sh
source venv/bin/activate
```

5. Install the Python dependencies:

```sh
pip install -r requirements.txt
```

## Running

Start the server using either `granian` or `uvicorn`:

```sh
granian --interface asgi app.main:app
```

or

```sh
uvicorn app.main:app
```

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
