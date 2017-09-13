	window.onload=function(){	//保证js代码在文档加载完成后才去执行，免得找不到对应的element
	    var fileInput = document.getElementById('image_file');
	    var info = document.getElementById('file_info');
	    var preview = document.getElementById('image_preview');

	    fileInput.addEventListener('change',function(){
	        // console.log('change...');
	        preview.style.backgroundImage='';
	        if (!fileInput.value){
	            info.innerHTML = '没有选择文件';
	            return ;
	        }

	        var file = fileInput.files[0];
	        info.innerHTML = '文件:' + file.name + '<br>'+'大小:'+file.size+'<br>'+'修改:'+file.lastModifiedDate;

	        if(file.type !== 'image/jpeg' && file.type !== 'image/png' && file.type !== 'image/jpg'){
	            alert('不是有效的图片文件!');
	            return;
	        }

	        var reader = new FileReader();
	        reader.readAsDataURL(file);	//发起一个异步操作来读取文件内容
	        reader.onload=function(e){	//当文件读取完成后，自动调用此函数
	            // console.log('reader.onload');
	            var data = e.target.result;
	            preview.style.backgroundImage='url('+ data +')';
	        };
	        
	    });
	};