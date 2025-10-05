# 🚨 TROUBLESHOOTING: Test Purchase Not Counted

**Date:** October 4, 2025  
**Issue:** Made test purchase, but no conversion recorded in Google Ads  
**Conversion:** Google Shopping App Purchase  

---

## 📋 QUICK DIAGNOSIS CHECKLIST

Check these items in order:

### ✅ 1. How Long Has It Been?
- [ ] **<3 hours:** WAIT - Conversions can take 3-24 hours to appear
- [ ] **3-24 hours:** Normal - Continue checking
- [ ] **>24 hours:** Problem - Continue troubleshooting below

**Action:** If less than 24 hours since purchase, wait before troubleshooting further.

---

### ✅ 2. Verify Conversion Settings

Looking at your screenshots, I see potential issues:

#### Issue A: Count Setting = "Every conversion"
**Current Setting:** Count = **Every conversion**  
**Should Be:** Count = **ONE** for purchases

**Why:** "Every conversion" means if someone purchases twice after one ad click, both count. For e-commerce purchases, you typically want "One" to count only the first purchase per click.

**Fix:**
1. Click on **Count** section to expand
2. Select **"One"** (recommended for purchases)
3. Click **Save**

---

#### Issue B: Value Setting Shows "$0" Default
**Current Setting:** "Use different values. If there's no value, use $0."  
**Concern:** If dynamic value isn't passing, conversions record as $0

**Check:**
1. Expand **Value** section
2. Verify: "Use different values for each conversion" is selected ✅
3. **Default value field:** Should be blank OR a realistic average (e.g., $150)
   - If it's $0, conversions might track but with no value

**Fix (if needed):**
1. Click **Value** to expand
2. In "Enter a default value" field, change from `0` to `150` (your average order)
3. This ensures if dynamic value fails, you still get some value data
4. Click **Save**

---

### ✅ 3. Check Conversion Source & Tag

**Current Setting:** Source = **Website**

**This means:** Conversion tracked via Google tag on your website (not GA4 import)

#### Verify Tag is Installed:

**Step 1: Check Thank-You Page**
1. Go to order confirmation page URL (after completing purchase)
2. Right-click → **View Page Source**
3. Press Ctrl+F and search for: `gtag`
4. Look for code like this:

```javascript
gtag('event', 'conversion', {
    'send_to': 'AW-XXXXXXXXX/AbC123',
    'value': 150.00,
    'currency': 'AUD',
    'transaction_id': ''
});
```

**If you DON'T see this code:**
❌ **Tag is not installed** → This is your problem!

**If you DO see this code:**
✅ **Tag is installed** → Continue to Step 2

---

**Step 2: Verify Conversion ID Matches**

In the gtag code, look for the `send_to` value:
```javascript
'send_to': 'AW-XXXXXXXXX/AbC123'
```

**Get the correct ID from Google Ads:**
1. In your conversion settings, scroll to **"Tag setup"** section
2. Click **"View tag setup instructions"** or similar
3. You'll see the conversion tracking snippet
4. Compare the `AW-XXXXXXXXX/AbC123` part
5. They should match EXACTLY

**If they don't match:**
❌ **Wrong conversion ID** → Update tag on website

---

### ✅ 4. Test with Google Tag Assistant

**Most Reliable Test:**

1. Install **Google Tag Assistant** Chrome extension
2. Go to: https://beliefsinwreaths.com.au
3. Click Tag Assistant icon → **Enable**
4. Refresh the page
5. Add item to cart → Complete checkout
6. On thank-you/confirmation page → Click Tag Assistant icon

**What You Should See:**
```
✅ Google Ads Conversion Tracking
   Conversion ID: AW-XXXXXXXXX
   Conversion Label: AbC123xyz
   Status: Tag fired successfully
   Value: 150.00 (or your order amount)
   Currency: AUD
```

**What It Means:**
- ✅ **Tag fired successfully:** Conversion is being sent to Google Ads
- ⚠️ **Tag not found:** Conversion tag not installed on confirmation page
- 🔴 **Tag error:** Conversion tag has configuration problem

---

### ✅ 5. Verify You're Checking the Right Place

**Where to Check Conversions:**

**Option A: Conversion Action Details**
1. Go to: **Goals** → **Conversions** (left sidebar)
2. Find: **Google Shopping App Purchase**
3. Click on the name
4. Look at the performance graph
5. Change date range to **"Last 7 days"**
6. Should show spike on day of test purchase

