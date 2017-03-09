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
	//window.app=require('ag').app
	window.hx=__webpack_require__(3)
	var syntax=__webpack_require__(4)
	syntax.myimport() 
	window.syntax=syntax

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
/* 4 */
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