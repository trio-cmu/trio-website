// Carousel functionality for project images
document.addEventListener('DOMContentLoaded', function() {
  const carousels = document.querySelectorAll('.carousel');

  carousels.forEach(carousel => {
    const slides = carousel.querySelectorAll('.carousel-slide');
    const prevButton = carousel.querySelector('.carousel-prev');
    const nextButton = carousel.querySelector('.carousel-next');
    const indicators = carousel.querySelectorAll('.carousel-indicator');

    if (slides.length <= 1) return;

    let currentIndex = 0;

    function showSlide(index) {
      // Wrap around
      if (index >= slides.length) {
        currentIndex = 0;
      } else if (index < 0) {
        currentIndex = slides.length - 1;
      } else {
        currentIndex = index;
      }

      // Update slides
      slides.forEach((slide, i) => {
        slide.setAttribute('data-active', i === currentIndex ? 'true' : 'false');
      });

      // Update indicators
      indicators.forEach((indicator, i) => {
        indicator.classList.toggle('active', i === currentIndex);
      });
    }

    function nextSlide() {
      showSlide(currentIndex + 1);
    }

    function prevSlide() {
      showSlide(currentIndex - 1);
    }

    // Add event listeners
    if (nextButton) {
      nextButton.addEventListener('click', nextSlide);
    }

    if (prevButton) {
      prevButton.addEventListener('click', prevSlide);
    }

    indicators.forEach((indicator, index) => {
      indicator.addEventListener('click', () => {
        showSlide(index);
      });
    });

    // Auto-advance slides every ~2s, pause on hover/focus
    let autoInterval = null;
    const AUTOPLAY_MS = 4000;

    function startAutoplay() {
      if (autoInterval) return;
      autoInterval = setInterval(nextSlide, AUTOPLAY_MS);
    }

    function stopAutoplay() {
      if (!autoInterval) return;
      clearInterval(autoInterval);
      autoInterval = null;
    }

    // start autoplay by default
    startAutoplay();

    // pause on mouse over or focus within carousel
    carousel.addEventListener('mouseenter', stopAutoplay);
    carousel.addEventListener('mouseleave', startAutoplay);
    carousel.addEventListener('focusin', stopAutoplay);
    carousel.addEventListener('focusout', startAutoplay);

    // Keyboard navigation
    document.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowRight') nextSlide();
      if (e.key === 'ArrowLeft') prevSlide();
    });
  });
});
