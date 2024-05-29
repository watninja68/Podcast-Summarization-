chrome.runtime.onInstalled.addListener(() => {
  console.log('Extension installed');
});

chrome.action.onClicked.addListener((tab) => {
  chrome.scripting.executeScript({
    target: { tabId: tab.id },
    files: ['content.js']
  });
});

const addEventToGoogleCalendar = (eventDetails) => {
  chrome.identity.getAuthToken({ interactive: true }, (token) => {
    fetch('https://www.googleapis.com/calendar/v3/calendars/primary/events', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(eventDetails)
    }).then(response => response.json())
      .then(data => console.log(data))
      .catch(error => console.error('Error:', error));
  });
};

// Example usage
const eventDetails = {
  summary: 'New Event',
  start: { dateTime: '2024-05-27T09:00:00-07:00' },
  end: { dateTime: '2024-05-27T10:00:00-07:00' }
};

addEventToGoogleCalendar(eventDetails);
