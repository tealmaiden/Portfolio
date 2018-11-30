# Shopify Liquid JS Bug

I had previously customized product pages in a Shopify store to update the selected variant when it's thumbnail image was selected, [here](https://github.com/rebeccapizano/Coursework/tree/master/Shopify-Liquid/ClickImageToSelectProduct). The thumbnail images are contained in a slider carousel that show 3 images at once and use arrows to scroll. The customization worked, but sometimes when an image was clicked, the carousel would revert unpredictably to the top. For some products with many variants, this would happen with every image, which made it incredibly annoying to select a product by clicking the image in these cases. This was probably caused by some default navigation function that was either faulty now or wasn't compatible with the new change. This was very discouraging.
___
## Objective
Fix the navigation function so that it doesn't move at all when an image is clicked. Only the arrows should reposition the slider.

## Steps Taken
1. Since this was a responsive error, I reasoned this was probably due to an error with the JavaScript, so I looked in the script of the product.liquid file and the theme.js.liquid file and looked for an area that dealt with thumbnails.
2. Found suspicious script in the theme.js.liquid file that repositioned a carousel, which might be causing the issue. I commented it out:
```
// If there is a slick carousel, get the slide index, and position it into view with animation.
  /*if (theme.cache.$productThumbs.hasClass('slick-initialized')) {
    var currentActiveSlideIndex = theme.cache.$productThumbs.slick('slickCurrentSlide');
    var newActiveSlideIndex = $el.parent().attr('data-slick-index');
    if (currentActiveSlideIndex !== newActiveSlideIndex) {
      theme.cache.$productThumbs.slick('slickGoTo', newActiveSlideIndex, false);
    }
  }*/
```
3. Saved and checked the results of the change.

## Results
This seemed to completely correct the problem. I was afraid this might take a very long time to fix, especially because the theme.js.liquid file is 1986 lines long, but it took less time than to write this summary! Luckily some problems can be fixed by a simple task of removing code.
