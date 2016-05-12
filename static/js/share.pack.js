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

	var ck=__webpack_require__(1)
	var http = __webpack_require__(2)
	var modewin=__webpack_require__(3)
	ck.import()

	app = angular.module('share',['ngSanitize']);
	app.config(function($interpolateProvider) {
	  $interpolateProvider.startSymbol('[[');
	  $interpolateProvider.endSymbol(']]');
	});
	http.add_ajax(app)
	modewin.add_model(app)

	app.directive('nameForm',function () {
		return {
			restrict:'EA',
			scope:{
				submit:'&',
			},
			template:'<form name="nameForm" ng-submit="submit({valid:nameForm.$valid,name:name})" novalidate >\
							<div class="form-group">\
								<label>名称</label>\
								<input class="form-control" type="text" name="name" value="" ng-model="name" required/>\
								<span ng-show="nameForm.name.$error.required">必填</span>\
								<input type="submit" name="test" value="提交" />\
							</div>\
						</form>',
			link:function (scope,ele,attr) {
				if(attr.name){
					scope.name=attr.name
				}
			}
		}
	});
		
	app.directive('editForm',function ($timeout) {
			function get_value(item) {
					item.content=editor.getData();
					return item;
		};
		return {
			restrict: 'EA',
			scope:{
				item:'=',
				submit:'&',
				cancel:'&',
				
			},
			template:'<form name="myForm" ng-submit="submit({valid:myForm.$valid,file:get_value(item)})" novalidate >\
					<div class="form-group">\
					<label>标题</label>\
					<input class="form-control" type="text" name="name" value="" ng-model="item.name" required/>\
					<span ng-show="myForm.name.$error.required">必填</span>\
					</div>\
					<div class="form-group">\
					<label>内容</label>\
					<textarea id="editor_id" class="form-control" class="form-control" name="ri"  ></textarea>\
					</div>\
					<input type="submit" name="test" value="提交" />\
					<button name="test" type="button" value="val" ng-click="cancel()">取消</button>\
					</form>',
			link :function (scope,iElem, iAttrs) {
				if(typeof(scope.item)=='undefined'){
					scope.item={}
				}
				$timeout(function () {
					 //KindEditor.ready(function(K) {
	                //window.editor = K.create('#editor_id');

	                editor = CKEDITOR.replace('ri')
	                editor.setData(scope.item.content)
	                scope.get_value=get_value;
	            //    editor = KindEditor.create(iElem.find('#editor_id'));
	            //    editor.html(scope.item.content);
	          		//scope.get_value=get_value;
				})
				
	        },
			}
	});




