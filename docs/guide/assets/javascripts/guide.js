/* Local full-size links and mobile alternatives; no external dependencies. */
(function () {
  const variants = new Set(["listening-moods.svg", "rediscovery-signals.svg", "musical-connections.svg"]);
  function prepareFigures() {
    document.querySelectorAll("figure.guide-figure").forEach(function (figure) {
      if (figure.dataset.zoomReady) return;
      const image = figure.querySelector("img");
      if (!image) return;
      figure.dataset.zoomReady = "true";
      const full = image.getAttribute("src");
      if (variants.has(full.split("/").pop())) {
        const mobile = image.cloneNode(false);
        mobile.src = full.replace(/\.svg$/, "-mobile.svg");
        mobile.alt = image.alt;
        mobile.classList.add("figure-mobile");
        image.classList.add("figure-desktop");
        figure.classList.add("figure-has-mobile");
        image.after(mobile);
      }
      const link = document.createElement("a");
      link.className = "figure-zoom";
      link.href = full;
      link.target = "_blank";
      link.rel = "noopener";
      link.textContent = "View full-size illustration";
      link.setAttribute("aria-label", "View full-size illustration: " + image.alt + " (opens in a new tab)");
      figure.append(link);
    });
  }
  if (typeof document$ !== "undefined") document$.subscribe(prepareFigures);
  else if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", prepareFigures);
  else prepareFigures();
})();
