


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
	var videoART = ["https://www.youtube.com/embed/0lglARTJOmY",
					"https://www.youtube.com/embed/cPnJAL207Kk",
					"https://www.youtube.com/embed/txmKr69jGBk",
					"https://www.youtube.com/embed/q_sQUK418mM",
				    "https://www.youtube.com/embed/Dk9JOd1PY9Y"];
	/*art連結文字*/
	var videoART_name = ["II. Fujui Wang's Electromagnetic Soundscape at Guetteurs Opening",
						 "Energies: Haines & Hinterding",
						 "Levitating Barbecue! Electromagnetic Induction",
						 "「only my railgun」歌ってみた【＊なみりん】",
						 "【Fun科學】太陽之石(維京人征服海洋的GPS)"];
	
	
	/*engineering的網址*/
	var videoENG=["https://www.youtube.com/embed/a4WjA87U3fw",
	"https://www.youtube.com/embed/6uM-80FSfaA",
	"https://www.youtube.com/embed/fDAQtlmtCe8",
	"https://www.youtube.com/embed/96ujJl_eSoo",
	"https://www.youtube.com/embed/JVh6sUHRxjg"];
	/*ngineering連結文字*/
	var videoENG_name=["【科學不一樣】超導磁浮列車原理　磁力線達吸斥力平衡",
	"電磁鐵吊車",
	"F-35 Electromagnetic Aircraft Launch System (EMALS)",
	"避雷针是如何避雷的？一根避雷针可以保护多大的范围？",
	"星链StarLink 5G蜂窝网络 WiFi 蓝牙 光通讯 电磁波 无线通讯的世界「硬核无线技术」第一期 系统讲解无线技术原理"];
	
	
	/*technology的網址*/
	var videoTEC=["https://www.youtube.com/embed/LkAOQAh0rek",
				  "https://www.youtube.com/embed/XLhcsXHnqCQ",
				  "https://www.youtube.com/embed/VIl_FuVBFbY",
				  "https://www.youtube.com/embed/lcNaMPM-i9E",
				  "https://www.youtube.com/embed/sKcblM1ayts"];
	/*technology連結文字*/
	var videoTEC_name=["5G通訊技術報給你知",
					   "无线电波是怎么产生的？为啥无线电波可以隔空传输图片、视频这些数据？",
					   "電流磁效應【觀念】質譜儀：帶電質點在磁場中所受磁力的應用（2／2）",
					   "無線充電是怎麼充的? 原理簡單介紹! | 一探啾竟 第21集 | 啾啾鞋",
					   "超‧電磁砲(噴飛的硬幣)"];
	
	/*science的網址*/
	var videoSCI=["https://www.youtube.com/embed/5APw_8kKJac",
				  "https://www.youtube.com/embed/joSjlFvRqFc",
				  "https://www.youtube.com/embed/Oe9FGJ7fcNc",
				  "https://www.youtube.com/embed/Elv3WpL32UE",
				  "https://www.youtube.com/embed/mYBdUWgZEWM"];
	/*science的網址*/
	var videoSCI_name=["麥克斯韋方程組是什麽？電場和磁場有什麽重要聯系？李永樂老師講最美物理公式",
					   "08涡流的热效应 电磁感应（3） 高中物理",
					   "電流磁效應【觀念】必歐－沙伐定律",
					   "Electromagnetism 101 | National Geographic",
					   "歡迎分享 Super Lightning 彰化八卦山脈 超級閃電慢動作いなびかり 稲光 稲妻 벼락 번개 foudre relámpago молния Blitz"];
	
	/*math的網址*/
	var videoMATH=["https://www.youtube.com/embed/0jW74lrpeM0",
				   "https://www.youtube.com/embed/OqZPX-gqWEQ",
				   "https://www.youtube.com/embed/WS9Wr3ecTuY",
				   "https://www.youtube.com/embed/CkBn8DTS_rY",
				   "https://www.youtube.com/embed/oP0QnIZYFEo"];
	/*math連結文字*/
	var videoMATH_name=["Let There Be Light: Maxwell's Equation EXPLAINED for BEGINNERS",
						"旋度",
						"1-5 高斯定律",
						"電磁感應（三）",
						"Lec30 物理(二) 第五週 27.2 電阻元件(歐姆定律、電阻率、電導率)"];
	
	/*other的網址*/
	var videoOTH=["https://www.youtube.com/embed/YTGCxS4f52I",
				  "https://www.youtube.com/embed/_syWNxi2nHA",
				  "https://www.youtube.com/embed/KBCjJVidXnM",
				  "https://www.youtube.com/embed/drLxfjqZHVo",
				  "https://www.youtube.com/embed/8DzCwyAm5YU",
				  "https://www.youtube.com/embed/onB0w3_Su9I"];
	/*other連結文字*/
	var videoOTH_name=["磁控管到底能发射多大功率的微波？",
					   "電偶極子 electric dipole, electric moment",
					   "Lec22 向量分析 第四章 曲線座標系統 (1/4)",
					   "How do Radios Work？",
					   "電磁學－馬克斯威爾方程式與電磁波",
					   "The World's First Room Temperature Superconductor"];

	/*chat的網址*/
	var videoCHAT=["https://www.youtube.com/embed/Wx0vlOaL4XE",
				   "https://www.youtube.com/embed/JjeGmvy0M-A",
				   "https://www.youtube.com/embed/BTqx3SN8fRY",
				   "https://www.youtube.com/embed/SBjZ1p3HfII",
				   "https://www.youtube.com/embed/koQ0-5kZ_g4",
				   "https://www.youtube.com/embed/sPa3_vEidTA",
				   "https://www.youtube.com/embed/hXjrz8lGq0s"];
	/*chat連結文字*/
	var videoCHAT_name=["2021 生活中的電磁學 高中生優秀講解影片",
						"2021 生活中的電磁學 高中生優秀講解影片",
						"2020 中山大學校慶演示 生活中的電磁學 講解影片",
						"2020台中場 線上活動 生活中的電磁學 高中生優秀講解影片",
						"2020台中場 線上活動 生活中的電磁學 講解影片",
						"2019台北場 生活中的電磁學 實驗講解",
						"2017台北場 生活中的電磁學 實驗講解"];

	
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

