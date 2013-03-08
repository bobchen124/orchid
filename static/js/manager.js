var M = {
		ias : null,
		w : null,
		h : null,
		img : '',
		au : [],
		selection : null,
		fg : null,
		
		invoke : function(action, param, sf) {
			//var url_href = "http://" + window.location.host +"/live/love/";
			var url_href = "http://" + window.location.host + action;
			$.ajax({
				url : url_href,
				dataType:'json',
				type:'post',
				timeout : 5000,
				//data:{'roomid':rid,'uid':uid},
				data : param,
				error : function() {
					M.errorMsg('操作失败');
				},
				success : sf
			});
		},
		
		login : function() {
			var n = $('#tab_name').val();
			var p = $('#tab_pass').val();
			if (n == '') {
				M.alertMsg('用户名不能为空');
				$('#tab_name').focus();
				return;
			}
			
			M.invoke('/manage/login/', {'name':n,'pwd':p}, loginSuccess);
		},
		
		tipMsg : function(msg) {
			var opts = {};
			opts.classes = ['gray','pushpin'];
			opts.autoHideDelay = 5000;
			opts.hideStyle = {
				opacity: 0,
				left: "400px"
			};
			opts.showStyle = {
				opacity: 1,
				left: 0
			};
			$('#freeow-tr').freeow('提示', msg, opts);
		},
		
		alertMsg : function(msg) {
			var opts = {};
			opts.classes = ['gray'];
			opts.autoHideDelay = 5000;
			opts.hideStyle = {
					opacity: 0,
					left: "400px"
			};
			opts.showStyle = {
					opacity: 1,
					left: 0
			};
			$('#freeow-tr').freeow('警告', msg, opts);
		},
		
		errorMsg : function(msg) {
			var opts = {};
			opts.classes = ['gray', 'slide', 'error'];
			opts.autoHideDelay = 5000;
			opts.hideStyle = {
				opacity: 0,
				left: "400px"
			};
			opts.showStyle = {
				opacity: 1,
				left: 0
			};
			$('#freeow-tr').freeow('错误', msg, opts);
		},
		
		currentTime : function() {
			var d = new Date();
			return d.format("yyyy-MM-dd hh:mm");
			//var ret = d.getFullYear()+ "-"; 
			//ret += ( "00 "+ (d.getMonth()+1)).slice(-2)+ "-"; 
			//ret += ( "00 "+ d.getDate()).slice(-2)+ " "; 
			//ret += ( "00 "+ d.getHours()).slice(-2)+ ":"; 
			//ret += ( "00 "+ d.getMinutes()).slice(-2);
			//return ret;
		},
		
		openImgUploadDialog : function() {
			$("#upload_dialog").dialog('open');
		},
		
		preview: function(img, selection) {
		    if (!selection.width || !selection.height)
		        return;
		    
		    var scaleX = 160 / selection.width;
		    var scaleY = 120 / selection.height;
		    
		    $('#preview img').css({
		        width: Math.round(scaleX * 400),
		        height: Math.round(scaleY * 300),
		        marginLeft: -Math.round(scaleX * selection.x1),
		        marginTop: -Math.round(scaleY * selection.y1)
		    });
		    
		    M.w = Math.round(scaleX * 400);
		    M.h = Math.round(scaleY * 300);
		},
		
		saveCover : function() {
			if (M.img == null || M.selection == null) {
				M.errorMsg("先选择一张图片！");
				return;
			}
			//var p = '';
			var name = M.img;
			var x1 = M.selection.x1;
			var y1 = M.selection.y1;
			var x2 = M.selection.x2;
			var y2 = M.selection.y2;
			var w = M.w;
			var h = M.h;
			//alert(x1 + "=" + y1 + "=" + x2 + "=" + y2 + "=" + w + "=" + h);
			//p += M.img +',' + M.selection.x1 + ',' + M.selection.y1 + ',' + M.selection.x2 + ',' + M.selection.y2 + ',';
			//p += M.w + ',' + M.h;
			//M.invoke("dataHelper", "saveCover", p, M.showCover);
			M.invoke('/manage/upload/imagecut/', {'name':name,'x':x1,'y':y1,'w':x2,'h':y2},  M.showCover);
		},
		
		closeUploadDialog : function() {
			$("#upload_dialog").dialog('close');
		},
		
		showCover : function() {
			M.closeUploadDialog();
			var s = M.img;
			//s = s.replace("-cover", "-real");
			s = '/static/upload/live/' + s;
			$('#select_cover_img').attr('src', s);
		},
		
		validNum : function(){
			var v = $('#romm_num').val();
			if(v != null && v != ''){
				v = v * 1;
				if(v > 1000){
					$('#romm_num').val('10');
					M.alertMsg('房间最多1000人！');
				}
				if(v == 0){
					$('#romm_num').val('10');
					M.alertMsg('房间0个人没有意义！');
				}
			}
		},
		
		isEmpty : function(s){
			var b = false;
			if(s == null || s == ''){
				b = true;
			}
			return b;
		},
		
		save : function() {
			var courseName = $('#course_name').val();
			if(M.isEmpty(courseName)) {
				M.errorMsg('填写课程名称！');
				$('#course_name').focus();
				return;
			}
			var openTime = $('#open_time').val()+'';
			if(M.isEmpty(openTime)) {
				M.errorMsg('选择开放时间！');
				$('#open_time').focus();
				return;
			}
			var time = $('#time').val();
			//var courseIntro = $('#course_intro').val();
			var courseIntro = editor.getContent();
			
			var cover = M.img;
			if(M.isEmpty(cover)) {
				M.errorMsg('上传封面！');
				return;
			}
			var rommNum = $('#romm_num').val();
			if(M.isEmpty(rommNum)){
				M.errorMsg('输入人数！');
				$('#romm_num').focus();
				return;
			}
			var roomAdmin = $('#romm_admin').val();
			if(M.isEmpty(roomAdmin)) {
				M.errorMsg('输入管理员！');
				$('#romm_admin').focus();
				return;
			}
			//if(jQuery.inArray(roomAdmin, M.au) == -1) {
				//M.errorMsg('你输入的管理员不存在！');
				//$('#romm_admin').focus();
				//return ;
			//}
			var courseClass = $('#course_class').val();
			if (M.isEmpty(courseClass)) {
				M.errorMsg('选择一个类别！');
				$('#course_class').focus();
				return;
			}
		
			var p={"courseName":courseName,"openTime":openTime,"time":time,"courseIntro":courseIntro,"cover":cover,"roomAdmin":roomAdmin,"courseClass":courseClass,"rommNum":rommNum};
			//p = encodeURIComponent(p);
			M.invoke("/manage/create/room/", p, M.saveSuccess);
			//M.invoke('/manage/upload/imagecut/', {'name':name,'x':x1,'y':y1,'w':w,'h':h},  M.showCover);
		},
		
		saveSuccess : function(data) {
			//alert(data.result);
			if (data.result) {
				M.alertMsg('成功添加课程！');
			}
		},
		
		saveUser : function() {
			var uid = $('#user_id').val();
			var name = $('#user_name').val();
			if(M.isEmpty(uid)) {
				M.errorMsg('请填写用户名ID！');
				$('#user_id').focus();
				return;
			}
			
			if(M.isEmpty(name)) {
				M.errorMsg('请填写用户名！');
				$('#user_name').focus();
				return;
			}
			//alert(uid +'--'+ name);
			M.invoke('/manage/add/user/', {'name':name,'uid':uid}, M.saveUserSuccess);
		},
		
		saveUserSuccess : function(data) {
			if (data.result) {
				M.alertMsg('成功添加用户！');
			}
		},
		
		queryCourse : function() {
			M.invoke("dataHelper", "getCourse", 0, function(d){M.alertMsg(d);});
		},
		
		getAu : function(){
			M.invoke("dataHelper", "getAu", null, M.setAu);
		},
		
		setAu : function(data) {
			M.au = eval('('+data+')');
			$('#romm_admin').autocomplete({
				source : M.au
			});
		},
		
		delC : function(com, grid) {
			var selected_count = $('.trSelected', grid).length;
			if(selected_count == 0){
				M.alertMsg("请选择一条记录！");
				return;
			}
			
			if (com == '删除') {
				if(confirm('确定删除？')){
					var selectes = '';
					var s = $('.trSelected td:nth-child(1) div',grid);
					//for(var i=0; i<s.length; i++) {
					selectes = $(s[0]).text();
					//}
//					$('.trSelected td:nth-child(1) div',grid).each(function(i){
//						if(i){
//							ii =i;
//							selectes += $(this).text()+',';
//						}
//					});
					
					M.invoke("/manage/room/delete/", {"roomId":selectes}, function() {
						M.alertMsg('成功删除 !');
						M.fg[0].grid.populate();
					});
					
					//M.invoke('/manage/upload/imagecut/', {'name':name,'x':x1,'y':y1,'w':x2,'h':y2},  M.showCover);
				}
			}
		}
};

