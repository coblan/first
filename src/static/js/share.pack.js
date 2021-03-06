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
	var hx=__webpack_require__(4)
	var syntax=__webpack_require__(5)
	ck.import()
	syntax.myimport()
	//syntax.load_all_brush()
	window.syntax=syntax


	app = angular.module('share',['ngSanitize']);
	app.config(function($interpolateProvider) {
	  $interpolateProvider.startSymbol('[[');
	  $interpolateProvider.endSymbol(']]');
	});
	http.add_ajax(app)
	modewin.add_model(app)
	function update_file_index(ele) {
		return hx.build_index(ele)
	}
	window.update_file_index=update_file_index;

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


/***/ },
/* 4 */
/***/ function(module, exports) {

	//构造h1-h6的索引
	function build_index(node){
	        // node :某个jquery对象
	        // 函数用于构建索引。以列表的形式，返回node下面所有的H1-6标题。
	        var out=$('<ul></ul>');

	        var count=0;
	        var stat=new Array(0,0,0,0,0,0);
	        var wrap=new Array(0,0,0,0,0,0);

	        node.find(":header").each(function(index, el) {
	          var id=$(this).attr('id');
	          if (!id){
	              $(this).attr('id','link'+count);
	              count+=1;
	            }
	  
	          var new_node=$('<li><a href="#'+$(this).attr('id')+'" target="_self">'+$(this).text()+'</a></li>');
	          x=parseInt(el.tagName.charAt(1))-1;
	          if (x==0){
	            out.append(new_node);
	            stat[x]=new_node;
	          }else{
	            if (!wrap[x-1]){
	              wrap[x-1]=$("<ul></ul>");
	              var tmp=out;
	              for (var i=x-1;i>-1;i--){
	                if (stat[i]){
	                  tmp=stat[i];
	                  break;
	                }
	              }
	            tmp.append(wrap[x-1]);

	            }
	            stat[x]=new_node;
	            wrap[x-1].append(new_node);
	            }
	            for (var i=x+1;i<6;i++){
	              stat[i]=0;
	              wrap[i-1]=0;
	            }
	      });
	    return out;
	  }

	module.exports={
		build_index:build_index,
	}

/***/ },
/* 5 */
/***/ function(module, exports) {

	
	function myimport() {
		var url=[
		'<script src="http://apps.bdimg.com/libs/SyntaxHighlighter/3.0.83/scripts/shCore.min.js"></script>',
		'<script src="http://apps.bdimg.com/libs/SyntaxHighlighter/3.0.83/scripts/shAutoloader.min.js"></script>',
		'<link rel="stylesheet" href="http://apps.bdimg.com/libs/SyntaxHighlighter/3.0.83/styles/shCore.min.css">',
	'<link rel="stylesheet" href="http://apps.bdimg.com/libs/SyntaxHighlighter/3.0.83/styles/shThemeDefault.min.css">']
		for(var i=0;i<url.length;i++){
			document.write(url[i])
		}
	}
	 function path() {
	        var args = arguments,
	        result = [];
	        for (var i = 0; i < args.length; i++){
		        var tmp=args[i].replace('$', 'http://apps.bdimg.com/libs/SyntaxHighlighter/3.0.83/scripts/')
		        result.push(tmp.replace('.js','.min.js'));
		        
	        }
	        return result
	    }
	    
	function autoload() {
		SyntaxHighlighter.vars.discoveredBrushes=null; // 对于动态内容极为重要，迫使syntax重新查看页面，重新load brush
		 SyntaxHighlighter.autoloader.apply(null, path(
	            'applescript            $shBrushAppleScript.js',
	            'actionscript3 as3      $shBrushAS3.js',
	            'bash shell             $shBrushBash.js',
	            'coldfusion cf          $shBrushColdFusion.js',
	            'cpp c                  $shBrushCpp.js',
	            'c# c-sharp csharp      $shBrushCSharp.js',
	            'css                    $shBrushCss.js',
	            'delphi pascal          $shBrushDelphi.js',
	            'diff patch pas         $shBrushDiff.js',
	            'erl erlang             $shBrushErlang.js',
	            'groovy                 $shBrushGroovy.js',
	            'java                   $shBrushJava.js',
	            'jfx javafx             $shBrushJavaFX.js',
	            'js jscript javascript  $shBrushJScript.js',
	            'perl pl                $shBrushPerl.js',
	            'php                    $shBrushPhp.js',
	            'text plain             $shBrushPlain.js',
	            'py python              $shBrushPython.js',
	            'ruby rails ror rb      $shBrushRuby.js',
	            'sass scss              $shBrushSass.js',
	            'scala                  $shBrushScala.js',
	            'sql                    $shBrushSql.js',
	            'vb vbnet               $shBrushVb.js',
	            'xml xhtml xslt html    $shBrushXml.js'
	        ));
	}


	 function  adapt_ck() {
		/*
		ckeditor输入的内容为:<pre><code class='language-python'></code></pre>
		需要调整为<pre class='brush:python'></pre>
		*/
	 	$('code[class^="language-"]').each(function () {
		 	var lan=/language-(\w+)/.exec($(this).attr('class'))
			$(this).parent().addClass('brush:'+lan[1])
			$(this).parent().html($(this).html())
		})
	 }
	 function load_all_brush() {
		 // load all brush
		 // 由于解决了autoload的问题，所以这个函数没用了。留在这里作为纪念
		 var brushs=['Python','JScript','Bash']
		 for (var i =0;i<brushs.length;i++){
			document.write('<script src="http://apps.bdimg.com/libs/SyntaxHighlighter/3.0.83/scripts/shBrush'+brushs[i]+'.min.js"></script>')
		 }
	 	
	 }
	 function all() {
	 	SyntaxHighlighter.all();
	 }
	 function highlight() {
		 // all()是监听的load事件，能够和autoloader配合使用，但是如果要自己手动刷新，就需要使用这个函数
	 	SyntaxHighlighter.highlight()
	 }
	module.exports={
			myimport:myimport,
			autoload:autoload,
			adapt_ck:adapt_ck,
			all:all,
			load_all_brush:load_all_brush,
			highlight:highlight,
		}

/***/ }
/******/ ]);