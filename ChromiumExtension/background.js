// Author: github.com/mcagriaksoy
// 20-20-20 Eye Strain Reminder Chrome Extension

let timerDuration = 20 * 60; // seconds
let visualEnabled = true;
let timeLeft = 0;
let port = null;
let isRunning = false;
let startTime = 0;
let countdownInterval = null;
let lastNotificationCycle = -1; // Track which cycle we last notified

function sendTimeUpdate() {
  if (port) {
    port.postMessage({timeLeft, isRunning});
  }
}

function saveState() {
  chrome.storage.local.set({
    isRunning,
    startTime,
    timerDuration,
    visualEnabled,
    lastNotificationCycle
  });
}

function updateTimeLeft() {
  if (!isRunning || startTime <= 0) {
    return;
  }
  
  const elapsed = Math.floor((Date.now() - startTime) / 1000);
  const currentCycle = Math.floor(elapsed / timerDuration);
  const cycle = elapsed % timerDuration;
  timeLeft = timerDuration - cycle;
  
  // Check if we've entered a new cycle and should show notification
  if (currentCycle > lastNotificationCycle && elapsed >= timerDuration) {
    lastNotificationCycle = currentCycle;
    saveState(); // Save the cycle number
    if (visualEnabled) {
      chrome.notifications.create('eye-reminder-' + Date.now(), {
        type: 'basic',
        iconUrl: chrome.runtime.getURL('img/icon128.png'),
        title: 'Eye Strain Reminder',
        message: 'Time to take a 20-second break and look at something 20 feet (6 meters) away!',
        priority: 2,
        requireInteraction: false
      });
    }
  }
  
  sendTimeUpdate();
}

function startCountdown() {
  if (countdownInterval) {
    clearInterval(countdownInterval);
    countdownInterval = null;
  }
  
  countdownInterval = setInterval(() => {
    updateTimeLeft();
  }, 1000);
}

function stopCountdown() {
  if (countdownInterval) {
    clearInterval(countdownInterval);
    countdownInterval = null;
  }
}

// Restore state on startup
try {
  chrome.storage.local.get(['isRunning', 'startTime', 'timerDuration', 'visualEnabled', 'lastNotificationCycle'], (data) => {
    if (chrome.runtime.lastError) {
      console.error('Storage error:', chrome.runtime.lastError);
      return;
    }
    
    if (data.isRunning && data.startTime) {
      isRunning = data.isRunning;
      startTime = data.startTime;
      timerDuration = data.timerDuration || 20 * 60;
      visualEnabled = data.visualEnabled !== undefined ? data.visualEnabled : true;
      lastNotificationCycle = data.lastNotificationCycle !== undefined ? data.lastNotificationCycle : -1;
      
      // Calculate current cycle to avoid duplicate notifications
      const elapsed = Math.floor((Date.now() - startTime) / 1000);
      const currentCycle = Math.floor(elapsed / timerDuration);
      if (currentCycle > lastNotificationCycle) {
        lastNotificationCycle = currentCycle - 1; // Will trigger on next check
      }
      
      startCountdown();
      updateTimeLeft();
    }
  });
} catch (error) {
  console.error('Failed to restore state:', error);
}

chrome.runtime.onConnect.addListener(function(p) {
  port = p;
  port.onDisconnect.addListener(() => {
    port = null;
  });
  updateTimeLeft();
});

chrome.runtime.onMessage.addListener((msg, sender, sendResponse) => {
  if (msg.action === 'start') {
    const duration = msg.duration;
    
    if (!duration || duration <= 0) {
      sendResponse({error: 'Invalid timer duration'});
      return true;
    }
    
    // Stop any existing timer
    stopCountdown();
    
    timerDuration = duration * 60;
    visualEnabled = msg.visual;
    isRunning = true;
    startTime = Date.now();
    timeLeft = timerDuration;
    lastNotificationCycle = -1;
    
    saveState();
    startCountdown();
    updateTimeLeft();
    
    if (visualEnabled) {
      chrome.notifications.create('eye-reminder-' + Date.now(), {
        type: 'basic',
        iconUrl: chrome.runtime.getURL('img/icon128.png'),
        title: 'Reminder Started',
        message: 'Timer started! You will be reminded in ' + duration + ' minutes.',
        priority: 2,
        requireInteraction: false
      });
    }
    
    sendResponse({started: true});
  } else if (msg.action === 'stop') {
    stopCountdown();
    isRunning = false;
    timeLeft = 0;
    startTime = 0;
    lastNotificationCycle = -1;
    saveState();
    sendTimeUpdate();
    sendResponse({stopped: true});
  } else if (msg.action === 'getStatus') {
    updateTimeLeft();
    sendResponse({timeLeft, isRunning});
  }
  return true;
});