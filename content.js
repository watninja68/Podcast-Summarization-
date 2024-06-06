const summarizeContent = (text) => {
  // Simple summary logic (can be replaced with a more advanced algorithm or API call)
  return text.split('. ').slice(0, 3).join('. ') + '...';
};

const getTextContent = () => {
  return document.body.innerText;
};

const showSummary = (summary) => {
  const summaryElement = document.createElement('div');
  summaryElement.style.position = 'fixed';
  summaryElement.style.bottom = '0';
  summaryElement.style.right = '0';
  summaryElement.style.backgroundColor = 'white';
  summaryElement.style.padding = '10px';
  summaryElement.style.border = '1px solid black';
  summaryElement.innerText = summary;
  document.body.appendChild(summaryElement);
};

const textContent = getTextContent();
const summary = summarizeContent(textContent);
showSummary(summary);
