# 🔍 CONVERSION TRACKING VERIFICATION GUIDE
## Updated: October 30, 2025

**Purpose:** Verify that GA4 and Google Ads conversion tracking is properly set up after Oct 29 updates

**Time Required:** 30-45 minutes

---

## 📋 WHAT I NEED FROM YOU

To verify your tracking setup is correct, please provide screenshots or information for each section below:

---

## 1️⃣ GOOGLE ADS - CONVERSION TRACKING

### A. Conversion Actions List

**Path:** Google Ads → Goals → Conversions → Summary

**Please provide screenshot or tell me:**
- [ ] How many conversion actions do you see?
- [ ] What are their names? (e.g., "Purchase", "Order", "Transaction")
- [ ] What's the "Source" for each? (Should say "Google Analytics 4" or "Website")
- [ ] What's the "Status"? (Should say "Recording conversions")
- [ ] Last conversion date shown?

**What I'm looking for:**
✅ At least one conversion action with "Google Analytics 4" as source
✅ Status: "Recording conversions" (green checkmark)
✅ Recent activity (conversions in last 7-30 days)

---

### B. Conversion Action Settings

**Path:** Click on the main conversion action name → View settings

**Please tell me:**
- [ ] **Goal:** What type? (Purchase, Add to cart, etc.)
- [ ] **Count:** "One" or "Every"? (Should be "One" for purchases)
- [ ] **Conversion window:**
  - Click-through conversion window: ___ days (recommend 30)
  - View-through conversion window: ___ day (recommend 1)
- [ ] **Attribution model:** Last click, Data-driven, or other?
- [ ] **Value:** 
  - Using transaction-specific value? (Recommended)
  - Or static value?
- [ ] **Include in 'Conversions':** Checked or unchecked?

