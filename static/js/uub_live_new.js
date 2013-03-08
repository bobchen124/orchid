var LiveHandler = {
	//xhr : null,
		
	init : function() {
		//this.xhr = this.createXHR();
		this.clickHandler();
	},
	
	createXHR : function() {
		var xhr = null;
		if(window.XMLHttpRequest){
			xhr = new XMLHttpRequest();
		} else if(window.ActiveXObject) {
			xhr = new ActiveXObject("Microsoft.XMLHTTP");
		}
		return xhr; 
	},
	
	/**
	 * 增加单击事件
	 */
	clickHandler : function() {
		$(".love_icon").bind("click",function() {
			var rid = $(this).attr('room-id');
			var uid =  $('#userid').val();
			LiveHandler.loveLive($(this),rid,uid,LiveHandler.loveRoom);
		});
		
		$(".like_course").bind("click",function() {
			var uid =  $('#userid').val();
			var rid =  $('#roomid').val();
			LiveHandler.loveLive($(this),rid,uid,LiveHandler.loveCourse);
		});
	},
	
	loveLive : function(obj,rid,uid,sucess) {
		var url_href = "http://" + window.location.host +"/live/love/";
		//alert(action);
		$.ajax({
			url:url_href, 
			dataType:'json',
			type:'post',
			data:{'roomid':rid,'uid':uid},
			success:function(json) {
				sucess(obj)
			},
			error:function() {
				sucess(obj)
			}
		});
	},
	
	loveRoom : function(obj) {
		obj.hide();
		obj.prev().show();
	},
	
	loveCourse :function(obj) {
		obj.hide();
		obj.prev().show();
		var num =  $('#sign_num').html();
		//alert(num);
		$('#sign_num').html(parseInt(num) + 1);
	}
 }

$(document).ready(function() {
	LiveHandler.init();
});
