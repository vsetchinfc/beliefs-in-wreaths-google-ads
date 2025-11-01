# Google Ads → GA4 Tracking Diagnostic Guide

**Problem:** Google Ads shows 13 clicks (Oct 28), but GA4 shows only 1 paid search session.

**Potential causes:**
1. Google Ads not linked to GA4
2. Missing/broken UTM parameters
3. GA4 tracking code missing on landing pages
4. Click fraud / bot traffic
5. Users bouncing before GA4 loads

---

## 🔍 Step 1: Verify Google Ads ↔ GA4 Link

### **In Google Ads (New UI):**

1. Click **Goals** icon in the left navigation menu (looks like a target 🎯)
2. Click **Conversions** in the submenu
3. Look for **"Google Analytics 4 properties"** section at the top
4. Check status:
   - ✅ **Shows property name "Beliefs in Wreaths Site"** with link status = GOOD
   - ❌ **"Connect to Google Analytics 4"** button visible = NOT LINKED

**Alternative path:**
1. Click **Tools** icon (wrench 🔧) in top right corner
2. Under **Setup**, click **Linked accounts**
3. Find **Google Analytics (GA4)** card
4. Check status: **Linked** or **Not linked**

**If NOT linked:**
1. Click **Link** or **Details** button
2. Select your GA4 property: **"Beliefs in Wreaths Site"**
3. Toggle these settings **ON**:
   - ☑️ **Personalized advertising** (import audiences from GA4)
   - ☑️ **Import site metrics** (get bounce rate, engagement data)
   - ☑️ **Enable auto-tagging** (automatically add GCLID to URLs)
4. Click **Link** or **Save**
5. Wait 24-48 hours for data to flow properly

---

### **In Google Analytics (GA4):**

1. Click **Admin** (gear icon ⚙️ bottom left corner)
2. In the **Property** column (middle), click **Google Ads Links**
3. Check if you see your Google Ads account listed
4. Status should show: **Link active** with green dot 🟢

**If NOT linked:**
1. Click **Link** button (top right)
2. Select **Choose Google Ads accounts**
3. Check the box next to your account
4. Click **Confirm**
5. In the link configuration:
   - Toggle **ON**: Enable personalized advertising
   - Toggle **ON**: Auto-tagging
6. Click **Next** → **Submit**
7. Wait 24 hours for link to activate

---

## 🔍 Step 2: Check Auto-Tagging (GCLID)

### **What is GCLID?**
When someone clicks your Google Ad, Google automatically adds `?gclid=xxxxx` to the URL. This tells GA4 the traffic came from Google Ads.

### **Verify Auto-Tagging is ON:**

**Option 1: Via Account Settings (New UI)**
1. Click **Settings** icon (gear ⚙️) in top right
2. Click **Account settings** in the dropdown
3. Scroll down to **Auto-tagging** section
4. Look for: **"Tag the URL that people click through from my ad"**
5. Should show: **ON** (toggle should be blue/enabled)

**Option 2: Via Tools Menu**
1. Click **Tools** icon (wrench 🔧) in top right
2. Under **Setup** section, click **Preferences**
3. Expand **Tracking** section
4. Find **Auto-tagging**
5. Should show: ☑️ **Tag the URL that people click through from my ad**

**If disabled:**
1. Click the toggle to turn it **ON**
2. Optionally enable: **"Allow auto-tagging to override manual tagging"**
3. Click **Save**
4. Wait 1 hour for changes to take effect

---

### **Test if GCLID is Working:**

**Method 1: Ad Preview Tool (Recommended)**
1. In Google Ads, click **Campaigns** in left navigation
2. Select your campaign: **B-in-W [Search | Sales]**
3. Click **Ads** tab
4. Find any active ad
5. Click the **Preview** icon (eye 👁️) next to the ad
6. Select **Mobile** or **Desktop** preview
7. When the preview loads, look at the URL
8. Should show:
   ```
   https://beliefsinwreaths.com.au/collections/christmas-wreaths?gclid=Cj0KCQiA...
   ```

**Method 2: Search Your Own Ad**
1. Google search: `christmas wreaths australia`
2. Look for your ad (may need to scroll)
3. **Right-click** your ad → **Copy link address**
4. Paste into notepad
5. Look for `gclid=` parameter

**If you see `?gclid=` or `&gclid=`** = ✅ Auto-tagging works
**If NO gclid parameter** = ❌ Auto-tagging broken (go back to Step 2)

---

## 🔍 Step 3: Check UTM Parameters (Backup Tracking)

### **Current Final URLs in Your Ads:**

Looking at your ad report, all 3 active ads use:
- `https://beliefsinwreaths.com.au/collections/christmas-wreaths`
- `https://beliefsinwreaths.com.au/collections/christmas-candle-holders-centrepieces`

**Problem:** No UTM parameters!

### **What You Should Add:**

UTM parameters are backup tracking (in case GCLID fails). They tell GA4:
- Where traffic came from (source)
- Which campaign (campaign name)
- What medium (CPC, paid search, etc.)

### **Recommended UTM Format:**

