## 🔍 How to Verify Conversion Tracking

### Method 1: Google Ads Interface (Easiest)

**Step 1: Check if Conversion Action Exists**
1. In Google Ads, in the left sidebar click **"Goals"**
2. Click **"Conversions"** in the submenu
   - **OR** click **"Tools"** icon (gear) → **"Measurement"** → **"Conversions"**
3. Look for a conversion action (e.g., "Purchase", "Buy Now", "Order")
4. **Status should show:** "Active" and recording conversions (not "No recent conversions")

**Step 2: Check Campaign Conversion Column**
1. In left sidebar, click **"Campaigns"**
2. Click **"Columns"** icon (looks like a table/grid) above the data table
3. Select **"Modify columns"**
4. Expand the **"Conversions"** section in the side panel
5. Check/add: "Conversions", "Conv. rate", "Cost / conv."
6. Click **"Apply"**
7. **If tracking works:** You'll see numbers appear in these columns after purchases

---

### Method 2: Google Tag Assistant (Most Reliable)

**Before a Real Purchase:**
1. Install **Google Tag Assistant** Chrome extension
2. Go to your website: https://beliefsinwreaths.com.au/
3. Click the Tag Assistant icon → **"Enable"** → Refresh page
4. Add item to cart → Go through checkout → Complete order
5. On thank-you page, check Tag Assistant:
   - ✅ Should show: "Google Ads Conversion Tracking" tag fired
   - ✅ Conversion ID and Label should appear

**What you're looking for:**
```
✅ Google Ads Conversion Tracking
   Conversion ID: AW-XXXXXXXXXX
   Conversion Label: abc123xyz
   Status: Tag fired successfully
```

---

### Method 3: Test Conversion (Recommended!)

**Do a Test Purchase:**
1. **Before testing:** Note current conversion count in Google Ads
2. **Make a real purchase** on your website (or ask client to)
3. **Wait 3-24 hours** (conversions can take time to show)
4. **Check Google Ads:**
   - Go to **Goals** → **Conversions** (left sidebar)
   - Click on your conversion action name
   - Look at the performance graph → Should show +1 conversion
5. **Check Campaign view:**
   - Go to **Campaigns** in left sidebar
   - Should see +1 in "Conversions" column

**If it shows up = Tracking works!** ✅

---

### Method 4: Check Source Code (Technical)

**On Thank-You Page:**
1. Go to your order confirmation/thank-you page URL
2. Right-click → **"View Page Source"**
3. Search (Ctrl+F) for: `gtag` or `conversion`
4. **Should see code like this:**

```javascript
<!-- Google Ads Conversion Tracking -->
<script>
gtag('event', 'conversion', {
    'send_to': 'AW-XXXXXXXXX/abc123xyz',
    'value': 150.00,
    'currency': 'AUD',
    'transaction_id': ''
});
</script>
```

**If you see this code = Tag is installed** ✅  
**If NOT there = Need to install it** ❌

---

### Method 5: Google Analytics 4 (If Integrated)

**If using GA4:**
1. Go to **Google Analytics** → **Reports** → **Acquisition** → **Traffic acquisition**
2. Look for **"google / cpc"** as a source
3. Click on it → Check if **"purchase"** events are tracked
4. **If GA4 linked to Google Ads:** Conversions should import automatically

---

## 🚨 Common Issues & Fixes

### Issue 1: "No conversions recorded"
**Possible causes:**
- Tag not installed on thank-you page
- Tag installed but missing conversion ID/label
- Conversion action not set up in Google Ads

**Fix:** Follow guide: setup-conversion-tracking.md

---

### Issue 2: Conversions show in GA4 but not Google Ads
**Cause:** GA4 not linked to Google Ads

**Fix:**
1. Google Ads → **Tools** (gear icon) → **Setup** → **Linked accounts**
   - **OR** in left sidebar → **Admin** → **Linked accounts**
2. Find **Google Analytics** → Click **"Link"** or **"Details"**
3. Import GA4 "purchase" event as conversion action

---

### Issue 3: Tag fires but no conversion shows
**Cause:** Wrong conversion ID or label

**Fix:**
1. Google Ads → **Goals** → **Conversions** (OR **Tools** → **Conversions**)
2. Click your conversion action name
3. Look for **"Tag setup"** or **"Set up tag"** section
4. Click **"View tag setup instructions"** or **"Set up tag"**
5. Copy the exact **tag code** provided (Global tag + Event snippet)
6. Replace existing code on thank-you page with correct code

---

## ✅ Quick Verification Checklist

**Right now, check these 3 things:**

```
[ ] 1. Google Ads → Goals → Conversions (OR Tools → Conversions) → Do you see a conversion action?
[ ] 2. Do a test purchase → Wait 3-24 hrs → Check if conversion shows up
[ ] 3. View thank-you page source code → Search for "gtag" or "conversion"
```

**If all 3 = YES** → Tracking works! ✅  
**If any = NO** → Need to set up tracking ⚠️

---

## 📝 What to Do If Not Set Up Yet:

1. **Read the guide:** setup-conversion-tracking.md
2. **You'll need:**
   - Access to website admin/Shopify
   - Ability to edit thank-you page code
   - Or developer to help install
3. **Install this weekend** (Priority #1!)
4. **Test with a purchase**
5. **Verify it shows in Google Ads**

---

**Want me to check if it's set up now?** 

Tell me:
1. Do you see a "Conversions" column in your Google Ads campaign view?
2. When you go to Tools → Conversions, what do you see?