# Cart Afterpay Message Setup

## 🎯 Problem
Cart abandonment rate: **69%** (13 add-to-cart, only 4 purchases)

Customers see $190 total in cart but don't realize they can pay $47.50 x 4 with Afterpay.

---

## ✅ Solution
Add Afterpay payment breakdown message above the "Check out" button in cart.

### Visual Example:

**Before:**
```
Your cart
─────────────────────────
Coastal Christmas Wreath     $190.00

Estimated total   $152.00 AUD
Taxes, discounts and shipping calculated...

[Check out]
[Shop Pay] [PayPal] [G Pay]
```

**After:**
```
Your cart
─────────────────────────
Coastal Christmas Wreath     $190.00

Estimated total   $152.00 AUD
Taxes, discounts and shipping calculated...

┌─────────────────────────────────────┐
│ or 4 interest-free payments of $38  │
│ Pay over time with afterpay ⓘ       │
└─────────────────────────────────────┘

[Check out]
[Shop Pay] [PayPal] [G Pay]
```

---

## 📋 Installation Steps

### Step 1: Create the Snippet

1. **Shopify Admin** → **Online Store** → **Themes**
2. Click **"..."** on your active theme → **Edit code**
3. In left sidebar, find **Snippets** folder
4. Click **Add a new snippet**
5. Name it: `cart-afterpay-message`
6. Paste the code from `cart-afterpay-message.liquid`
7. Click **Save**

---

### Step 2: Add to Cart Template

1. Still in **Edit code**, find your cart template (one of these):
   - `sections/main-cart.liquid` ← Most likely
   - `sections/cart-template.liquid`
   - `templates/cart.liquid`

2. Search for the **"Check out"** button
   - Look for: `button` with text "Check out" or "Checkout"
   - Usually has class like `checkout-button` or `cart__checkout`

3. **Add this line ABOVE the checkout button:**
   ```liquid
   {% render 'cart-afterpay-message' %}
   ```

4. **Save**

---

### Step 3: Find the Right Location

If you're not sure where to add it, search for these patterns:

**Pattern 1: Simple button**
```liquid
<div class="cart-footer">
  {% render 'cart-afterpay-message' %}  <-- ADD HERE
  <button type="submit" class="checkout-button">
    Check out
  </button>
</div>
```

**Pattern 2: Form with total**
```liquid
<div class="cart__footer">
  <div class="cart__total">
    Estimated total {{ cart.total_price | money }}
  </div>
  {% render 'cart-afterpay-message' %}  <-- ADD HERE
  <button name="checkout">
    Check out
  </button>
</div>
```

**Pattern 3: With terms checkbox**
```liquid
<div class="cart-footer-wrapper">
  <p class="cart-terms">Taxes and shipping calculated at checkout</p>
  {% render 'cart-afterpay-message' %}  <-- ADD HERE
  <button class="btn btn--primary" type="submit">
    Proceed to checkout
  </button>
</div>
```

---

## 🎨 Customization Options

### Change Colors
Edit the snippet and adjust these values:

**Mint green border (current):**
```liquid
background: #f0fdf9;
border: 2px solid #b2fce4;
```

**White with subtle border:**
```liquid
background: #ffffff;
border: 2px solid #e5e5e5;
```

**Match your theme color:**
```liquid
background: #f5f5f5;
border: 2px solid #your-brand-color;
```

### Change Size
```liquid
font-size: 14px;  <-- Make bigger (16px) or smaller (12px)
padding: 16px;    <-- More/less spacing
```

### Hide Info Icon
Remove this part:
```liquid
<svg style="...">...</svg>
```

---

## 📊 Expected Impact

### Current Performance:
- Add to cart: 13 people
- Complete purchase: 4 people
- **Abandonment rate: 69%**

### After Adding Afterpay Message:
- **Expected abandonment: 35-40%**
- **Expected conversions: +4-6 per month**
- **Expected revenue increase: $600-900/month**

### Why It Works:
1. **Reduces sticker shock** - $190 → $47.50 feels manageable
2. **Decision made in cart** - Don't wait until checkout page
3. **Trust signal** - Legitimate payment option, not a trick
4. **Impulse purchase enabler** - "I can afford this NOW"

---

## ✅ Testing Checklist

After installation:

1. **Desktop Test:**
   - [ ] Add item to cart
   - [ ] Go to cart page
   - [ ] See Afterpay message above checkout button
   - [ ] Amount shows correctly (cart total ÷ 4)

2. **Mobile Test:**
   - [ ] Same as desktop
   - [ ] Message is readable on small screen
   - [ ] Doesn't break layout

3. **Different Cart Totals:**
   - [ ] Test with $50 item → Shows $12.50 x 4
   - [ ] Test with $190 item → Shows $47.50 x 4
   - [ ] Test with $300 item → Shows $75 x 4

4. **Actual Checkout:**
   - [ ] Click "Check out"
   - [ ] Afterpay available in payment methods
   - [ ] Can complete purchase with Afterpay

---

## 🚨 Troubleshooting

### Message not showing?
1. Check snippet name matches exactly: `cart-afterpay-message`
2. Check render call: `{% render 'cart-afterpay-message' %}`
3. Clear browser cache (Ctrl+Shift+R)
4. Check cart has items (message only shows if cart.total_price > 0)

### Amount calculation wrong?
- Uses cart.total_price (includes items + shipping estimate)
- Divides by 4 automatically
- Shows in your store currency

### Layout broken?
- Add `style="margin-bottom: 16px;"` to push checkout button down
- Or adjust padding in the snippet

### Not mobile responsive?
- Already responsive (stacks text vertically)
- If issues, change `font-size: 14px` to `font-size: 13px`

---

## 💡 Pro Tips

### Combine with Other Strategies:

1. **Show Afterpay on Product Pages Too**
   - Add similar message below "Add to cart" button
   - Format: "or 4 payments of $XX.XX with afterpay"

2. **Add to Mini Cart (Drawer)**
   - If you have cart drawer that slides out
   - Show message there too

3. **Email Abandoned Carts**
   - Mention Afterpay in recovery emails
   - "Did you know you can pay in 4 installments?"

4. **Update Shipping/Returns Page**
   - Explain Afterpay in FAQ
   - Build confidence before checkout

---

## 📈 Tracking Results

### Week 1 After Implementation:
- Monitor cart abandonment rate in Google Analytics
- Target: Drop from 69% to 50-55%

### Week 2-4:
- Track conversions attributed to cart improvements
- Compare: Conversions with cart message vs before

### Success Metrics:
- ✅ Cart abandonment drops 20-30%
- ✅ Afterpay usage increases 40-60%
- ✅ Average order value stable (not dropping due to Afterpay)
- ✅ Revenue per visitor increases

---

## 🎯 Next Steps After This

Once cart message is working:

1. **Product Page Afterpay** - Show payment breakdown before "Add to cart"
2. **Checkout Page Optimization** - Ensure Afterpay is first payment option
3. **Collection Page Badges** - Show "Afterpay available" on product cards
4. **FAQ/Trust Section** - Explain how Afterpay works

---

## Need Help?

If you get stuck, share a screenshot of:
1. Your cart page code (sections/main-cart.liquid)
2. Error messages (if any)
3. What you see vs what you expected

The message should appear within 5 minutes of installation! 🚀
