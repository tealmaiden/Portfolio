# Shopify Theme Edits
My Shopify store uses the [Venture](https://themes.shopify.com/themes/venture/styles/outdoors) theme. I wanted to make some changes to the store that I couldn't do through the built-in user interface, so I learned how to access the theme code, learned how the Liquid templating engine worked, and made some manual edits. Results are shown at the bottom.
___
## Objective
Make the following edits to my Shopify store by editing the code directly:

1. Center the website title/logo in the header.
2. Move down the collection links on the front page so that they don't overlap with the front image ("hero image").
3. Add an image to the contact page. 
4. Shrink the empty space around the top and bottom of the title/logo.

The following image, showing the [Venture](https://themes.shopify.com/themes/venture/styles/outdoors) theme preview, illustrates 2 of the main changes I wanted to make:
![alt text](https://github.com/rebeccapizano/Portfolio/blob/master/HTML-CSS/ShopifyThemeEdits/pics/plan.png)

## Steps Taken
* Tried to make the changes through the built-in interface, but it didn't appear there was a way to do so.
* Found where the theme code was stored to make the changes manually. In the edit themes section, there's a dropdown to edit code.
* Liquid was unfamiliar to me. There are also many theme code files that are many pages long. 
It was not straightforward to find where the code was that I needed to change. 
The main way I did so was by right-clicking and inspecting elements of the page, to get an idea of what the code looked like and then searching files with relevant-looking titles. 
* Centering the logo and altering other elements of the header:
    1. Tried changing the css in theme.scss.liquid file in the assets folder in a section under .site-header__logo. 
        * Horizontal aligning attempts: Added ```margin: auto;```, ```textalign: center;```, and changed float to center. 
        * To align vertically, added ```vertical-align: middle;```
        * RESULT: Only the vertical-aligning worked. 
        * By inspecting elements I discovered that the header was in a cell of a grid. 
        The structure of a grid and the horizontal alignment within it could be altered as described below.
    2. Made the following changes in the theme.liquid file, which had a format similar to html:
        * There was a grid table in for the header with 3 grid spaces in that would respond for different screen sizes, small and medium-up.
        * To center the hamburger menu that shows up on the left for small window sizes, changed:
       ```<div class="grid__item small--one-quarter medium-up--hide">``` to 
        ```<div class="grid__item small--one-quarter small--text-center medium-up--hide">```
        * To finally center the logo, changed:```<div class="grid__item small--one-half medium-up--two-thirds small--text-center">``` to
        ```<div class="grid__item small--one-half medium-up--one medium-up--text-center small--text-center">```
        * To make the header look more centered overall, I shrank the size of the right grid by changing:
        ```<div class="grid__item small--one-quarter medium-up--one-third text-right">```
        to ```<div class="grid__item small--one-quarter medium-up--one-eighth text-left">```        
* Moved down the collection links on the front page so that they don't overlap with the front image ("hero image"). In theme.scss.liquid, changed the margin of the hero image from negative to 0:
    ```
    .hero {
      background-color: adaptive-color($color-header, 10%); // default background color
      height: 330px;
      margin-bottom: -($gutter-site * 1.5);

      @include media-query($medium-up) {
        height: 600px;
        margin-bottom: -($gutter-site * 3);
      }
  ```
  to 
  ```
  .hero {
      background-color: adaptive-color($color-header, 10%); // default background color
      height: 330px;
      margin-bottom: 0;

      @include media-query($medium-up) {
        height: 400px; // Also shrank the size of the hero image here for medium-up from 600 to 400 px.
        margin-bottom: 0;
      }
  ```
* Added an image to the contact page. 
    1. In page.contact.liquid, changed grid to grid--table.
    2. Added image (hidden for small window size) by adding:
    ```
    <div class="grid__item small--hide medium-up--one-half" id=verticalTop> <img src="[path to image file]" alt=""></img></div>
    ```
    3. In theme.scss.liquid, changed image vertical alignment from middle to top:
    ```
    #verticalTop {vertical-align: top;}   
    ```
    4. Re-used verticalTop ID tag for the contact form and other items around the site that needed to stick to the top.
* Shrank the padding around the top and bottom of the title/logo. Changed from / 2 to / 4:
    ```
    .site-header__upper {
      padding-top: $gutter-site / 4;
      padding-bottom: $gutter-site / 4;

      @include media-query($medium-up) {
        padding-top: $gutter-site / 4;
        padding-bottom: $gutter-site / 4;
    ```
  
## Results
1. Centering and adjusting header elements:
   * Comparison for large screens:<br>
   ![alt text](https://github.com/rebeccapizano/Portfolio/blob/master/HTML-CSS/ShopifyThemeEdits/pics/largeCompED.jpg)
   * Comparison for small screens: <br>
   ![alt text](https://github.com/rebeccapizano/Portfolio/blob/master/HTML-CSS/ShopifyThemeEdits/pics/smallCompED.jpg)
   * Looks cleaner for intermediate screen size:<br>
   ![alt text](https://github.com/rebeccapizano/Portfolio/blob/master/HTML-CSS/ShopifyThemeEdits/pics/cleanerEdit.jpg)
2. Moving down collection links / removing overlap:
   * Before: <br> ![alt text](https://github.com/rebeccapizano/Portfolio/blob/master/HTML-CSS/ShopifyThemeEdits/pics/overlap1ED.jpg)
   * After: <br> ![alt text](https://github.com/rebeccapizano/Portfolio/blob/master/HTML-CSS/ShopifyThemeEdits/pics/overlap2ED.jpg)
3. Adding an image to Contact page:
   * Before: <br> ![alt text](https://github.com/rebeccapizano/Portfolio/blob/master/HTML-CSS/ShopifyThemeEdits/pics/contactBefore.png)
   * After: <br> ![alt text](https://github.com/rebeccapizano/Portfolio/blob/master/HTML-CSS/ShopifyThemeEdits/pics/contactED.jpg)
4. Removing the padding:
   * Before: <br> ![alt text](https://github.com/rebeccapizano/Portfolio/blob/master/HTML-CSS/ShopifyThemeEdits/pics/padding1ED.jpg)
   * After: <br> ![alt text](https://github.com/rebeccapizano/Portfolio/blob/master/HTML-CSS/ShopifyThemeEdits/pics/padding2ED.jpg)

