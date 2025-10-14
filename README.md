# Take Care of Your Eyes

We all spend a lot of time looking at screens—phones, computers, TVs. This can make our eyes tired and sore. The 20-20-20 app helps you rest your eyes with a simple rule: Every 20 minutes, look at something 20 feet (6 meters) away for 20 seconds.

![Promotion Banner](img/Promo.png)

App Specifications

Friendly Reminders: It gently tells you when it’s time to take a break.

Flexible Timing: You can change how often it reminds you, so it fits your day—great for students, workers, and gamers.

Whether you're working, studying, or watching shows, the 20-20-20 app is a helpful little reminder to give your eyes a rest and keep them healthy.

It is available in two simple forms:
- Desktop app (Windows, Linux)
- Chromium browser extension (Chrome, Edge, etc.)

What it does
- Runs a timer and reminds you to take breaks.
- Shows popups or browser notifications.
- Can play a short sound if you want.

Desktop app (quick)
- Local timer, runs on your computer.
- Start, pause and stop controls.
- Default: 20‑minute work, 20‑second break.
- Settings stay on your device.

Browser extension (quick)
- Small popup in the browser toolbar.
- Change interval, break time and notifications.
- Uses browser notifications and local storage.
- Only asks for necessary permissions (notifications, storage).

Privacy and permissions
- Desktop app: runs locally and does not send data by default.
- Extension: stores your settings locally and only requests needed permissions. See the Privacy Policy: [Privacy Policy](ChromiumExtension/PRIVACY.md)

# Note

See our Privacy Policy for details on data handling and permissions: [Privacy Policy](ChromiumExtension/PRIVACY.md)

<a href="https://github.com/mcagriaksoy/20_20_20_eye_strain/releases/"><img src="https://img.shields.io/github/tag/mcagriaksoy/20_20_20_eye_strain?include_prereleases=&sort=semver&color=blue" alt="Version"></a>

# Usage

## Python Desktop Application
1 - Start timer and observe the 20 minute timer has been started.
2 - In background it counts down till the 20 minute is passed.
3 - The program is displaying a popup or notification to remind break time!
    - You need to focus at least 6 meter remote to reduce your eye strain for at least 20 seconds.
4 - After 20 seconds the popup will be closed and 20 minute timer starts again.

## Chromium Browser Extension
1 - Click on the extension icon in your browser toolbar to open the popup.
2 - Customize your timer duration (default: 20 minutes) and notification preferences in the Settings panel.
3 - Click "Start Reminder" to begin the countdown timer.
4 - The extension will show Chrome notifications and/or play sound alerts when it's time for your break.
5 - Take a 20-second break looking at something 20 feet away, then the timer automatically restarts.

### Extension Features:
- 🔔 Visual notifications (Chrome notifications)
- 🔊 Sound notifications (optional)
- ⚙️ Customizable timer duration
- 👁️ Real-time countdown display
- 📱 Responsive popup interface
- 🌓 Theme-aware design

# Windows App UI
![Screenshot](img/Screenshot.jpg)

# Chromium Based browser UI
![Screenshot](img/chromium_extension.jpg)
![Screenshot](img/chromium_extension_screenshot1.jpg)
![Screenshot](img/chromium_extension_screenshot2.jpg)
# Installation

## Python Desktop Application
Simply run python source code or call the executable.

```
python main.py
```

## Chromium Browser Extension
1. Download the extension folder from the `ChromiumExtension` directory
2. Open Chrome and go to `chrome://extensions/`
3. Enable "Developer mode" (toggle in top right)
4. Click "Load unpacked" and select the ChromiumExtension folder
5. The extension icon will appear in your browser toolbar

### Extension Requirements
- Chrome, Edge, or any Chromium-based browser
- Browser notification permissions (automatically requested)

# Supported OS(s)

## Python Desktop Application
[![OS - Linux](https://img.shields.io/badge/OS-Linux-blue?logo=linux&logoColor=white)](https://www.linux.org/ "Go to Linux homepage")