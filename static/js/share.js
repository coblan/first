var ck=require('editor/ckeditor')
ck.import()

app = angular.module('share',['ngSanitize']);
app.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('[[');
  $interpolateProvider.endSymbol(']]');
});
app.directive('nameForm',function () {
	return {
		restrict:'EA',
		scope:{
			submit:'&',
			item:'='
		},
		template:'<form name="nameForm" ng-submit="submit({valid:nameForm.$valid})" novalidate >\
						<div class="form-group">\
							<label>名称</label>\
							<input class="form-control" type="text" name="name" value="" ng-model="item.name" required/>\
							<span ng-show="nameForm.name.$error.required">必填</span>\
							<input type="submit" name="test" value="提交" />\
						</div>\
					</form>'
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



//app.directive('editForm',function ($timeout) {
//		function get_value(item) {
//				item.content=editor.html();
//				return item;
//	};
//	return {
//		restrict: 'EA',
//		scope:{
//			item:'=',
//			submit:'&',
//			cancel:'&',
			
//		},
//		template:'<form name="myForm" ng-submit="submit({valid:myForm.$valid,file:get_value(item)})" novalidate >\
//						<div class="form-group">\
//							<label>标题</label>\
//							<input class="form-control" type="text" name="name" value="" ng-model="item.name" required/>\
//							<span ng-show="myForm.name.$error.required">必填</span>\
//						</div>\
//						<div class="form-group">\
//							<label>内容</label>\
//						<textarea id="editor_id" class="form-control" class="form-control" name="ri"  ></textarea>\
//						</div>\
//						<input type="submit" name="test" value="提交" />\
//						<button name="test" type="button" value="val" ng-click="cancel()">取消</button>\
//						</form>',
//		link :function (scope,iElem, iAttrs) {
//			$timeout(function () {
//				 //KindEditor.ready(function(K) {
//                //window.editor = K.create('#editor_id');
                
//                editor = KindEditor.create(iElem.find('#editor_id'));
//                editor.html(scope.item.content);
//          		scope.get_value=get_value;
//			})
			
//        },
//		}
//});
