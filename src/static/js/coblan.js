function clear_sel() {
			if (window.getSelection) {
			  if (window.getSelection().empty) {  // Chrome
			    window.getSelection().empty();
			  } else if (window.getSelection().removeAllRanges) {  // Firefox
			    window.getSelection().removeAllRanges();
			  }
			} else if (document.selection) {  // IE?
			  document.selection.empty();
			}
		}
function dragable(el) {
	var wrap =$("<div style='position:absolute'><div class='title' style='height:25px;background-color:#f5f5f5;border-bottom:1px solid #e5e5e5;cursor:move'></div></div>")
	wrap.insertBefore(el)
	//el.detach()
	wrap.append(el)
	//el.css({position:'absolute'})
	//el.prepend('<div class="title" style="height:25px;background-color:#f5f5f5;border-bottom:1px solid #e5e5e5;cursor:move"></div>')
	var is_down=false
	var det_x=0
	var det_y=0
	wrap.children(".title").bind('mousedown',function (e) {
		is_down=true
		var div_x = wrap.offset().left
		var div_y= wrap.offset().top
		det_x = e.pageX - div_x
		det_y = e.pageY - div_y
	})
	$(document).bind('mousemove',function (e) {
		if(is_down){
			wrap.css({
				       left: e.pageX - det_x, //e.clientX -det_x,
				       top:  e.pageY -det_y, //e.clientY - det_y,
				    })
			clear_sel()
		}
	})
	$(document).bind('mouseup',function () {
		is_down=false
	})
}
function sizeable(el) {
	el.append('<div class="size_block" style="position:absolute;bottom:0px;right:0px;background-color:black;width:10px;height:10px;cursor:se-resize;clear:both"></div>')
	is_down=false
	var old_x = 0
	var old_y = 0
	el.children(".size_block").bind('mousedown',function (e) {
		is_down=true
		old_x = e.pageX
		old_y = e.pageY
	})
	$(document).bind('mousemove',function (e) {
		if(is_down){
			var det_x = e.pageX-old_x
			var det_y = e.pageY-old_y
			old_x = e.pageX
			old_y = e.pageY
			el.width(el.width()+det_x)
			el.height(el.height()+det_y)
			clear_sel()
			e.stopPropagation();
		}
	})
	$(document).bind('mouseup',function () {
		is_down=false
	})
}
