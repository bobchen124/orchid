var Msg = {
		tipMsg : function(msg){
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
		
		alertMsg : function(msg){
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
		
		errorMsg : function(msg){
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
		}
};