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
/******/ ({

/***/ 0:
/***/ function(module, exports, __webpack_require__) {

	


	var app = angular.module('he',[]);
	app.config(function($interpolateProvider) {
		  $interpolateProvider.startSymbol('$[[');
		  $interpolateProvider.endSymbol(']]^');
	});
	var agc=__webpack_require__(5)
	agc.input_hole()
	app.controller('hole',function ($scope) {
		$scope.wo='wold';
		$scope.src_type=$('#id_type').val();
		$scope.src=$('#id_src').val();
	})
	compileAngularElement=agc.compileAngularElement
	CKEDITOR.timestamp='ABCDF';
	$(function () {
		
		$('<span id="pig"><span>ok</span><span ng-bind="wo"></span></span>').insertAfter($('#id_type'))
		$('#id_type').attr('ng-model',"src_type")
		$('#id_src').attr('ng-show',"src_type!='ck'")
		$('#id_src').attr('ng-model',"src")

		$('<div id="ck_wrap" style="margin-left:200px;min-width:750px;" ng-show="src_type==\'ck\'"><textarea name="editor1" id="editor1" cols="40" ng-model="src"></textarea></div>').insertAfter($('#id_src'))
		var editor=$( '#editor1' ).ckeditor().editor;
		$( "form" ).submit(function( event ) {
	  		$('#id_src').val($('#editor1').val())
		});
		//editor.on('change',function () {
		//	$('#id_src').val($('#editor1').val())
		//})
		//editor.on('instanceReady',function () {
		//	$('#id_src').val($('#editor1').val())
		//})
		 //CKEDITOR.replace( 'editor1')
		//var editor=$( '#editor1' ).ckeditor().editor;
		//editor.on('instanceReady',function () {
		//	$(editor).attr('ng-show','src_type=="ck"')
		//	compileAngularElement('#cke_editor1','#hole')
		//})
			
		compileAngularElement($('#id_type'),$('#hole'))
		compileAngularElement($('#id_src'),$('#hole'))
		compileAngularElement($('#ck_wrap'),$('#hole'))

		
	})


	//function compileAngularElement( elSelector,pSelector) {

	//        var elSelector = (typeof elSelector == 'string') ? elSelector : null ;  
	//            // The new element to be added
	//        if (elSelector != null ) {
	//            var $div = $( elSelector );

	//                // The parent of the new element
	//                var $target = $(pSelector)//$("[ng-app]");

	//              angular.element($target).injector().invoke(['$compile', function ($compile) {
	//                        var $scope = angular.element($target).scope();
	//                        $compile($div)($scope);
	//                        // Finally, refresh the watch expressions in the new element
	//                        $scope.$apply();
	//                    }]);
	//            }

	//        }

/***/ },

/***/ 5:
/***/ function(module, exports) {

	


	function input_hole() {
		document.write("<div style='display:none' ng-app='he'><span ng-controller='hole' id='hole'></span></div>")
	}

	function compileAngularElement( ele,target_ctr) {

	        //var elSelector = (typeof elSelector == 'string') ? elSelector : null ;  
	        //    // The new element to be added
	        //if (elSelector != null ) {
	            //var $div = $( elSelector );

	                // The parent of the new element
	                //var $target = p_ele//$("[ng-app]");

	              angular.element(target_ctr).injector().invoke(['$compile', function ($compile) {
	                        var $scope = angular.element(target_ctr).scope();
	                        $compile(ele)($scope);
	                        // Finally, refresh the watch expressions in the new element
	                        $scope.$apply();
	                    }]);
	            //}

	        }

	module.exports={
		compileAngularElement:compileAngularElement,
		input_hole:input_hole,
		
		
	}

/***/ }

/******/ });