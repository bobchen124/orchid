$(function(){
	var cm = [];
	cm.push({display:'课程ID',name:'roomId',width:300,sortable:false,align:'center'});
	cm.push({display:'课程名称',name:'courseName',width:300,sortable:false,align:'center'});
	cm.push({display:'开始时间',name:'openTime',width:100,sortable:true,align:'center'});
	//cm.push({display:'时长',name:'courseTime',width:50,sortable:true,align:'center'});
	cm.push({display:'状态',name:'status',width:80,sortable:true,align:'center'});
	//cm.push({display:'主讲人',name:'adminUser',width:100,sortable:false,align:'left'});
	
	var si = [];
	si.push({display:'课程名称',name:'courseName',isdefault:true});
//	si.push({display:'状态',name:'status'});
	si.push({display:'主讲人',name:'adminUser'});
	
	var bs = [];
	bs.push({name:'删除',bclass:'delete',onpress:M.delC});
	bs.push({separator: true });
	
	M.fg = $('#course_grid').flexigrid({
		url: "http://" + window.location.host + '/manage/room/query/',
		dataType:'json',
		colModel:cm,
		searchitems:si,
		sortname:'openTime',
		sortorder:'ASC',
		title:'课程',
		usepager:true,
		useRp:true,
		rp:10,
		showTableToggleBtn:false,
		width:800,
		height:400,
		autoload: true,
		striped:true,
		checkbox:false,
		
		pagestat: '当前显示记录 {from} 到 {to} 条，总 {total} 条',  
        procmsg: '正在处理，请稍等 ...',  
        nomsg: '找不到符合条件的资料！',  
        errormsg: '连接后台失败！', 
        buttons : bs
	});
});