// Get the video element
var video = document.querySelector('video');

// Add a click event listener to the video element
video.addEventListener('click', function () {
  if (video.muted) {
    // Unmute the video when clicked if it's currently muted
    video.muted = false;
  } else {
    // Mute the video when clicked if it's currently unmuted
    video.muted = true;
  }
});
