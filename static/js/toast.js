let toastTimeout;
let progressInterval;

function showToast(title, message, type = "normal", duration = 3000) {
  const toastComponent = document.getElementById("toast-component");
  const toastTitle = document.getElementById("toast-title");
  const toastMessage = document.getElementById("toast-message");
  const toastIcon = document.getElementById("toast-icon");
  const toastIconContainer = document.getElementById("toast-icon-container");
  const toastProgress = document.getElementById("toast-progress");

  if (!toastComponent) return;

  // Clear any existing timeout
  if (toastTimeout) clearTimeout(toastTimeout);
  if (progressInterval) clearInterval(progressInterval);

  // Remove all type classes first
  toastComponent.classList.remove(
    "border-red-200",
    "bg-red-50",
    "border-green-200",
    "bg-green-50",
    "border-blue-200",
    "bg-blue-50",
    "border-yellow-200",
    "bg-yellow-50",
    "border-gray-200",
    "bg-white"
  );

  toastIconContainer.classList.remove(
    "bg-red-100",
    "text-red-600",
    "bg-green-100",
    "text-green-600",
    "bg-blue-100",
    "text-blue-600",
    "bg-yellow-100",
    "text-yellow-600",
    "bg-gray-100",
    "text-gray-600"
  );

  // Set type styles and icon based on type
  if (type === "success") {
    toastComponent.classList.add("border-green-200", "bg-green-50");
    toastIconContainer.classList.add("bg-green-100", "text-green-600");
    toastIcon.textContent = "✓";
    toastProgress.className =
      "h-full bg-gradient-to-r from-green-500 to-green-400 transition-all duration-300 ease-linear";
  } else if (type === "error") {
    toastComponent.classList.add("border-red-200", "bg-red-50");
    toastIconContainer.classList.add("bg-red-100", "text-red-600");
    toastIcon.textContent = "×";
    toastProgress.className =
      "h-full bg-gradient-to-r from-red-500 to-red-400 transition-all duration-300 ease-linear";
  } else if (type === "warning") {
    toastComponent.classList.add("border-yellow-200", "bg-yellow-50");
    toastIconContainer.classList.add("bg-yellow-100", "text-yellow-600");
    toastIcon.textContent = "!";
    toastProgress.className =
      "h-full bg-gradient-to-r from-yellow-500 to-yellow-400 transition-all duration-300 ease-linear";
  } else if (type === "info") {
    toastComponent.classList.add("border-blue-200", "bg-blue-50");
    toastIconContainer.classList.add("bg-blue-100", "text-blue-600");
    toastIcon.textContent = "i";
    toastProgress.className =
      "h-full bg-gradient-to-r from-blue-500 to-blue-400 transition-all duration-300 ease-linear";
  } else {
    toastComponent.classList.add("border-gray-200", "bg-white");
    toastIconContainer.classList.add("bg-gray-100", "text-gray-600");
    toastIcon.textContent = "ℹ";
    toastProgress.className =
      "h-full bg-gradient-to-r from-[#db1d24] to-[#ff4444] transition-all duration-300 ease-linear";
  }

  toastTitle.textContent = title;
  toastMessage.textContent = message;

  // Show toast with animation
  toastComponent.classList.remove("opacity-0", "translate-y-16");
  toastComponent.classList.add("opacity-100", "translate-y-0");

  // Animate progress bar
  toastProgress.style.width = "100%";
  let progress = 100;
  const progressStep = 100 / (duration / 50); // Update every 50ms

  progressInterval = setInterval(() => {
    progress -= progressStep;
    if (progress <= 0) {
      progress = 0;
      clearInterval(progressInterval);
    }
    toastProgress.style.width = progress + "%";
  }, 50);

  // Hide toast after duration
  toastTimeout = setTimeout(() => {
    hideToast();
  }, duration);
}

function hideToast() {
  const toastComponent = document.getElementById("toast-component");
  if (!toastComponent) return;

  // Clear timeouts and intervals
  if (toastTimeout) clearTimeout(toastTimeout);
  if (progressInterval) clearInterval(progressInterval);

  // Hide toast with animation
  toastComponent.classList.remove("opacity-100", "translate-y-0");
  toastComponent.classList.add("opacity-0", "translate-y-16");
}
