


$(document).ready(function() {

	/*=========================使用者可更改部分開始=============================*/
	
	/*
	使用youtube->分享->嵌入(裡面的src="http....")
	
	(1)
	更改網址:
	["嵌入網址1",
	 "嵌入網址2",
	 .
	 .
	 .
	]
	
	(2)
	更改連結文字:
	["嵌入網址1的文字",
	 "嵌入網址2的文字",
	 .
	 .
	 .
	]
	(3)
	若是只有填入嵌入網址，而沒有文字，上方youtube影片將為嵌入網址1的影片
	e.g.
	videoENG=["https://www.youtube.com/embed/II1g92jFItE"];
	videoENG_name=[];
	上方影片就會是https://www.youtube.com/embed/II1g92jFItE
	而下方不會出現相關連結
	
	
	*/
	/*art網址*/
	var videoART = ["https://www.youtube.com/embed/t0v7p7l427M",
					"https://www.youtube.com/embed/yYqumY4am0A",
					"https://www.youtube.com/embed/x-FBeh86z_Y",
					"https://www.youtube.com/embed/jGu_ULz9Klk"];
	/*art連結文字*/
	var videoART_name = ["熱對流玩具 走馬燈",
						 "雪花的奧秘(中文字幕)",
						 "喝水鳥",
						 "【虹吸壺咖啡】虹吸咖啡競賽冠軍教你，怎麼煮一杯美味的虹吸咖啡/TSC虹吸咖啡競賽冠軍/簡嘉程老師不藏私分享虹吸咖啡沖煮小訣竅"];
	
	
	/*engineering的網址*/
	var videoENG=["https://www.youtube.com/embed/yQQxT1b3RlY",
				  "https://www.youtube.com/embed/VkTSCgkXHhk",
				  "https://www.youtube.com/embed/eqn0VBVWS50"];
	/*ngineering連結文字*/
	var videoENG_name=["冷氣系統的作動原理流程(中文字幕)",
					   "【Fun科學】無限能源攪拌杯(真的不需裝電池)",
					   "How Coal Fired Thermal Power Stations Work"];
	
	
	/*technology的網址*/
	var videoTEC=["https://www.youtube.com/embed/PMjXPQOYXCA",
				  "https://www.youtube.com/embed/XFiGr1tMhKc",
				  "https://www.youtube.com/embed/gQb2sN6UWkA",
				  "https://www.youtube.com/embed/n8sT4d-szJk",
				  "https://www.youtube.com/embed/q9DP6v0IW1k"];
	/*technology連結文字*/
	var videoTEC_name=["採用均熱板 + 4熱導管　Cooler Master TPC 612 散熱器",
					   "蒸氣火車的由來與構造",
					   "Stirling Engines - How They Work",
					   "Heat Pipe 中文",
					   "Bosch Geo 101 - How Geothermal Heat Pump Systems Work"];
	
	/*science的網址*/
	var videoSCI=["https://www.youtube.com/embed/cPPI8o-SHnc",
				  "https://www.youtube.com/embed/yRZu6JmzQYg",
				  "https://www.youtube.com/embed/dL9NfiJjV14",
				  "https://www.youtube.com/embed/XEDSTXlM4h4"];
	/*science的網址*/
	var videoSCI_name=["布朗運動 理想氣體",
					   "高中化學_選修化學(上)_液態與溶液:過冷現象Supercooling【莫斯利高中自然科教學網】",
					   "Zeroth, First, Second and Third Laws of Thermodynamics",
					   "【科技数码】趣味科普：热管的工作原理 简述！"];
	
	/*math的網址*/
	var videoMATH=["https://www.youtube.com/embed/p_W3ZbsI3fo",
				   "https://www.youtube.com/embed/Wf0VRMiXD_4",
				   "https://www.youtube.com/embed/NyOYW07-L5g",
				   "https://www.youtube.com/embed/LNMwstcSTbM"];
	/*math連結文字*/
	var videoMATH_name=["什麼是熵? - What is Entropy by the Good Stuff (中文字幕)",
						"如何選擇壹個節能省電的空調？空調的原理又是什麽？李永樂老師9分鐘講解熱機原理和卡諾定理",
						"First Law of Thermodynamics, Basic Introduction - Internal Energy, Heat and Work - Chemistry",
						"高中_物理_熱力學_熱膨脹與膨脹係數"];
	
	/*other的網址*/
	var videoOTH=["https://www.youtube.com/embed/Ab8JIzckx_M",
				  "https://www.youtube.com/embed/Qe5H78mVZts",
				  "https://www.youtube.com/embed/v6lqBT7UaeU"];
	/*other連結文字*/
	var videoOTH_name=["The Black Hole Entropy Enigma | Space Time",
					   "為何磁鐵吸不到燒紅的鐵?(Why can't a magnet attract the red hot iron?)",
					   "【Fun科學】絕熱膨脹對受傷女性的效果(熱力學第一定律入門)"];

	/*chat的網址*/
	var videoCHAT=["https://www.youtube.com/embed/lP5guWyuK18",
				   "https://www.youtube.com/embed/EFUOKt68hgQ",
				   "https://www.youtube.com/embed/4VZ-d3ETwLY",
				   "https://www.youtube.com/embed/wjlEHgRkcUc"];
	/*chat連結文字*/
	var videoCHAT_name=["2020 中山大學校慶演示 生活中的熱學 講解影片",
						"2020台中場 線上活動 生活中的熱學 高中生優秀講解影片",
						"2020台中場 線上活動 生活中的熱學 講解影片",
						"2019台北場 生活中的熱學 實驗講解"];

	
	/*設定底下的pdf長度*/
	/*長度大小:不要讓內部的pdf有右邊的拉把(scroll bar)即可*/

	/*更新：no need to set if you are using jpg version(tell others)*/
	var art_html_height = 1000; 
	var eng_html_height = 1000;
	var tec_html_height = 3400;
	var sci_html_height = 5000;
	var math_html_height = 6000;
	var oth_html_height = 1000;
	var chat_html_height = 1000;
	
	
	/*=========================使用者更改部分結束==================================*/
	
	
	

	
	/*video function*/
	//$('#totalVideo').attr('src', videoEng + "&autoplay=1");
	//videoMove();
	/*=======================================================================*/
	/*Button function*/
	
	/*function reload_html(html,height){
		var parent = $('#inner-html').parent();
		var newElement = "<embed src='html/"+htm+"' id"+"='inner-html'>";
	
		$('#inner-html').remove();
		parent.append(newElement);
		
		$("#inner-html").attr("height",height);
		$("#inner-html").attr("width","100%");
		
	}
	$("#art_btn").click(reload_html('art.htm',art_html_height));*/
	
	
	
	/*$("#m_art_btn").click(function(){

		window.location.href = "test.html";
		//alert("zz");
		
		
		var parent = document.getElementById("inner-html").parent();
		//var parent = $('#inner-html').parent();
		var newemb = "<embed src='html/art.htm' id='inner-html'>";
		$('#inner-html').remove();
		parent.append(newemb);
		$("#inner-html").attr("height",art_html_height);
		$("#inner-html").attr("width","100%"); 
			

	});*/
	
	//videoMove();
	
	$("#art_btn").click(function(){
		
		var videoArt = "";
		videoArt = $("#art_changing_video").attr("href");
		
		if(videoArt=="" && videoART.length>0)
			videoArt = videoART[0]+"?enablejsapi=1";/*Take first*/
		
			
		
		var parent2 = $('#totalVideo').parent();
		var newframe = "<iframe id='totalVideo' src='' frameborder=0 allowfullscreen></iframe>";
		
		$('#totalVideo').remove();
		if(videoArt!="")
		{
			parent2.append(newframe);

			$("#totalVideo").addClass("video-style");
			$('#totalVideo').attr('src', videoArt + "&autoplay=1");
		}
		
		
		var parent = $('#inner-html').parent();
		var newemb = "<embed src='../heading_pdf/art.jpg' id='inner-html' pluginspage='http://www.adobe.com/products/acrobat/readstep2.html'></embed>";
		$('#inner-html').remove();
		parent.append(newemb);
		//$("#inner-html").attr("height",art_html_height);
		//$("#inner-html").height(art_html_height);
		/*Origin
		$("#inner-html").width("55%");
		*/
		/***New change***/
		var wid = "";
		if($(window).width()<1019)
			wid = "150%";
		else
			wid = "55%";
		$("#inner-html").width(wid);
		/************/
		$("#inner-html").addClass("inner-html"); 
		
		
		
	});
		
	
	$("#eng_btn").click(function(){
		
		var videoEng = "";
		videoEng = $("#eng_changing_video").attr("href");
		
		if(videoEng=="" && videoENG.length>0)
			videoEng = videoENG[0]+"?enablejsapi=1";/*Take first*/
			
		
		
		var parent2 = $('#totalVideo').parent();
		var newframe = "<iframe id='totalVideo' src='' frameborder=0 allowfullscreen></iframe>";
		$('#totalVideo').remove();
		
		if(videoENG!="")
		{
			parent2.append(newframe);
			/*$("#totalVideo").attr("height","600");
			$("#totalVideo").attr("width","60%");*/
			$("#totalVideo").addClass("video-style");
			$('#totalVideo').attr('src', videoEng + "&autoplay=1");
	
		}
		var parent = $('#inner-html').parent();
		var newElement = "<embed src='../heading_pdf/engineering.jpg' pluginspage='http://www.adobe.com/products/acrobat/readstep2.html' id='inner-html'></embed>";
	
		$('#inner-html').remove();
		parent.append(newElement);
		
		//$("#inner-html").height(eng_html_height);
		/*Origin
		$("#inner-html").width("55%");
		*/
		/***New change***/
		var wid = "";
		if($(window).width()<1019)
			wid = "100%";
		else
			wid = "55%";
		$("#inner-html").width(wid);
		/************/
		$("#inner-html").addClass("inner-html"); 
	});
	$("#tec_btn").click(function(){
		
		var videoTec = "";
		videoTec = $("#tec_changing_video").attr("href");
		
		if(videoTec=="" && videoTEC.length>0)
			videoTec = videoTEC[0]+"?enablejsapi=1";/*Take first*/
		
		
		var parent2 = $('#totalVideo').parent();
		var newframe = "<iframe id='totalVideo' src='' frameborder=0 allowfullscreen></iframe>";
		$('#totalVideo').remove();
		if(videoTEC!="")
		{
			parent2.append(newframe);
			$("#totalVideo").addClass("video-style");
			$('#totalVideo').attr('src', videoTec + "&autoplay=1");
		}
		
		/*$("#totalVideo").attr("height","0");
		$("#totalVideo").attr("width","0");*/
		
		
		var parent = $('#inner-html').parent();
		var newElement = "<embed src='../heading_pdf/technology.jpg' pluginspage='http://www.adobe.com/products/acrobat/readstep2.html' id='inner-html'></embed>";
	
		$('#inner-html').remove();
		parent.append(newElement);
		
		//$("#inner-html").height(tec_html_height);
		/*Origin
		$("#inner-html").width("55%");
		*/
		/***New change***/
		var wid = "";
		if($(window).width()<1019)
			wid = "100%";
		else
			wid = "55%";
		$("#inner-html").width(wid);
		/************/
		$("#inner-html").addClass("inner-html"); 
	});
	$("#sci_btn").click(function(){
		
		var videoSci = "";
		videoSci = $("#sci_changing_video").attr("href");
		
		if(videoSci=="" && videoSCI.length>0)
			videoSci = videoSCI[0]+"?enablejsapi=1";/*Take first*/
		
		var parent2 = $('#totalVideo').parent();
		var newframe = "<iframe id='totalVideo' src='' frameborder=0 allowfullscreen></iframe>";
		$('#totalVideo').remove();
		
		if(videoSCI!="")
		{
			parent2.append(newframe);
			$("#totalVideo").addClass("video-style");
			$('#totalVideo').attr('src', videoSci + "&autoplay=1");
		}
		
		
		var parent = $('#inner-html').parent();
		var newElement = "<embed src='../heading_pdf/science.jpg' pluginspage='http://www.adobe.com/products/acrobat/readstep2.html' id='inner-html'></embed>";
	
		$('#inner-html').remove();
		parent.append(newElement);
		
		//$("#inner-html").height(sci_html_height);
		/*Origin
		$("#inner-html").width("55%");
		*/
		/***New change***/
		var wid = "";
		if($(window).width()<1019)
			wid = "100%";
		else
			wid = "55%";
		$("#inner-html").width(wid);
		/************/
		$("#inner-html").addClass("inner-html"); 
	});
	$("#math_btn").click(function(){
		
		var videoMath = "";
		videoMath = $("#math_changing_video").attr("href");
		
		if(videoMath=="" && videoMATH.length>0)
			videoMath = videoMATH[0]+"?enablejsapi=1";/*Take first*/
		
		var parent2 = $('#totalVideo').parent();
		var newframe = "<iframe id='totalVideo' src='' frameborder=0 allowfullscreen></iframe>";
		$('#totalVideo').remove();
		
		if(videoMATH!="")
		{
			parent2.append(newframe);

			$("#totalVideo").addClass("video-style");
			$('#totalVideo').attr('src', videoMath + "&autoplay=1");
		}
		
		
		
		var parent = $('#inner-html').parent();
		var newElement = "<embed src='../heading_pdf/math.jpg' pluginspage='http://www.adobe.com/products/acrobat/readstep2.html' id='inner-html'></embed>";
	
		$('#inner-html').remove();
		parent.append(newElement);
		
		//$("#inner-html").height(math_html_height);
		/*Origin
		$("#inner-html").width("55%");
		*/
		/***New change***/
		var wid = "";
		if($(window).width()<1019)
			wid = "100%";
		else
			wid = "55%";
		$("#inner-html").width(wid);
		/************/
		$("#inner-html").addClass("inner-html"); 
	});
	$("#oth_btn").click(function(){
		
		var videoOth = "";
		videoOth = $("#oth_changing_video").attr("href");
		
		if(videoOth=="" && videoOTH.length>0)
			videoOth = videoOTH[0]+"?enablejsapi=1";/*Take first*/
		
		var parent2 = $('#totalVideo').parent();
		var newframe = "<iframe id='totalVideo' src='' frameborder=0 allowfullscreen></iframe>";
		$('#totalVideo').remove();
		
		if(videoOth!="")
		{
			parent2.append(newframe);
		
			$("#totalVideo").addClass("video-style");
			$('#totalVideo').attr('src', videoOth + "&autoplay=1");
		}
		
		
		var parent = $('#inner-html').parent();
		var newElement = "<embed src='../heading_pdf/other.jpg' pluginspage='http://www.adobe.com/products/acrobat/readstep2.html' id='inner-html'></embed>";
	
		$('#inner-html').remove();
		parent.append(newElement);
		
		//$("#inner-html").height(oth_html_height);

		/*Origin
		$("#inner-html").width("55%");
		*/
		/***New change***/
		var wid = "";
		if($(window).width()<1019)
			wid = "100%";
		else
			wid = "55%";
		$("#inner-html").width(wid);
		/************/


		$("#inner-html").addClass("inner-html"); 
	});
	$("#chat_btn").click(function(){
		
		var videoChat = "";
		videoChat = $("#chat_changing_video").attr("href");
		
		if(videoChat=="" && videoCHAT.length>0)
			videoChat = videoCHAT[0]+"?enablejsapi=1";/*Take first*/
		
		var parent2 = $('#totalVideo').parent();
		var newframe = "<iframe id='totalVideo' src='' frameborder=0 allowfullscreen></iframe>";
		$('#totalVideo').remove();
		
		if(videoChat!="")
		{
			parent2.append(newframe);
		
			$("#totalVideo").addClass("video-style");
			$('#totalVideo').attr('src', videoChat + "&autoplay=1");
		}
		
		
		var parent = $('#inner-html').parent();
		var newElement = "<embed src='../heading_pdf/fb.jpg' pluginspage='http://www.adobe.com/products/acrobat/readstep2.html' id='inner-html'></embed>";
	
		$('#inner-html').remove();
		parent.append(newElement);
		
		//$("#inner-html").height(chat_html_height);

		/*Origin
		$("#inner-html").width("55%");
		*/
		/***New change***/
		var wid = "";
		if($(window).width()<1019)
			wid = "100%";
		else
			wid = "55%";
		$("#inner-html").width(wid);
		/************/


		$("#inner-html").addClass("inner-html"); 
	});
	/*=======================================================================*/
	
	
	/*===================Dynamic addition of video link======================*/
	
	/*Use let to declare in order to make video_link be the local variables*/
	let page_type=7;/*6 types of buttons(no chat)*/
	
	for(let j=0;j<page_type;j++)
	{
		let page_length;/*length of link array*/
		let type_name = "";
		let video_array;/*link array*/
		let video_name;/*link name array*/
		let name_length;/*lengh of link name array*/
		switch(j)
		{
			case 0:
				type_name = 'art';
				page_length = videoART.length;
				video_array = videoART.slice();
				video_name = videoART_name.slice();
				break;
			case 1:
				type_name = 'eng';
				page_length = videoENG.length;
				video_array = videoENG.slice();
				video_name = videoENG_name.slice();
				break;
			case 2:
				type_name = 'tec';
				page_length = videoTEC.length;
				video_array = videoTEC.slice();
				video_name = videoTEC_name.slice();
				break;
			case 3:
				type_name = 'sci';
				page_length = videoSCI.length;
				video_array = videoSCI.slice();
				video_name = videoSCI_name.slice();
				break;
			case 4:
				type_name = 'math';
				page_length = videoMATH.length;
				video_array = videoMATH.slice();
				video_name = videoMATH_name.slice();
				break;
			case 5:
				type_name = 'oth';
				page_length = videoOTH.length;
				video_array = videoOTH.slice();
				video_name = videoOTH_name.slice();
				break;
			case 6:
				type_name = 'chat';
				page_length = videoCHAT.length;
				video_array = videoCHAT.slice();
				video_name = videoCHAT_name.slice();
				break;	
			default:
				;
		}
		
				
		for(let i=1;i<=page_length;i++)
		{
			
			let video_link = video_array[i-1]+"?enablejsapi=1";
			let new_element = '<a id="'+type_name+'link'+i+'" class="html-content"></a></br>'
			$('.'+type_name+'-html-video').append(new_element);
			
			
			$('#'+type_name+'link'+i).click(function(){
				
				$('#'+type_name+'_changing_video').attr("href", video_link);
				$('#'+type_name+'_btn').trigger("click");
			});
			
			
			if(video_name.length>0 && i==1)
			{
				let str = '<div>相關影片</div>'
				$('.'+type_name+'-html-video').prepend(str);
			}
				
			$('a#'+type_name+'link'+i).text(video_name[i-1]);
		}
	}
	
		
	
	
	/*=======================================================================*/

	/*Screen resize============================================*/
	/*$(window).resize(function() {

		if(screen.height>=800)
		{
			$('#iframeArt').attr("height", 400);
			$('#iframeEng').attr("height", 400);
			$('#iframeTec').attr("height", 400);
			$('#iframeSci').attr("height", 400);
			$('#iframeMath').attr("height", 400);
			$('#iframeChat').attr("height", 400);

		}
		else if(screen.height<800 && screen.height>=650)
		{
			$('#iframeArt').attr("height", 300);
			$('#iframeEng').attr("height", 300);
			$('#iframeTec').attr("height", 300);
			$('#iframeSci').attr("height", 300);
			$('#iframeMath').attr("height", 300);
			$('#iframeChat').attr("height", 300);

		}
		else if(screen.height<650)
		{
			$('#iframeArt').attr("height", 200);
			$('#iframeEng').attr("height", 200);
			$('#iframeTec').attr("height", 200);
			$('#iframeSci').attr("height", 200);
			$('#iframeMath').attr("height", 200);
			$('#iframeChat').attr("height", 200);

		}

	});*/
	
	
	//elementMove();
	
});

/*=================Responsive Desgin======================*/


function openNav() {
	$('.container a').css('display','none');
    document.getElementById("mySidenav").style.width = "230px";
    document.getElementById("main").style.marginLeft = "230px";
	$('.sidebar').css('opacity', '0');
	setTimeout("$('.container a').css('display','block');", 500);
}

function closeNav() {
	$('.container a').css('display','none');
    document.getElementById("mySidenav").style.width = "0";
    document.getElementById("main").style.marginLeft= "0";
	$('.sidebar').css('opacity', '1');
	
}

/*=========================================================*/

