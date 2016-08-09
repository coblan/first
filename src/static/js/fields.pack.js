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

	'use strict';

	Object.defineProperty(exports, "__esModule", {
	    value: true
	});
	exports.field = field;
	exports.merge = merge;

	var _color = __webpack_require__(1);

	function is_valid(form_fun_rt, errors_obj, callback) {
	    if (form_fun_rt) {
	        if (form_fun_rt.errors) {
	            for (x in errors_obj) {
	                Vue.delete(errors_obj, x);
	            }
	            for (x in form_fun_rt.errors) {
	                Vue.set(errors_obj, x, form_fun_rt.errors[x]);
	            }
	        } else {
	            callback();
	        }
	    }
	} /*
	  * 正常field:
	  * field()
	  * 水平field:
	  * field({template:field_str('horizon'),name:'horizon-field'})
	  * */

	/*
	*配合自家的jsonpost使用，效果最好
	*/

	/*
	自动处理form.errors
	$.post('',JSON.stringify(post_data),function (data) {
		is_valid(data.do_login,self.meta.errors,function () {
			location=next;
	})
	*/

	var normal_str = '\n<div for=\'field\' class="form-group" :class=\'{"error":error_data(name)}\'>\n\t<label :for="\'id_\'+name" v-text="head.label"><span class="req_star" v-if=\'head.required\'> *</span>\n\t</label>\n\t<component :is=\'head.type\'\n\t\tv-model=\'row[name]\'\n\t\t:name=\'name\'\n\t\t:id="\'id_\'+name"\n\t\t:placeholder=\'head.placeholder\'\n\t\t:autofocus=\'head.autofocus\'\n\t\t:maxlength=\'head.maxlength\'>\n\t</component>\n\t<slot> </slot>\n\t<div v-text=\'error_data(name)\' class=\'error\'></div>\n\n</div>\n';

	function field_str() {
	    var orient = arguments.length <= 0 || arguments[0] === undefined ? 'normal' : arguments[0];
	    var label_cls = arguments.length <= 1 || arguments[1] === undefined ? 'col-md-3' : arguments[1];
	    var input_cls = arguments.length <= 2 || arguments[2] === undefined ? 'col-md-9' : arguments[2];

	    if (orient == 'normal') {
	        return normal_str;
	    } else {
	        return '\n<div for=\'field\' class="form-group" :class=\'{"error":error_data(name)}\'>\n\t<label :for="\'id_\'+name" v-text="head.label" class="' + label_cls + '  control-label"><span class="req_star" v-if=\'head.required\'> *</span>\n\t</label>\n\t<div class="' + input_cls + '">\n        <component :is=\'head.type\'\n            :val.sync=\'row[name]\'\n            :name=\'name\'\n            :id="\'id_\'+name"\n            :placeholder=\'head.placeholder\'\n            :autofocus=\'head.autofocus\'\n            :maxlength=\'head.maxlength\'>\n        </component>\n\t</div>\n\t<slot> </slot>\n\t<div v-text=\'error_data(name)\' class=\'error\'></div>\n\n</div>\n';
	    }
	}

	function field() {
	    var _ref = arguments.length <= 0 || arguments[0] === undefined ? {} : arguments[0];

	    var _ref$template = _ref.template;
	    var template = _ref$template === undefined ? field_str() : _ref$template;
	    var _ref$name = _ref.name;
	    var name = _ref$name === undefined ? 'field' : _ref$name;

	    /*
	     使用的meta结构
	     meta={
	     errors:{},
	     row:{
	     username:'',
	     password:'',
	     pas2:'',
	     },
	     heads:[
	     {name:'username',label:'用户名',type:'text',required:true,autofocus:true},
	     ]
	     }
	       <field name='username' :meta='meta'></field>
	       */
	    Vue.component(name, {
	        template: template,
	        props: ['name', 'kw'],
	        //data: function () {
	        //    var heads = this.meta.heads
	        //    //var head=''
	        //    for (var head  of heads) {
	        //        if (head.name == this.name) {
	        //            //head = x
	        //            break
	        //        }
	        //    }
	        //    return {
	        //        head: head,
	        //        row: this.meta.row,
	        //        errors: this.meta.errors,
	        //    }
	        //},
	        computed: {
	            row: function row() {
	                return this.kw.row;
	            },
	            errors: function errors() {
	                return this.kw.errors;
	            },
	            head: function head() {
	                var heads = this.kw.heads;
	                //var head=''
	                var _iteratorNormalCompletion = true;
	                var _didIteratorError = false;
	                var _iteratorError = undefined;

	                try {
	                    for (var _iterator = heads[Symbol.iterator](), _step; !(_iteratorNormalCompletion = (_step = _iterator.next()).done); _iteratorNormalCompletion = true) {
	                        var head = _step.value;

	                        if (head.name == this.name) {
	                            //head = x
	                            return head;
	                        }
	                    }
	                } catch (err) {
	                    _didIteratorError = true;
	                    _iteratorError = err;
	                } finally {
	                    try {
	                        if (!_iteratorNormalCompletion && _iterator.return) {
	                            _iterator.return();
	                        }
	                    } finally {
	                        if (_didIteratorError) {
	                            throw _iteratorError;
	                        }
	                    }
	                }
	            }
	        },
	        methods: {
	            error_data: function error_data(name) {
	                if (this.errors[name]) {
	                    return this.errors[name];
	                } else {
	                    return '';
	                }
	            }
	        },
	        components: {
	            text: {
	                props: ['name', 'val'],
	                template: '<input type="text" class="form-control" v-model="val">'
	            },
	            password: {
	                props: ['name', 'val'],
	                template: '<input type="password" class="form-control" v-model="val">'
	            },
	            area: {
	                props: ['name', 'val'],
	                template: '<textarea class="form-control" rows="3" v-model="val"></textarea>'
	            },
	            color: {
	                props: ['name', 'val'],
	                //data:function(){
	                //    return {
	                //        val:''
	                //    }
	                //},
	                template: '<input type="text" v-model="val">',
	                //computed:{
	                //    val:function(){
	                //        if($(this.$el).val()){
	                //            return $(this.$el).val()
	                //        }else{
	                //            return '#000'
	                //        }
	                //    }
	                //},
	                watch: {
	                    'val': function val() {
	                        this.sync_to_spec();
	                    }
	                },
	                methods: {
	                    sync_to_spec: function sync_to_spec() {
	                        var self = this;
	                        Vue.nextTick(function () {
	                            $(self.$el).spectrum({
	                                color: this.val,
	                                showInitial: true,
	                                showInput: true,
	                                preferredFormat: "name"
	                            });
	                        });
	                    }
	                },
	                compiled: function compiled() {
	                    this.sync_to_spec();
	                }
	            }
	        }
	    });
	}

	function update_vue_obj(vue_obj, obj) {
	    for (var _x5 in vue_obj) {
	        Vue.delete(vue_obj, _x5);
	    }
	    for (var _x6 in obj) {
	        Vue.set(vue_obj, _x6, obj[_x6]);
	    }
	}

	function merge(mains, subs) {
	    var _iteratorNormalCompletion2 = true;
	    var _didIteratorError2 = false;
	    var _iteratorError2 = undefined;

	    try {
	        for (var _iterator2 = sub[Symbol.iterator](), _step2; !(_iteratorNormalCompletion2 = (_step2 = _iterator2.next()).done); _iteratorNormalCompletion2 = true) {
	            var _sub = _step2.value;
	            var _iteratorNormalCompletion3 = true;
	            var _didIteratorError3 = false;
	            var _iteratorError3 = undefined;

	            try {
	                for (var _iterator3 = mains[Symbol.iterator](), _step3; !(_iteratorNormalCompletion3 = (_step3 = _iterator3.next()).done); _iteratorNormalCompletion3 = true) {
	                    var main = _step3.value;

	                    if (main.name == _sub.name) {
	                        for (var k in _sub) {
	                            main[k] = _sub[k];
	                        }
	                        break;
	                    }
	                }
	            } catch (err) {
	                _didIteratorError3 = true;
	                _iteratorError3 = err;
	            } finally {
	                try {
	                    if (!_iteratorNormalCompletion3 && _iterator3.return) {
	                        _iterator3.return();
	                    }
	                } finally {
	                    if (_didIteratorError3) {
	                        throw _iteratorError3;
	                    }
	                }
	            }
	        }
	    } catch (err) {
	        _didIteratorError2 = true;
	        _iteratorError2 = err;
	    } finally {
	        try {
	            if (!_iteratorNormalCompletion2 && _iterator2.return) {
	                _iterator2.return();
	            }
	        } finally {
	            if (_didIteratorError2) {
	                throw _iteratorError2;
	            }
	        }
	    }
	}
	window.use_color = _color.use_color;
	window.field_str = field_str;
	window.field = field;
	window.merge = merge;

/***/ },
/* 1 */
/***/ function(module, exports) {

	"use strict";

	Object.defineProperty(exports, "__esModule", {
	    value: true
	});
	exports.use_color = use_color;
	function use_color() {
	    if (!window._color) {
	        window._color = true;
	        document.write("<script src=\"http://cdn.bootcss.com/spectrum/1.8.0/spectrum.min.js\"></script>");
	        document.write("<link href=\"http://cdn.bootcss.com/spectrum/1.8.0/spectrum.min.css\" rel=\"stylesheet\">");
	    }
	}

/***/ }
/******/ ]);