(function($) {
	
	$.fn.profilePopup = function(){
		
		return this.each(function(){
			
			var $loggedInInfo = $('#user_account'),
				$profileToPop = $("a.pop_profile"),
			    $profilePopLayerDOM = $('<div id="profile_popup_layer" style="display:none;"></div>'),
			    $prePopLayerDOM = $('<div class="profile_pop_layer">'
			    		+   			'<div class="pre_pop_loader"></div>'
			            +    			'<p class="pre_pop_tip">正在努力加载中...请耐心等待...</p>'
			            +				'<div class="profile_pop_arrow"></div>'
			            +			'</div>'),
			    $profilePopLayer = $profilePopLayerDOM.appendTo('body'),
			    $loginTrigger = $('#anonymous-login'),
			    timeDelay = null,
			    popedProfiles = {},
			    lastPsition={},
			    showPopLayer = function(html, position, profileWidth){
				
					$profilePopLayer.html(html);
					
					var popLayerWidth = $profilePopLayerDOM.width(),
						popLayerHeight = $profilePopLayerDOM.height();

					$profilePopLayer.css({
						'position':'absolute',
						'top':position.top - popLayerHeight - 11,
						'left':position.left - (popLayerWidth - profileWidth)/2 - 3,
						'opacity':1,
						'z-index':1000
					}).show();
				};
			
			//鼠标移入或移出标签
			$profileToPop.live("mouseenter",function(event){
				var position = $(this).offset(),
					profileWidth = $(this).outerWidth(),
					profileUniqueUserId = $(this).attr('data-user'),
					profileUrl = [$.global.getContextPath(), '/', profileUniqueUserId].join('');
				//鼠标快速移出$profileToPop又快速移入，如果浮层已经显示并且此次滑入的头像与上一次的位置相同，则停止（消失浮层的）动画，继续显示。
				if($profilePopLayer.is(':visible') && lastPsition[0] == position.top && lastPsition[1] == position.left){
					
					$profilePopLayer.stop(true, true);
					
				} else {
					
					$profilePopLayer.stop(true, true);
					
					if(popedProfiles[profileUniqueUserId] != null){//该用户已经弹出过浮层，可从缓存中取浮层信息直接显示
						
						timeDelay = setTimeout(function(){
							showPopLayer(popedProfiles[profileUniqueUserId], position, profileWidth);
						}, 400);

						
					} else {//异步请求所需的浮层数据
						
						timeDelay = setTimeout(function(){
							
							showPopLayer($prePopLayerDOM, position, profileWidth);
							
							$.ajax({
								async:false,
								url:profileUrl,
								type:'get',
								dataType:'html',
								beforeSend: function (xhr) {
									 xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest");
								},
								success:function(html){
									
									showPopLayer(html, position, profileWidth);
									
									popedProfiles[profileUniqueUserId] = html;
								}
							});
						}, 400);
					}
				}
				
				lastPsition[0] = position.top;
				lastPsition[1] = position.left;
				
				return false;	
					
			}).live("mouseleave", function(){
				$profilePopLayer.delay(400).animate({'opacity':0}, 0, function(){
					$profilePopLayer.hide();
				});
				clearTimeout(timeDelay);
			});
			
			//鼠标滑入或滑出浮层
			$("#profile_popup_layer").live('mouseenter',function(){
				
				$(this).stop(true, true);
				
			}).live("mouseleave", function(){
				
				$(this).delay(400).animate({'opacity':0}, 0, function(){
					$profilePopLayer.hide();
				});
				clearTimeout(timeDelay);   
			});
			
			//鼠标浮到已关注或移开
			$('.remove_follow').live('mouseenter', function(){
				
				$(this).val('取消');
				
			}).live('mouseleave', function(){
				
				$(this).val('已关注');
				
			});
			
			//TO-DO:浮层的关注
			$('.follow_form').live('submit', function() {
				
				$.ajax({
					async:false,
					url:$(this).attr('action'),
					type:'post',
					dataType:'json',
					data:$(this).serialize(),
					context:$(this),
					beforeSend: function (xhr) {
						 xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest");
					},
					statusCode: {
						405: function() {
							$loginTrigger.click();
						},
						404: function() {
					   	 	return false;
						},
						403: function() {
							$loginTrigger.click();
						}
					},
					success:function(json){
						
						var $followBtn = $(this).find('.follow_btn'),
							$fansNum = $('.fans a', $profilePopLayer),
							profileUniqueUserId = $('.followedUniqueUserId', $profilePopLayer).val();
						
						$('.follow_form').toggle();
						
						$fansNum.text(
							$followBtn.hasClass('remove_follow') ? 
								(parseInt($fansNum.text()) - 1) : 
									(parseInt($fansNum.text()) + 1));
						
						popedProfiles[profileUniqueUserId] = $('#profile_popup_layer').html();
					}
				});
				
				return false;
			});
			
			if($loggedInInfo[0]){
				$('.write_pm', $profilePopLayer).wokaobox({
					width	: 440,
					height	: 270,
					type	: 'iframe'
				});
			} else {
				$('.write_pm, .follow_btn').live('click', function(){
					$loginTrigger.click();
					return false;
				});
			}
			
			if($.browser.msie && $.browser.version < 7 && !window.XMLHttpRequest){
				DD_belatedPNG.fix('.profile_pop_arrow');
			}
		});
	};
})(jQuery);