var loginSuccess = function(data) {
	data = eval(data);
	if (data.result == 'ok') {
		$('#login_div').dialog("close");
		$('#tabs').show();
		$('#create_btn').removeClass('ui-state-default');
		$('#create_btn').bind('click', M.save);
	} else {
		M.alertMsg('用户名或密码不对！');
		$('#tabs').hide();
	}
};

Date.prototype.format = function(format) {
    var o = {
    	"M+" : this.getMonth()+1, //month
    	"d+" : this.getDate(),    //day
    	"h+" : this.getHours(),   //hour
    	"m+" : this.getMinutes(), //minute
    	"s+" : this.getSeconds(), //second
    	"q+" : Math.floor((this.getMonth()+3)/3),  //quarter
    	"S" : this.getMilliseconds() //millisecond
    }
    
    if(/(y+)/.test(format)) {
    	format=format.replace(RegExp.$1,(this.getFullYear()+"").substr(4 - RegExp.$1.length));
    }
    	
    for(var k in o) {
    	if(new RegExp("("+ k +")").test(format)) {
    		 format = format.replace(RegExp.$1,RegExp.$1.length==1 ? o[k] : ("00"+ o[k]).substr((""+ o[k]).length));
    	}
    }
   
    return format;
}

var u = {
		auto : true,
		swf : '/static/plugins/uploadify/uploadify.swf?t=' + new Date().getTime(),
		uploader : "http://" + window.location.host + '/manage/upload/image/',
		queueID        : 'fileQueue',
		multi          : false, 
		fileTypeDesc   : '图片文件',
		fileTypeExts   : '*.jpg;*.png;*.gif;*.jpeg',
		buttonImage : '/static/plugins/img_upload.png',
		//buttonClass : 'uub-album-createbtn',
		//fileType     : 'image',
		fileSizeLimit : '3MB',
		//queueSizeLimit : 4,
		removeTimeout : 1,
		width : 155,
		height : 33,
		onUploadStart:function(queueData) {
//			$('#uploadify_select_btn').uploadify('disable', true);
//			 $('#uploadify_select_btn-button').hide();
			if (M.ias != null) {
				M.ias.cancelSelection();
			}
		},
		onQueueComplete:function(queueData) {
			
		},
		
		onUploadSuccess : function(file, data, response) {
			if (response) {
				$('#cover_img_div p').hide();
				var imgsrc = '/static/upload/temp/' + data;
				M.img = data + "";
				var img = '<img id="'+data+'" class="cover_src_preview" src="'+imgsrc+'"/>';
				$('#local_img').empty();
				$('#local_img').append(img);
				//$('#local_img>img').css('width', "400px");
				//$('#local_img>img').css('height', "300px");
				
				$('#preview img').attr('src', imgsrc);
				
				M.ias = $('#local_img>img').imgAreaSelect({
					instance:true,
			        handles: true,
			        aspectRatio: '4:3',
			        x1: 120, y1: 90, x2: 280, y2: 210,
			        onSelectChange: M.preview,
			        onSelectEnd : function(img, selection) {
			        	M.selection = selection;
			        }
			    });
				
				var i = new Image();
				i.src = imgsrc;
				i.onload = function() {
					var h = i.height;
					if (h < 300) {
						h = 300 - h;
						h = h / 2;
						$('#local_img>img').css('margin-top', h+"px");
					}
				};
			}
		}
};

