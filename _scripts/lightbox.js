/*
  Opens project images in a larger popup dialog when clicked.
*/

{
  const onLoad = () => {
    const dialog = document.querySelector(".lightbox");
    if (!dialog || typeof dialog.showModal !== "function") return;

    const image = dialog.querySelector("[data-lightbox-image]");
    const caption = dialog.querySelector("[data-lightbox-caption]");
    const closeButton = dialog.querySelector("[data-lightbox-close]");

    const closeDialog = () => {
      if (dialog.open) dialog.close();
    };

    // gallery state when dialog open
    let gallery = [];
    let galleryIndex = -1;

    const showGalleryIndex = (index) => {
      if (!gallery || gallery.length === 0) return;
      galleryIndex = (index + gallery.length) % gallery.length;
      const item = gallery[galleryIndex];
      image.src = item.src;
      image.alt = item.alt || item.src;
      caption.textContent = item.caption || "";
    };

    const galleryNext = () => showGalleryIndex(galleryIndex + 1);
    const galleryPrev = () => showGalleryIndex(galleryIndex - 1);

    const openDialog = (trigger) => {
      // prefer explicit dataset, otherwise fall back to contained img src
      let src = trigger.dataset.lightboxSrc?.trim();
      if (!src) {
        const img = trigger.tagName === 'IMG' ? trigger : trigger.querySelector('img');
        src = img?.src;
      }
      if (!src) return;

      image.src = src;
      image.alt = trigger.dataset.lightboxAlt?.trim() || trigger.getAttribute("aria-label") || "Image preview";
      caption.textContent = trigger.dataset.lightboxCaption?.trim() || "";

      // build gallery: prefer grouping by data-lightbox-group, otherwise any triggers on page
      const group = trigger.dataset.lightboxGroup;
      let triggers = [];
      if (group) {
        triggers = Array.from(document.querySelectorAll(`[data-lightbox-group="${group}"]`));
      }
      if (!triggers || triggers.length === 0) {
        triggers = Array.from(document.querySelectorAll('[data-lightbox-src]'));
      }

      gallery = triggers.map(t => ({
        src: t.dataset.lightboxSrc?.trim() || (t.tagName === 'IMG' ? t.src : (t.querySelector('img')?.src || null)),
        alt: t.dataset.lightboxAlt?.trim() || t.getAttribute('aria-label') || '',
        caption: t.dataset.lightboxCaption?.trim() || ''
      })).filter(i => i.src);

      // find index
      galleryIndex = gallery.findIndex(i => i.src === src);
      if (galleryIndex === -1) galleryIndex = 0;

      showGalleryIndex(galleryIndex);

      dialog.showModal();
      // focus close button for accessibility
      closeButton?.focus();
    };

    document.addEventListener("click", (event) => {
      const trigger = event.target.closest("[data-lightbox-src]");
      if (!trigger) return;
      event.preventDefault();
      openDialog(trigger);
    });

    // keyboard: Escape to close and arrow keys to navigate when dialog open
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') return closeDialog();
      if (!dialog.open) return;
      if (e.key === 'ArrowRight') return galleryNext();
      if (e.key === 'ArrowLeft') return galleryPrev();
    });

    closeButton?.addEventListener("click", closeDialog);

    dialog.addEventListener("click", (event) => {
      const rect = dialog.getBoundingClientRect();
      const clickedOutside =
        event.clientX < rect.left ||
        event.clientX > rect.right ||
        event.clientY < rect.top ||
        event.clientY > rect.bottom;
      if (clickedOutside) closeDialog();
    });

    dialog.addEventListener("close", () => {
      image.removeAttribute("src");
      image.alt = "";
      caption.textContent = "";
    });
  };

  window.addEventListener("load", onLoad);
}