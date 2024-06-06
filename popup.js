document.getElementById('summarizeButton').addEventListener('click', () => {
  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    chrome.scripting.executeScript({
      target: { tabId: tabs[0].id },
      function: () => {
        const textContent = document.body.innerText;
        const summary = textContent.split('. ').slice(0, 3).join('. ') + '...';
        return summary;
      }
    }, (results) => {
      document.getElementById('summary').innerText = results[0].result;
    });
  });
});
