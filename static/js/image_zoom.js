// Get references to the modal and the image inside it
const lightboxModal = document.getElementById('lightbox-modal');
const lightboxImage = document.getElementById('lightbox-image');

// Get all the lightbox trigger elements
const lightboxTriggers = document.querySelectorAll('.lightbox-trigger');

// Add a click event listener to each trigger element
lightboxTriggers.forEach((trigger) => {
  trigger.addEventListener('click', (e) => {
    e.preventDefault(); // Prevent the default link behavior

    // Set the image source in the modal to the clicked image's href
    lightboxImage.src = trigger.getAttribute('href');

    // Display the modal
    lightboxModal.style.display = 'block';
  });
});

// Add a click event listener to the close button
document.querySelector('.close-lightbox').addEventListener('click', () => {
  // Close the modal
  lightboxModal.style.display = 'none';
});

// Add a click event listener to the modal background
lightboxModal.addEventListener('click', (e) => {
  if (e.target === lightboxModal) {
    // Close the modal if the click occurred on the modal background
    lightboxModal.style.display = 'none';
  }
});

// Add a click event listener to the enlarged image
lightboxImage.addEventListener('click', () => {
  // Close the modal
  lightboxModal.style.display = 'none';
});
