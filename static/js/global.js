(function($) {

	$.global = {

		init: function() {
			
			var $userAccount = $("#header .user_account"),
				$menuListAndArrowWrap = $(".menu_list_and_arrow_wrap"),
				$leaveMsgTrigger = $('#footer a.contact'),
				$anonymousLogin = $('#anonymous-login'),
				$searchForm = $('#header #search_form'),
				$searchInput = $('#header #search_text');
			
			$('input').placeholder();
			
			$('.message_datail_wrap li a').click(function(){
				$(this).parent().hide(); 
			});
			
			
			/*榧犳爣鎸囧悜澶村儚寮瑰嚭涓汉璁剧疆娴眰*/
			$userAccount.hover(function() {
				$menuListAndArrowWrap.stop(true,true); 
				$menuListAndArrowWrap.css("opacity","1").show();
			},function(){
				$menuListAndArrowWrap.delay(500).animate({'opacity':0}, 0, function(){
					$menuListAndArrowWrap.hide();
				}); 
			});
			
			/*榧犳爣浠庡ご鍍忕Щ鍒板拰绉诲嚭涓汉璁剧疆娴眰*/
			$menuListAndArrowWrap.live('mouseenter',function(){
				$(this).stop(true, true);
			}).live("mouseleave", function(){
				$(this).delay(400).animate({'opacity':0}, 0, function(){
					$(this).hide();
				});
			}); 
			
			/*榧犳爣鎸囧悜鍜岀Щ鍑轰釜浜鸿缃诞灞傜殑姣忎釜杩炴帴*/
			$('#menu_list li a').hover(function(){
				$(this).css({'background-color':'#27b5f2','color':'#fff'});
			},function(){
				$(this).css({'background-color':'#fff','color':'#888'});
			});
			
			$searchForm.submit(function() {

		    	if($.trim($searchInput.val()) == '') {
		    		
					$searchInput.css('background', '#f5cfcf');
					$searchInput.animate({
						opacity: 0.3
					}, 300, function() {
						$searchInput.css('background','none').css('opacity', '1');
					});
					return false;
				}
				return true;
			});
			
			$leaveMsgTrigger.wokaobox({
				'width'			: 500,
				'height'		: 360,
				'href'			: [$.global.getContextPath(), '/feedback'].join(''),
				'type'			: 'iframe',
				'openMethod'	: 'changeUp',
				'closeMethod'	: 'changeOut'
			});
			
			$anonymousLogin.wokaobox({
				'width'			: 582,
				'height'		: 290,
				'type'			: 'iframe',
				'openMethod'	: 'changeIn',
				'closeMethod'	: 'changeOut'
			});
		},
		
		getNewMessages: function(){
			
			var newPrivateMessage = $('.private_message', $('#header')),
				newInformation = $('.information',$('#header')),
				newFans = $('.fans',$('#header')),
				newNotice = $('.notice', $('#header')),
				spanOfMessageSum = $('.messages_sum',$('#header')),
				spanOfNewCourseSum = $('.new_course_sum',$('#header')),
				messageDatailWrap = $('.message_datail_wrap',$('#header')),
				curMessageCount = 0,
				closeNotice=$('.close_message_datail_wrap').attr('close-data'),
				closeClick = false;
				
				interval = setInterval(function(){
					getMessages();
				},60000),
			
				getMessages = function(){
				
					$.ajax({
						url: $.global.getContextPath() + '/push/message/count',
						type:'GET',
						dataType:'json',
						beforeSend: function (xhr) {
					        xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest");
					   	},
					  	statusCode: {
							403: function() {
								 window.clearInterval(interval);
							}
						},
						success:function(json){
							//娑堟伅涓績杞
							if(json.totalCount > 0){
								spanOfMessageSum.text(json.totalCount).show(); 
								
								if(json.incPrivateMessageCount > 0){
									newPrivateMessage.find('.header_message_num').text(json.incPrivateMessageCount);
									newPrivateMessage.show();
								}
								else{
									newPrivateMessage.hide();
								}
								
								if(json.incMessageCount > 0){
									newInformation.find('.header_infomation_num').text(json.incMessageCount);
									newInformation.show();
								}
								else{
									newInformation.hide();
								}
								
								if(json.incNoticeCount > 0){
									newNotice.find('.header_notice_num').text(json.incNoticeCount);
									newNotice.show();
								}
								else{
									newNotice.hide(); 
								}
								
								if(json.incFansCount > 0){
									newFans.find('.header_fans_num').text(json.incFansCount);
									newFans.show();
								}
								else{
									newFans.hide();
								}
								
//								鍒ゆ柇鏄惁鏄剧ず娴眰
								if((closeClick == false) || (closeClick == true && json.totalCount > curMessageCount)){
									if(closeNotice){
										messageDatailWrap.hide();
									}
									else{
										messageDatailWrap.show();
									}
								}
								
								else{
									messageDatailWrap.hide();
								}
							}
							else{
								spanOfMessageSum.hide();
								messageDatailWrap.hide();
							}
							
							//鎴戠殑璇剧▼琛ㄨ疆璇�
							if(json.incScheduleCourseCount > 0){
								spanOfNewCourseSum.text(json.incScheduleCourseCount).show(); 
							}
							else{
								spanOfNewCourseSum.hide();
							}
						}
					});
					return false;
				};
				
			getMessages();
			
			/*瑙ｅ喅鍙湁涓�鎻愮ず鐐瑰嚮鍚庢诞灞傜灛闂寸缉灏忕殑闂*/
			$('.message_datail a').click(function(){
				$(this).parent().show();
			});
			
			/*鍏抽棴娑堟伅涓績鐨勬彁閱掓诞灞 */
			$('.close_message_datail_wrap').click(function(){
				$.ajax({
					url:$.global.getContextPath() + '/cancel/notice/tips',
					type:'GET',
					dataType:'json',
					success:function(json){
						if(json.success){
							closeClick = true;
							curMessageCount = spanOfMessageSum.text();
							messageDatailWrap.hide(); 
						}
					}
				});
				return false;
			});
			
		},

		getContextPath: function() {
			var contextPath = $('#context_path', $('#global_paths'));
			return contextPath.val();
		},

		getImagePath: function() {
			var imagesPath = $('#images_path', $('#global_paths'));
			return imagesPath.val();
		},

		getAvatarPath: function() {
			var avatarPath = $('#avatar_path', $('#global_paths'));
			return avatarPath.val();
		},

		getCourseImgPath: function() {
			var courseImgPath = $('#course_img_path', $('#global_paths'));
			return courseImgPath.val();
		}
	};
})(jQuery);
