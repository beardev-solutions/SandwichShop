'use strict';

var utils = require('../utils/writer.js');
var Default = require('../service/DefaultService');

module.exports.ordersCreateOrderOrderPOST = function ordersCreateOrderOrderPOST (req, res, next, order) {
  Default.ordersCreateOrderOrderPOST(order)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.productsAddProductNameNameproductNamepriceproductPricePOST = function productsAddProductNameNameproductNamepriceproductPricePOST (req, res, next, productName, productPrice) {
  Default.productsAddProductNameNameproductNamepriceproductPricePOST(productName, productPrice)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.productsGetAllProductsGET = function productsGetAllProductsGET (req, res, next) {
  Default.productsGetAllProductsGET()
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.productsPricesProductIdGET = function productsPricesProductIdGET (req, res, next, productId) {
  Default.productsPricesProductIdGET(productId)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.productsProductIdGET = function productsProductIdGET (req, res, next, productId) {
  Default.productsProductIdGET(productId)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.productsRemoveProductProductIdDELETE = function productsRemoveProductProductIdDELETE (req, res, next, productId) {
  Default.productsRemoveProductProductIdDELETE(productId)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.productsUpdatePricePidproductIdnewPricenewPricePUT = function productsUpdatePricePidproductIdnewPricenewPricePUT (req, res, next, productId, newPrice) {
  Default.productsUpdatePricePidproductIdnewPricenewPricePUT(productId, newPrice)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};
