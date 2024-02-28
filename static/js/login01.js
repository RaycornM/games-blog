$(document).ready(function(){
			//。blur 和input标签中的 onBlur等效
            $("#inputEmail3").blur(function(){
				var upwdValue= $("#inputEmail3").val(); //val 等效于 js中的 value
				console.log(upwdValue);
				var cssr=/^[0-9a-zA-Z]{6,18}$/;
				var arr = $(".unameErr");
				if(cssr.test(upwdValue)){
					//jq对象转js对象
					var jsObj=arr[0]; //获取arr的0下标;同时 jq对象依据转为js对象
					//$(jsObj) 是将js对象转为jq对象
					$(jsObj).html("<h3>OK</h3>");  //等效与 js中的 innerTest
				}else{
					//jq对象转js对象
					var jsObj=arr[0]; //获取arr的0下标;同时 jq对象依据转为js对象
					//$(jsObj) 是将js独享转为jq对象
					$(jsObj).html("<h3>用户名长度不对 长度为6-18</h3>");
				}
			});//绑定事件
			$("#inputPassword3").blur(function(){
				var upwdValue02= $("#inputPassword3").val(); //val 等效于 js中的 value
				console.log(upwdValue02);
				var cssr=/^[0-9]{6,8}$/;
				var arr = $(".pwdErr");
				if(cssr.test(upwdValue02)){
					//jq对象转js对象
					var jsObj02=arr[0]; //获取arr的0下标;同时 jq对象依据转为js对象
					//$(jsObj) 是将js对象转为jq对象
					$(jsObj02).html("<h3>OK</h3>");  //等效与 js中的 innerTest
				}else{
					//jq对象转js对象
					var jsObj02=arr[0]; //获取arr的0下标;同时 jq对象依据转为js对象
					//$(jsObj02) 是将js独享转为jq对象
					$(jsObj02).html("<h3>密码长度不对 7-8个数字</h3>");
				}
			});//绑定事件





		}); //传入一个参数 function


