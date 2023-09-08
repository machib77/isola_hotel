document.getElementById('facebook-link').addEventListener('click', function () {
  // Check if the user is on a mobile device
  if (
    /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(
      navigator.userAgent
    )
  ) {
    // Try to open the Facebook app using its custom URL scheme
    window.location.href = 'fb://page/289682824559537'; // Replace 'YourPageID' with your Facebook Page ID

    // If the app is not installed, fall back to the web URL
    setTimeout(function () {
      window.location.href = 'https://www.facebook.com/hotel.isola.aiquile'; // Replace 'YourPageURL' with your Facebook Page URL
    }, 500); // Wait for a short period before falling back to the web URL
  } else {
    // If the user is not on a mobile device, open the web URL directly
    window.location.href = 'https://www.facebook.com/hotel.isola.aiquile'; // Replace 'YourPageURL' with your Facebook Page URL
  }
});
