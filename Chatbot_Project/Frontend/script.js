document.addEventListener('DOMContentLoaded', () => {
  const chatbotToggle = document.querySelector('.chat-bot-toggle');
  const chatbotIframe = document.querySelector('.chat-bot');

  chatbotToggle.addEventListener('click', () => {
    chatbotIframe.classList.toggle('hidden');
    if (chatbotIframe.classList.contains('hidden')) {
      chatbotToggle.textContent = 'Open Chat';
    } else {
      chatbotToggle.textContent = 'Close Chat';
    }
  });
});
