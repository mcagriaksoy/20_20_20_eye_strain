let timer = 20 * 60; // seconds
let intervalId = null;
let countdownId = null;
let visualEnabled = true;
let soundEnabled = false;

function updateRemaining() {
  const min = Math.floor(timer / 60);
  const sec = timer % 60;
  document.getElementById('remaining').textContent = `${min.toString().padStart(2, '0')}:${sec.toString().padStart(2, '0')}`;
}

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

  // Simple timer logic
  function startTimer() {
    const duration = parseInt(document.getElementById('timerInput').value);
    
    // Guard against invalid timer values
    if (!duration || duration <= 0) {
      document.getElementById('status').textContent = 'Please enter a valid timer duration (1 minute or more)';
      document.getElementById('status').style.color = '#e74c3c';
      return;
    }
    
    document.getElementById('status').textContent = 'Reminder started!';
    document.getElementById('status').style.color = '#27ae60';
    timer = duration * 60;
    visualEnabled = document.getElementById('visualNotif').checked;
    soundEnabled = document.getElementById('soundNotif').checked;
    
    updateRemaining();
    
    if (countdownId) clearInterval(countdownId);
    if (intervalId) clearInterval(intervalId);
    
    // Update display every second
    countdownId = setInterval(() => {
      if (timer > 0) {
        timer--;
        updateRemaining();
      }
    }, 1000);
    
    // Show notification every interval
    intervalId = setInterval(() => {
      if (visualEnabled) {
        chrome.notifications.create({
          type: 'basic',
          iconUrl: 'img/icon128.png',
          title: '20-20-20 Eye Strain Reminder',
          message: 'Time to take a 20-second break and look at something 20 feet away!'
        });
      }
      if (soundEnabled) {
        // Create audio each time to avoid issues
        const audio = new Audio('img/notification.mp3');
        audio.play().catch(e => console.log('Audio play failed:', e));
      }
      timer = duration * 60;
      updateRemaining();
    }, duration * 60 * 1000);
  }
  
  document.getElementById('start').addEventListener('click', startTimer);
});