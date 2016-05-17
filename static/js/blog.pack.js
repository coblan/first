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

	//var img_tool=require('dosome/img')
	//$(function () {
	//	img_tool.ratio($('.ban-img'))
		
	//})

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

/***/ }
/******/ ]);