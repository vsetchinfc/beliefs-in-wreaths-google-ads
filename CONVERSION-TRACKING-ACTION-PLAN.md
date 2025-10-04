# 🎯 CONVERSION TRACKING FIX - ACTION PLAN
## Beliefs in Wreaths - Clean Up & Optimize

**Date:** October 4, 2025  
**Priority:** CRITICAL - Must complete before campaign optimization  
**Time Required:** 1-2 hours  
**Status:** IN PROGRESS

---

## 📊 CURRENT SITUATION

### Problems Identified:
❌ **12+ conversion actions** (too many!)  
❌ **Duplicate purchase tracking** (counting same sale twice)  
❌ **Multiple "Needs attention" warnings**  
❌ **0 conversions on 8+ actions** (useless clutter)  
❌ **Not clear which conversion is PRIMARY**  

### Impact:
- Google can't optimize properly (too many signals)
- Conversion data is inaccurate (duplicates)
- Can't tell which keywords drive actual sales
- Wasting time managing unnecessary conversions

---

## ✅ TARGET STATE (What We Want)

### Clean Setup:
✅ **1 PRIMARY conversion:** Purchase (optimize bids for this)  
✅ **2-3 SECONDARY conversions:** Add to Cart, Begin Checkout (track but don't optimize)  
✅ **All others:** Removed or disabled  
✅ **Clear data:** No duplicates, accurate counting  

### Benefits:
- Google knows exactly what to optimize for
- Accurate conversion reporting
- Better bid optimization
- Cleaner account, easier to manage

---

## 🎯 ACTION PLAN - 3 PHASES

### PHASE 1: AUDIT & DECIDE (15 minutes) ⚡ DO FIRST

**Goal:** Understand what you have and decide what to keep

#### Step 1.1: Export Current Conversion List
- [ ] Go to: Tools & Settings → Conversions
- [ ] Take screenshots of all conversion actions
- [ ] Note which are PRIMARY vs SECONDARY
- [ ] Document conversion counts for each

#### Step 1.2: Identify Purchase Conversions (THE IMPORTANT ONES)
Currently you have 2 purchase tracking methods:

**Option A: Google Shopping App - Purchase**
- Conversions: 7.00
- Value: $940.00
- Source: Website (direct tag)
- Status: Needs attention
- Action: PRIMARY

**Option B: Beliefs in Wreaths Site (web) purchase**
- Conversions: 6.00
- Value: $912.50
- Source: Website (Google Analytics GA4)
- Status: No recent conversions
- Action: SECONDARY

**Decision Required:** Choose ONE as your PRIMARY purchase conversion

**✅ RECOMMENDATION: Keep "Google Shopping App - Purchase" as PRIMARY**

**Why:**
- Already set as PRIMARY
- Direct tracking (not dependent on GA4)
- More conversions (7 vs 6)
- Higher value tracked

**Action:**
- [ ] Keep: Google Shopping App - Purchase (PRIMARY)
- [ ] Change: GA4 purchase to SECONDARY or REMOVE
- [ ] This prevents double-counting

---

### PHASE 2: CLEAN UP & SIMPLIFY (30 minutes)

**Goal:** Remove useless conversions, fix duplicates

#### Step 2.1: Handle Purchase Tracking (MOST IMPORTANT)

**A. Set Google Shopping App - Purchase as PRIMARY**
- [ ] Go to: Tools & Settings → Conversions
- [ ] Click: "Google Shopping App - Purchase"
- [ ] Verify: Action optimisation = **PRIMARY**
- [ ] Verify: Count = **One** (not Every)
- [ ] Click: "Troubleshoot" button
- [ ] Follow any recommendations to fix "Needs attention"
- [ ] Save changes

**B. Handle GA4 Purchase Duplicate**
Choose one option:

**OPTION 1: Remove GA4 Purchase** (Recommended - simplest)
- [ ] Click: "Beliefs in Wreaths Site (web) purchase"
- [ ] Click: "Remove" or "Edit"
- [ ] Status: Change to "Removed"
- [ ] Reason: Duplicates Google Shopping App Purchase

**OPTION 2: Keep as Secondary** (If you want both sources)
- [ ] Click: "Beliefs in Wreaths Site (web) purchase"
- [ ] Action optimisation: Change to **SECONDARY**
- [ ] This way it won't affect bid optimization
- [ ] Note: You'll still see some double-counting in reports

---

#### Step 2.2: Fix Micro-Conversions (Keep as Secondary)

**These are useful to track but shouldn't drive bidding:**

**A. Add to Cart Conversions**

Currently have 2 - consolidate:
- [ ] **"Google Shopping App - Add To Cart"** (18 conv., $2,566)
  - Action optimisation: **SECONDARY**
  - Status: Fix "Needs attention" (click Troubleshoot)
  
- [ ] **"Shopping Cart"** (0 conversions)
  - Action: **REMOVE** (not working, duplicate)

**B. Begin Checkout Conversions**

Currently have 2 - consolidate:
- [ ] **"Google Shopping App - Begin Checkout"** (14 conv., $2,022)
  - Action optimisation: **SECONDARY**
  - Status: Fix "Needs attention" (click Troubleshoot)
  
- [ ] **"Contact Information"** (0 conversions)
  - Action: **REMOVE** (not working, duplicate)

---

#### Step 2.3: Remove Useless Conversions (Zero Value)

**Phone Call Conversions (All showing 0 conversions):**
- [ ] "Calls from Smart Campaign Ads" - **REMOVE**
- [ ] "Clicks to call" - **REMOVE**
- [ ] "Smart campaign ad clicks to call" - **REMOVE**
- [ ] "Smart campaign map clicks to call" - **REMOVE**

**Why remove:** 0 conversions in 3+ years = not working, cluttering account

---

#### Step 2.4: Handle Page View Conversions (Optional)

**High volume, zero value conversions:**
- [ ] "Google Shopping App - Page View" (16,652 conv., $0)
- [ ] "Google Shopping App - View Item" (1,352 conv., $0)
- [ ] "Google Shopping App - Search" (126 conv., $0)

**OPTION 1: Remove** (Recommended)
- Not useful for optimization
- Too high volume, dilutes important data
- Action: Remove all 3

**OPTION 2: Keep as Secondary**
- Action optimisation: **SECONDARY**
- Exclude from "Conversions" column (they'll show in "All conversions")
- Only if you want to see this data

**My Recommendation:** Remove them - focus on sales, not page views

---

#### Step 2.5: Handle Payment Info Conversion
- [ ] "Google Shopping App - Add Payment Info" (4 conv., $0)
  - Decision: Keep as SECONDARY or Remove
  - Recommendation: Keep as SECONDARY (indicates purchase intent)

---

### PHASE 3: VERIFY & TEST (15 minutes)

**Goal:** Confirm everything is working correctly

#### Step 3.1: Review Final Setup

After cleanup, you should see:

**PRIMARY Conversions (1):**
```
✅ Google Shopping App - Purchase
   - Action optimisation: PRIMARY
   - Count: One
   - Status: Active (no warnings)
```

**SECONDARY Conversions (2-4):**
```
⚪ Google Shopping App - Add To Cart
   - Action optimisation: SECONDARY
   
⚪ Google Shopping App - Begin Checkout
   - Action optimisation: SECONDARY
   
⚪ Add Payment Info (optional)
   - Action optimisation: SECONDARY
```

**Removed (8-10):**
```
❌ Beliefs in Wreaths Site (web) purchase (duplicate)
❌ Shopping Cart (0 conv)
❌ Contact Information (0 conv)
❌ All phone call conversions (4 items, 0 conv)
❌ Page views (3 items, too many, not useful)
```

#### Step 3.2: Check Campaign Columns

- [ ] Go to: Campaigns view
- [ ] Columns → Modify columns → Conversions
- [ ] Verify "Conversions" column shows ONLY PRIMARY conversions
- [ ] Check "All conversions" column shows PRIMARY + SECONDARY
- [ ] Confirm numbers make sense (no crazy high numbers from page views)

#### Step 3.3: Test Purchase Tracking (CRITICAL)

**Do a test purchase:**
- [ ] Go to beliefsinwreaths.com.au
- [ ] Add item to cart
- [ ] Complete checkout (real purchase or test)
- [ ] Wait 3-24 hours
- [ ] Check Google Ads → Conversions
- [ ] Verify +1 conversion appears in "Google Shopping App - Purchase"
- [ ] If it shows = **TRACKING WORKS!** ✅
- [ ] If it doesn't = See troubleshooting guide

---

## 📋 QUICK REFERENCE CHECKLIST

### Must Do Today:
- [ ] Choose PRIMARY purchase conversion (Google Shopping App - Purchase)
- [ ] Remove or set GA4 purchase to SECONDARY
- [ ] Change Add to Cart to SECONDARY
- [ ] Change Begin Checkout to SECONDARY
- [ ] Remove 4 phone call conversions (0 conv)
- [ ] Remove Shopping Cart (0 conv)
- [ ] Remove Contact Information (0 conv)
- [ ] Fix "Needs attention" warnings (click Troubleshoot)

### Optional but Recommended:
- [ ] Remove page view conversions (3 items)
- [ ] Test purchase tracking works
- [ ] Update campaign columns to show clean data

---

## 🚨 TROUBLESHOOTING

### Issue: "Needs Attention" Warning on Purchase Conversion

**Possible Causes:**
1. Conversion tag not firing correctly
2. Duplicate tags on website
3. Tag configuration mismatch

**Fix:**
1. Click "Troubleshoot" button
2. Common fixes:
   - Update conversion tag on website
   - Remove duplicate tags
   - Verify tag ID matches Google Ads
3. Test with Google Tag Assistant
4. See: `docs/guides/CONVERSION-TRACKING-GUIDE.md` for detailed steps

---

### Issue: Still Seeing Duplicate Conversions

**Cause:** Both Google Ads tag AND GA4 tracking same purchase

**Fix:**
- Remove one conversion action completely, OR
- Set one to SECONDARY and exclude from optimization

---

### Issue: Zero Recent Conversions After Cleanup

**Possible Causes:**
1. Website not generating sales (check with client)
2. Conversion tag broken/removed
3. Tag not on thank-you page

**Fix:**
1. Check with client: Any recent sales?
2. View page source on thank-you page
3. Search for: `gtag('event', 'conversion'`
4. If missing: Reinstall tracking tag
5. See: `docs/guides/setup-conversion-tracking.md`

---

## 📊 EXPECTED RESULTS AFTER CLEANUP

### Before Cleanup:
- 12+ conversion actions
- Confusing data (duplicates, page views)
- "Needs attention" warnings
- Google optimizing for wrong things
- Hard to see what's working

### After Cleanup:
- 1 PRIMARY conversion (Purchase)
- 2-3 SECONDARY conversions (micro-conversions)
- Clean, accurate data
- No warnings
- Google optimizes for actual sales
- Easy to see which keywords drive revenue

### Performance Impact:
- 🎯 Better bid optimization (focused on sales)
- 📊 Cleaner reporting (accurate conversion data)
- 💰 Better ROAS (optimizing for right goal)
- ⏱️ Less time managing conversions
- 🚀 Campaign performance improves over 2-4 weeks

---

## 🔗 RELATED GUIDES

- **Detailed Steps:** `docs/guides/CONVERSION-TRACKING-GUIDE.md`
- **Setup from Scratch:** `docs/guides/setup-conversion-tracking.md`
- **Tag Testing:** Use Google Tag Assistant Chrome extension
- **GA4 Integration:** Google Ads → Tools → Linked Accounts

---

## ✅ SUCCESS CRITERIA

**You'll know it's working when:**
- [ ] Only 1 PRIMARY conversion action (Purchase)
- [ ] "Conversions" column shows only actual purchases
- [ ] No "Needs attention" warnings
- [ ] Test purchase shows up in 3-24 hours
- [ ] Conversion reports are clean and accurate
- [ ] Google can optimize bids for sales (not page views)

---

## 📅 TIMELINE

**Total Time:** 1-2 hours

**Today (1 hour):**
- Phase 1: Audit & Decide (15 min)
- Phase 2: Clean Up (30 min)
- Phase 3: Verify (15 min)

**This Weekend:**
- Do test purchase
- Wait 24 hours
- Verify tracking works

**Next Week:**
- Monitor conversion data
- Confirm bid optimization improving
- Weekly check-in on conversion accuracy

---

## 💡 PRO TIPS

1. **Take screenshots before you delete anything** (in case you need to reference)
2. **Start with least important conversions** (phone calls with 0 conv)
3. **Keep secondary conversions** (Add to Cart, Begin Checkout are useful)
4. **One PRIMARY conversion only** (Google needs clear optimization signal)
5. **Test after changes** (do a purchase, verify it tracks)
6. **Wait 48 hours** for Google's bidding to adjust to new setup

---

## 📞 NEED HELP?

**If stuck:**
1. See detailed guide: `docs/guides/CONVERSION-TRACKING-GUIDE.md`
2. Check Google Ads Help: [Conversion Tracking](https://support.google.com/google-ads/answer/1722022)
3. Use Google Tag Assistant: Test if tags are firing
4. Document what you see and ask for help

---

**Status:** Ready to implement  
**Next Review:** After Phase 3 completion  
**Last Updated:** October 4, 2025
