/******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};

/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {

/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId])
/******/ 			return installedModules[moduleId].exports;

/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			exports: {},
/******/ 			id: moduleId,
/******/ 			loaded: false
/******/ 		};

/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);

/******/ 		// Flag the module as loaded
/******/ 		module.loaded = true;

/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}


/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;

/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;

/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "";

/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(0);
/******/ })
/************************************************************************/
/******/ ([
/* 0 */
/***/ function(module, exports, __webpack_require__) {

	var test=__webpack_require__(1);
	var test2=__webpack_require__(2)
	window.app=__webpack_require__(3).app
	//test.say()
	//test2.say()


/***/ },
/* 1 */
/***/ function(module, exports) {

	module.exports={
		say:function () {
			alert('hello world')
		}
	}

/***/ },
/* 2 */
/***/ function(module, exports) {

	module.exports={
		say:function () {
			alert('i m test2')
		}
	}

/***/ },
/* 3 */
/***/ function(module, exports, __webpack_require__) {

	
	var angular=__webpack_require__(4);
	var app = angular.module('he',['ngSanitize']);
	app.config(function($interpolateProvider) {
		  $interpolateProvider.startSymbol('[[');
		  $interpolateProvider.endSymbol(']]');
	});

	module.exports={
		app:app
	}

/***/ },
/* 4 */
/***/ function(module, exports) {

	module.exports = angular;

/***/ }
/******/ ]);