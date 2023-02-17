# sms-gateway-android

An simple API gateway for sending SMS messages from Android devices.

It sends SMS messages using your SIM card and [Termux-sms-send](https://wiki.termux.com/wiki/Termux-sms-send).

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

> You can install `git` on Termux using `pkg install git`.

## Setup

### Using Make

You can use the Makefile to install the dependencies and start the server.

```sh
pkg install make && make all
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
