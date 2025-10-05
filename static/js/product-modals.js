// Product Modal Management Functions
let currentProductId = null;
let isEditMode = false;

// Helper function to get CSRF token
function getCsrfToken() {
  const csrfToken = document.querySelector("[name=csrfmiddlewaretoken]");
  return csrfToken ? csrfToken.value : "";
}

function openCreateModal() {
  isEditMode = false;
  currentProductId = null;

  document.getElementById("modalTitle").textContent = "Add New Product";
  document.querySelector(".submit-text").textContent = "Add Product";

  // Reset form
  const form = document.getElementById("productForm");
  form.reset();
  clearErrorMessages();

  showProductModal();
}

function openEditModal(
  id,
  name,
  price,
  description,
  thumbnail,
  category,
  is_featured
) {
  isEditMode = true;
  currentProductId = id;

  document.getElementById("modalTitle").textContent = "Edit Product";
  document.querySelector(".submit-text").textContent = "Update Product";

  // Fill form with product data
  document.getElementById("modalName").value = name;
  document.getElementById("modalPrice").value = price;
  document.getElementById("modalDescription").value = description;
  document.getElementById("modalThumbnail").value = thumbnail || "";
  document.getElementById("modalCategory").value = category;
  document.getElementById("modalIsFeatured").checked = is_featured;

  clearErrorMessages();
  showProductModal();
}

function showProductModal() {
  const modal = document.getElementById("productModal");
  const modalContent = document.getElementById("modalContent");

  modal.classList.remove("hidden");

  // Animate modal in
  setTimeout(() => {
    modalContent.classList.remove("scale-95", "opacity-0");
    modalContent.classList.add("scale-100", "opacity-100");
  }, 10);

  // Prevent background scroll
  document.body.style.overflow = "hidden";
}

function closeProductModal() {
  const modal = document.getElementById("productModal");
  const modalContent = document.getElementById("modalContent");

  // Animate modal out
  modalContent.classList.remove("scale-100", "opacity-100");
  modalContent.classList.add("scale-95", "opacity-0");

  setTimeout(() => {
    modal.classList.add("hidden");
    document.body.style.overflow = "auto";
  }, 300);
}

function clearErrorMessages() {
  const errorElements = document.querySelectorAll(".text-red-500");
  errorElements.forEach((el) => {
    el.classList.add("hidden");
    el.textContent = "";
  });

  // Remove error styling from inputs
  const inputs = document.querySelectorAll(
    "#productForm input, #productForm textarea, #productForm select"
  );
  inputs.forEach((input) => {
    input.classList.remove("border-red-500");
  });
}

function showFieldError(fieldName, message) {
  const errorElement = document.getElementById(fieldName + "Error");
  const inputElement = document.getElementById(
    "modal" + fieldName.charAt(0).toUpperCase() + fieldName.slice(1)
  );

  if (errorElement) {
    errorElement.textContent = message;
    errorElement.classList.remove("hidden");
  }

  if (inputElement) {
    inputElement.classList.add("border-red-500");
  }
}

// Delete Modal Functions
let deleteProductId = null;

function openDeleteModal(id, name) {
  deleteProductId = id;
  document.getElementById("deleteProductName").textContent = name;

  const modal = document.getElementById("deleteModal");
  const modalContent = document.getElementById("deleteModalContent");

  modal.classList.remove("hidden");

  // Animate modal in
  setTimeout(() => {
    modalContent.classList.remove("scale-95", "opacity-0");
    modalContent.classList.add("scale-100", "opacity-100");
  }, 10);

  document.body.style.overflow = "hidden";
}

function closeDeleteModal() {
  const modal = document.getElementById("deleteModal");
  const modalContent = document.getElementById("deleteModalContent");

  // Animate modal out
  modalContent.classList.remove("scale-100", "opacity-100");
  modalContent.classList.add("scale-95", "opacity-0");

  setTimeout(() => {
    modal.classList.add("hidden");
    document.body.style.overflow = "auto";
  }, 300);

  deleteProductId = null;
}