/***/ },
/* 1 */
/***/ function(module, exports) {

	
	function import_ckeditor() {
		document.write("<script src='/static/ckeditor/ckeditor.js'></script>")
	}

	ckEditor={
			import:import_ckeditor,
		}
	module.exports=ckEditor

/***/ },
/* 2 */
/***/ function(module, exports) {

	
	function add_ajax(app) {
		app.factory('ajax',function ($http) {
			return {
				post:function (post_url,post_data,callback) {
					$http.post(post_url,post_data)
						.success(function(data, status, headers, config) {
							if(data.msg){
								alert(data.msg)
							} 
							if (callback){
								callback(data)
							}
						}).error(function(data, status, headers, config) {  
						    alert('有错误,返回码为:'+status)
						});
				}
			}
		})
	}

	module.exports={
		add_ajax:add_ajax,
	}

/***/ },
/* 3 */
/***/ function(module, exports) {

	//angular.module('styleInjector', ['ng'])
	function add_model(app) {
		
	  app.factory('styleInjector', function($rootElement) {
	    var ss = angular.element('<style>'),
	    initializedDirectives = {};
	    $rootElement.append(ss);
	    return {
	      insertCSS: insertCSS,
	      importCSSLink: importCSSLink,
	      initDirective: initDirective,
	      
	    };
	    function initDirective(desc) {
	      // A helper for directives to add their styles once.
	      if (!initializedDirectives[desc.name]) {
	        if (desc.css)
	          insertCSS(desc.css);
	        if (desc.cssUrl)
	          importCSSLink(desc.cssUrl);
	        initializedDirectives[desc.name] = true;
	      }
	    }
	    function insertCSS(css) {
	      ss.text(ss.text()+css+'\n');
	    }
	    
	    function importCSSLink(url) {
	      insertCSS('@import url('+JSON.stringify(url)+');');
	    }
	    
	  })

	  app.directive('modelForm',function ($window,styleInjector,$timeout) {
		/* <width>: 百分数 或者 px
		    [height]: 百分数，或者px
		<div model-form style='text-align: center;' ng-show='show_form' width='30%' height='30px'>
		*/
		var css=hereDoc(function () {/*
		.-model-back{
		    width: 100%;
		    height: 100%;
		    position: fixed;
		    top:0;
		    left:0;
		    z-index: 8;
		    background: rgba(0,0,0,0.4);
		}
		.-model-form{
		    font-size: 1.1em;
		    border-radius: 5px;
		    background:  #fff;
		}*/}); 
		styleInjector.insertCSS(css)
		return {
			restrict:'A',
			transclude:true,
			template:"<div class='-model-back'>\
					<div ng-transclude class='-model-form'></div></div>",
			link:function (scope,ele,attr) {
				var form = ele.find('.-model-form')
				if (attr.style){
					form.attr('style',attr.style)
				}
				//if(attr.width){
				//	//var mt=/(\d+)%/.exec(attr.width);
				//	//if(mt){
				//	//	form.css('width',$(window).width()*parseFloat('0.'+mt[1]))
				//	//	$(window).resize(function () {
				//	//		form.css('width',$(window).width()*parseFloat('0.'+mt[1]))
				//	//	})
				//	//}else{
				//		form.css('width',attr.width)
				//	//}
				//}
				//if(attr.height){
				//	//var mt = /(\d+)%/.exec(attr.height);
				//	//if(mt){
				//	//	form.css('height',$(window).height()*parseFloat('0.'+mt[1]))
				//	//	$(window).resize(function () {
				//	//		form.css('height',$(window).height()*parseFloat('0.'+mt[1]))
				//	//	})
				//	//}else{
				//		form.css('height',attr.height)
				//	//}
					
				//}
				scope.$watch(attr.ngShow, function(value){
					if (value){
						$timeout(function () {
							win_width=$window.innerWidth;
							win_height=$window.innerHeight;
							form_width=form.width()
							form_height=form.height()
							form.css('margin-left',parseInt((win_width-form_width)/2)+'px')
							form.css('margin-top',parseInt((win_height-form_height)/2)+'px')
						})
					}
				})
			}
		}
	})
	app.directive('inform',function () {
		var form=hereDoc(function () {/*
		<div model-form style='text-align: center;' ng-show='show_form' width=[[width]]>
		<div style='padding: 20px;'>
			<p  ng-bind='content'></p>
			<button type="button" style="min-width:100px;"
				class="btn btn-success" 
				ng-click='hide()'>
				知道了
			</button>
		</div>
		</div>
		*/
		})
		return {
			restrict:'A',
			template:form,
			scope:{
				self:'=',
				width:'@'
			},
			
			link:function (scope,ele,attr) {
				scope.callback=null;
				scope.self={
					info:function (content,callback) {
						scope.show_form=true;
						scope.content=content;
						if (callback){
							scope.callback=callback
						}
						}
				}
				//scope.width=attr.width;
				scope.show_form=false;
				scope.hide=function () {
					scope.show_form=false;
					if(scope.callback){
						scope.$parent.$eval(scope.callback)
						scope.callback=null;
					}
				}
			}
		}
	})

	app.directive('assureForm',function () {
		var form=hereDoc(function () {/*
		<div model-form style='text-align: center;' ng-show='show_form' width=[[width]] height=[[height]]>
		<div style='padding: 20px;'>
			<p ng-bind='content'></p>
			<button type="button" style='position:relative;left:-10px;min-width:100px;'
				class="btn btn-success" 
				ng-click='hide(true)'>
				确定
			</button>
			<button type="button" style='position:relative;left:10px;min-width:100px;'
				class="btn btn-default" 
				ng-click='hide(false)'>
				取消
			</button>
		</div>
		</div>
		*/
		})
		return {
			restrict:'A',
			template:form,
			scope:{
				self:'=',
				width:'@',
				height:'@',
			},
			
			link:function (scope,ele,attr) {
				scope.callback=null;
				scope.self={
					info:function (content,callback) {
						scope.show_form=true;
						scope.content=content;
						if (callback){
							scope.callback=callback
						}
						}
				}
				scope.show_form=false;
				scope.hide=function (bool) {
					scope.show_form=false;
					if(scope.callback){
						scope.$parent.$eval(scope.callback(bool))
						scope.callback=null;
					}
				}
			}
		}
	})

		
	}



	//var app = angular.module('he',['ngSanitize','styleInjector']);
	//app.config(function($interpolateProvider) {
	//	  $interpolateProvider.startSymbol('[[');
	//	  $interpolateProvider.endSymbol(']]');
	//	});

	function hereDoc(f) {　
	    return f.toString().replace(/^[^\/]+\/\*!?\s?/, '').replace(/\*\/[^\/]+$/, '');
	}
	function const_div(first_argument) {
		
		return true;
	}
	module.exports={
		add_model:add_model,
	}
		//var modewin=require('augular/modewin')
		//modewin.add_model(app)
		
		//<!-----------------弹出框------------------------>
		//<div inform self='inform' width='50%'></div>
		//<div assure-form self='assure' width='50%'></div>

		//$scope.inform.info(data.msg)
		//$scope.assure.info(data.msg,callback)


/***/ }
/******/ ]);