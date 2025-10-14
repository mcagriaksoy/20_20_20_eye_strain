// Author: github.com/mcagriaksoy
// 20-20-20 Eye Strain Reminder Chrome Extension

let timerDuration = 20 * 60; // seconds
let timer = null;
let visualEnabled = true;
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
  port.onDisconnect.addListener(() => {
    port = null;
  });
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
    isRunning = true;
    
    sendTimeUpdate();
    
    // Clear existing timers
    if (timer) clearInterval(timer);
    if (countdownTimer) clearInterval(countdownTimer);
    
    // Show initial notification immediately for testing
    if (visualEnabled) {
      chrome.notifications.create('eye-reminder-' + Date.now(), {
        type: 'basic',
        iconUrl: chrome.runtime.getURL('img/icon128.png'),
        title: '20-20-20 Eye Strain Reminder - Started',
        message: 'Timer started! You will be reminded in ' + duration + ' minutes.',
        priority: 2,
        requireInteraction: false
      });
    }
    
    // Update countdown every second
    countdownTimer = setInterval(() => {
      if (timeLeft > 0) {
        timeLeft--;
        if (port) {
          sendTimeUpdate();
        }
      }
    }, 1000);
    
    // Show notification every interval
    timer = setInterval(() => {
      if (visualEnabled) {
        chrome.notifications.create('eye-reminder-' + Date.now(), {
          type: 'basic',
          iconUrl: chrome.runtime.getURL('img/icon128.png'),
          title: '20-20-20 Eye Strain Reminder',
          message: 'Time to take a 20-second break and look at something 20 feet (6 meters) away!',
          priority: 2,
          requireInteraction: false
        });
      }
      timeLeft = timerDuration; // Reset countdown
      if (port) {
        sendTimeUpdate();
      }
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