```
https://beliefsinwreaths.com.au/collections/christmas-wreaths?utm_source=google&utm_medium=cpc&utm_campaign=christmas_wreaths_search&utm_term={keyword}&utm_content={creative}
```

**Parameters explained:**
- `utm_source=google` → Traffic from Google
- `utm_medium=cpc` → Paid (cost-per-click)
- `utm_campaign=christmas_wreaths_search` → Campaign name
- `utm_term={keyword}` → Which keyword triggered ad (dynamic)
- `utm_content={creative}` → Which ad variation (dynamic)

---

### **How to Add UTM Parameters to Google Ads:**

#### **Option A: Edit Individual Ads (New UI)**

1. Click **Campaigns** in left navigation
2. Click **Ads** tab at the top
3. Check the box next to the ad you want to edit
4. Click **Edit** button (pencil icon) that appears
5. In the **Final URL** field, add your UTM parameters
6. Click **Save**
7. Repeat for all active ads

#### **Option B: Bulk Edit (Faster for Multiple Ads)**

1. Click **Campaigns** → **Ads** tab
2. Check boxes for all ads you want to edit
3. Click **Edit** dropdown → **Change URLs**
4. Select **Final URL**
5. Choose **Replace** operation
6. Enter your new URL with UTM parameters
7. Click **Apply**

#### **Option C: Use Account-Level Tracking Template (Recommended)**

**This automatically adds UTMs to ALL ads:**

1. Click **Settings** (gear ⚙️) in top right
2. Click **Account settings**
3. Scroll to **Tracking** section
4. Click **Tracking template** field
5. Enter:
   ```
   {lpurl}?utm_source=google&utm_medium=cpc&utm_campaign={campaignid}&utm_term={keyword}&utm_content={creative}
   ```
6. Click **Test** to verify (should show "Valid")
7. Click **Save**
8. **All ads now automatically get UTM parameters!**

**Note:** `{lpurl}` preserves your existing final URL
- `{campaignid}` = Campaign ID number
- `{keyword}` = Keyword that triggered ad
- `{creative}` = Ad variation ID

**Important:** Keep GCLID enabled. UTMs are BACKUP tracking.

---

## 🔍 Step 4: Verify GA4 Code on Landing Pages

### **Check if GA4 is Installed:**

1. **Visit your collection pages:**
   - https://beliefsinwreaths.com.au/collections/christmas-wreaths
   - https://beliefsinwreaths.com.au/collections/christmas-candle-holders-centrepieces

2. **Open browser developer tools:**
   - **Chrome/Edge:** Press `F12` or `Ctrl+Shift+I`
   - **Firefox:** Press `F12`
   - **Safari:** `Cmd+Option+I`

3. **Go to Console tab**

4. **Type this command and press Enter:**
   ```javascript
   dataLayer
   ```

5. **Check output:**
   - ✅ **Shows array with events** = GA4 is working
   - ❌ **"dataLayer is not defined"** = GA4 NOT installed

---

### **Alternative: Use Google Tag Assistant**

