
//document.write('<script src="https://cdnjs.cloudflare.com/ajax/libs/angular.js/1.4.6/angular.min.js"></script>')
//document.write("<div style='display:none' ng-app='he'><span ng-controller='hole' id='hole'></span></div>")




var app = angular.module('he',[]);
app.config(function($interpolateProvider) {
	  $interpolateProvider.startSymbol('$[[');
	  $interpolateProvider.endSymbol(']]^');
});
var agc=require('agcompile')
agc.input_hole()
app.controller('hole',function ($scope) {
	$scope.wo='wold';
	$scope.src_type=$('#id_type').val();
	$scope.src=$('#id_src').val();
})
compileAngularElement=agc.compileAngularElement
CKEDITOR.timestamp='ABCDFD';
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