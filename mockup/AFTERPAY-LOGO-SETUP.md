# Afterpay Logo Setup Instructions

## Step 1: Save the Afterpay Logo Image

1. Right-click on the Afterpay logo image you showed me (the mint green rounded rectangle with "afterpay" text and arrow)
2. Save it as: `afterpay-logo.png` or `afterpay-logo.svg`

**Or download it from:**
- https://www.afterpay.com/en-AU/press (official brand assets page)

---

## Step 2: Upload to Shopify

### Option A: Via Theme Editor (Easiest)

1. Go to **Shopify Admin** → **Online Store** → **Themes**
2. Click the **"..."** menu on your active theme → **Edit code**
3. In the left sidebar, scroll to **Assets** folder
4. Click **"Add a new asset"**
5. Click **"Upload file"**
6. Select your `afterpay-logo.png` file
7. Click **Upload**

### Option B: Via Settings

1. **Shopify Admin** → **Content** → **Files**
2. Click **Upload files**
3. Select `afterpay-logo.png`
4. Copy the file URL (you'll need this)

---

## Step 3: Update the Code

After uploading, find this section in `announcement-bar-updated.liquid`:

```liquid
{%- if section.settings.show_afterpay -%}
  <div class="payment-logo-badge payment-logo-badge--afterpay">
    <span class="payment-logo-badge__text">Pay in 4 with</span>
    <span style="font-weight: 600; font-size: 14px; color: #000;">afterpay</span>
  </div>
{%- endif -%}
```

**Replace with:**

```liquid
{%- if section.settings.show_afterpay -%}
  <div class="payment-logo-badge payment-logo-badge--afterpay">
    <img 
      src="{{ 'afterpay-logo.png' | asset_url }}" 
      alt="Afterpay - Pay in 4" 
      style="height: 24px; width: auto;"
      loading="lazy"
    />
  </div>
{%- endif -%}
```

**If you used Option B (Files), use:**

```liquid
{%- if section.settings.show_afterpay -%}
  <div class="payment-logo-badge payment-logo-badge--afterpay">
    <img 
      src="YOUR_COPIED_URL_HERE" 
      alt="Afterpay - Pay in 4" 
      style="height: 24px; width: auto;"
      loading="lazy"
    />
  </div>
{%- endif -%}
```

---

## Step 4: Adjust Styling (Optional)

You can also remove the mint green background since the image already has it:

**In the `{%- style -%}` section, change:**

```css
.payment-logo-badge--afterpay {
  background: #b2fce4;
  border-color: #00d9a0;
}
```

**To:**

```css
.payment-logo-badge--afterpay {
  background: transparent;
  border: none;
  padding: 0;
  box-shadow: none;
}
```

---

## Quick Reference: Full Updated Code with Image

Once uploaded, the complete section will look like:

```liquid
{%- if section.settings.show_payment_logos -%}
  <div class="payment-logos-wrapper">
    {%- if section.settings.show_afterpay -%}
      <div class="payment-logo-badge payment-logo-badge--afterpay">
        <img 
          src="{{ 'afterpay-logo.png' | asset_url }}" 
          alt="Afterpay - Pay in 4" 
          style="height: 24px; width: auto;"
          loading="lazy"
        />
      </div>
    {%- endif -%}
    
    {%- if section.settings.show_paypal -%}
      <div class="payment-logo-badge">
        <img 
          src="https://www.paypalobjects.com/webstatic/mktg/Logo/pp-logo-100px.png" 
          alt="PayPal" 
          class="payment-logo-badge__img"
          loading="lazy"
        />
      </div>
    {%- endif -%}
  </div>
{%- endif -%}
```

---

## Troubleshooting

### Image not showing?

1. **Check filename matches exactly** - case-sensitive!
   - Uploaded: `afterpay-logo.png`
   - Code: `{{ 'afterpay-logo.png' | asset_url }}`

2. **Clear browser cache** - Hard refresh (Ctrl+F5 / Cmd+Shift+R)

3. **Verify upload location:**
   - Should be in: `Assets/afterpay-logo.png`
   - NOT in: `Files/` or `Sections/`

4. **Check file format:**
   - PNG works: `.png`
   - SVG works: `.svg`
   - JPG works: `.jpg`

### Image too big/small?

Adjust the `height` value:
- Smaller: `height: 20px`
- Larger: `height: 28px`

---

## Result

You'll have the official Afterpay logo (mint green rounded pill with text and arrow) displayed perfectly in your announcement bar!

✅ Brand-compliant
✅ High quality
✅ Matches your screenshot exactly