1. **Install Chrome extension:** [Google Tag Assistant](https://chrome.google.com/webstore/detail/tag-assistant-legacy-by-g/kejbdjndbnbjgmefkgdddjlbokphdefk)

2. **Visit your collection page**

3. **Click Tag Assistant icon** (top right)

4. **Click "Enable" → Refresh page**

5. **Check for:**
   - ✅ **Google Analytics: GA4** (with measurement ID like `G-XXXXXXXXXX`)
   - ❌ **No GA4 tag found** = Not installed

---

### **If GA4 Code is Missing:**

**Shopify Sites (your case):**

1. **Shopify Admin** → **Online Store** → **Themes**
2. **Actions** → **Edit code**
3. Open: `layout/theme.liquid`
4. Look for GA4 code in `<head>` section (around line 10-30)

Should look like:
```html
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

**If missing:**
1. **GA4 Admin** → **Data Streams** → Click your stream
2. **View tag instructions** → Copy GA4 code
3. Paste into `theme.liquid` inside `<head>` section
4. **Save**
5. Test again

---

## 🔍 Step 5: Test Real-Time Tracking

### **Verify Clicks are Reaching GA4:**

1. **GA4** → **Reports** → **Realtime**

2. **In another browser (or incognito):**
   - Google your business: `christmas wreaths australia`
   - Click your ad
   - Land on collection page
   - Browse for 30+ seconds

3. **Back in GA4 Realtime:**
   - Should see: **+1 user** (within 10 seconds)
   - Click on user → Check:
     - **First user source:** `google`
     - **First user medium:** `cpc`
     - **Session source:** `google` / `cpc`

**If you see it:** ✅ Tracking works!
**If you DON'T see it:** ❌ Tracking broken

---

## 🔍 Step 6: Check for Click Fraud / Bot Traffic

### **Why 13 Clicks but 1 Session?**

Possible causes:
1. **Click fraud:** Competitors/bots clicking ads
2. **Accidental clicks:** Mobile users misclicking
3. **Fast bounces:** Users click, immediately hit back

### **Check Invalid Click Activity:**

**Method 1: Account Overview (New UI)**
1. Click **Overview** in left navigation (home icon 🏠)
2. Scroll to **"Invalid activity"** card
3. Check for:
   - **Invalid clicks** count
   - **Filtered clicks %**
4. If > 10% filtered = potential click fraud issue

**Method 2: Insights & Reports**
1. Click **Insights and reports** icon in left navigation (📊 chart icon)
2. Click **Reports** at the top
3. In the left sidebar, select **Predefined reports**
4. Navigate to: **Other** → **Basic account stats**
5. Look at **Invalid clicks** column
6. Compare to total clicks

**Method 3: Request Invalid Clicks Report**
1. Click **Help** (question mark ?) in top right
2. Click **Contact us**
3. Choose: **Campaign performance & data discrepancies**
4. Select: **Chat** or **Phone**
5. Request: **"Invalid click activity report for Oct 28, 2025"**

**If high invalid click rate (>10%):**
- Google automatically filters most bot clicks
- You may be eligible for credits
- Request manual review from support

### **Enable Click Fraud Protection:**

**Check Current Settings:**
1. Click **Settings** (gear ⚙️) in top right
2. Click **Account settings**
3. Scroll to **Protection** section
4. Verify: **Invalid click protection** shows as **Active**

**Add IP Exclusions (Block Competitors):**
1. Click **Campaigns** in left navigation
2. Select your campaign: **B-in-W [Search | Sales]**
3. Click **Settings** tab
4. Scroll to **Advanced settings** → Expand it
5. Click **IP exclusions**
6. Click **+ Add IP address**
7. Enter IP addresses to block (competitor offices, known bots)
8. Click **Save**

**Find Your Own IP (to exclude test clicks):**
1. Google search: "what is my ip"
2. Copy the IP address shown
3. Add it to IP exclusions so your test clicks don't count

---

## 🔍 Step 7: Check Page Load Speed

### **Why This Matters:**
If your collection pages load SLOWLY, users might bounce before GA4 tracking code fires.

### **Test Page Speed:**

1. Visit: https://pagespeed.web.dev/
2. Enter: `https://beliefsinwreaths.com.au/collections/christmas-wreaths`
3. Click **Analyze**

**Check scores:**
- ✅ **Mobile: 80+** = Good
- ⚠️ **Mobile: 50-79** = Needs improvement
- ❌ **Mobile: <50** = Users bouncing before GA4 loads

**If score is low (<80):**
- Images may be too large
- Too many apps/scripts loading
- Consider optimizing Shopify theme

---

## 📋 Diagnostic Checklist

Work through this checklist **in order**:

### **Google Ads Setup:**
- [ ] Google Ads linked to GA4 (in both platforms)
- [ ] Auto-tagging (GCLID) enabled
- [ ] UTM parameters added to final URLs
- [ ] Invalid click protection enabled

### **GA4 Setup:**
- [ ] GA4 tracking code installed on all collection pages
- [ ] GA4 shows property: "Beliefs in Wreaths Site"
- [ ] Data stream active (not paused)
- [ ] Google Ads linked in GA4 admin

### **Testing:**
- [ ] GCLID parameter appears in URLs after clicking ads
- [ ] GA4 Realtime shows traffic when you test-click your own ad
- [ ] Page speed score > 80 (mobile)
- [ ] Invalid click rate < 10%

### **Monitoring:**
- [ ] Check GA4 daily for next 3 days
- [ ] Compare Google Ads clicks to GA4 paid search sessions
- [ ] Should match within 10-15% (some discrepancy normal)

---

## 🚨 Most Likely Issue (Based on Your Data)

**My diagnosis:** GCLID auto-tagging is probably broken OR GA4 code not firing fast enough.

**Quick fix test:**
1. Add UTM parameters to all ad final URLs (takes 10 minutes)
2. Wait 24 hours
3. Check if GA4 "Paid Search" sessions increase

**If UTMs work but GCLID doesn't:**
- Problem is with Google Ads ↔ GA4 link
- Unlink and re-link accounts

**If neither work:**
- GA4 code might not be on collection pages
- Check theme.liquid file

---

## 📞 Need Help?

**Google Ads Support (Australia):**
- **Phone:** 1800 009 617 (Mon-Fri, 9am-5pm AEDT)
- **Chat/Email:** 
  1. Click **Help** (?) in top right of Google Ads
  2. Click **Contact us**
  3. Choose your issue type
  4. Select **Chat** or **Request a callback**

**What to tell them:**
> "My Google Ads campaign shows 13 clicks on October 28, but Google Analytics 4 only shows 1 paid search session. I've verified auto-tagging is enabled. Can you check if my Google Ads account is properly linked to GA4 property 'Beliefs in Wreaths Site'? Also, can you send me an invalid clicks report for Oct 28?"

**GA4 Support:**
- **Help Center:** Click **Help** (?) in GA4 → **Contact support**
- Usually responds within 24-48 hours
- Can check if they're receiving GCLID data from Google Ads

They can see backend data and diagnose linking issues faster than manual troubleshooting.

---

**Start with Step 1 (verify link) and work through each step. The tracking template method (Option C in Step 3) is the fastest fix!** 🔍
