// Author: github.com/mcagriaksoy
// 20-20-20 Eye Strain Reminder Chrome Extension

document.addEventListener('DOMContentLoaded', function() {
  // Switch image based on theme
  function setRuleImage() {
    const ruleImg = document.getElementById('ruleImg');
    if (ruleImg) {
      // Try to load the default image first
      ruleImg.src = 'img/rule.jpg';
      ruleImg.onerror = function() {
        // If image fails to load, show a placeholder text
        const placeholder = document.createElement('div');
        placeholder.style.cssText = 'background:#eaf1fb;padding:20px;border-radius:8px;text-align:center;color:#357ae8;font-weight:bold;margin-bottom:10px;';
        placeholder.textContent = '👁️ 20-20-20 Rule Image';
        ruleImg.parentNode.replaceChild(placeholder, ruleImg);
      };
    }
  }
  setRuleImage();

  // Info popup logic
  document.body.addEventListener('click', function(e) {
    if (e.target && e.target.id === 'infoBtn') {
      document.getElementById('infoPopup').style.display = 'block';
    }
    if (e.target && e.target.id === 'closeInfo') {
      document.getElementById('infoPopup').style.display = 'none';
    }
  });

  // Settings panel logic
  const settingsBtn = document.getElementById('settingsBtn');
  const settingsPanel = document.getElementById('settings');
  if (settingsBtn && settingsPanel) {
    settingsBtn.addEventListener('click', function() {
      settingsPanel.style.display = settingsPanel.style.display === 'none' ? 'block' : 'none';
    });
  }

  // Connect to background service worker
  const port = chrome.runtime.connect();
  port.onMessage.addListener((msg) => {
    const { timeLeft, isRunning } = msg;
    const remainingEl = document.getElementById('remaining');
    if (isRunning) {
      const min = Math.floor(timeLeft / 60);
      const sec = timeLeft % 60;
      remainingEl.textContent = `${min.toString().padStart(2, '0')}:${sec.toString().padStart(2, '0')}`;
    } else {
      remainingEl.textContent = 'Not Started';
    }
    // Update button visibility
    const startBtn = document.getElementById('start');
    const stopBtn = document.getElementById('stop');
    if (isRunning) {
      startBtn.style.display = 'none';
      stopBtn.style.display = 'inline-block';
    } else {
      startBtn.style.display = 'inline-block';
      stopBtn.style.display = 'none';
    }
  });

  // Start reminder
  document.getElementById('start').addEventListener('click', () => {
    const duration = parseInt(document.getElementById('timerInput').value);
    if (!duration || duration <= 0) {
      document.getElementById('status').textContent = 'Please enter a valid timer duration (1 minute or more)';
      document.getElementById('status').style.color = '#e74c3c';
      return;
    }
    chrome.runtime.sendMessage({
      action: 'start',
      duration,
      visual: document.getElementById('visualNotif').checked
    }, (response) => {
      if (response && response.error) {
        document.getElementById('status').textContent = response.error;
        document.getElementById('status').style.color = '#e74c3c';
      } else {
        document.getElementById('status').textContent = 'Reminder started!';
        document.getElementById('status').style.color = '#27ae60';
      }
    });
  });

  // Stop reminder
  document.getElementById('stop').addEventListener('click', () => {
    chrome.runtime.sendMessage({ action: 'stop' }, (response) => {
      if (response.stopped) {
        document.getElementById('status').textContent = 'Reminder stopped.';
        document.getElementById('status').style.color = '#e74c3c';
      }
    });
  });
});