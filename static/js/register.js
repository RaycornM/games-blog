function contrast() {
        var name= document.getElementById('inputUserName');
		$.ajaxSetup({data: {csrfmiddlewaretoken: '{{ csrf_token }}'}});
		$.ajax({
			type:"post",
			url:"/userContrast/"+name+"/",
			data: $('#inputUserName').serialize(),//序列化 按一定的格式写进去
			dataType: 'JSON',//提交的数据类型

		});

}