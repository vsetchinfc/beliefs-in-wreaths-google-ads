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





# 🔧 CONVERSION TRACKING SETUP & FIX GUIDE
## Complete Step-by-Step Instructions for Beliefs in Wreaths

**Last Updated:** October 4, 2025  
**Difficulty:** Intermediate  
**Time Required:** 1-2 hours  
**Prerequisites:** Admin access to Google Ads account

---

## 📚 TABLE OF CONTENTS

1. [Understanding Conversion Tracking](#understanding)
2. [How to Access Conversions](#access)
3. [How to Edit Conversion Actions](#edit)
4. [How to Remove Conversions](#remove)
5. [How to Set Primary vs Secondary](#primary-secondary)
6. [How to Fix "Needs Attention"](#fix-warnings)
7. [How to Test Tracking](#test)
8. [Troubleshooting Common Issues](#troubleshooting)

---

## 🎓 UNDERSTANDING CONVERSION TRACKING {#understanding}

### What is a Conversion?

A **conversion** is a valuable action someone takes on your website after clicking your ad:
- ✅ **Purchase** (most important!)
- ✅ **Add to Cart**
- ✅ **Begin Checkout**
- ✅ **Phone Call**
- ✅ **Contact Form Submit**

### Why It Matters

**Without conversion tracking:**
- ❌ Can't measure ROI
- ❌ Don't know which keywords drive sales
- ❌ Can't optimize bids effectively
- ❌ Flying blind!

**With conversion tracking:**
- ✅ See exactly which keywords = sales
- ✅ Calculate real ROAS
- ✅ Google can optimize bids automatically
- ✅ Make data-driven decisions

### Primary vs Secondary Conversions

**PRIMARY Conversion:**
- The MAIN action you want (Purchase!)
- Google optimizes bids to get MORE of these
- Appears in "Conversions" column
- **You should have only 1 PRIMARY**

**SECONDARY Conversion:**
- Useful to track, but don't optimize for it
- Examples: Add to Cart, Page Views
- Appears in "All conversions" column
- Doesn't affect bid optimization
- Can have multiple SECONDARY conversions

### Conversion Counting

**One:** Count only first conversion per click
- Best for: Purchases (one sale per customer)
- Prevents: Counting same sale multiple times

**Every:** Count all conversions per click
- Best for: Phone calls, leads (can have multiple)
- Use carefully: Can inflate numbers

---

## 🔍 HOW TO ACCESS CONVERSIONS {#access}

### Step 1: Log into Google Ads
- Go to: https://ads.google.com
- Sign in with your account

### Step 2: Navigate to Conversions
1. In the left sidebar menu, click **"Goals"**
2. Click **"Conversions"** in the submenu
   - OR look for **"Conversions"** directly in left sidebar (depending on account setup)

**Alternative path:**
1. Click **"Tools"** icon (wrench/gear icon) in top navigation
2. Under **"Measurement"** section
3. Click **"Conversions"**

### What You'll See

**Main Conversions Page:**
- Table with all conversion actions listed
- Columns: 
  - Conversion action name
  - Category (Purchase, Submit lead form, etc.)
  - Source (Google Analytics, Google Ads tag, etc.)
  - Status (Active, Removed, etc.)
- Top section shows summary metrics for different conversion categories

**Summary Cards (Top of page):**
- Different categories: Sales, Leads, etc.
- Each card shows:
  - Number of conversions
  - Total conversion value
  - Conversion rate

---

## ✏️ HOW TO EDIT CONVERSION ACTIONS {#edit}

### Step 1: Find the Conversion

1. Go to: **Goals → Conversions** (left sidebar)
2. Find the conversion in the table
3. Click on the **conversion name** (it's a clickable link)

**OR use the 3-dot menu:**
1. Hover over the conversion row
2. Click the **three dots (⋮)** on the right side
3. Select **"Edit settings"**

### Step 2: Edit Settings

You'll see the conversion details page with various settings:

**Key Settings to Check/Change:**

**A. Goal and action optimization** (or "Action optimization")
```
Options: Primary | Secondary

Primary = Optimize bids for this conversion
Secondary = Track but don't optimize

Your Setup:
- Purchase → PRIMARY (only 1!)
- Add to Cart → SECONDARY
- Begin Checkout → SECONDARY
```

**How to change:**
1. Find the **"Goal and action optimization"** section
2. Look for dropdown or toggle options
3. Select **"Primary"** or **"Secondary"**
4. Scroll down, click **"Save"** or **"Done"** button

---

**B. Count**
```
Options: One | Every

One = Count first conversion only (best for purchases)
Every = Count all conversions (best for leads/calls)

Your Setup:
- Purchase → ONE
- Add to Cart → ONE
- Phone Calls → EVERY (if you keep them)
```

**How to change:**
1. Scroll to the **"Count"** section
2. Select **"One"** or **"Every"** from dropdown/radio buttons
3. Click **"Save"** or **"Done"**

---

**C. Value**
```
Options: 
- Use different values for each conversion (transaction-specific)
- Use the same value for each conversion (e.g., $150)
- Don't use a value

Your Setup:
- Purchase → Use transaction-specific value
- Add to Cart → Don't use a value (or same value)
```

**How to set:**
1. Find the **"Value"** section
2. Choose the value method from options
3. If "Use the same value": Enter amount (e.g., $150)
4. Click **"Save"** or **"Done"**

---

**D. Attribution model**
```
Options:
- Last click (default, most common)
- Data-driven (needs 300+ conversions/month)
- First click, Linear, Time decay, Position-based

Your Setup:
- Use "Last click" (simplest, standard)
```

**Note:** In new UI, this may be under an **"Advanced settings"** section or separate tab.

---

### Step 3: Save Changes

- Review all your changes
- Scroll to bottom of the page
- Click **"Save"** or **"Done"** button
- You'll return to the conversions list

---

## 🗑️ HOW TO REMOVE CONVERSIONS {#remove}

### When to Remove

Remove conversions that are:
- ❌ Not tracking anything (0 conversions for months)
- ❌ Duplicates (two tags tracking same action)
- ❌ Not useful (page views when you only care about sales)
- ❌ Broken/not working

### Method 1: Remove Conversion Action

**Step 1: Access the Conversion**
1. Go to: **Goals → Conversions** (left sidebar)
2. Find the conversion in the table

**Step 2: Remove Using 3-Dot Menu**
1. Hover over the conversion row
2. Click the **three dots (⋮)** on the right side
3. Select **"Remove"** from dropdown menu
4. Confirm removal in popup dialog
5. Conversion status will change to **"Removed"**

**Alternative - Remove from Edit Page:**
1. Click on conversion name to open details
2. Scroll to bottom of settings page
3. Look for **"Remove"** button or link
4. Click and confirm removal

**Note:** Removed conversions don't delete historical data, just stop tracking new ones. They'll still appear in reports with status "Removed".

---

### Method 2: Change Status (Alternative)

If you want to pause it temporarily instead of removing:

1. Find the conversion in the list
2. Click the **three dots (⋮)** menu
3. Select **"Pause"** or **"Disable"** (if available)
   - **Note:** Not all conversion sources allow pausing
4. Or open conversion settings and look for status toggle
5. Save changes

---

## 🎯 HOW TO SET PRIMARY VS SECONDARY {#primary-secondary}

### The Rule: Only 1 PRIMARY Conversion

**Your Setup Should Be:**
```
PRIMARY (1):
✅ Google Shopping App - Purchase

SECONDARY (2-4):
⚪ Google Shopping App - Add To Cart
⚪ Google Shopping App - Begin Checkout
⚪ Add Payment Info (optional)

REMOVED (8+):
❌ All others
```

### How to Change Goal and Action Optimization

**Step 1: Edit the Conversion**
1. Go to: **Goals → Conversions** (left sidebar)
2. Click on the conversion name to open settings

**Step 2: Find "Goal and action optimization"**
- Look for section labeled **"Goal and action optimization"**
- It's usually near the top of the settings page
- You'll see options: **Primary** | **Secondary**

**Step 3: Select Optimization Level**

**For Purchase Conversion:**
```
Goal and action optimization: Primary ← SELECT THIS
```

**For Add to Cart, Begin Checkout:**
```
Goal and action optimization: Secondary ← SELECT THIS
```

**Step 4: Save**
- Scroll to bottom
- Click **"Save"** or **"Done"** button
- Repeat for each conversion you need to change

---

### How to Verify Primary Settings

**Check Campaign View:**
1. Click **"Campaigns"** in the left sidebar
2. Look at the **"Conversions"** column in the table
3. This should show ONLY primary conversions (Purchases)

**Check "All Conversions" Column:**
1. Stay on Campaigns view
2. Look for the **"All conversions"** column
3. This shows: Primary + Secondary conversions combined

**If columns are missing:**
1. Look for the **"Columns"** icon (table/grid icon) above the data table
2. Click **"Columns"** → Select **"Modify columns"**
3. In the side panel, expand **"Conversions"** section
4. Check/add these columns:
   - ✅ **Conversions** (Primary only)
   - ✅ **All conversions** (Primary + Secondary)
   - ✅ **Conversion value** (optional)
5. Click **"Apply"** button

---

## ⚠️ HOW TO FIX "NEEDS ATTENTION" {#fix-warnings}

### What "Needs Attention" Means

Common issues:
- 🔴 Conversion tag not firing
- 🔴 Tag configuration mismatch
- 🔴 Duplicate tags on website
- 🔴 Tag ID doesn't match
- 🔴 Not receiving conversions recently

### How to Troubleshoot

**Step 1: Identify the Issue**
1. Go to: **Goals → Conversions** (left sidebar)
2. Find conversions with warning icons or "Needs attention" in Status column
3. Click on the conversion name

**Step 2: View Diagnostics**
- On the conversion details page, look for:
  - **Status banner** at top (may show warnings/errors)
  - **"View details"** or **"Learn more"** links
  - **Alert/warning icons** with hover text

**Step 3: Use Troubleshooting Tools**
- Some conversions have a **"Troubleshoot"** button or link
- Click it to see specific diagnostics
- Google will show specific issues:
  - "Tag not detected on your website" → Reinstall tag
  - "Duplicate conversion actions" → Remove one
  - "Tag ID mismatch" → Update tag code
  - "No recent conversions" → May be normal if no sales

---

### Common Fix: Update Conversion Tag

**Step 1: Get Correct Tag Code**
1. Open the conversion action (click on conversion name)
2. Look for the **"Tag setup"** section (may need to scroll)
3. Click **"Set up tag"** or **"View tag setup instructions"** button
4. Select: **"Install the tag yourself"** or **"Use Google tag"**
5. You'll see:
   - **Google tag** (gtag.js) - Global site tag
   - **Event snippet** - Conversion-specific code
6. Copy both code snippets

**Step 2: Verify Tag on Website**
1. Go to your thank-you/confirmation page
2. Right-click → **"View Page Source"**
3. Search (Ctrl+F) for: `gtag`
4. Check if conversion ID matches

**Example of correct tag:**
```javascript
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=AW-XXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'AW-XXXXXXXXX');
</script>

<!-- Event snippet for Purchase conversion -->
<script>
  gtag('event', 'conversion', {
      'send_to': 'AW-XXXXXXXXX/AbC123dEf',
      'value': 150.00,
      'currency': 'AUD',
      'transaction_id': ''
  });
</script>
```

**Step 3: Update Tag (if needed)**
- Give updated code to website developer, OR
- If using Shopify: Add to Settings → Checkout → Order status page
- If using WordPress: Add to thank-you page template

---

### Use Google Tag Assistant

**Install Extension:**
1. Chrome browser → chrome.google.com/webstore
2. Search: "Google Tag Assistant"
3. Install extension

**Test Your Tags:**
1. Go to your website
2. Click Tag Assistant icon → "Enable"
3. Refresh page
4. Complete a test purchase
5. On thank-you page, check Tag Assistant
6. Should show: ✅ "Google Ads Conversion Tracking" tag fired

---

## 🧪 HOW TO TEST TRACKING {#test}

### Method 1: Test Purchase (Most Reliable)

**Step 1: Note Current Count**
1. Tools & Settings → Conversions
2. Note current count for "Purchase" conversion
3. Example: Currently shows "7 conversions"

**Step 2: Make Test Purchase**
- Go to beliefsinwreaths.com.au
- Add item to cart
- Complete checkout
- Use real payment OR ask client to do test order
- Make note of order time/ID

**Step 3: Wait**
- Conversions can take **3-24 hours** to appear
- Usually appear within 3 hours
- Be patient!

**Step 4: Check Google Ads**
- After 24 hours, go to: Tools → Conversions
- Check "Purchase" conversion count
- Should now show: "8 conversions" (+1)
- If it shows = ✅ **TRACKING WORKS!**

---

### Method 2: Google Tag Assistant (Instant)

**Step 1: Install Tag Assistant**
- Chrome extension (see "Fix Needs Attention" section above)

**Step 2: Enable Tag Assistant**
1. Go to beliefsinwreaths.com.au
2. Click Tag Assistant icon
3. Click **"Enable"**
4. Refresh page

**Step 3: Simulate Purchase**
1. Add item to cart
2. Go through checkout
3. Reach thank-you/confirmation page
4. Click Tag Assistant icon

**Step 4: Check Tag Status**

**Should see:**
```
✅ Google Ads Conversion Tracking
   Conversion ID: AW-XXXXXXXXX
   Conversion Label: AbC123dEf
   Status: Tag fired successfully
   Value: 150.00
   Currency: AUD
```

**If you see this = Tag is working!** ✅

**If you see errors:**
- 🔴 "Tag not found" → Tag not installed
- 🔴 "Tag error" → Tag configuration issue
- 🔴 "Duplicate tags" → Multiple tags firing

---

### Method 3: Check Recent Conversions Report

**Step 1: View Conversion Details**
1. Go to: **Goals → Conversions** (left sidebar)
2. Click on the conversion name: "Purchase"
3. Look at the performance graph/chart at top
4. Use the **date range selector** (top right) to select **"Last 7 days"**

**Step 2: Analyze the Data**
- Do you see any conversions in the last week?
- Check the graph for conversion spikes
- Look at the data table below the graph
- If conversions showing = Tracking is active ✅
- If zero = Either no sales OR tracking issue

**Step 3: Cross-Reference with Actual Sales**
- Ask client: "Did we have any sales in last 7 days?"
- Check Shopify/website admin for actual orders
- **If actual sales exist but Google Ads shows zero** = Tracking broken
- **If no actual sales** = Tracking might be fine, just no conversions yet

---

## 🔧 TROUBLESHOOTING COMMON ISSUES {#troubleshooting}

### Issue 1: Zero Conversions Showing

**Possible Causes:**
1. No actual sales on website
2. Conversion tag not installed
3. Tag on wrong page
4. Tag broken/misconfigured

**How to Fix:**

**A. Verify Sales Are Happening**
- Check with client: "Any recent orders?"
- Check website admin/Shopify: Order history
- If no orders = Can't track what doesn't exist!

**B. Check Tag Installation**
1. View page source on thank-you page
2. Search for: `gtag('event', 'conversion'`
3. If NOT found = Tag not installed
4. See: "How to Fix Needs Attention" section above

**C. Verify Tag Location**
- Tag must be on **ORDER CONFIRMATION page**
- Not on: Homepage, product pages, cart page
- Only fires after successful purchase

---

### Issue 2: Duplicate Conversions

**Symptoms:**
- Same conversion counted 2x
- Have multiple purchase tracking actions
- Numbers don't match actual sales

**Causes:**
- Both Google Ads tag AND GA4 tracking same purchase
- Multiple conversion actions for same event
- Tag firing twice on same page

**How to Fix:**

**Option A: Remove Duplicate (Recommended)**
1. Identify which conversion is duplicate
2. Remove or disable the duplicate
3. Keep only 1 purchase conversion as PRIMARY

**Option B: Set Duplicate to Secondary**
1. Keep both conversions
2. Set one to PRIMARY (optimize for this)
3. Set other to SECONDARY (track only)
4. Note: Reports will show both, but bids optimize for PRIMARY only

---

### Issue 3: "Needs Attention" Won't Go Away

**Tried "Troubleshoot" but still shows warning:**

**Step 1: Verify Tag is Current**
1. Get latest tag code from Google Ads
2. Compare to tag on website
3. Conversion ID must match exactly
4. Update if different

**Step 2: Remove Duplicate Tags**
- Check page source for multiple `gtag` tags
- Should only have ONE global site tag
- Can have multiple event snippets (for different conversions)

**Step 3: Wait 48 Hours**
- After fixing, warning can take 24-48 hours to clear
- Generate a test conversion
- If conversion shows up, tracking works (ignore warning)

**Step 4: Contact Google Support**
- If still showing after 48 hours
- Google Ads → Help → Contact Support
- Explain: "Fixed tag but 'Needs attention' won't clear"

---

### Issue 4: Conversion Value is $0.00

**Symptoms:**
- Conversions tracked: ✅
- Conversion value: $0.00

**Causes:**
- Value not configured in conversion action
- Tag not passing transaction value
- Using "Don't use a value" setting

**How to Fix:**

**Method A: Set Same Value for All**
1. Edit conversion action
2. Find "Value" setting
3. Select: "Use the same value for each conversion"
4. Enter: Average order value (e.g., $150)
5. Save

**Method B: Pass Transaction-Specific Value**
1. Edit conversion action
2. Select: "Use different values for each conversion"
3. Update event snippet on website to pass value:
```javascript
gtag('event', 'conversion', {
    'send_to': 'AW-XXXXXXXXX/AbC123dEf',
    'value': transaction_value, // Dynamic value from order
    'currency': 'AUD',
    'transaction_id': order_id
});
```
4. Developer help needed for dynamic value

---

### Issue 5: Conversions Delayed or Not Real-Time

**Normal Behavior:**
- Conversions typically appear within **3 hours**
- Can take up to **24 hours**
- Not instant!

**If >24 hours:**
- Check tag is firing (Tag Assistant)
- Verify conversion action is "Active"
- Do another test purchase
- Contact support if persists

---

## 📋 CONVERSION TRACKING CHECKLIST

### Initial Setup
- [ ] 1 PRIMARY conversion: Purchase
- [ ] 2-4 SECONDARY conversions: Micro-conversions
- [ ] All duplicates removed
- [ ] All 0-conversion actions removed
- [ ] "Needs attention" warnings fixed

### Tag Installation
- [ ] Tag installed on order confirmation page
- [ ] Tag ID matches Google Ads
- [ ] No duplicate tags
- [ ] Tested with Tag Assistant
- [ ] Test purchase completed

### Configuration
- [ ] Action optimisation: PRIMARY (Purchase only)
- [ ] Count: ONE (for Purchase)
- [ ] Value: Transaction-specific OR same value set
- [ ] Attribution: Last click
- [ ] Campaigns: Correct campaigns included

### Verification
- [ ] Test conversion appeared in 3-24 hours
- [ ] "Conversions" column shows purchases only
- [ ] "All conversions" shows PRIMARY + SECONDARY
- [ ] No warnings in conversions list
- [ ] Numbers match actual sales (ask client)

---

## 🎯 QUICK REFERENCE

### Access Conversions
`Google Ads → Goals (left sidebar) → Conversions`  
**OR**  
`Google Ads → Tools icon → Measurement → Conversions`

### Edit Conversion
`Goals → Conversions → Click conversion name → Edit settings → Save/Done`  
**OR**  
`Hover over conversion → Three dots (⋮) → Edit settings`

### Remove Conversion
`Goals → Conversions → Hover over row → Three dots (⋮) → Remove → Confirm`  
**OR**  
`Click conversion name → Scroll to bottom → Remove → Confirm`

### Set Primary/Secondary
`Goals → Conversions → Click conversion name → Goal and action optimization section → Select Primary or Secondary → Save`

### Fix "Needs Attention"
`Goals → Conversions → Click conversion with warning → View diagnostics → Follow recommendations`

### Test Tracking
`Google Tag Assistant extension → Enable → Complete purchase → Check tag fired`

### View Conversion Columns in Reports
`Campaigns → Columns icon → Modify columns → Conversions section → Add "Conversions" and "All conversions" → Apply`

---

## 📞 NEED MORE HELP?

**Resources:**
- Google Ads Help: https://support.google.com/google-ads/answer/1722022
- Tag Assistant: Chrome web store
- Community: Google Ads Community forum

**Professional Help:**
- Google Ads Support: In-account chat/phone
- Web Developer: For tag installation
- Google Ads Specialist: For advanced setup

---

**Document Version:** 1.0  
**Last Updated:** October 4, 2025  
**Related:** CONVERSION-TRACKING-ACTION-PLAN.md
