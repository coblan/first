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

	
	var agc=__webpack_require__(1);
	//document.write('<>')
	agc.input_hole()
	alert('hole ok ')

/***/ },
/* 1 */
/***/ function(module, exports) {

	


	function input_hole() {
		document.write("<div style='display:none' ng-app='he'><span ng-controller='hole'></span></div>")
	}

	function compileAngularElement( elSelector,p_ele) {

	        var elSelector = (typeof elSelector == 'string') ? elSelector : null ;  
	            // The new element to be added
	        if (elSelector != null ) {
	            var $div = $( elSelector );

	                // The parent of the new element
	                var $target = p_ele//$("[ng-app]");

	              angular.element($target).injector().invoke(['$compile', function ($compile) {
	                        var $scope = angular.element($target).scope();
	                        $compile($div)($scope);
	                        // Finally, refresh the watch expressions in the new element
	                        $scope.$apply();
	                    }]);
	            }

	        }

	module.exports={
		compileAngularElement:compileAngularElement,
		input_hole:input_hole,
		
		
	}

/***/ }
/******/ ]);