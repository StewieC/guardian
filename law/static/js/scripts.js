document.addEventListener('DOMContentLoaded', function() {
    console.log('Peace and Justice Platform loaded');

    // --- Mobile Navigation Toggle ---
    const hamburger = document.getElementById('hamburger-button');
    const navMenu = document.getElementById('nav-links-menu');

    // Check if the elements exist before adding an event listener
    if (hamburger && navMenu) {
        hamburger.addEventListener('click', function() {
            // Toggle the 'active' class on both the hamburger and the menu
            hamburger.classList.toggle('active');
            navMenu.classList.toggle('active');
        });
    }
});

// --- Modal Functionality (Unchanged) ---
function openModal(content) {
    const modal = document.getElementById('modal');
    const modalBody = document.getElementById('modal-body');
    modalBody.innerHTML = content;
    modal.style.display = 'block';
}

function closeModal() {
    const modal = document.getElementById('modal');
    if (modal) {
        modal.style.display = 'none';
    }
}

// Close modal when clicking outside
window.onclick = function(event) {
    const modal = document.getElementById('modal');
    if (event.target === modal) {
        closeModal();
    }
}