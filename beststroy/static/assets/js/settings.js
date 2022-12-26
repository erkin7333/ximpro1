let isVoiceAssistantOn = localStorage.getItem("isVoiceAssistantOn") === "true" || false;
let isPageFilterOn = localStorage.getItem("filter") === "true" || false;
const voiceToggler = document.querySelector(".settings__voice-helper");
const voiceDecreaseButton = document.querySelector(".settings__font-decrease");
const voiceIncreaseButton = document.querySelector(".settings__font-increase");
const colorChangeButton = document.querySelector(".settings__color-changer");
const minimumFontSize = 7;
const maximumFontSize = 15;

voiceDecreaseButton.addEventListener("click", () => {
  let currentFontSize = window.getComputedStyle(
    document.documentElement
  ).fontSize;
  currentFontSize = parseInt(currentFontSize);
  if (currentFontSize <= minimumFontSize) return;
  document.documentElement.style.fontSize = currentFontSize - 1;
});

voiceIncreaseButton.addEventListener("click", () => {
  let currentFontSize = window.getComputedStyle(
    document.documentElement
  ).fontSize;
  currentFontSize = parseInt(currentFontSize);
  if (currentFontSize >= maximumFontSize) return;
  document.documentElement.style.fontSize = currentFontSize + 1;
});

if (isVoiceAssistantOn) {
  console.log(isVoiceAssistantOn);
  voiceToggler.classList.remove("disabled");
}
if (isPageFilterOn) {
  document.documentElement.classList.add("filter");
}
voiceToggler.addEventListener("click", () => {
  voiceToggler.classList.toggle("disabled");
  localStorage.setItem("isVoiceAssistantOn",!isVoiceAssistantOn);
  isVoiceAssistantOn = !isVoiceAssistantOn;
});

colorChangeButton.addEventListener('click',()=>{
  document.documentElement.classList.toggle("filter");
  localStorage.setItem("filter",!isPageFilterOn);
  isPageFilterOn = !isPageFilterOn;
});

function debounce(callee, timeoutMs) {
  return function perform(...args) {
    let previousCall = this.lastCall;
    this.lastCall = Date.now();
    if (previousCall && this.lastCall - previousCall <= timeoutMs) {
      clearTimeout(this.lastCallTimer);
    }
    this.lastCallTimer = setTimeout(() => callee(...args), timeoutMs);
  };
}

function speak() {
  if (!isVoiceAssistantOn) return;
  const message = new SpeechSynthesisUtterance();
  message.text = document.getSelection().toString();
  const lang = document.location.href.includes("/ru/") ? "ru-RU" : document.location.href.includes("/en/") ? "en-US" : "uz";
  message.lang = lang;
  console.log(message.lang);
  window.speechSynthesis.speak(message);
}

const debouncedHandle = debounce(speak, 1000);

document.addEventListener("selectionchange", debouncedHandle);

// console.log(window.getComputedStyle(document.documentElement).getPropertyValue("--color-blue-6").trim());