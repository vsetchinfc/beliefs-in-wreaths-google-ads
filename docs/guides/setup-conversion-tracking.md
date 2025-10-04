# Setup Conversion Tracking for Google Ads

## Introduction
Setting up conversion tracking is essential for any e-commerce website to measure the effectiveness of online advertising. This guide provides a comprehensive step-by-step process for setting up Google Ads conversion tracking for various platforms including Shopify, WooCommerce, and custom solutions.

## Step 1: Create Conversion Actions
1. **Log in to your Google Ads account.**
2. In the left sidebar, click **"Goals"** → **"Conversions"**
   - **OR** click **"Tools"** icon (gear) → Under **"Measurement"** → **"Conversions"**
3. Click the **"+ New conversion action"** or **"+ (plus)"** button.
4. Select the conversion source you want to track:
   - **Website** (most common for e-commerce)
   - App, Phone calls, Import, etc.
5. For website conversions, enter your website URL and click **"Scan"**
   - Or select **"Add a conversion action manually"**
6. Fill in the necessary details:
   - **Goal and action optimization**: Primary or Secondary
   - **Conversion name**: e.g., "Purchase", "Add to cart"
   - **Value**: Transaction-specific or same value
   - **Count**: One (for purchases) or Every (for leads)
7. Click **"Done"** or **"Save and continue"** to save your conversion action.

## Step 2: Install Tracking Tags
### For Shopify:
1. Go to your Shopify admin panel.
2. Navigate to **Online Store > Themes**.
3. Click **Actions > Edit Code**.
4. Locate the **theme.liquid** file.
5. Add your Google Ads tracking code before the closing `</head>` tag.
6. Save changes.

### For WooCommerce:
1. Install and activate the **Insert Headers and Footers** plugin.
2. Go to **Settings > Insert Headers and Footers**.
3. Paste your Google Ads tracking code into the **Scripts in Header** section.
4. Save changes.

### For Custom Platforms:
1. Access the HTML of your website.
2. Add the Google Ads tracking code in the `<head>` section of your website's HTML.
3. Ensure the code is placed before the closing `</head>` tag.

## Step 3: Test Your Setup
1. Use the **Google Tag Assistant** Chrome extension to verify that your tracking tag is firing correctly.
2. Test the conversion action by completing a sample transaction on your website.
3. Check your Google Ads account to see if the conversion is recorded correctly.

## Step 4: Troubleshoot Common Issues
- **Issue: Conversion not recorded.**
  - Ensure the tracking code is installed correctly.
  - Check if the conversion action settings are configured properly.

- **Issue: Incorrect values recorded.**
  - Verify that dynamic values and transaction IDs are being sent correctly in the tracking code.

## Best Practices for Tracking Purchase Conversions
1. Use dynamic values to track individual transaction amounts.
2. Include transaction IDs to avoid duplicate conversions.
3. Regularly review your conversion actions to ensure they align with your business goals.

## Conclusion
By following this guide, you should be able to successfully set up Google Ads conversion tracking for your e-commerce website. Regularly monitor your conversion actions and make adjustments as needed to optimize your advertising efforts.