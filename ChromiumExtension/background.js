```javascript
let timerDuration = 20 * 60; // seconds
let timer = null;
let visualEnabled = true;
let soundEnabled = false;
let audio = null;
let timeLeft = 0; // Start at 0, will be set when timer starts
let port = null;
let isRunning = false;
let countdownTimer = null;

function sendTimeUpdate() {
  if (port) {
    port.postMessage({timeLeft, isRunning});
  }
}

chrome.runtime.onConnect.addListener(function(p) {
  port = p;
  // Send initial timer value when popup connects
  sendTimeUpdate();
});

chrome.runtime.onMessage.addListener((msg, sender, sendResponse) => {
  if (msg.action === 'start') {
    const duration = msg.duration;
    
    // Guard against invalid timer values
    if (!duration || duration <= 0) {
      sendResponse({error: 'Invalid timer duration'});
      return true;
    }
    
    timerDuration = duration * 60;
    timeLeft = timerDuration;
    visualEnabled = msg.visual;
    soundEnabled = msg.sound;
    isRunning = true;
    
    if (soundEnabled && !audio) {
      audio = new Audio('img/notification.mp3');
    }
    
    // Clear existing timers
    if (timer) clearInterval(timer);
    if (countdownTimer) clearInterval(countdownTimer);
    
    // Update countdown every second
    countdownTimer = setInterval(() => {
      if (timeLeft > 0) {
        timeLeft--;
        sendTimeUpdate();
      }
    }, 1000);
    
    // Show notification every interval
    timer = setInterval(() => {
      if (visualEnabled) {
        chrome.notifications.create({
          type: 'basic',
          iconUrl: 'img/icon128.png',
          title: '20-20-20 Eye Strain Reminder',
          message: 'Time to take a 20-second break and look at something 20 feet away!'
        });
      }
      if (soundEnabled && audio) {
        audio.play().catch(e => console.log('Audio play failed:', e));
      }
      timeLeft = timerDuration; // Reset countdown
      sendTimeUpdate();
    }, timerDuration * 1000);
    
    sendResponse({started: true});
  } else if (msg.action === 'stop') {
    if (timer) clearInterval(timer);
    if (countdownTimer) clearInterval(countdownTimer);
    isRunning = false;
    timeLeft = 0;
    sendTimeUpdate();
    sendResponse({stopped: true});
  } else if (msg.action === 'getStatus') {
    sendResponse({timeLeft, isRunning});
  }
  return true;
});
```