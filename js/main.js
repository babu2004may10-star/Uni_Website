(function () {
  const header = document.querySelector('[data-header]');
  const menuToggle = document.querySelector('[data-menu-toggle]');
  const nav = document.querySelector('[data-nav]');
  const body = document.body;

  function updateHeader() {
    if (!header) return;
    header.classList.toggle('is-scrolled', window.scrollY > 8);
  }

  updateHeader();
  window.addEventListener('scroll', updateHeader, { passive: true });

  function setMenu(open) {
    if (!menuToggle || !header) return;
    header.classList.toggle('nav-open', open);
    menuToggle.setAttribute('aria-expanded', String(open));
    document.body.classList.toggle('is-locked', open);
  }

  if (menuToggle && nav) {
    menuToggle.addEventListener('click', function () {
      setMenu(menuToggle.getAttribute('aria-expanded') !== 'true');
    });

    nav.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        setMenu(false);
      });
    });

    document.addEventListener('click', function (event) {
      if (!header.classList.contains('nav-open')) return;
      if (!header.contains(event.target)) setMenu(false);
    });

    document.addEventListener('keydown', function (event) {
      if (event.key === 'Escape' && header.classList.contains('nav-open')) {
        setMenu(false);
        menuToggle.focus();
      }
    });

    window.addEventListener('resize', function () {
      if (window.innerWidth > 980) setMenu(false);
    });
  }

  const programmeCards = Array.from(document.querySelectorAll('.programme-card'));
  const programmeSearch = document.querySelector('[data-programme-search]');
  const levelButtons = Array.from(document.querySelectorAll('[data-level-filter]'));
  const schoolFilter = document.querySelector('[data-school-filter]');
  const programmeCount = document.querySelector('[data-programme-count]');
  const noResults = document.querySelector('[data-no-results]');
  const clearFilters = document.querySelector('[data-clear-filters]');
  let activeLevel = 'all';

  function filterProgrammes() {
    if (!programmeCards.length) return;

    const searchTerm = programmeSearch ? programmeSearch.value.trim().toLowerCase() : '';
    const school = schoolFilter ? schoolFilter.value : 'all';
    let visibleCount = 0;

    programmeCards.forEach(function (card) {
      const title = card.dataset.title || '';
      const description = card.textContent || '';
      const cardSchool = card.dataset.school || '';
      const level = card.dataset.level || '';
      const matchesSearch = !searchTerm ||
        title.toLowerCase().includes(searchTerm) ||
        description.toLowerCase().includes(searchTerm);
      const matchesLevel = activeLevel === 'all' || level === activeLevel;
      const matchesSchool = school === 'all' || cardSchool === school;
      const visible = matchesSearch && matchesLevel && matchesSchool;

      card.hidden = !visible;
      if (visible) visibleCount += 1;
    });

    if (programmeCount) {
      const programmeWord = visibleCount === 1 ? 'programme' : 'programmes';
      programmeCount.textContent = 'Showing ' + visibleCount + ' of ' + programmeCards.length + ' ' + programmeWord;
    }

    if (noResults) noResults.hidden = visibleCount !== 0;
  }

  if (programmeSearch) {
    programmeSearch.addEventListener('input', filterProgrammes);
  }

  levelButtons.forEach(function (button) {
    button.addEventListener('click', function () {
      activeLevel = button.dataset.levelFilter || 'all';
      levelButtons.forEach(function (item) {
        const selected = item === button;
        item.classList.toggle('is-active', selected);
        item.setAttribute('aria-pressed', String(selected));
      });
      filterProgrammes();
    });
  });

  if (schoolFilter) {
    schoolFilter.addEventListener('change', filterProgrammes);
  }

  if (clearFilters) {
    clearFilters.addEventListener('click', function () {
      activeLevel = 'all';
      if (programmeSearch) programmeSearch.value = '';
      if (schoolFilter) schoolFilter.value = 'all';
      levelButtons.forEach(function (button) {
        const selected = button.dataset.levelFilter === 'all';
        button.classList.toggle('is-active', selected);
        button.setAttribute('aria-pressed', String(selected));
      });
      filterProgrammes();
    });
  }

  filterProgrammes();

  function updateBodyLock() {
    const hasOpenDialog = Boolean(document.querySelector('dialog[open]'));
    const privacyOpen = document.querySelector('.privacy-panel:not([hidden])');
    body.classList.toggle('is-locked', hasOpenDialog || Boolean(privacyOpen) || Boolean(header && header.classList.contains('nav-open')));
  }

  function openDialog(dialog) {
    if (!dialog) return;
    if (typeof dialog.showModal === 'function') {
      dialog.showModal();
    } else {
      dialog.setAttribute('open', '');
    }
    updateBodyLock();
  }

  function closeDialog(dialog) {
    if (!dialog || !dialog.open) return;
    if (typeof dialog.close === 'function') {
      dialog.close();
    } else {
      dialog.removeAttribute('open');
      updateBodyLock();
    }
  }

  document.querySelectorAll('dialog').forEach(function (dialog) {
    dialog.addEventListener('close', updateBodyLock);
    dialog.addEventListener('click', function (event) {
      if (event.target === dialog) closeDialog(dialog);
    });
  });

  document.querySelectorAll('[data-close-dialog]').forEach(function (button) {
    button.addEventListener('click', function () {
      closeDialog(button.closest('dialog'));
    });
  });

  document.querySelectorAll('[data-dialog-apply]').forEach(function (link) {
    link.addEventListener('click', function () {
      closeDialog(link.closest('dialog'));
    });
  });

  const programmeDialog = document.getElementById('programme-dialog');
  const programmeOpenButtons = document.querySelectorAll('[data-programme-open]');

  programmeOpenButtons.forEach(function (button) {
    button.addEventListener('click', function () {
      const card = button.closest('.programme-card');
      if (!card || !programmeDialog) return;

      const setText = function (selector, value) {
        const element = programmeDialog.querySelector(selector);
        if (element) element.textContent = value;
      };

      setText('[data-dialog-type]', card.dataset.type || 'Programme');
      setText('[data-dialog-title]', card.dataset.title || '');
      setText('[data-dialog-school]', card.dataset.school || '');
      setText('[data-dialog-description]', card.dataset.description || '');
      setText('[data-dialog-requirements]', card.dataset.requirements || '');
      setText('[data-dialog-careers]', card.dataset.careers || '');
      openDialog(programmeDialog);
    });
  });

  const stories = {
    'climate-centre': {
      type: 'Campus · 12 November 2026',
      title: 'Our new Centre for Climate Innovation opens its doors',
      description: 'A collaborative space bringing researchers, students, and local partners together to prototype a more resilient future.',
      body: [
        'The Centre for Climate Innovation has opened on the eastern edge of campus, creating a shared home for climate research, teaching, and public engagement.',
        'Its first programme brings together environmental scientists, engineers, designers, and community organisations to test practical responses to rising temperatures and changing weather patterns.',
        'Students will have access to live projects, specialist laboratories, and a public events space designed to make research visible and useful beyond the university.'
      ]
    },
    'inclusive-campus': {
      type: 'Student life · 5 November 2026',
      title: 'Meet the students building a more inclusive campus',
      description: 'How a student-led accessibility project is changing the way we design spaces, services, and everyday experiences.',
      body: [
        'A group of students has spent the past year auditing the places where campus life happens — from lecture halls and libraries to social spaces and digital services.',
        'Their report combines lived experience with practical recommendations, including clearer wayfinding, quieter study areas, and more flexible ways to take part in events.',
        'The university is now working with the team to put the first recommendations into practice, with student involvement continuing throughout the process.'
      ]
    },
    'northbridge-medal': {
      type: 'Community · 28 October 2026',
      title: 'Northbridge graduates recognised for community impact',
      description: 'Three alumni receive this year’s Northbridge Medal for work in public health, education, and environmental justice.',
      body: [
        'The annual Northbridge Medal recognises graduates whose work has made a lasting difference to communities beyond the university.',
        'This year’s recipients have helped expand access to public health support, built new learning opportunities for young people, and campaigned for cleaner, safer neighbourhoods.',
        'They were honoured at a ceremony on campus, where students also presented projects developed through the university’s community partnership programme.'
      ]
    }
  };

  const storyDialog = document.getElementById('story-dialog');

  document.querySelectorAll('[data-story-open]').forEach(function (button) {
    button.addEventListener('click', function () {
      const story = stories[button.dataset.storyKey];
      if (!story || !storyDialog) return;

      storyDialog.querySelector('[data-story-type]').textContent = story.type;
      storyDialog.querySelector('[data-story-title]').textContent = story.title;
      storyDialog.querySelector('[data-story-description]').textContent = story.description;
      const bodyContainer = storyDialog.querySelector('[data-story-body]');
      bodyContainer.replaceChildren();
      story.body.forEach(function (paragraph) {
        const paragraphElement = document.createElement('p');
        paragraphElement.textContent = paragraph;
        bodyContainer.appendChild(paragraphElement);
      });
      openDialog(storyDialog);
    });
  });

  const fundingDialog = document.getElementById('funding-dialog');
  const researchDialog = document.getElementById('research-dialog');

  document.querySelectorAll('[data-funding-open]').forEach(function (button) {
    button.addEventListener('click', function () {
      openDialog(fundingDialog);
    });
  });

  document.querySelectorAll('[data-research-open]').forEach(function (button) {
    button.addEventListener('click', function () {
      openDialog(researchDialog);
    });
  });

  const privacyPanel = document.querySelector('.privacy-panel');
  let privacyTrigger = null;

  function openPrivacy(trigger) {
    if (!privacyPanel) return;
    privacyTrigger = trigger || document.activeElement;
    privacyPanel.hidden = false;
    updateBodyLock();
    const closeButton = privacyPanel.querySelector('[data-privacy-close]');
    if (closeButton) closeButton.focus();
  }

  function closePrivacy() {
    if (!privacyPanel || privacyPanel.hidden) return;
    privacyPanel.hidden = true;
    updateBodyLock();
    if (privacyTrigger && typeof privacyTrigger.focus === 'function') privacyTrigger.focus();
  }

  document.querySelectorAll('a[href="#privacy"]').forEach(function (link) {
    link.addEventListener('click', function (event) {
      event.preventDefault();
      openPrivacy(link);
    });
  });

  if (privacyPanel) {
    privacyPanel.querySelectorAll('[data-privacy-close]').forEach(function (button) {
      button.addEventListener('click', closePrivacy);
    });

    privacyPanel.addEventListener('click', function (event) {
      if (event.target === privacyPanel) closePrivacy();
    });

    privacyPanel.addEventListener('keydown', function (event) {
      if (event.key === 'Escape') {
        closePrivacy();
        return;
      }

      if (event.key !== 'Tab') return;

      const focusable = Array.from(
        privacyPanel.querySelectorAll('a[href], button:not([disabled]), [tabindex]:not([tabindex="-1"])')
      ).filter(function (element) {
        return element.offsetParent !== null;
      });

      if (!focusable.length) return;

      const first = focusable[0];
      const last = focusable[focusable.length - 1];

      if (event.shiftKey && document.activeElement === first) {
        event.preventDefault();
        last.focus();
      } else if (!event.shiftKey && document.activeElement === last) {
        event.preventDefault();
        first.focus();
      }
    });
  }

  const form = document.querySelector('[data-visit-form]');

  if (form) {
    const fields = {
      name: form.querySelector('#visit-name'),
      email: form.querySelector('#visit-email'),
      interest: form.querySelector('#visit-interest')
    };
    const success = form.querySelector('[data-form-success]');

    function errorFor(field) {
      return form.querySelector('[data-error-for="' + field.id + '"]');
    }

    function setFieldError(field, message) {
      const error = errorFor(field);
      field.setAttribute('aria-invalid', message ? 'true' : 'false');
      if (error) {
        if (!error.id) error.id = field.id + '-error';
        field.setAttribute('aria-describedby', error.id);
        error.textContent = message;
      }
    }

    function validateField(field) {
      const value = field.value.trim();
      let message = '';

      if (field === fields.name && value.length < 2) {
        message = 'Please enter your name.';
      } else if (field === fields.email) {
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;
        if (!value) {
          message = 'Please enter your email address.';
        } else if (!emailPattern.test(value)) {
          message = 'Enter a valid email address.';
        }
      } else if (field === fields.interest && !value) {
        message = 'Please select an option.';
      }

      setFieldError(field, message);
      return !message;
    }

    Object.values(fields).forEach(function (field) {
      if (!field) return;
      field.addEventListener('blur', function () {
        validateField(field);
      });
      field.addEventListener('input', function () {
        if (field.getAttribute('aria-invalid') === 'true') validateField(field);
      });
      field.addEventListener('change', function () {
        if (field.getAttribute('aria-invalid') === 'true') validateField(field);
      });
    });

    form.addEventListener('submit', function (event) {
      event.preventDefault();
      const validFields = Object.values(fields).filter(Boolean).map(validateField);
      const firstInvalid = Object.values(fields).find(function (field) {
        return field && field.getAttribute('aria-invalid') === 'true';
      });

      if (firstInvalid) {
        firstInvalid.focus();
        return;
      }

      if (!validFields.every(Boolean)) return;

      form.reset();
      Object.values(fields).forEach(function (field) {
        if (field) setFieldError(field, '');
      });

      if (success) {
        success.hidden = false;
        success.focus();
      }
    });
  }
})();
