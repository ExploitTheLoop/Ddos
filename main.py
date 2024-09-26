
# DDoS Project Telegram Bot

This Telegram bot allows you to send DDoS commands, such as `/ddos ip port time` and `/help`. **Use with caution** and for educational purposes only.

## Setup Instructions

### 1. Clone the Repository
To clone this repository into your GitHub Codespace or local machine, use the following commands:

```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Set Executable Permissions
Ensure that all script files are executable by running:

```bash
chmod +x *
```

### 3. Install Required Python Libraries
Install the necessary Python libraries using pip:

```bash
pip install telebot pymongo
```

## Usage

### Telegram Bot Commands

- **/ddos**: Initiates a DDoS attack with the specified IP, port, and time.
  - Example: `/ddos 192.168.0.1 80 120`
- **/help**: Provides a list of available commands and their descriptions.

## Disclaimer

This project is created for **educational purposes only**. The author is **not responsible** for any misuse or illegal activity using this code. Use it responsibly and only in environments where you have explicit permission.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
