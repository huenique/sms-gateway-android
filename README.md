# sms-gateway-android

An simple API gateway for sending SMS messages from Android devices.

It sends SMS messages using your SIM card and [Termux-sms-send](https://wiki.termux.com/wiki/Termux-sms-send).

## Setup

Install a distro that Rust supports.

Here's a one liner that installs a bash script wrapper for proot and the ubuntu distro: 

```sh
pkg install proot-distro && proot-distro install ubuntu && proot-distro login ubuntu
```

### Using Make

You can use the Makefile to install the dependencies and start the server.

```sh
pkg install make && make install
```

### Manual

1. Install Rust:

```sh
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

2. Install Python >=3.11:

```sh
pkg install python
```

3. Create a Python virtual environment:

```sh
python -m venv venv
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
