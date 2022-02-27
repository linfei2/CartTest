# CartTest
> Shopping cart test on https://moim.store/ automated with Selenium, WebDriver Manager and pytest for practice purposes

## Technologies
```
* Python 3.7.5
* WebDriver Manager
```

#### Environment
```
The most recent versions of Chrome and Firefox browsers (determined by WebDriver Manager)
```

## Test Case 1 - Add product to cart

#### Steps
```
1. Open https://moim.store/
2. Click "Nowości" [New in] in top navigation menu
3. Select the first product on product listing page
4. Click "DO KOSZYKA" [Add to cart] button
```

#### Expected result
```
Selected product is added to cart and user gets redirected to cart page
```


#### Actual result
```
As expected
```

## Test Case 2 - Remove product from cart

#### Steps
```
Prerequisites: user is on https://moim.store/koszyk/ and there is a product in the cart

1. Click "X" on the left side of the product in cart
```

#### Expected result
```
The product is removed from cart and "Twój koszyk aktualnie jest pusty."
[Your cart is currently empty] message shows up
```


#### Actual result
```
As expected
```