// Initialize modal event listeners when DOM is loaded
document.addEventListener("DOMContentLoaded", function () {
  // Product form submission handler
  const form = document.getElementById("productForm");
  const submitBtn = document.getElementById("submitBtn");
  const submitText = document.querySelector(".submit-text");
  const loadingSpinner = document.querySelector(".loading-spinner");

  if (form) {
    form.addEventListener("submit", async function (e) {
      e.preventDefault();

      clearErrorMessages();

      // Show loading state
      submitBtn.disabled = true;
      submitText.classList.add("hidden");
      loadingSpinner.classList.remove("hidden");

      try {
        const formData = new FormData(form);
        const data = Object.fromEntries(formData.entries());
        data.is_featured = document.getElementById("modalIsFeatured").checked;

        const url = isEditMode
          ? `/product/${currentProductId}/edit-ajax/`
          : "/create-product-ajax/";
        const method = "POST";

        const response = await fetch(url, {
          method: method,
          headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": getCsrfToken(),
          },
          body: JSON.stringify(data),
        });

        const result = await response.json();

        if (result.success) {
          showToast("Success!", result.message, "success");
          closeProductModal();

          // Reload products if function exists
          if (typeof reloadProducts === "function") {
            reloadProducts();
          } else if (window.productManagerInstance) {
            window.productManagerInstance.loadProducts();
          }
        } else {
          if (result.errors) {
            for (const [field, messages] of Object.entries(result.errors)) {
              if (Array.isArray(messages)) {
                showFieldError(field, messages[0]);
              } else {
                showFieldError(field, messages);
              }
            }
          } else {
            showToast("Error!", result.message || "An error occurred", "error");
          }
        }
      } catch (error) {
        console.error("Error submitting form:", error);
        showToast(
          "Network Error!",
          "Please check your connection and try again.",
          "error"
        );
      } finally {
        // Reset loading state
        submitBtn.disabled = false;
        submitText.classList.remove("hidden");
        loadingSpinner.classList.add("hidden");
      }
    });
  }

  // Delete confirmation handler
  const confirmDeleteBtn = document.getElementById("confirmDeleteBtn");
  const deleteText = document.querySelector(".delete-text");
  const deleteLoadingSpinner = document.querySelector(
    ".delete-loading-spinner"
  );

  if (confirmDeleteBtn) {
    confirmDeleteBtn.addEventListener("click", async function () {
      if (!deleteProductId) return;

      // Show loading state
      confirmDeleteBtn.disabled = true;
      deleteText.classList.add("hidden");
      deleteLoadingSpinner.classList.remove("hidden");

      try {
        const response = await fetch(
          `/product/${deleteProductId}/delete-ajax`,
          {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
              "X-CSRFToken": getCsrfToken(),
            },
          }
        );

        const result = await response.json();

        if (result.success) {
          showToast("Success!", result.message, "success");
          closeDeleteModal();

          // Reload products if function exists
          if (typeof reloadProducts === "function") {
            reloadProducts();
          } else if (window.productManagerInstance) {
            window.productManagerInstance.loadProducts();
          }
        } else {
          showToast(
            "Error!",
            result.message || "Failed to delete product",
            "error"
          );
        }
      } catch (error) {
        console.error("Error deleting product:", error);
        showToast(
          "Network Error!",
          "Please check your connection and try again.",
          "error"
        );
      } finally {
        // Reset loading state
        confirmDeleteBtn.disabled = false;
        deleteText.classList.remove("hidden");
        deleteLoadingSpinner.classList.add("hidden");
      }
    });
  }

  // Close modals when clicking outside
  const productModal = document.getElementById("productModal");
  if (productModal) {
    productModal.addEventListener("click", function (e) {
      if (e.target === this) {
        closeProductModal();
      }
    });
  }

  const deleteModal = document.getElementById("deleteModal");
  if (deleteModal) {
    deleteModal.addEventListener("click", function (e) {
      if (e.target === this) {
        closeDeleteModal();
      }
    });
  }

  // Close modals with Escape key
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") {
      closeProductModal();
      closeDeleteModal();
    }
  });
});
