


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
	var videoART = ["https://www.youtube.com/embed/uqcR3lNCspQ",
					"https://www.youtube.com/embed/15qWtQkqSps",
					"https://www.youtube.com/embed/XKSe4BglLyw",
					"https://www.youtube.com/embed/3BO4760tuKo",
					"https://www.youtube.com/embed/SpPHnPIfjSE",
					"https://www.youtube.com/embed/67rhvLv6Nac"];
	/*art連結文字*/
	var videoART_name = ["How to create augmented reality from your sketchbook using Artivive",
						 "遊戲與影像藝術",
						 "TikTok Wonderful Night 2018, Openning AR Show.开场AR秀《看见每个你》",
						 "梵谷藝術沉浸式體驗展亮相北京 梵谷作品肖像悉數復活",
						 "Detroit: Become Human | The Art Behind Detroit | PS4",
						 "如何打造《紀念碑谷》的建築奇觀？| ChaosMuseum"];
	
	
	/*engineering的網址*/
	var videoENG=["https://www.youtube.com/embed/2pJ64XM_BRY",
				  "https://www.youtube.com/embed/biI5KkvFKPY",
				  "https://www.youtube.com/embed/d5l8za7E2Ho",
				  "https://www.youtube.com/embed/UOiigMvBwqA"];
	/*ngineering連結文字*/
	var videoENG_name=["建築建造AR應用｜宇萌數位科技 arplanet",
					   "GPU是怎么处理游戏画面的？和我们画画一样简单？",
					   "【游戏开发经验】独立游戏开发者必备的11款免费软件 | 软件推荐 | 游戏开发经验分享",
					   "超建築VR「XR EXPO」VR建築展示場　サンプル映像"];
	
	
	/*technology的網址*/
	var videoTEC=["https://www.youtube.com/embed/cQ_bdqb-zX4",
				  "https://www.youtube.com/embed/O_07SE5f2cg",
				  "https://www.youtube.com/embed/02Xy9wd01FQ",
				  "https://www.youtube.com/embed/Rnk_akgSjqg",
				  "https://www.youtube.com/embed/gZA3xKwMStI",
				  "https://www.youtube.com/embed/uq9SEJxZiUg",
				  "https://www.youtube.com/embed/d3ZO9nI4mkc",
				  "https://www.youtube.com/embed/uIHPPtPBgHk",
				  "https://www.youtube.com/embed/Z6PESYjuNHs",
				  "https://www.youtube.com/embed/VOt_ADeWNno"];
	/*technology連結文字*/
	var videoTEC_name=["FOCUS360/ 網購體驗再升級 AR虛擬試穿科技",
					   "光線追蹤到底在追什麼？要不要買RTX顯卡？【攻殼搜索科】",
					   "虛幻引擎5是怎麼榨乾PS5性能的？",
					   "Why Microsoft Uses Virtual Reality Headsets To Train Workers",
					   "VR手術訓練影片修2",
					   "How the Kinect Depth Sensor Works in 2 Minutes",
					   "《雅集科學新世紀》 - 擴增實境（AR）使用簡介",
					   "HoloLens 2 AR Headset: On Stage Live Demonstration",
					   "懷舊遊戲-打鴨子的光線槍原理! | 超邊緣冷知識 第20集 | 啾啾鞋",
					   "【科普】VR是什么原理？"];
	
	/*science的網址*/
	var videoSCI=["https://www.youtube.com/embed/5-hcpyR4YWU",
				  "https://www.youtube.com/embed/bYCH_Gbupzo",
				  "https://www.youtube.com/embed/YJRAJvOU7nI",
				  "https://www.youtube.com/embed/Q89ebAcFaWQ",
			 	  "https://www.youtube.com/embed/lDXbaNDTnVQ"];
	/*science的網址*/
	var videoSCI_name=["Xperia小教室#5 Google Lens 智慧鏡頭",
					   "Light Ignite - Laser Puzzle Gameplay Walkthrough #1 (Android, IOS)",
					   "[Vlog] How to play RakugakiAR",
					   "PhotoMath App Review",
					   "Relicta Gameplay (PC HD) [1080p60FPS]"];
	
	/*math的網址*/
	var videoMATH=["https://www.youtube.com/embed/UWrSuEFXxhY",
				   "https://www.youtube.com/embed/uq9SEJxZiUg",
				   "https://www.youtube.com/embed/ztsi0CLxmjw",
				   "https://www.youtube.com/embed/BnpPkPTlkGs",
				   "https://www.youtube.com/embed/-A_XpXRhOsQ"];
	/*math連結文字*/
	var videoMATH_name=["How to Use GeoGebra 3D (Augmented Reality Powered by ARCore by Google)",
						"How the Kinect Depth Sensor Works in 2 Minutes",
						"Non-euclidean virtual reality",
						"VR Math Intro",
						"How does Virtual Reality work? The Math behind VR (VR180)"];
	
	/*other的網址*/
	var videoOTH=["https://www.youtube.com/embed/ys9cneFeLxc",
				  "https://www.youtube.com/embed/ecg9JxsrNw8",
				  "https://www.youtube.com/embed/20ZgiAXPuA4",
				  "https://www.youtube.com/embed/BoSuyF3FWAM"];
	/*other連結文字*/
	var videoOTH_name=["How to become an AR Developer (in 2020)",
					   "Design Concepts in VR",
					   "《芝麻街》走入Xbox 互動教育趣味多",
					   "Learn Programming and Electronics With AR"];

	/*chat的網址*/
	var videoCHAT=["https://www.youtube.com/embed/kE-ZZPX2nyg",
	               "https://www.youtube.com/embed/OjvB7weW3f0",
				   "https://www.youtube.com/embed/vCR_dE7yRaI",
				   "https://www.youtube.com/embed/lnXK688iloA",
				   "https://www.youtube.com/embed/VPB5yyECq4o",
				   "https://www.youtube.com/embed/-KA3eP7-mes",
				   "https://www.youtube.com/embed/qaKnfhB5Ucs",
				   "https://www.youtube.com/embed/_7_H6jxkB1M",
				   "https://www.youtube.com/embed/dtAEB31bZuM"];
	/*chat連結文字*/
	var videoCHAT_name=["2021 遊戲機的物理 高中生優秀講解影片 1",
	                    "2021 遊戲機的物理 高中生優秀講解影片 2",
						"2021 遊戲機的物理 高中生優秀講解影片",
						"2021 遊戲機的物理 高中生優秀講解影片",
						"2020 中山大學校慶演示 遊戲機的物理 講解影片",
						"2020台中場 線上活動 遊戲機的物理 高中生優秀講解影片",
						"2020台中場 線上活動 遊戲機的物理 講解影片",
						"2019台北場 遊戲機的物理 實驗講解",
						"2017台北場 遊戲機的物理 實驗講解"];

	
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

