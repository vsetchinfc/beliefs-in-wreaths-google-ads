class CartNotification extends HTMLElement {
  constructor() {
    super();

    this.notification = document.getElementById('cart-notification');
    this.header = document.querySelector('sticky-header');
    this.onBodyClick = this.handleBodyClick.bind(this);

    this.notification.addEventListener('keyup', (evt) => evt.code === 'Escape' && this.close());
    this.querySelectorAll('button[type="button"]').forEach((closeButton) =>
      closeButton.addEventListener('click', this.close.bind(this))
    );
  }

  open() {
    this.notification.classList.add('animate', 'active');

    this.notification.addEventListener(
      'transitionend',
      () => {
        this.notification.focus();
        trapFocus(this.notification);
      },
      { once: true }
    );

    document.body.addEventListener('click', this.onBodyClick);
  }

  close() {
    this.notification.classList.remove('active');
    document.body.removeEventListener('click', this.onBodyClick);

    removeTrapFocus(this.activeElement);
  }

  renderContents(parsedState) {
    this.cartItemKey = parsedState.key;
    this.getSectionsToRender().forEach((section) => {
      document.getElementById(section.id).innerHTML = this.getSectionInnerHTML(
        parsedState.sections[section.id],
        section.selector
      );
    });

    // Update free shipping progress bar - fetch fresh cart data
    this.updateFreeShippingProgress();

    if (this.header) this.header.reveal();
    this.open();
  }

  async updateFreeShippingProgress() {
    const freeShippingThreshold = 14000; // $140 in cents
    
    // Fetch fresh cart data
    let cartTotal = 0;
    try {
      const response = await fetch('/cart.js');
      const cart = await response.json();
      cartTotal = cart.total_price || 0;
    } catch (error) {
      console.error('Error fetching cart:', error);
      return;
    }
    
    const remaining = freeShippingThreshold - cartTotal;
    
    const shippingContainer = document.getElementById('cart-notification-shipping');
    const shippingMessage = document.getElementById('shipping-message');
    const shippingProgress = document.getElementById('shipping-progress');
    const progressBar = document.getElementById('shipping-progress-bar');
    const progressText = document.getElementById('shipping-progress-text');
    
    if (!shippingContainer || !shippingMessage) return;
    
    // Format currency
    const formatMoney = (cents) => {
      return '$' + (cents / 100).toFixed(2);
    };
    
    if (remaining <= 0) {
      // Free shipping achieved!
      shippingContainer.style.background = '#d4edda';
      shippingContainer.style.borderColor = '#c3e6cb';
      shippingMessage.style.color = '#155724';
      shippingMessage.innerHTML = '✓ You\'ve earned <strong>FREE SHIPPING</strong>! 🚚';
      
      // Add subtitle
      const subtitle = document.createElement('div');
      subtitle.style.cssText = 'text-align: center; color: #155724; font-size: 12px; margin-top: 4px;';
      subtitle.textContent = 'Orders $140+ ship free across Australia';
      shippingMessage.appendChild(subtitle);
      
      if (shippingProgress) shippingProgress.style.display = 'none';
    } else {
      // Show progress toward free shipping
      shippingContainer.style.background = '#fff3cd';
      shippingContainer.style.borderColor = '#ffeaa7';
      shippingMessage.style.color = '#856404';
      shippingMessage.innerHTML = `🚚 Add <strong>${formatMoney(remaining)}</strong> more for FREE SHIPPING!`;
      
      if (shippingProgress && progressBar && progressText) {
        shippingProgress.style.display = 'block';
        const percentage = Math.min((cartTotal / freeShippingThreshold) * 100, 100);
        progressBar.style.width = percentage + '%';
        progressText.textContent = `${formatMoney(cartTotal)} / $140.00`;
      }
    }
  }

  getSectionsToRender() {
    return [
      {
        id: 'cart-notification-product',
        selector: `[id="cart-notification-product-${this.cartItemKey}"]`,
      },
      {
        id: 'cart-notification-button',
      },
      {
        id: 'cart-icon-bubble',
      },
    ];
  }

  getSectionInnerHTML(html, selector = '.shopify-section') {
    return new DOMParser().parseFromString(html, 'text/html').querySelector(selector).innerHTML;
  }

  handleBodyClick(evt) {
    const target = evt.target;
    if (target !== this.notification && !target.closest('cart-notification')) {
      const disclosure = target.closest('details-disclosure, header-menu');
      this.activeElement = disclosure ? disclosure.querySelector('summary') : null;
      this.close();
    }
  }

  setActiveElement(element) {
    this.activeElement = element;
  }
}

customElements.define('cart-notification', CartNotification);