**Option B: Campaign View**
1. Go to: **Campaigns** (left sidebar)
2. Find your campaign
3. Look at **"Conversions"** column
4. Should show +1 after test purchase appears

**Option C: Check "All Time" Date Range**
1. Make sure date range selector shows **"All time"** or includes test purchase date
2. Your screenshot shows: "31 July 2022 - 4 Oct 2025" ✅ Good
3. If date range excludes today, you won't see the conversion!

---

## 🔧 MOST LIKELY CAUSES & FIXES

Based on your setup, here are the probable issues:

### Issue #1: Conversion Tag Not on Confirmation Page (80% likely)

**Symptom:** Tag Assistant shows "Tag not found" on order confirmation page

**Why:** 
- Shopify/website checkout redirects to external payment processor
- Tag only on product pages, not confirmation page
- Thank-you page is custom URL not tracked

**Fix:**
1. Identify your order confirmation page URL
   - Usually: `/thank-you`, `/order-confirmed`, `/checkout/thank_you`
2. Access website admin (Shopify, WordPress, etc.)
3. Find "Order status page" or "Thank you page" settings
4. Add Google Ads conversion tracking code there
5. Test again

**For Shopify Specifically:**
1. Shopify Admin → **Settings** → **Checkout**
2. Scroll to **Order status page** section
3. Paste conversion tracking code in **Additional scripts** box
4. **Save**

---

### Issue #2: Dynamic Value Not Passing (15% likely)

**Symptom:** 
- Tag fires successfully (Tag Assistant shows it)
- But conversion value shows as $0.00 in Google Ads
- Or conversions don't appear at all

**Why:**
- Conversion tag isn't receiving transaction value dynamically
- E-commerce platform not passing order amount to tag

**Fix:**

**Check Current Tag:**
```javascript
gtag('event', 'conversion', {
    'send_to': 'AW-XXXXXXXXX/AbC123',
    'value': 150.00,  // ← Is this static or dynamic?
    'currency': 'AUD',
    'transaction_id': ''
});
```

**If value is static (e.g., always 150.00):**
- Conversions will track, but all show same value
- Not ideal, but better than nothing

**If value should be dynamic:**
- Needs to use variable from e-commerce platform
- Example for Shopify: `{{ checkout.total_price }}`
- May need developer help

**Temporary Workaround:**
1. In Google Ads conversion settings
2. Set "Enter a default value" to your average order value (e.g., $150)
3. At least you'll get estimated value data

---

### Issue #3: Conversion Attributed to Wrong Source (3% likely)

**Symptom:**
- You made test purchase directly (not from ad click)
- Conversion tracked, but Google Ads doesn't count it

**Why:**
- Google Ads only counts conversions from people who clicked your ad
- Direct purchases (no ad click) don't appear in Google Ads reports
- But they DO appear in conversion action's total count

**Check:**
1. Did you click your own Google Ad before making test purchase?
2. If NO → Conversion won't show in campaign reports
3. If YES → Should show up (if tag works)

**Fix for Test:**
1. Search for your keywords on Google (use Incognito mode)
2. Click your own ad
3. Complete a purchase
4. Wait 3-24 hours
5. Check Google Ads

**Note:** You'll be charged for clicking your own ad!

---

### Issue #4: Conversion Window Too Short (1% likely)

**Your Settings:**
- Click-through conversion window: **90 days** ✅ Good
- Engaged-view conversion window: **3 days** ✅ Good
- View-through conversion window: **30 days** ✅ Good

**This is NOT your problem** - windows are fine.

---

### Issue #5: Enhanced Conversions Issue (1% likely)

**Your Setting:** Enhanced conversions = **Managed through Google tag** ✅

This should be fine, but if you're NOT sending enhanced conversion data (email, phone, address), it might cause issues in some rare cases.

**Quick Check:**
- Enhanced conversions need customer data (email) hashed and sent
- If your tag doesn't include this, it's okay
- Enhanced conversions are optional (not required for basic tracking)

---

## 🎯 RECOMMENDED ACTION PLAN

### Step 1: Wait (if <24 hours)
- [ ] Wait 24 hours from test purchase time
- [ ] Check again tomorrow morning
- [ ] If still not showing → Continue to Step 2

### Step 2: Fix "Count" Setting
- [ ] Go to conversion settings
- [ ] Change **Count** from "Every" to **"One"**
- [ ] Click **Save**

### Step 3: Set Default Value
- [ ] Expand **Value** section
- [ ] Change default value from `0` to `150` (or your average)
- [ ] Click **Save**

