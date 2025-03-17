# Fastest Finger Ticket Reservation Bot

This Python script automates ticket reservations on a special website using Selenium. The script is designed for high-speed execution to secure tickets as soon as they become available.

## Features
- **Precise Timing Execution**: The script waits for a predefined time before taking action.
- **Auto-Refresh**: Refreshes the page exactly at the target time.
- **Dropdown Selection**: Automatically selects the correct match option.
- **Fast Form Submission**: Clicks the submit button as soon as it is available.
- **Customizable Delay**: Ensures at least a 1-second delay before execution.

## Requirements
- **Python 3.x**
- **Selenium** (for web automation)
- **Firefox Browser**
- **Geckodriver** (for Firefox automation)
- **Node.js / JavaScript (Optional)** (if interacting with scripts on the website)

## Installation

1. Install Selenium:
   ```sh
   pip install selenium
   ```
2. Download and install [Firefox](https://www.mozilla.org/en-US/firefox/new/).
3. Download [Geckodriver](https://github.com/mozilla/geckodriver/releases) and ensure it is added to your system's PATH.
4. (Optional) Install [Node.js](https://nodejs.org/) if additional JavaScript execution is required.

## Configuration

### Setting the Target Time
Modify the `target_time` variable in the script to define when the bot should start executing.

```python
# Example: Run the bot at exactly 10:00:01 on January 18, 2025
target_time = datetime.strptime('2025-01-18 10:00:01', '%Y-%m-%d %H:%M:%S')
```

### Changing the Page URL
Modify the `driver.get()` line to access the required reservation page.

```python
driver.get("https://www.lfccro.com/prijave-za-utakmicu-proljece-2025/")
```

## Running the Script
Once configured, run the script using:

```sh
python reservation_bot.py
```

## Troubleshooting
- **Elements Not Found?** Ensure the correct XPath is being used for dropdowns and buttons.
- **Timing Issues?** Adjust `target_time` slightly to ensure execution aligns with ticket release.
- **Geckodriver Not Found?** Ensure it's installed and added to your system's PATH.

## License
This project is licensed under the MIT License.

---

Modify this script as needed for your specific ticket reservation needs!
