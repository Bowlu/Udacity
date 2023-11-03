let totalPaid = 0;
let totalPrice = 0;
const products = []; // takes in the products 

const product1 = {
  "name": "Carton of Cherries",
  "price": 100,
  "quantity": 0,
  "productId": 2345,
  "image": "images/cherry.jpg"
};

const product2 = {
  "name": "Carton of Strawberries",
  "price": 200,
  "quantity": 0,
  "productId": 5748,
  "image": "images/strawberry.jpg"
};

const product3 = {
  "name": "Bag of Oranges",
  "price": 300,
  "quantity": 0,
  "productId": 7839,
  "image": "images/orange.jpg"
};

products.push(product1);
products.push(product2);
products.push(product3);

const cart = [];

//adds each product to cart using the productID or SKU
function addProductToCart(productId) {
  for (let eachProduct = 0; eachProduct < products.length; eachProduct++) {
    if (products[eachProduct].productId === productId) {
      const productInCart = cart.find((item) => item.productId === productId);
      if (productInCart) {
        productInCart.quantity += 1;
      } else {
        products[eachProduct].quantity = 1;
        cart.push(products[eachProduct]);
      }
      return cart;
    }
  }
}
//increase in product quantity
function increaseQuantity(productId) {
  const productInCart = cart.find((item) => item.productId === productId);
  if (productInCart) {
    productInCart.quantity += 1;
  }
  return cart;
}
//decrease in product quantity
function decreaseQuantity(productId) {
  const productInCart = cart.find((item) => item.productId === productId);
  if (productInCart) {
    if (productInCart.quantity > 0) {
      productInCart.quantity -= 1;
    }
    if (productInCart.quantity === 0) {
      // Remove the product from the cart if the quantity reaches 0
      cart.splice(cart.indexOf(productInCart), 1);
    }
  }
  return cart;
}

function removeProductFromCart(productId) {
  const productInCart = cart.find((item) => item.productId === productId);
  if (productInCart) {
    productInCart.quantity = 0;
    cart.splice(cart.indexOf(productInCart), 1);
  }
  return cart;
}
//cp = cart products
function cartTotal() {
  let total = 0;
  for (let cp = 0; cp < cart.length; cp++) {
    total += cart[cp].price * cart[cp].quantity;
  }
  return total;
}

function emptyCart() {
  cart.length = 0;
}

function pay(totalPaid) {
  const balance = totalPaid - cartTotal();
  if (balance < 0) {
    return balance;
  } else {
    return balance;
  }
}

module.exports = {
   products,
   cart,
   addProductToCart,
   increaseQuantity,
   decreaseQuantity,
   removeProductFromCart,
   cartTotal,
   pay, 
   emptyCart
};
