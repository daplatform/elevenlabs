document.addEventListener('DOMContentLoaded', () => {
    // Store the current avatar and video series.
    let currentAvatar = 'santa';  // Default avatar
    let videoSeries = {
        santa: {
            polish: "santa-1.mp4",
            italian: "santa-2.mp4",
            hindi: "santa-3.mp4",
            german: "santa-4.mp4",
            english: "santa-5.mp4"
            // Add more languages for Santa
        },
        swetha: {
            italian: "swetha-1.mp4",
            german: "swetha-2.mp4",
            polish: "swetha-3.mp4",
            hindi: "swetha-4.mp4",
            english: "swetha-5.mp4"
            // Add more languages for Swetha
        }
    };

    // Get the video player elements after DOM is loaded
    const videoPlayer = document.getElementById('videoPlayer');
    const videoSource = document.getElementById('videoSource');

    if (!videoPlayer || !videoSource) {
        console.error("Video player or source elements not found");
        return;
    }

    // Function to switch video based on avatar and language
// Function to switch video based on avatar and language and ensure autoplay
function switchVideo(avatar, language) {
    let currentTime = videoPlayer.currentTime;  // Preserve the current playback time
    let isPlaying = !videoPlayer.paused && !videoPlayer.ended;  // Check if the video is playing

    let newVideo = videoSeries[avatar][language];  // Get the correct video based on avatar and language
    
    // Debugging: Log the avatar, language, and video being switched to
    console.log("Switching to avatar:", avatar);
    console.log("Switching to language:", language);
    console.log("New video source:", newVideo);

    videoSource.src = `/static/videos/${newVideo}`;  // Update the video source
    videoPlayer.load();  // Load the new video
    videoPlayer.currentTime = currentTime;  // Set the video to continue from the same time

    // Play the video immediately after loading
    if (isPlaying) {
        videoPlayer.play();
    }
}

    // Switch avatar when clicked
    document.querySelectorAll('.avatar-icon').forEach(avatar => {
        avatar.addEventListener('click', () => {
            currentAvatar = avatar.getAttribute('data-video');  // Get the avatar from data-video attribute
            switchVideo(currentAvatar, 'english');  // Default to English video for the selected avatar
        });
    });

    // Switch video when language tile is clicked
    document.querySelectorAll('.lang-tile').forEach(tile => {
        tile.addEventListener('click', (e) => {
            let selectedLang = e.target.getAttribute('data-lang');  // Get selected language from data-lang
            switchVideo(currentAvatar, selectedLang);  // Switch video based on current avatar and selected language
        });
    });
});
