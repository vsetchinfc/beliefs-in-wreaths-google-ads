# 🔗 How to Verify Google Ads ↔ Google Analytics Linking

**Last Updated:** October 5, 2025  
**Google Ads UI:** Updated for new interface (2024+)  
**Purpose:** Check if Google Ads and GA4 are linked (and understand the implications)  
**Time Required:** 5 minutes

---

## 🎯 Why This Matters

**If Google Ads and GA4 are linked:**
- GA4 can send conversion data to Google Ads
- You'll see GA4 conversions imported as conversion actions
- Risk of duplicate tracking if you also have Google Ads tags

**If NOT linked:**
- Google Ads and GA4 work independently
- No duplicate conversion counting
- Each system tracks separately (usually better!)

---

## 📋 METHOD 1: Check in Google Ads (Easiest)

### Step 1: Go to Linked Accounts

1. In left sidebar, look for **"Admin"** or settings area
2. Click **"Linked accounts"** 
3. Find **"Google Analytics (GA4) & Firebase"** section

### Step 2: Check Link Status

**If Linked (You'll See):**
```
✅ Google Analytics (GA4) & Firebase
   Property: Beliefs in Wreaths Site (G-5CK5545MMJ)
   Status: Linked / Active
   Link created: [Date]
   [Details] or [Manage link] button
```

**If NOT Linked (You'll See):**
```
⚪ Google Analytics (GA4) & Firebase
   No linked properties
   [+ Link] or [Set up link] button available
```

**Note:** In the new UI, you may see cards/tiles instead of a list format.

---

## 📋 METHOD 2: Check in Google Analytics

### Step 1: Go to GA4 Admin

1. Open Google Analytics: https://analytics.google.com
2. Click **"Admin"** (gear icon) in bottom left
3. Make sure you're viewing: "Beliefs in Wreaths" property

### Step 2: Check Google Ads Links

1. In the **"Property"** column (middle), scroll down
2. Click **"Google Ads Links"**
3. You'll see a list of linked Google Ads accounts

**If Linked:**
```
✅ [Your Google Ads Account Name]
   Account ID: 123-456-7890
   Status: Active
   Link created: [Date]
```

**If NOT Linked:**
```
(Empty list)
No Google Ads accounts linked
[Link accounts] button
```

---

## 📋 METHOD 3: Check Conversion Actions (What You Can Do Now)

### Look for GA4-Sourced Conversions

1. In left sidebar, click **"Goals"** 
2. Click **"Conversions"** in the submenu
   - **OR** Tools (gear icon) → Measurement → Conversions
3. Look at the **"Source"** column for each conversion
4. Check what source each conversion has

**Note:** You may need to add the "Source" column if it's not visible:
- Click **"Columns"** icon (grid/table icon) above the data
- Select **"Modify columns"**
- Look for **"Source"** and check it
- Click **"Apply"**

**Conversion Sources:**

| Source | What It Means |
|--------|---------------|
| **Website** | Direct Google Ads tag tracking |
| **Google Analytics 4** | Imported from GA4 (means LINKED!) |
| **App** | Mobile app tracking |
| **Import** | Manual import |

---

## 🔍 ANALYZING YOUR SCREENSHOTS

Based on the conversion settings screenshot you sent earlier, let me check...

### What I See:

**Google Shopping App Purchase:**
- Conversion name: Google Shopping App Purchase
- Action optimisation: Purchases, Primary action
- Value: Use different values. If there's no value, use $0.
- **Source: Website** ← This is GOOGLE ADS direct tracking
- Count: Every conversion
- Enhanced conversions: Managed through Google tag

**This tells me:**
- ✅ This conversion uses Google Ads tag (NOT GA4 import)
- ✅ Source = "Website" = Direct Google Ads tracking
- ✅ NOT imported from GA4

### But You Also Have:

From your earlier mention of conversion list, you have:
- "Beliefs in Wreaths Site (web) purchase" with 6 conversions

**If this exists, its source is likely:**
- Source: **Google Analytics 4** ← This WOULD mean you're linked!

---

## 🎯 HOW TO CHECK YOUR SPECIFIC SETUP

### Do This Right Now:

1. **Go to:** Goals → Conversions (left sidebar)
   - Or: Tools (gear) → Measurement → Conversions
2. **Look at ALL your conversion actions** in the table
3. **For EACH conversion, check the "Source" column**
   - If column not visible: Click Columns icon → Modify columns → Add "Source"
4. **Take a screenshot of the full conversions list**

### What to Look For:

**Scenario A: All conversions show "Source: Website"**
```
✅ Google Shopping App Purchase | Website
✅ Add to Cart | Website
✅ Begin Checkout | Website
```
**Result:** NOT linked to GA4. All conversions are direct Google Ads tracking. ✅

**Scenario B: Some show "Source: Google Analytics 4"**
```
✅ Google Shopping App Purchase | Website
⚠️ Purchase | Google Analytics 4
⚠️ Begin Checkout | Google Analytics 4
```
**Result:** You ARE linked! GA4 is importing conversions. ⚠️

---

## 📸 What Screenshot Would Help

**Take a screenshot showing:**

1. **Full conversions list view:**
   - Conversion action name (column 1)
   - Source (look for this column)
   - Status
   - All conversion actions visible

2. **Or go to individual conversion:**
   - Click on "Beliefs in Wreaths Site (web) purchase" (if it exists)
   - Show the settings page
   - The "Source" field will tell us if it's GA4 import

---

## 🔍 QUICK TEST: Check Conversion Source

### Method: Click on Each Conversion

1. **Goals → Conversions** (left sidebar)
2. Click on the conversion name: **"Google Shopping App Purchase"**
3. Look for the **"Source"** field in the details page
   - Should say: **"Website"** or **"Google tag"**
4. Go back to conversions list
5. Click: **"Beliefs in Wreaths Site (web) purchase"** (if it exists)
6. Look for: **"Source"** field
   - If says: **"Google Analytics 4"** → You're linked!
   
**Note:** Source field is usually near the top of the conversion settings page, may be labeled "Source" or "Conversion source".

---

## ⚠️ SIGNS YOU'RE LINKED (Even Without Checking)

### Red Flags That Suggest Linking:

1. **You have conversions with GA4 property name in the title**
   - Example: "Beliefs in Wreaths Site (web) purchase"
   - This naming pattern = GA4 import

2. **You see duplicate purchase conversions**
   - One from Google Ads tag
   - One from GA4
   - Both tracking same purchases

3. **Conversion counts don't match actual orders**
   - If conversions = 2x actual orders
   - Likely counting each purchase twice (both systems)

4. **You see GA4 events as conversions**
   - Like: "purchase", "begin_checkout", "add_to_cart"
   - These are GA4 event names, not Google Ads convention

---

## 🎯 MY ANALYSIS OF YOUR SETUP

### From Your Tag Assistant Screenshots:

**Tags Firing:**
1. ✅ **Untitled tag (AW-10958689789)** - Google Ads
2. ✅ **Beliefs in Wreaths Site (G-5CK5545MMJ)** - GA4
3. ✅ **Shopify Channel App** - Shopify tracking

**Conversions Detected:**
1. **Google Shopping App Purchase** (×2) - Google Ads tag
2. **Purchase** - GA4 tag

**This suggests:**
- Both Google Ads AND GA4 tags are installed on your site ✅
- Both are tracking purchases ⚠️
- They might be sending duplicate data to Google Ads ⚠️

### Most Likely Scenario:

**You ARE linked**, because:
1. You have a conversion named "Beliefs in Wreaths Site (web) purchase"
2. This naming pattern matches GA4 imports
3. Tag Assistant shows both Google Ads and GA4 purchase events firing

---

## 📋 STEP-BY-STEP: Check Right Now

### 5-Minute Verification:

**Step 1: Check Linked Accounts (2 min)**
- [ ] Google Ads → Tools (gear icon) → Setup → Linked accounts
- [ ] OR: Admin → Linked accounts (in new UI)
- [ ] Look for "Google Analytics (GA4) & Firebase" card/section
- [ ] Is there a linked property? Screenshot it.

**Step 2: Check Conversion Sources (2 min)**
- [ ] Google Ads → Goals → Conversions (left sidebar)
- [ ] Look at "Source" column for each conversion
  - If not visible: Columns icon → Modify columns → Add "Source"
- [ ] Do any say "Google Analytics 4"? Screenshot it.

**Step 3: Report Back (1 min)**
- [ ] Tell me: Are you linked? (Yes/No)
- [ ] How many conversions have "Source: Google Analytics 4"?
- [ ] Send screenshot of conversions list

---

## 🔧 IF YOU ARE LINKED: How to Unlink

### Why Unlink:
- Prevents duplicate conversion counting
- Google Ads direct tracking is usually better
- Simpler, cleaner setup

### How to Unlink:

**Option A: From Google Ads (New UI)**
1. Tools (gear icon) → Setup → Linked accounts
   - OR: Admin → Linked accounts
2. Find **"Google Analytics (GA4) & Firebase"** card/section
3. Click **"Details"**, **"Manage link"**, or the property name
4. Look for **"Unlink"** or **"Remove link"** button
5. Confirm unlinking in the popup

**Option B: From Google Analytics**
1. GA4 → Admin (gear icon in bottom left) → Property column
2. Scroll down and click **"Google Ads Links"**
3. Find your Google Ads account in the list
4. Click the three dots (⋮) menu on the right
5. Select **"Remove link"** or **"Delete link"**
6. Confirm removal

**What Happens After Unlinking:**
- GA4 stops sending conversion data to Google Ads
- Google Ads conversions still work (via its own tag)
- GA4 still tracks everything (for analytics)
- No more duplicate counting

---

## ✅ RECOMMENDED SETUP

### Best Practice:

**USE ONLY ONE CONVERSION SOURCE:**

**Option 1: Google Ads Direct Tracking (Recommended)**
```
✅ Keep: Google Ads tag on website
✅ Keep: Google Shopping App Purchase (PRIMARY)
❌ Unlink: GA4 from Google Ads
✅ Keep: GA4 running (for analytics)
```

**Why:** Faster, more accurate for Google Ads optimization

**Option 2: GA4 Import Only (Alternative)**
```
❌ Remove: Google Ads conversion tag
✅ Link: GA4 to Google Ads
✅ Import: GA4 purchase events
✅ Use: GA4 as single source of truth
```

**Why:** Unified analytics across all platforms

---

## 🎯 NEXT STEPS FOR YOU

### 1. Verify Link Status (Do This First!)

**Quick Check:**
- [ ] Google Ads → Tools (gear icon) → Linked accounts
- [ ] OR: Admin → Linked accounts (new UI)
- [ ] Is GA4 linked? (Yes/No)

### 2. If Linked → Choose Action

**Option A: Unlink and Use Google Ads Tracking**
- Unlink GA4 from Google Ads
- Keep Google Ads conversion tag
- Remove/disable GA4 imported conversions

**Option B: Keep Link but Remove Duplicates**
- Keep GA4 link
- Remove Google Ads conversion tag from website
- Use only GA4 imports

### 3. Clean Up Conversions

After deciding, remove duplicate conversion actions.

---

## 📞 TELL ME YOUR RESULTS

**After checking, tell me:**

1. **Are you linked?**
   - Go to: Tools → Linked accounts (OR Admin → Linked accounts)
   - Is "Google Analytics (GA4) & Firebase" showing as linked?
   - YES / NO / NOT SURE

2. **What sources do your conversions show?**
   - Go to: Goals → Conversions (left sidebar)
   - Look at "Source" column (add it via Columns if needed)
   - What does each conversion say?

3. **Which setup do you prefer?**
   - Google Ads direct tracking only? (Recommended)
   - GA4 import only?
   - Not sure / need advice?

Once you tell me, I can give you exact steps to fix your setup! 🎯

---

## 🎯 QUICK REFERENCE (New UI)

### Check if Linked
`Google Ads → Tools (gear) → Setup → Linked accounts → Look for "Google Analytics (GA4) & Firebase"`

### Check Conversion Sources
`Goals (left sidebar) → Conversions → View "Source" column (add via Columns icon if needed)`

### Unlink GA4
`Tools → Linked accounts → GA4 card → Details/Manage → Unlink button`

---

**Document Version:** 2.0  
**Last Updated:** October 5, 2025  
**UI Version:** New Google Ads interface (2024+)  
**Related:** CONVERSION-TRACKING-ACTION-PLAN.md, TROUBLESHOOTING-CONVERSION-NOT-COUNTED.md