### Step 4: Verify Tag Installation
- [ ] Install Google Tag Assistant
- [ ] Complete another test purchase
- [ ] Check if tag fires on confirmation page
- [ ] **If NOT firing:** Tag not installed (see Issue #1 fix above)
- [ ] **If firing:** Tag is working, may just need to wait

### Step 5: Check Confirmation Page Code
- [ ] Go to thank-you page
- [ ] View page source
- [ ] Search for `gtag('event', 'conversion'`
- [ ] **If NOT found:** Add conversion tag (see Issue #1)
- [ ] **If found:** Verify conversion ID matches Google Ads

### Step 6: Test from Ad Click
- [ ] Search Google for your keywords (Incognito mode)
- [ ] Click your ad
- [ ] Complete purchase
- [ ] Wait 24 hours
- [ ] Check if conversion appears

### Step 7: Contact Support (if still not working)
- [ ] Google Ads → **Help** → **Contact Support**
- [ ] Explain: "Conversion tag fires but not recording in account"
- [ ] Provide: Conversion name, test purchase date/time
- [ ] Support can check backend logs

---

## 📊 EXPECTED TIMELINE

| Action | When You'll See Results |
|--------|------------------------|
| Tag fires (Tag Assistant shows it) | Immediately |
| Conversion appears in "All conversions" | 3-24 hours |
| Conversion appears in campaign reports | 3-24 hours |
| Conversion value updates | 3-24 hours |

**Be Patient:** Even when everything is correct, Google Ads can take up to 24 hours to process conversions.

---

## 🔍 DIAGNOSTIC QUESTIONS

Answer these to narrow down the issue:

1. **When did you make the test purchase?**
   - [ ] Less than 3 hours ago → WAIT
   - [ ] 3-12 hours ago → Wait a bit longer
   - [ ] 12-24 hours ago → Should appear soon
   - [ ] More than 24 hours ago → Troubleshoot now

2. **Did you click your Google Ad before purchasing?**
   - [ ] Yes, clicked ad then purchased
   - [ ] No, went directly to website
   - If NO → Conversion won't show in ad reports (expected)

3. **What website platform are you using?**
   - [ ] Shopify
   - [ ] WooCommerce (WordPress)
   - [ ] Custom website
   - Different platforms need different tag installation

4. **Have you installed the Google Ads conversion tag?**
   - [ ] Yes, I added it myself
   - [ ] Yes, developer added it
   - [ ] Not sure / Don't think so → **THIS IS THE PROBLEM**

5. **Does Tag Assistant show the conversion tag firing?**
   - [ ] Haven't tested with Tag Assistant yet → DO THIS FIRST
   - [ ] Yes, tag fires successfully → Good, just need to wait
   - [ ] No, tag not found → Tag not installed on confirmation page

---

## 🆘 IMMEDIATE NEXT STEPS

**RIGHT NOW, do these 3 things:**

### 1️⃣ Install Google Tag Assistant (5 min)
- Chrome browser: https://chrome.google.com/webstore
- Search: "Google Tag Assistant"
- Install extension

### 2️⃣ Test Your Conversion Tag (10 min)
- Go to beliefsinwreaths.com.au
- Enable Tag Assistant
- Do a test purchase
- Check if conversion tag fires on confirmation page

### 3️⃣ Check Your Order Confirmation Page (5 min)
- Find your thank-you page URL
- View page source
- Search for: `gtag('event', 'conversion'`
- If NOT found → **Tag needs to be installed**

---

## 📝 REPORT BACK

After completing the 3 steps above, tell me:

1. **Does Tag Assistant show conversion tag firing?** (Yes/No)
2. **Does confirmation page source code have the gtag conversion code?** (Yes/No)
3. **How many hours since test purchase?** (Number)
4. **Did you click your ad before purchasing?** (Yes/No)

This will help me give you the exact fix you need.

---

## 🎯 MOST LIKELY FIX

**Based on "Google Shopping App Purchase" setup:**

**90% chance your issue is:**
❌ Conversion tag not installed on order confirmation page

**Quick Fix:**
1. Get conversion tag code from Google Ads (Tag setup section)
2. Add it to your Shopify/website order status page
3. Test with Tag Assistant
4. Do another test purchase
5. Wait 24 hours
6. Check conversions

**Need help with this?** Let me know your website platform (Shopify, WordPress, etc.) and I can provide specific installation instructions.

---

**Document Version:** 1.0  
**Last Updated:** October 4, 2025  
**Related:** CONVERSION-TRACKING-ACTION-PLAN.md, CONVERSION-TRACKING-GUIDE.md
