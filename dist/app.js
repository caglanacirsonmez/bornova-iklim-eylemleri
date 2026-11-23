(() => {
  "use strict";

  const contentByLanguage = {
    tr: window.COP31_CONTENT || [],
    en: window.COP31_CONTENT_EN || []
  };

  const COPY = {
    tr: {
      pageTitle: "Bornova Belediyesi Yerel İklim Eylemleri",
      metaDescription: "Bornova Belediyesi'nin iklim, enerji, dayanıklılık, sosyal kalkınma ve sıfır atık çalışmalarını keşfedin.",
      kicker: "COP31 · BORNOVA’DAN YEREL AKSİYONLAR",
      homeTitle: "İklim için<br><em>birlikte harekete.</em>",
      intro: "Toprağı koruyan, temiz enerji üreten, afetlere hazırlanan ve yaşamı güçlendiren Bornova’yı keşfedin.",
      reportBiodiversity: "Bornova Biyoçeşitlilik Envanteri",
      reportSecap: "Bornova SECAP (İngilizce)",
      reportSustainability: "Bornova Sürdürülebilirlik Raporu 2025 (İngilizce)",
      reportOpen: "PDF’yi aç",
      reportBiodiversityLabel: "Bornova Biyoçeşitlilik Envanteri PDF raporunu aç",
      reportSecapLabel: "Bornova SECAP İngilizce PDF raporunu aç",
      reportSustainabilityLabel: "Bornova Sürdürülebilirlik Raporu 2025 İngilizce PDF raporunu aç",
      footerPrompt: "Bir başlığa dokunarak keşfedin",
      footerSummary: (themes, initiatives) => `${themes} başlık · ${initiatives} çalışma`,
      categoryNavigation: "İklim eylemi başlıkları",
      initiativeCount: (count) => `${count} çalışma`,
      exploreCategory: (title, count) => `${title}: ${count} çalışmayı keşfet`,
      home: "Ana sayfa",
      brandLabel: "Bornova Belediyesi ve COP31 Türkiye",
      municipalityLogo: "Bornova Belediyesi",
      categoryArea: "İKLİM EYLEM ALANI",
      topicNavigation: "Alt başlıklar",
      photoGallery: (title) => `${title} fotoğrafları`,
      placeholder: "Fotoğraf yakında",
      previousPhoto: "Önceki fotoğraf",
      nextPhoto: "Sonraki fotoğraf",
      photoAlt: (title, index, total) => `${title} çalışmasından fotoğraf ${index} / ${total}`,
      tapToEnlarge: "büyütmek için dokunun",
      keyFigures: "Öne çıkan sayılar",
      previousInitiative: "Önceki çalışma",
      nextInitiative: "Sonraki çalışma",
      previous: "Önceki",
      next: "Sonraki",
      dialogKicker: "FOTOĞRAF GALERİSİ",
      closeLargePhoto: "Büyük fotoğrafı kapat",
      shrinkPhoto: "Fotoğrafı küçült",
      previousLargePhoto: "Önceki büyük fotoğraf",
      nextLargePhoto: "Sonraki büyük fotoğraf",
      dialogHint: "Küçültmek için fotoğrafa yeniden dokunun.",
      fullscreen: "Tam ekran",
      exitFullscreen: "Tam ekrandan çık",
      openFullscreen: "Tam ekranı aç",
      fullscreenError: "Tam ekran modu açılamadı.",
      languageButton: "EN",
      languageButtonLang: "en",
      languageLabel: "Switch to English",
      feedbackButton: "Görüşünü paylaş",
      feedbackOpenLabel: "Anonim görüş paylaş",
      feedbackKicker: "ANONİM GERİ BİLDİRİM",
      feedbackTitle: "Görüşünüz bizim için değerli",
      feedbackDescription: "Bornova’nın iklim eylemleriyle ilgili görüş ve önerilerinizi anonim olarak paylaşabilirsiniz.",
      feedbackPrivacy: "Ad, telefon veya e-posta bilgisi istemiyoruz.",
      feedbackFieldLabel: "Görüş ve öneriniz",
      feedbackPlaceholder: "Görüşünüzü buraya yazın…",
      feedbackCancel: "Vazgeç",
      feedbackSubmit: "Anonim gönder",
      feedbackCloseLabel: "Geri bildirim penceresini kapat",
      feedbackSending: "Gönderiliyor…",
      feedbackValidation: "Lütfen en az 3 karakter yazın.",
      feedbackError: "Görüşünüz şu anda kaydedilemedi. Lütfen yeniden deneyin.",
      feedbackSuccessKicker: "TEŞEKKÜR EDERİZ",
      feedbackSuccessTitle: "Görüşünüz kaydedildi",
      feedbackSuccessText: "Katkınız, Bornova’nın iklim çalışmalarını geliştirmemize yardımcı olacak.",
      feedbackSuccessClose: "Kapat",
      municipalityWebsite: "Bornova Belediyesi web sitesini aç"
    },
    en: {
      pageTitle: "Bornova Municipality Local Climate Action",
      metaDescription: "Explore Bornova Municipality’s work on climate, energy, resilience, social development and zero waste.",
      kicker: "COP31 · LOCAL ACTIONS FROM BORNOVA",
      homeTitle: "For the climate,<br><em>let’s act together.</em>",
      intro: "Explore Bornova’s actions to protect the soil, generate clean energy, prepare for disasters and strengthen everyday life.",
      reportBiodiversity: "Bornova Biodiversity Inventory (Turkish)",
      reportSecap: "Bornova SECAP 2025 (English)",
      reportSustainability: "Bornova Sustainability Report 2025",
      reportOpen: "Open PDF",
      reportBiodiversityLabel: "Open the Bornova Biodiversity Inventory PDF report",
      reportSecapLabel: "Open the Bornova SECAP 2025 PDF report",
      reportSustainabilityLabel: "Open the Bornova Sustainability Report 2025 PDF",
      footerPrompt: "Tap a theme to explore",
      footerSummary: (themes, initiatives) => `${themes} themes · ${initiatives} initiatives`,
      categoryNavigation: "Climate action themes",
      initiativeCount: (count) => `${count} ${count === 1 ? "initiative" : "initiatives"}`,
      exploreCategory: (title, count) => `${title}: explore ${count} ${count === 1 ? "initiative" : "initiatives"}`,
      home: "Home",
      brandLabel: "Bornova Municipality and COP31 Türkiye",
      municipalityLogo: "Bornova Municipality",
      categoryArea: "CLIMATE ACTION AREA",
      topicNavigation: "Topics",
      photoGallery: (title) => `${title} photo gallery`,
      placeholder: "Photo coming soon",
      previousPhoto: "Previous photo",
      nextPhoto: "Next photo",
      photoAlt: (title, index, total) => `${title}, photo ${index} of ${total}`,
      tapToEnlarge: "tap to enlarge",
      keyFigures: "Key figures",
      previousInitiative: "Previous initiative",
      nextInitiative: "Next initiative",
      previous: "Previous",
      next: "Next",
      dialogKicker: "PHOTO GALLERY",
      closeLargePhoto: "Close enlarged photo",
      shrinkPhoto: "Minimise photo",
      previousLargePhoto: "Previous enlarged photo",
      nextLargePhoto: "Next enlarged photo",
      dialogHint: "Tap the photo again to minimise it.",
      fullscreen: "Full screen",
      exitFullscreen: "Exit full screen",
      openFullscreen: "Open full screen",
      fullscreenError: "Full-screen mode could not be opened.",
      languageButton: "TR",
      languageButtonLang: "tr",
      languageLabel: "Türkçeye geç",
      feedbackButton: "Share feedback",
      feedbackOpenLabel: "Share anonymous feedback",
      feedbackKicker: "ANONYMOUS FEEDBACK",
      feedbackTitle: "Your feedback matters",
      feedbackDescription: "You can anonymously share your views and suggestions about Bornova’s climate action.",
      feedbackPrivacy: "We do not ask for your name, phone number or email address.",
      feedbackFieldLabel: "Your feedback and suggestions",
      feedbackPlaceholder: "Write your feedback here…",
      feedbackCancel: "Cancel",
      feedbackSubmit: "Send anonymously",
      feedbackCloseLabel: "Close feedback dialog",
      feedbackSending: "Sending…",
      feedbackValidation: "Please enter at least 3 characters.",
      feedbackError: "Your feedback could not be saved right now. Please try again.",
      feedbackSuccessKicker: "THANK YOU",
      feedbackSuccessTitle: "Your feedback has been saved",
      feedbackSuccessText: "Your contribution will help us improve Bornova’s climate action.",
      feedbackSuccessClose: "Close",
      municipalityWebsite: "Open the Bornova Municipality website"
    }
  };

  const requestedLanguage = new URLSearchParams(location.search).get("lang") === "en" ? "en" : "tr";
  let language = requestedLanguage === "en" && contentByLanguage.en.length ? "en" : "tr";
  let categories = contentByLanguage[language];
  const iconPaths = {
    sprout: '<svg viewBox="0 0 32 32" aria-hidden="true"><path d="M16 27V15m0 3c-5 0-9-3-9-8 5 0 9 2 9 8Zm0-3c0-5 4-9 10-9 0 6-4 9-10 9ZM9 27h14"/></svg>',
    energy: '<svg viewBox="0 0 32 32" aria-hidden="true"><path d="m18 3-9 15h7l-2 11 9-15h-7l2-11Z"/></svg>',
    resilience: '<svg viewBox="0 0 32 32" aria-hidden="true"><path d="M16 3 27 7v7c0 7-4.6 12-11 15C9.6 26 5 21 5 14V7l11-4Z"/><path d="m11 16 3 3 7-7"/></svg>',
    community: '<svg viewBox="0 0 32 32" aria-hidden="true"><path d="M11 15a5 5 0 1 0 0-10 5 5 0 0 0 0 10Zm10-2a4 4 0 1 0 0-8"/><path d="M2 27c.8-6 4-9 9-9s8.2 3 9 9m0-10c5 0 8 3 9 8"/></svg>',
    recycle: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 19H4.815a1.83 1.83 0 0 1-1.57-.881 1.785 1.785 0 0 1-.004-1.784L7.196 9.5"/><path d="M11 19h8.203a1.83 1.83 0 0 0 1.556-.89 1.784 1.784 0 0 0 0-1.775l-1.226-2.12"/><path d="m14 16-3 3 3 3"/><path d="M8.293 13.596 7.196 9.5 3.1 10.598"/><path d="m9.344 5.811 1.093-1.892A1.83 1.83 0 0 1 11.985 3a1.784 1.784 0 0 1 1.546.888l3.943 6.843"/><path d="m13.378 9.633 4.096 1.098 1.097-4.096"/></svg>'
  };

  const elements = {
    homeView: document.querySelector("#home-view"),
    detailView: document.querySelector("#detail-view"),
    metaDescription: document.querySelector('meta[name="description"]'),
    homeKicker: document.querySelector("#home-kicker"),
    homeTitle: document.querySelector("#home-title"),
    introCopy: document.querySelector("#intro-copy"),
    reportBiodiversityLink: document.querySelector("#report-biodiversity-link"),
    reportBiodiversityTitle: document.querySelector("#report-biodiversity-title"),
    reportSecapLink: document.querySelector("#report-secap-link"),
    reportSecapTitle: document.querySelector("#report-secap-title"),
    reportSustainabilityLink: document.querySelector("#report-sustainability-link"),
    reportSustainabilityTitle: document.querySelector("#report-sustainability-title"),
    reportActions: document.querySelectorAll("[data-report-action]"),
    footerPrompt: document.querySelector("#footer-prompt"),
    footerSummary: document.querySelector("#footer-summary"),
    categoryGrid: document.querySelector("#category-grid"),
    homeButton: document.querySelector("#home-button"),
    homeButtonLabel: document.querySelector("#home-button span"),
    brandLockups: document.querySelectorAll(".brand-lockup, .detail-brand"),
    languageButtons: document.querySelectorAll("[data-language-toggle]"),
    categoryNumber: document.querySelector("#category-number"),
    categoryHeadingLabel: document.querySelector("#category-heading-label"),
    categoryTitle: document.querySelector("#category-title"),
    topicList: document.querySelector("#topic-list"),
    storyGallery: document.querySelector("#story-gallery"),
    galleryTrack: document.querySelector("#gallery-track"),
    galleryPrevious: document.querySelector("#gallery-previous"),
    galleryNext: document.querySelector("#gallery-next"),
    galleryCounter: document.querySelector("#gallery-counter"),
    imagePlaceholder: document.querySelector("#image-placeholder"),
    imagePlaceholderLabel: document.querySelector("#image-placeholder-label"),
    storyIndex: document.querySelector("#story-index"),
    storyTitle: document.querySelector("#story-title"),
    storyLead: document.querySelector("#story-lead"),
    storyText: document.querySelector("#story-text"),
    storyLink: document.querySelector("#story-link"),
    storyLinkLabel: document.querySelector("#story-link-label"),
    metricGrid: document.querySelector("#metric-grid"),
    municipalityLinks: document.querySelectorAll(".municipality-link"),
    photoDialog: document.querySelector("#photo-dialog"),
    photoDialogKicker: document.querySelector("#photo-dialog-kicker"),
    photoDialogTitle: document.querySelector("#photo-dialog-title"),
    photoDialogCounter: document.querySelector("#photo-dialog-counter"),
    photoDialogBackdrop: document.querySelector("#photo-dialog-backdrop"),
    photoDialogImage: document.querySelector("#photo-dialog-image"),
    photoDialogImageButton: document.querySelector("#photo-dialog-image-button"),
    photoDialogClose: document.querySelector("#photo-dialog-close"),
    photoDialogPrevious: document.querySelector("#photo-dialog-previous"),
    photoDialogNext: document.querySelector("#photo-dialog-next"),
    photoDialogHint: document.querySelector("#photo-dialog-hint"),
    feedbackOpenButtons: document.querySelectorAll("[data-feedback-open]"),
    feedbackDialog: document.querySelector("#feedback-dialog"),
    feedbackForm: document.querySelector("#feedback-form"),
    feedbackClose: document.querySelector("#feedback-close"),
    feedbackEntry: document.querySelector("#feedback-entry"),
    feedbackKicker: document.querySelector("#feedback-kicker"),
    feedbackTitle: document.querySelector("#feedback-title"),
    feedbackDescription: document.querySelector("#feedback-description"),
    feedbackPrivacy: document.querySelector("#feedback-privacy span"),
    feedbackLabel: document.querySelector("#feedback-label"),
    feedbackMessage: document.querySelector("#feedback-message"),
    feedbackStatus: document.querySelector("#feedback-status"),
    feedbackCounter: document.querySelector("#feedback-counter"),
    feedbackCancel: document.querySelector("#feedback-cancel"),
    feedbackSubmit: document.querySelector("#feedback-submit"),
    feedbackSuccess: document.querySelector("#feedback-success"),
    feedbackSuccessKicker: document.querySelector("#feedback-success-kicker"),
    feedbackSuccessTitle: document.querySelector("#feedback-success-title"),
    feedbackSuccessText: document.querySelector("#feedback-success-text"),
    feedbackSuccessClose: document.querySelector("#feedback-success-close")
  };

  let categoryIndex = 0;
  let itemIndex = 0;
  let galleryImages = [];
  let galleryLeadIndex = 0;
  let dialogIndex = 0;
  let lastHomeCard = null;
  let lastGalleryTrigger = null;
  let galleryScrollFrame = null;
  let lastFeedbackTrigger = null;
  let feedbackSubmissionId = null;
  let feedbackSubmitting = false;
  let feedbackStatusState = "idle";
  let feedbackSuccessTimer = null;

  const FEEDBACK_ENDPOINT = "https://bornova-iklim-geri-bildirim.caglanacir.chatgpt.site/api/feedback";

  const getCopy = () => COPY[language];
  const formatIndex = (index) => String(index + 1).padStart(2, "0");

  function getItemHash(category, item) {
    return `#/${encodeURIComponent(category.id)}/${encodeURIComponent(item.id || "1")}`;
  }

  function decodeRoutePart(value) {
    try {
      return decodeURIComponent(value);
    } catch {
      return value;
    }
  }

  function getSafeHttpUrl(value) {
    if (!value) return null;
    try {
      const url = new URL(String(value), location.href);
      return url.protocol === "http:" || url.protocol === "https:" ? url.href : null;
    } catch {
      return null;
    }
  }

  function applyStaticCopy() {
    const copy = getCopy();
    const totalInitiatives = categories.reduce((total, category) => total + category.items.length, 0);

    document.documentElement.lang = language;
    if (elements.metaDescription) elements.metaDescription.content = copy.metaDescription;

    const kickerDot = document.createElement("span");
    elements.homeKicker.replaceChildren(kickerDot, document.createTextNode(` ${copy.kicker}`));
    elements.homeTitle.innerHTML = copy.homeTitle;
    elements.introCopy.textContent = copy.intro;
    elements.reportBiodiversityTitle.textContent = copy.reportBiodiversity;
    elements.reportSecapTitle.textContent = copy.reportSecap;
    elements.reportSustainabilityTitle.textContent = copy.reportSustainability;
    elements.reportBiodiversityLink.setAttribute("aria-label", copy.reportBiodiversityLabel);
    elements.reportSecapLink.setAttribute("aria-label", copy.reportSecapLabel);
    elements.reportSustainabilityLink.setAttribute("aria-label", copy.reportSustainabilityLabel);
    elements.reportActions.forEach((action) => { action.textContent = copy.reportOpen; });
    elements.footerPrompt.textContent = copy.footerPrompt;
    elements.footerSummary.textContent = copy.footerSummary(categories.length, totalInitiatives);
    elements.categoryGrid.setAttribute("aria-label", copy.categoryNavigation);
    elements.homeButtonLabel.textContent = copy.home;
    elements.categoryHeadingLabel.textContent = copy.categoryArea;
    elements.topicList.setAttribute("aria-label", copy.topicNavigation);
    elements.imagePlaceholderLabel.textContent = copy.placeholder;
    elements.galleryPrevious.setAttribute("aria-label", copy.previousPhoto);
    elements.galleryNext.setAttribute("aria-label", copy.nextPhoto);
    elements.metricGrid.setAttribute("aria-label", copy.keyFigures);
    elements.photoDialogKicker.textContent = copy.dialogKicker;
    elements.photoDialogClose.setAttribute("aria-label", copy.closeLargePhoto);
    elements.photoDialogImageButton.setAttribute("aria-label", copy.shrinkPhoto);
    elements.photoDialogPrevious.setAttribute("aria-label", copy.previousLargePhoto);
    elements.photoDialogNext.setAttribute("aria-label", copy.nextLargePhoto);
    elements.photoDialogHint.textContent = copy.dialogHint;

    elements.brandLockups.forEach((lockup) => {
      lockup.setAttribute("aria-label", copy.brandLabel);
      const images = lockup.querySelectorAll("img");
      if (images[0]) images[0].alt = copy.municipalityLogo;
    });

    elements.languageButtons.forEach((button) => {
      const label = button.querySelector("span");
      if (label) label.textContent = copy.languageButton;
      button.setAttribute("aria-label", copy.languageLabel);
      button.setAttribute("title", copy.languageLabel);
      button.setAttribute("lang", copy.languageButtonLang);
    });

    elements.municipalityLinks.forEach((link) => {
      link.setAttribute("aria-label", copy.municipalityWebsite);
      link.setAttribute("title", copy.municipalityWebsite);
    });

    elements.feedbackOpenButtons.forEach((button) => {
      const label = button.querySelector("span");
      if (label) label.textContent = copy.feedbackButton;
      button.setAttribute("aria-label", copy.feedbackOpenLabel);
      button.setAttribute("title", copy.feedbackOpenLabel);
    });
    elements.feedbackClose.setAttribute("aria-label", copy.feedbackCloseLabel);
    elements.feedbackKicker.textContent = copy.feedbackKicker;
    elements.feedbackTitle.textContent = copy.feedbackTitle;
    elements.feedbackDescription.textContent = copy.feedbackDescription;
    elements.feedbackPrivacy.textContent = copy.feedbackPrivacy;
    elements.feedbackLabel.textContent = copy.feedbackFieldLabel;
    elements.feedbackMessage.placeholder = copy.feedbackPlaceholder;
    elements.feedbackCancel.textContent = copy.feedbackCancel;
    elements.feedbackSubmit.textContent = feedbackSubmitting ? copy.feedbackSending : copy.feedbackSubmit;
    elements.feedbackSuccessKicker.textContent = copy.feedbackSuccessKicker;
    elements.feedbackSuccessTitle.textContent = copy.feedbackSuccessTitle;
    elements.feedbackSuccessText.textContent = copy.feedbackSuccessText;
    elements.feedbackSuccessClose.textContent = copy.feedbackSuccessClose;
    updateFeedbackStatus();

    updateFullscreenButtons();
  }

  function updateFeedbackCounter() {
    elements.feedbackCounter.textContent = `${elements.feedbackMessage.value.length} / 1000`;
  }

  function updateFeedbackStatus() {
    const copy = getCopy();
    const statusCopy = {
      idle: "",
      validation: copy.feedbackValidation,
      sending: copy.feedbackSending,
      error: copy.feedbackError
    };
    elements.feedbackStatus.textContent = statusCopy[feedbackStatusState] || "";
  }

  function setFeedbackStatus(nextStatus) {
    feedbackStatusState = nextStatus;
    updateFeedbackStatus();
  }

  function setFeedbackControlsLocked(locked) {
    feedbackSubmitting = locked;
    elements.feedbackForm.setAttribute("aria-busy", String(locked));
    elements.feedbackMessage.readOnly = locked;
    elements.feedbackCancel.disabled = locked;
    elements.feedbackSubmit.disabled = locked;
    elements.feedbackClose.disabled = locked;
    elements.feedbackSubmit.textContent = locked ? getCopy().feedbackSending : getCopy().feedbackSubmit;
  }

  function clearFeedbackSuccessTimer() {
    if (!feedbackSuccessTimer) return;
    window.clearTimeout(feedbackSuccessTimer);
    feedbackSuccessTimer = null;
  }

  function resetFeedbackDialog() {
    clearFeedbackSuccessTimer();
    feedbackSubmissionId = null;
    setFeedbackControlsLocked(false);
    setFeedbackStatus("idle");
    elements.feedbackMessage.value = "";
    elements.feedbackMessage.removeAttribute("aria-invalid");
    elements.feedbackEntry.hidden = false;
    elements.feedbackSuccess.hidden = true;
    updateFeedbackCounter();
  }

  function openFeedbackDialog(trigger) {
    if (elements.feedbackDialog.open) return;
    resetFeedbackDialog();
    lastFeedbackTrigger = trigger;
    elements.feedbackDialog.showModal();
    elements.feedbackMessage.focus({ preventScroll: true });
  }

  function closeFeedbackDialog() {
    if (feedbackSubmitting || !elements.feedbackDialog.open) return;
    elements.feedbackDialog.close();
  }

  function generateSubmissionId() {
    if (window.crypto?.randomUUID) return window.crypto.randomUUID();

    const bytes = new Uint8Array(16);
    window.crypto.getRandomValues(bytes);
    bytes[6] = (bytes[6] & 0x0f) | 0x40;
    bytes[8] = (bytes[8] & 0x3f) | 0x80;
    const hex = Array.from(bytes, (byte) => byte.toString(16).padStart(2, "0"));
    return `${hex.slice(0, 4).join("")}-${hex.slice(4, 6).join("")}-${hex.slice(6, 8).join("")}-${hex.slice(8, 10).join("")}-${hex.slice(10).join("")}`;
  }

  async function submitFeedback() {
    const message = elements.feedbackMessage.value.trim();
    if (message.length < 3 || message.length > 1000) {
      elements.feedbackMessage.setAttribute("aria-invalid", "true");
      setFeedbackStatus("validation");
      elements.feedbackMessage.focus({ preventScroll: true });
      return;
    }

    elements.feedbackMessage.removeAttribute("aria-invalid");
    feedbackSubmissionId ||= generateSubmissionId();
    setFeedbackControlsLocked(true);
    setFeedbackStatus("sending");

    try {
      const response = await fetch(FEEDBACK_ENDPOINT, {
        method: "POST",
        mode: "cors",
        credentials: "omit",
        cache: "no-store",
        referrerPolicy: "no-referrer",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          submissionId: feedbackSubmissionId,
          message,
          language,
          pagePath: location.hash || null
        })
      });

      if (!response.ok) throw new Error("Feedback request failed");

      feedbackSubmissionId = null;
      setFeedbackControlsLocked(false);
      setFeedbackStatus("idle");
      elements.feedbackMessage.value = "";
      updateFeedbackCounter();
      elements.feedbackEntry.hidden = true;
      elements.feedbackSuccess.hidden = false;
      elements.feedbackSuccessClose.focus({ preventScroll: true });
      feedbackSuccessTimer = window.setTimeout(closeFeedbackDialog, 5000);
    } catch {
      setFeedbackControlsLocked(false);
      setFeedbackStatus("error");
      elements.feedbackMessage.focus({ preventScroll: true });
    }
  }

  function changeLanguage(nextLanguage) {
    if (!contentByLanguage[nextLanguage]?.length || nextLanguage === language) return;

    const wasShowingDetail = !elements.detailView.hidden;
    const activeCategoryId = categories[categoryIndex]?.id;
    const activeItemId = categories[categoryIndex]?.items[itemIndex]?.id;

    closePhotoDialog(false);
    language = nextLanguage;
    categories = contentByLanguage[language];
    lastHomeCard = null;
    applyStaticCopy();
    renderHome();

    const matchingCategoryIndex = categories.findIndex((category) => category.id === activeCategoryId);
    const matchingCategory = categories[matchingCategoryIndex];
    const matchingItemIndex = matchingCategory
      ? matchingCategory.items.findIndex((item) => item.id === activeItemId)
      : -1;

    const url = new URL(location.href);
    if (language === "en") url.searchParams.set("lang", "en");
    else url.searchParams.delete("lang");

    if (wasShowingDetail && matchingCategory) {
      categoryIndex = matchingCategoryIndex;
      itemIndex = matchingItemIndex >= 0 ? matchingItemIndex : 0;
      url.hash = getItemHash(matchingCategory, matchingCategory.items[itemIndex]);
    } else {
      categoryIndex = 0;
      itemIndex = 0;
      url.hash = "";
    }

    history.replaceState({ categoryIndex, itemIndex, language }, "", `${url.pathname}${url.search}${url.hash}`);
    syncFromLocation();

    requestAnimationFrame(() => {
      const button = Array.from(elements.languageButtons).find((candidate) => candidate.offsetParent !== null);
      button?.focus();
    });
  }

  function renderHome() {
    const copy = getCopy();
    const fragment = document.createDocumentFragment();

    categories.forEach((category, index) => {
      const button = document.createElement("button");
      button.type = "button";
      button.className = "category-card";
      button.style.setProperty("--accent", category.accent);
      button.style.setProperty("--accent-soft", category.accentSoft || category.accent);
      button.style.setProperty("--accent-ink", category.accentInk || "#062D3C");
      button.style.setProperty("--image", `url("${category.homeImage}")`);
      button.style.setProperty("--image-position", category.homePosition || "center");
      button.setAttribute("aria-label", copy.exploreCategory(category.title, category.items.length));

      const inner = document.createElement("span");
      inner.className = "category-card-inner";

      const top = document.createElement("span");
      top.className = "category-card-top";
      const number = document.createElement("span");
      number.className = "category-card-number";
      number.textContent = formatIndex(index);
      const icon = document.createElement("span");
      icon.className = "category-card-icon";
      icon.innerHTML = iconPaths[category.icon] || "";
      top.append(number, icon);

      const bottomWrap = document.createElement("span");
      const title = document.createElement("h2");
      title.textContent = category.title;
      const bottom = document.createElement("span");
      bottom.className = "category-card-bottom";
      const count = document.createElement("span");
      count.textContent = copy.initiativeCount(category.items.length);
      const arrow = document.createElement("span");
      arrow.className = "category-card-arrow";
      arrow.setAttribute("aria-hidden", "true");
      arrow.textContent = "↗";
      bottom.append(count, arrow);
      bottomWrap.append(title, bottom);

      inner.append(top, bottomWrap);
      button.append(inner);
      button.addEventListener("click", () => {
        lastHomeCard = button;
        showCategory(index, 0, true);
      });
      fragment.append(button);
    });

    elements.categoryGrid.replaceChildren(fragment);
  }

  function renderTopicList(category) {
    const fragment = document.createDocumentFragment();

    category.items.forEach((item, index) => {
      const button = document.createElement("button");
      button.type = "button";
      button.className = "topic-button";
      button.dataset.topicIndex = String(index);
      button.setAttribute("aria-pressed", String(index === itemIndex));
      if (index === itemIndex) button.classList.add("active");

      const number = document.createElement("span");
      number.textContent = formatIndex(index);
      const title = document.createElement("strong");
      title.textContent = item.title;
      const arrow = document.createElement("span");
      arrow.innerHTML = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="m9 18 6-6-6-6"/></svg>';
      button.append(number, title, arrow);
      button.addEventListener("click", () => selectItem(index, true));
      fragment.append(button);
    });

    elements.topicList.replaceChildren(fragment);
  }

  function getGalleryImages(category, item) {
    const galleryKeys = [
      ...(Array.isArray(item.galleryKeys) ? item.galleryKeys : []),
      item.galleryKey,
      item.id
    ].filter(Boolean);
    const keyedManifest = window.COP31_GALLERY_BY_KEY || {};
    const keyedImages = galleryKeys.flatMap((key) => {
      const entry = keyedManifest[key] || keyedManifest[category.id]?.[key];
      return Array.isArray(entry) ? entry : [];
    });
    const uniqueKeyedImages = [...new Set(keyedImages.filter((source) => typeof source === "string" && source))];
    if (uniqueKeyedImages.length) return uniqueKeyedImages;

    if (!item.id) {
      const manifestImages = window.COP31_GALLERY?.[category.id]?.[itemIndex] || [];
      if (manifestImages.length) return manifestImages;
    }
    return item.image ? [item.image] : [];
  }

  function galleryAltText(item, index) {
    return getCopy().photoAlt(item.title, index + 1, galleryImages.length);
  }

  function getGallerySlides() {
    return Array.from(elements.galleryTrack.querySelectorAll(".gallery-slide"));
  }

  function getVisibleGalleryRange() {
    const slides = getGallerySlides();
    if (!slides.length) return { first: 0, last: 0, count: 0 };

    const viewStart = elements.galleryTrack.scrollLeft;
    const viewEnd = viewStart + elements.galleryTrack.clientWidth;
    const visible = [];
    slides.forEach((slide, index) => {
      const left = slide.offsetLeft;
      const right = left + slide.offsetWidth;
      const overlap = Math.max(0, Math.min(right, viewEnd) - Math.max(left, viewStart));
      const threshold = Math.min(slide.offsetWidth * .35, 72);
      if (overlap >= threshold) visible.push(index);
    });

    if (!visible.length) {
      const nearest = slides.reduce((best, slide, index) => (
        Math.abs(slide.offsetLeft - viewStart) < Math.abs(slides[best].offsetLeft - viewStart) ? index : best
      ), 0);
      return { first: nearest, last: nearest, count: 1 };
    }

    return {
      first: visible[0],
      last: visible[visible.length - 1],
      count: visible.length
    };
  }

  function updateGalleryNavigation() {
    const hasImages = galleryImages.length > 0;
    elements.galleryCounter.hidden = !hasImages;
    if (!hasImages) {
      elements.galleryCounter.textContent = "";
      elements.galleryPrevious.hidden = true;
      elements.galleryNext.hidden = true;
      return;
    }

    const range = getVisibleGalleryRange();
    galleryLeadIndex = range.first;
    elements.galleryCounter.textContent = range.first === range.last
      ? `${range.first + 1} / ${galleryImages.length}`
      : `${range.first + 1}–${range.last + 1} / ${galleryImages.length}`;

    const hasOverflow = elements.galleryTrack.scrollWidth > elements.galleryTrack.clientWidth + 2;
    elements.galleryPrevious.hidden = !hasOverflow;
    elements.galleryNext.hidden = !hasOverflow;
    elements.galleryPrevious.disabled = elements.galleryTrack.scrollLeft <= 2;
    elements.galleryNext.disabled = (
      elements.galleryTrack.scrollLeft + elements.galleryTrack.clientWidth >= elements.galleryTrack.scrollWidth - 2
    );
  }

  function goToGalleryImage(nextIndex, smooth = true) {
    if (!galleryImages.length) return;
    const slides = getGallerySlides();
    galleryLeadIndex = Math.max(0, Math.min(nextIndex, galleryImages.length - 1));
    const target = slides[galleryLeadIndex];
    if (!target) return;
    elements.galleryTrack.scrollTo({
      left: target.offsetLeft,
      behavior: smooth ? "smooth" : "auto"
    });
    requestAnimationFrame(updateGalleryNavigation);
  }

  function stepGallery(direction) {
    const range = getVisibleGalleryRange();
    const visibleCount = Math.max(range.count, 1);
    const nextIndex = direction > 0
      ? Math.min(range.last + 1, galleryImages.length - 1)
      : Math.max(range.first - visibleCount, 0);
    goToGalleryImage(nextIndex);
  }

  function updatePhotoDialog() {
    const category = categories[categoryIndex];
    const item = category.items[itemIndex];
    const source = galleryImages[dialogIndex];
    if (!source) return;

    elements.photoDialogTitle.textContent = item.title;
    elements.photoDialogCounter.textContent = `${dialogIndex + 1} / ${galleryImages.length}`;
    elements.photoDialogBackdrop.src = source;
    elements.photoDialogImage.src = source;
    elements.photoDialogImage.alt = galleryAltText(item, dialogIndex);
    const hasMultiple = galleryImages.length > 1;
    elements.photoDialogPrevious.hidden = !hasMultiple;
    elements.photoDialogNext.hidden = !hasMultiple;
    elements.photoDialogPrevious.disabled = dialogIndex === 0;
    elements.photoDialogNext.disabled = dialogIndex === galleryImages.length - 1;
  }

  function openPhotoDialog(index, trigger) {
    dialogIndex = index;
    lastGalleryTrigger = trigger;
    updatePhotoDialog();
    elements.photoDialog.showModal();
  }

  function closePhotoDialog(restoreFocus = true) {
    if (!elements.photoDialog.open) return;
    elements.photoDialog.close();
    if (restoreFocus && lastGalleryTrigger) {
      requestAnimationFrame(() => lastGalleryTrigger.focus());
    }
  }

  function stepPhotoDialog(direction) {
    const nextIndex = dialogIndex + direction;
    if (nextIndex < 0 || nextIndex >= galleryImages.length) return;
    dialogIndex = nextIndex;
    updatePhotoDialog();
  }

  function renderGallery(category, item) {
    closePhotoDialog(false);
    galleryImages = getGalleryImages(category, item);
    galleryLeadIndex = 0;
    dialogIndex = 0;
    lastGalleryTrigger = null;

    if (!galleryImages.length) {
      elements.storyGallery.hidden = true;
      elements.imagePlaceholder.hidden = false;
      elements.galleryTrack.replaceChildren();
      updateGalleryNavigation();
      return;
    }

    const fragment = document.createDocumentFragment();
    galleryImages.forEach((source, index) => {
      const slide = document.createElement("button");
      slide.type = "button";
      slide.className = "gallery-slide";
      if (galleryImages.length === 1) slide.classList.add("is-single");
      slide.setAttribute("aria-label", `${galleryAltText(item, index)}; ${getCopy().tapToEnlarge}`);

      const image = document.createElement("img");
      image.className = "gallery-image";
      image.alt = galleryAltText(item, index);
      image.decoding = "async";
      image.loading = index < 4 ? "eager" : "lazy";
      if (index === 0) image.setAttribute("fetchpriority", "high");
      image.draggable = false;
      image.addEventListener("load", () => {
        if (!image.naturalWidth || !image.naturalHeight) return;
        const ratio = image.naturalWidth / image.naturalHeight;
        slide.classList.toggle("is-portrait", ratio < 1);
        slide.style.setProperty("--image-ratio", `${image.naturalWidth} / ${image.naturalHeight}`);
        requestAnimationFrame(updateGalleryNavigation);
      }, { once: true });
      image.src = source;

      slide.append(image);
      slide.addEventListener("click", () => openPhotoDialog(index, slide));
      fragment.append(slide);
    });

    elements.galleryTrack.replaceChildren(fragment);
    elements.storyGallery.hidden = false;
    elements.imagePlaceholder.hidden = true;
    requestAnimationFrame(() => {
      elements.galleryTrack.scrollLeft = 0;
    });
    updateGalleryNavigation();
  }

  function renderHighlightedText(element, value, emphasis = []) {
    const text = String(value || "");
    const phrases = emphasis.filter((phrase) => phrase && text.includes(phrase));

    if (!phrases.length) {
      element.textContent = text;
      return;
    }

    const fragment = document.createDocumentFragment();
    let cursor = 0;

    while (cursor < text.length) {
      const next = phrases.reduce((match, phrase) => {
        const index = text.indexOf(phrase, cursor);
        if (index === -1) return match;
        if (!match || index < match.index || (index === match.index && phrase.length > match.phrase.length)) {
          return { index, phrase };
        }
        return match;
      }, null);

      if (!next) {
        fragment.append(document.createTextNode(text.slice(cursor)));
        break;
      }

      if (next.index > cursor) fragment.append(document.createTextNode(text.slice(cursor, next.index)));
      const strong = document.createElement("strong");
      strong.textContent = next.phrase;
      fragment.append(strong);
      cursor = next.index + next.phrase.length;
    }

    element.replaceChildren(fragment);
  }

  function appendRichRuns(container, runs) {
    const fragment = document.createDocumentFragment();

    (Array.isArray(runs) ? runs : []).forEach((runValue) => {
      const run = typeof runValue === "string" ? { text: runValue } : (runValue || {});
      let node = document.createTextNode(String(run.text || ""));

      if (run.bold) {
        const strong = document.createElement("strong");
        strong.append(node);
        node = strong;
      }
      if (run.italic) {
        const emphasis = document.createElement("em");
        emphasis.append(node);
        node = emphasis;
      }
      if (run.underline) {
        const underline = document.createElement("u");
        underline.append(node);
        node = underline;
      }

      const safeHref = getSafeHttpUrl(run.href);
      if (safeHref) {
        const link = document.createElement("a");
        link.className = "story-inline-link";
        link.href = safeHref;
        link.target = "_blank";
        link.rel = "noopener noreferrer";
        link.append(node);
        node = link;
      }

      fragment.append(node);
    });

    container.append(fragment);
  }

  function renderStoryBlocks(element, item) {
    const blocks = Array.isArray(item.blocks) ? item.blocks : [];
    if (!blocks.length) {
      renderHighlightedText(element, item.text, item.emphasis);
      return;
    }

    const fragment = document.createDocumentFragment();
    blocks.forEach((block) => {
      if (!block || typeof block !== "object") return;

      if (block.type === "list") {
        const list = document.createElement(block.ordered ? "ol" : "ul");
        list.className = "story-list";
        if (["left", "center", "right", "justify"].includes(block.align)) {
          list.classList.add(`story-align-${block.align}`);
        }
        (Array.isArray(block.items) ? block.items : []).forEach((runs) => {
          const listItem = document.createElement("li");
          listItem.className = "story-list-item";
          appendRichRuns(listItem, runs);
          list.append(listItem);
        });
        if (list.children.length) fragment.append(list);
        return;
      }

      const content = document.createElement(block.type === "subheading" ? "h3" : "p");
      content.className = block.type === "subheading" ? "story-subheading" : "story-paragraph";
      if (["left", "center", "right", "justify"].includes(block.align)) {
        content.classList.add(`story-align-${block.align}`);
      }
      appendRichRuns(content, block.runs);
      fragment.append(content);
    });

    element.replaceChildren(fragment);
  }

  function renderStory() {
    const category = categories[categoryIndex];
    const item = category.items[itemIndex];

    document.documentElement.style.setProperty("--category-accent", category.accent);
    document.documentElement.style.setProperty("--category-accent-soft", category.accentSoft || category.accent);
    document.documentElement.style.setProperty("--category-accent-ink", category.accentInk || "#06394A");
    elements.categoryNumber.textContent = formatIndex(categoryIndex);
    elements.categoryTitle.textContent = category.title;
    elements.storyIndex.textContent = `${formatIndex(itemIndex)} / ${String(category.items.length).padStart(2, "0")}`;
    elements.storyTitle.textContent = item.title;
    elements.storyLead.textContent = item.lead;
    elements.storyLead.classList.remove("story-align-left", "story-align-center", "story-align-right", "story-align-justify");
    if (["left", "center", "right", "justify"].includes(item.leadAlign)) {
      elements.storyLead.classList.add(`story-align-${item.leadAlign}`);
    }
    renderStoryBlocks(elements.storyText, item);
    elements.storyGallery.setAttribute("aria-label", getCopy().photoGallery(item.title));
    renderGallery(category, item);

    const metricFragment = document.createDocumentFragment();
    (Array.isArray(item.metrics) ? item.metrics : []).forEach((metric) => {
      if (!Array.isArray(metric)) return;
      const [value, label] = metric;
      const card = document.createElement("div");
      card.className = "metric-card";
      const strong = document.createElement("strong");
      strong.className = "metric-value";
      if (Array.from(String(value)).length > 9) strong.classList.add("metric-value-compact");
      strong.textContent = value;
      const span = document.createElement("span");
      span.textContent = label;
      card.append(strong, span);
      metricFragment.append(card);
    });
    elements.metricGrid.replaceChildren(metricFragment);

    const safeLinkUrl = getSafeHttpUrl(item.link?.url);
    if (item.link && safeLinkUrl) {
      elements.storyLink.hidden = false;
      elements.storyLink.href = safeLinkUrl;
      elements.storyLinkLabel.textContent = item.link.label || safeLinkUrl;
    } else {
      elements.storyLink.hidden = true;
      elements.storyLink.removeAttribute("href");
      elements.storyLinkLabel.textContent = "";
    }

    elements.topicList.querySelectorAll(".topic-button").forEach((button, index) => {
      const active = index === itemIndex;
      button.classList.toggle("active", active);
      button.setAttribute("aria-pressed", String(active));
      if (active) button.scrollIntoView({ block: "nearest", inline: "nearest" });
    });

    document.title = `${getCopy().pageTitle} • ${item.title}`;
  }

  function showCategory(nextCategoryIndex, nextItemIndex = 0, pushHistory = false) {
    if (!categories[nextCategoryIndex]) return;
    categoryIndex = nextCategoryIndex;
    itemIndex = Math.max(0, Math.min(nextItemIndex, categories[categoryIndex].items.length - 1));
    elements.homeView.hidden = true;
    elements.detailView.hidden = false;
    renderTopicList(categories[categoryIndex]);
    renderStory();

    const hash = getItemHash(categories[categoryIndex], categories[categoryIndex].items[itemIndex]);
    if (pushHistory) history.pushState({ categoryIndex, itemIndex }, "", hash);
    else history.replaceState({ categoryIndex, itemIndex }, "", hash);
  }

  function selectItem(nextIndex, replaceHistory = true) {
    const category = categories[categoryIndex];
    if (!category || !category.items[nextIndex]) return;
    itemIndex = nextIndex;
    renderStory();
    const hash = getItemHash(category, category.items[itemIndex]);
    if (replaceHistory) history.replaceState({ categoryIndex, itemIndex }, "", hash);
  }

  function showHome(pushHistory = false) {
    closePhotoDialog(false);
    elements.detailView.hidden = true;
    elements.homeView.hidden = false;
    document.title = getCopy().pageTitle;
    if (pushHistory) history.pushState({}, "", `${location.pathname}${location.search}`);
    if (lastHomeCard) requestAnimationFrame(() => lastHomeCard.focus());
  }

  function syncFromLocation() {
    const nextLanguage = new URLSearchParams(location.search).get("lang") === "en" && contentByLanguage.en.length
      ? "en"
      : "tr";
    if (nextLanguage !== language) {
      closePhotoDialog(false);
      language = nextLanguage;
      categories = contentByLanguage[language];
      lastHomeCard = null;
      applyStaticCopy();
      renderHome();
    }

    const match = location.hash.match(/^#\/([^/]+)(?:\/([^/]+))?\/?$/);
    if (!match) {
      showHome(false);
      return;
    }

    const categoryId = decodeRoutePart(match[1]);
    const itemRoute = decodeRoutePart(match[2] || "");
    const foundCategory = categories.findIndex((category) => category.id === categoryId);
    if (foundCategory === -1) {
      showHome(false);
      return;
    }

    const foundItems = categories[foundCategory].items;
    let foundItem = 0;
    if (/^\d+$/.test(itemRoute)) {
      foundItem = Math.max(0, Number(itemRoute) - 1);
    } else if (itemRoute) {
      const matchedItemIndex = foundItems.findIndex((item) => item.id === itemRoute);
      foundItem = matchedItemIndex >= 0 ? matchedItemIndex : 0;
    }
    showCategory(foundCategory, foundItem, false);
  }

  async function toggleFullscreen() {
    try {
      if (!document.fullscreenElement) await document.documentElement.requestFullscreen();
      else await document.exitFullscreen();
    } catch (error) {
      console.warn(getCopy().fullscreenError, error);
    }
  }

  function updateFullscreenButtons() {
    const copy = getCopy();
    const isFullscreen = Boolean(document.fullscreenElement);
    document.querySelectorAll("[data-fullscreen]").forEach((button) => {
      const label = button.querySelector("span");
      if (label) label.textContent = isFullscreen ? copy.exitFullscreen : copy.fullscreen;
      button.setAttribute("aria-label", isFullscreen ? copy.exitFullscreen : copy.openFullscreen);
    });
  }

  applyStaticCopy();
  renderHome();
  elements.languageButtons.forEach((button) => button.addEventListener("click", () => {
    changeLanguage(language === "tr" ? "en" : "tr");
  }));
  elements.feedbackOpenButtons.forEach((button) => button.addEventListener("click", () => {
    openFeedbackDialog(button);
  }));
  elements.feedbackForm.addEventListener("submit", (event) => {
    event.preventDefault();
    if (!feedbackSubmitting) submitFeedback();
  });
  elements.feedbackMessage.addEventListener("input", () => {
    updateFeedbackCounter();
    if (elements.feedbackMessage.value.trim().length >= 3) {
      elements.feedbackMessage.removeAttribute("aria-invalid");
    }
    if (feedbackStatusState === "validation" || feedbackStatusState === "error") {
      setFeedbackStatus("idle");
    }
  });
  elements.feedbackCancel.addEventListener("click", closeFeedbackDialog);
  elements.feedbackClose.addEventListener("click", closeFeedbackDialog);
  elements.feedbackSuccessClose.addEventListener("click", closeFeedbackDialog);
  elements.feedbackDialog.addEventListener("cancel", (event) => {
    if (feedbackSubmitting) event.preventDefault();
  });
  elements.feedbackDialog.addEventListener("close", () => {
    const trigger = lastFeedbackTrigger;
    lastFeedbackTrigger = null;
    resetFeedbackDialog();
    if (trigger?.isConnected) requestAnimationFrame(() => trigger.focus());
  });
  elements.homeButton.addEventListener("click", () => showHome(true));
  elements.galleryPrevious.addEventListener("click", () => stepGallery(-1));
  elements.galleryNext.addEventListener("click", () => stepGallery(1));
  elements.photoDialogPrevious.addEventListener("click", () => stepPhotoDialog(-1));
  elements.photoDialogNext.addEventListener("click", () => stepPhotoDialog(1));
  elements.photoDialogClose.addEventListener("click", () => closePhotoDialog());
  elements.photoDialogImageButton.addEventListener("click", () => closePhotoDialog());
  elements.photoDialog.addEventListener("cancel", () => {
    if (lastGalleryTrigger) requestAnimationFrame(() => lastGalleryTrigger.focus());
  });
  elements.galleryTrack.addEventListener("scroll", () => {
    if (galleryScrollFrame) cancelAnimationFrame(galleryScrollFrame);
    galleryScrollFrame = requestAnimationFrame(() => {
      updateGalleryNavigation();
    });
  }, { passive: true });
  elements.galleryTrack.addEventListener("keydown", (event) => {
    if (event.key === "ArrowLeft") {
      event.preventDefault();
      event.stopPropagation();
      stepGallery(-1);
    }
    if (event.key === "ArrowRight") {
      event.preventDefault();
      event.stopPropagation();
      stepGallery(1);
    }
  });
  document.querySelectorAll("[data-fullscreen]").forEach((button) => button.addEventListener("click", toggleFullscreen));
  document.addEventListener("fullscreenchange", updateFullscreenButtons);
  window.addEventListener("popstate", syncFromLocation);
  window.addEventListener("resize", () => {
    requestAnimationFrame(() => goToGalleryImage(galleryLeadIndex, false));
  });
  window.addEventListener("keydown", (event) => {
    if (elements.feedbackDialog.open) return;
    if (elements.photoDialog.open) {
      if (event.key === "ArrowLeft") {
        event.preventDefault();
        stepPhotoDialog(-1);
      }
      if (event.key === "ArrowRight") {
        event.preventDefault();
        stepPhotoDialog(1);
      }
      return;
    }
    if (event.target instanceof Element && event.target.closest("button, a, input, select, textarea, [contenteditable]")) return;
    if (!elements.detailView.hidden && event.key === "Escape" && !document.fullscreenElement) showHome(true);
    if (!elements.detailView.hidden && event.key === "ArrowLeft") selectItem(itemIndex - 1);
    if (!elements.detailView.hidden && event.key === "ArrowRight") selectItem(itemIndex + 1);
  });

  if (!document.fullscreenEnabled) {
    document.querySelectorAll("[data-fullscreen]").forEach((button) => { button.hidden = true; });
  }

  syncFromLocation();
})();
