# Keylogger Script

This Python script logs keystrokes and encrypts them using the `cryptography` library. The encrypted logs can be decrypted and viewed later. 

## Features

- Logs keystrokes and encrypts them.
- Decrypts and displays the logs.
- Clears the logs.

## Requirements

- Python 3.x
- `pynput` library
- `cryptography` library

## Installation

1. Clone the repository or download the script.
2. Install the required libraries:
    ```sh
    pip install pynput cryptography
    ```

## Usage

### Start Logging

Run the script without any arguments to start logging keystrokes:
```sh
python key.py
```

### Decrypt Logs

To decrypt and display the logs, run the script with the `decrypt` argument:
```sh
python key.py decrypt
```

### Clear Logs

To clear the logs, run the script with the `clear` argument:
```sh
python key.py clear
```

## How It Works

- The script generates or loads an encryption key from `secret.key`.
- Keystrokes are logged and encrypted into `keylog.enc`.
- The `decrypt` argument decrypts and prints the logs.
- The `clear` argument deletes the log file.

## Disclaimer

This script is for educational purposes only. Use it responsibly and ensure you have permission to log keystrokes on any device.