**What I'm looking for:**
✅ Count: "One" (don't double-count same customer)
✅ Click-through window: 30 days (standard for e-commerce)
✅ Value: Transaction-specific (actual order value)
✅ Include in 'Conversions': CHECKED

---

### C. Campaign Conversions Column

**Path:** Google Ads → Campaigns → Click on "B-in-W [Search | Sales]"

**Please check:**
- [ ] Do you see a "Conversions" column? (If not, add it from column selector)
- [ ] Any conversions showing since Oct 29?
- [ ] What's the number?

**Then go to Keywords tab:**
- [ ] Do you see "Conversions" column for each keyword?
- [ ] Does "luxury christmas wreath" show 2 conversions?
- [ ] Any new conversions since Oct 29?

**Screenshot would be helpful here!**

---

## 2️⃣ GA4 - CONVERSION TRACKING

### A. Key Events (Conversions)

**Path:** GA4 → Admin (gear icon) → Events

**Please provide screenshot or tell me:**
- [ ] Is there a "purchase" event in the list?
- [ ] Is it marked as a "Key event"? (toggle should be ON/blue)
- [ ] What's the "Event count" in last 30 days?
- [ ] Any other events marked as Key events?

**What I'm looking for:**
✅ "purchase" event exists
✅ Marked as Key event (blue toggle)
✅ Event count > 0 (showing some purchase activity)

---

### B. Google Ads Link

**Path:** GA4 → Admin → Product Links → Google Ads Links

**Please tell me:**
- [ ] How many Google Ads accounts are linked?
- [ ] What's the link status? (Should show green "Linked")
- [ ] Click on the link name → What's configured?
  - [ ] Auto-tagging: Enabled?
  - [ ] Personalized advertising: Enabled?
  - [ ] Import conversions to Google Ads: Enabled?
  - [ ] Which key events are being imported? (Should include "purchase")

**Screenshot would be very helpful here!**

**What I'm looking for:**
✅ Link status: Active/Linked (green)
✅ Auto-tagging: Enabled
✅ Import conversions: Enabled
✅ "purchase" event selected for import

---

### C. Recent Conversions Data

**Path:** GA4 → Reports → Monetization → Ecommerce purchases

**Please check:**
- [ ] Do you see any purchase events in last 7 days?
- [ ] How many?
- [ ] What's the total revenue showing?
- [ ] Click "View purchase journey" → What traffic sources are converting?
  - Is "Paid Search" showing any purchases?

**Alternative Path:** GA4 → Reports → Engagement → Events
- [ ] Filter to "purchase" event
- [ ] Event count in last 7/30 days?

**What I'm looking for:**
✅ Purchase events recorded (should match Shopify orders)
✅ Some attribution to "Paid Search" if you had Google Ads clicks

---

### D. Google Signals

**Path:** GA4 → Admin → Data Settings → Data Collection

**Please tell me:**
- [ ] Google signals data collection: Activated or Not activated?

**If not activated:**
This is optional but recommended. It helps with cross-device tracking and remarketing.

---

## 3️⃣ SHOPIFY - GA4 INTEGRATION

### A. GA4 Measurement ID

**Path:** Shopify Admin → Online Store → Preferences → Scroll to "Google Analytics"

**Please tell me:**
- [ ] Is there a Google Analytics 4 measurement ID entered?
- [ ] What's the format? (Should be G-XXXXXXXXXX)
- [ ] Any Universal Analytics ID (UA-XXXXXXX)? (Old, can ignore)

**What I'm looking for:**
✅ GA4 measurement ID present (starts with G-)
✅ Correctly formatted

---

### B. Enhanced Ecommerce (Optional)

**Path:** Shopify Admin → Settings → Checkout and accounts → Order status page

**Check:**
- [ ] Is there any additional Google Analytics code in "Additional scripts"?
- [ ] What does it contain?

**What I'm looking for:**
- Usually not needed if using GA4 properly
- Just checking if there's conflicting code

---

## 4️⃣ CROSS-REFERENCE WITH SHOPIFY ORDERS

### Recent Orders Check

**Path:** Shopify Admin → Orders → Filter by date

**Please check orders from Oct 1-30, 2025:**
- [ ] How many orders total?
- [ ] For each order, click into it → Check "Additional details" section
- [ ] What does "Referrer" or "Landing page" show?
  - Look for anything with "google", "gclid", or "utm_source=google"

**What I'm looking for:**
- Orders that came from Google Ads but maybe weren't tracked
- Helps us identify if tracking is missing conversions

**Approximate data is fine:**
- "I had 8 orders in October"
- "2-3 showed Google/gclid in the referrer"
- etc.

---

## 5️⃣ VERIFICATION TEST (OPTIONAL BUT RECOMMENDED)

### Option A: Live Test with Real Small Order

1. [ ] Click on one of your own Google Ads
2. [ ] Add cheapest item to cart
3. [ ] Complete checkout (use real payment or test mode if available)
4. [ ] Wait 24-48 hours
5. [ ] Check Google Ads → Conversions → Recent conversions
6. [ ] Check GA4 → Reports → Monetization → Ecommerce purchases

**This is the gold standard test but costs a small order amount**

---

### Option B: Google Tag Assistant Test

1. [ ] Install "Google Tag Assistant" Chrome extension
2. [ ] Visit your site: https://beliefsinwreaths.com.au
3. [ ] Click on Tag Assistant icon → Start recording
4. [ ] Add product to cart
5. [ ] Go to checkout page
6. [ ] Fill out forms (don't need to complete payment)
7. [ ] Check Tag Assistant → Does it show:
   - GA4 tags firing?
   - "purchase" event (if you went to thank you page)?
   - Any errors?

**Screenshot of Tag Assistant would be helpful!**

---

## 6️⃣ AUTO-TAGGING VERIFICATION

### Google Ads Auto-Tagging

**Path:** Google Ads → Settings (tools icon) → Account settings

**Please verify:**
- [ ] "Auto-tagging" section: Is it turned ON?
- [ ] "Tag the URL that people click through from my ad": Checked?

**What I'm looking for:**
✅ Auto-tagging: ON (this adds gclid parameter to URLs)

### URL Parameters Test

**Manual check:**
1. [ ] Go to Google Ads → Preview your ad
2. [ ] Click the ad preview
3. [ ] Look at the URL in browser address bar
4. [ ] Does it have "?gclid=XXXXXXX" or "&gclid=XXXXXXX" in it?

**What I'm looking for:**
✅ URL contains "gclid=" parameter (this is how Google tracks the click)

---

## 📊 SUMMARY CHECKLIST

Once you provide the information above, I'll verify:

- ✅ GA4 is tracking purchases correctly
- ✅ GA4 is linked to Google Ads properly
- ✅ Google Ads is importing GA4 conversions
- ✅ Auto-tagging is enabled
- ✅ Conversion settings are optimal
- ✅ No conflicts or double-tracking issues

---

## 🚀 WHAT TO SEND ME

**Easiest option:** Screenshots of:
1. Google Ads → Conversions → Summary page
2. Google Ads → Conversion action → Settings page
3. GA4 → Admin → Product Links → Google Ads Links (detail page)
4. GA4 → Admin → Events (showing purchase as Key event)
5. GA4 → Reports → Monetization → Ecommerce purchases (last 30 days)

**OR just tell me the answers to the questions above in a message!**

**Time-saving tip:** You can use Windows Snipping Tool (Windows + Shift + S) to take screenshots quickly.

---

## 🎯 NEXT STEPS AFTER VERIFICATION

Once tracking is verified:
1. ✅ Update daily budget to $25
2. ✅ Pause 9 non-converting keywords
3. ✅ Increase "luxury christmas wreath" bid to $5
4. ✅ Add 6 new luxury keywords
5. ✅ Monitor for first Week 1 conversions

**Let's get your tracking verified so we can confidently scale!** 🚀