$(function() {
	$("#login_div").dialog({
        autoOpen: true,
        modal: true,
        closeOnEscape: false,
        buttons: {
            '登录': function () {
                M.login();
            }
        },
        open : function(){
        	$('#tab_name').focus();
//        	$('.ui-dialog-titlebar-close').removeClass('ui-dialog-titlebar-close');
//        	$('span > .ui-icon').removeClass('ui-icon');
        	$('a.ui-dialog-titlebar-close').remove();
        },
        close : function(){
        	$('#login_form')[0].reset();
        }
    });
	
	$('#login_div').parent().addClass('sh');
	$('#tabs').tabs();
	$('#tab_pass').keypress(function(e){
		switch(e.which){
			case 13:
				M.login();
				break;
		}
	});
	
	$('#open_time').datetimepicker({
		dateFormat : 'yy-mm-dd',
		timeFormat : 'hh:mm',
		dayNames:['星期日','星期一','星期二','星期三','星期四','星期五','星期六'],
		dayNamesMin : ['日','一','二','三','四','五','六'],
		monthNames : ['一月','二月','三月','四月','五月','六月','七月','八月','九月','十月','十一月','十二月'],
		prevText : '往前',
		nextText:'往后',
		defaultValue : M.currentTime(),
		minDateTime : new Date()
	});
	
	$('button').button();
	
	$("#upload_dialog").dialog({
        autoOpen: false,
        modal: true,
        width:800,
        height:500,
        closeOnEscape: false,
        buttons: {
           '保存' : function() {
        	   M.saveCover();
           },
           
           '取消' : function() {
        	   M.closeUploadDialog();
           }
        },
        open : function() {
        	$('#local_img').show();
        	$('#preview').show();
        	$('#cover_img_div p').show();
        },
        close : function(){
        	$('#preview img').attr('src', "");
        	$('#preview').hide();
        	$('#local_img').empty();
        	$('.imgareaselect-outer').remove();
        	M.ias.cancelSelection();
        }
    });
	
	$('#uploadify_select_btn').uploadify(u);
	
	//M.getAu();
	//M.au = ["ActionScript", "AppleScript", "Asp", "BASIC", "C", "C++", "Clojure", "COBOL", "ColdFusion", "Erlang", "Fortran", "Groovy", "Haskell", "Java", "JavaScript", "Lisp", "Perl", "PHP", "Python", "Ruby", "Scala", "Scheme"];
});
