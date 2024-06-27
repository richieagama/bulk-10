const puppeteer = require('puppeteer');

(async () => {
  try {
    const browser = await puppeteer.launch({
      headless: false,
      executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
      args: ['--no-sandbox', '--disable-setuid-sandbox'],
    });

    const page = await browser.newPage();
    await page.goto('https://members.helium10.com/user/signin');

    // Wait for the email input field to be visible
    await page.waitForSelector('#loginform-email');
    
    // Type 'test' into the email input field
    await page.type('#loginform-email', 'test');

    // Type 'test' into the password input field
    await page.type('#loginform-password', 'test');

    // Click the submit button
    await page.click('.login-form button[type="submit"]');
    
    // Optionally, wait for navigation or some other indicator that the form submission has completed
    await page.waitForNavigation();

    console.log('Login form submitted.');

    // Keep the browser open
    // Comment out the following line if you want to keep the browser open indefinitely
    // await browser.close();
  } catch (error) {
    console.error('Error launching browser:', error);
  }
})();
