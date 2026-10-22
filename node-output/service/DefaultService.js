'use strict';


/**
 * Create a new order
 *
 * order String Product Order
 * no response value expected for this operation
 **/
exports.ordersCreateOrderOrderPOST = function(order) {
  return new Promise(function(resolve, reject) {
    resolve();
  });
}


/**
 * Add a new item to menu
 *
 * productName String Name of the product
 * productPrice Integer Name of the product
 * no response value expected for this operation
 **/
exports.productsAddProductNameNameproductNamepriceproductPricePOST = function(productName,productPrice) {
  return new Promise(function(resolve, reject) {
    resolve();
  });
}


/**
 * Returns a list of all the products available
 *
 * returns inline_response_200_2
 **/
exports.productsGetAllProductsGET = function() {
  return new Promise(function(resolve, reject) {
    var examples = {};
    examples['application/json'] = {
  "productsList" : [ "BLT", "Pulled Pork", "Grilled Chicken", "Cuban" ]
};
    if (Object.keys(examples).length > 0) {
      resolve(examples[Object.keys(examples)[0]]);
    } else {
      resolve();
    }
  });
}


/**
 * Returns the price (rounded up) of a single product based on productId
 *
 * productId Integer Unique product Id
 * returns inline_response_200_1
 **/
exports.productsPricesProductIdGET = function(productId) {
  return new Promise(function(resolve, reject) {
    var examples = {};
    examples['application/json'] = {
  "price" : 5
};
    if (Object.keys(examples).length > 0) {
      resolve(examples[Object.keys(examples)[0]]);
    } else {
      resolve();
    }
  });
}


/**
 * Returns a product/product name based on its unique product id
 *
 * productId Integer Unique prouduct ID
 * returns inline_response_200
 **/
exports.productsProductIdGET = function(productId) {
  return new Promise(function(resolve, reject) {
    var examples = {};
    examples['application/json'] = {
  "name" : "BLT",
  "id" : 8
};
    if (Object.keys(examples).length > 0) {
      resolve(examples[Object.keys(examples)[0]]);
    } else {
      resolve();
    }
  });
}


/**
 * Delete an item based on product id provided
 *
 * productId Integer Unique Product Id
 * no response value expected for this operation
 **/
exports.productsRemoveProductProductIdDELETE = function(productId) {
  return new Promise(function(resolve, reject) {
    resolve();
  });
}


/**
 * Update the price of a an item
 *
 * productId String Unique id of product
 * newPrice Integer New price of Product
 * no response value expected for this operation
 **/
exports.productsUpdatePricePidproductIdnewPricenewPricePUT = function(productId,newPrice) {
  return new Promise(function(resolve, reject) {
    resolve();
  });
}

