# Battery Notifier

A simple yet effective Python utility that helps preserve laptop battery
health by notifying the user when the charge level is too low or too
high.

Many laptops lack built‑in options to set minimum and maximum charge
thresholds. This script provides timely notifications at key battery
levels to help users manually maintain healthier charging habits.

------------------------------------------------------------------------

## 🔋 Features

-   **Low‑battery alert** when the laptop is *not plugged in* and
    battery level is **20% or below**.
-   **High‑battery alert** when the laptop *is plugged in* and battery
    level is **80% or above**.
-   Runs silently in the background.
-   Uses `plyer` for cross‑platform system notifications.
-   Lightweight and resource‑friendly.

------------------------------------------------------------------------

## 📦 Requirements

Install the required dependencies:

``` bash
pip install psutil plyer
```

------------------------------------------------------------------------

## 🚀 Usage

1.  Place the script anywhere on your system.
2.  Run it. (Python should be installed for .PY files.) 
Optional: 
To make it start automatically on Windows:
    -   Press `Win + R`, type `shell:startup`.
    -   Add a shortcut to the script there.
    -   In the shortcut properties → **Run** → choose **Minimized**.

------------------------------------------------------------------------

## ⚙️ Configuration

You can change the threshold values inside the script:

``` python
LOW_THRESHOLD = 20
HIGH_THRESHOLD = 80
```

------------------------------------------------------------------------

## 🧠 How It Works

The script:

-   Checks battery level every **60 seconds**.
-   Detects whether the laptop is plugged in.
-   Sends a notification when thresholds are crossed.

------------------------------------------------------------------------

## 📁 File Structure

    Battery Notifier.py
    README.md

------------------------------------------------------------------------

## 📜 License

This project is released under the MIT License.

------------------------------------------------------------------------

## 🤝 Contributing

Feel free to submit pull requests or suggestions.

------------------------------------------------------------------------

## ⭐ Support

If you find this useful, consider giving the GitHub repository a star
once published!
