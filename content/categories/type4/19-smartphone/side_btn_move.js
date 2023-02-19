$(document).ready(function() {
	videoMove();
	elementMove();
});
var videoMove=function () {

	/*if($("#totalVideo").attr("src")!="")*/ {

		// 取得其 top 值
		var $totalVideo = $('#totalVideo'),
			_top = $totalVideo.offset().top;
		var clientWin=screen.height;
		//alert(clientWin);

		// 當網頁捲軸捲動時
		var $win = $(window).scroll(function () {
			
			// 如果現在的 scrollTop 大於原本的 top 時
			if ($win.scrollTop() >= _top+ clientWin/4) {

					try {
						$('#totalVideo')[0].contentWindow.postMessage('{"event":"command","func":"pauseVideo","args":""}', '*');
					}catch (err){

					}
			}
		});
	}
}

var elementMove=function () {
	/*if(document.getElementById('#allBTN')) */{
		// 取得其 top 值
		var $allBTN = $('#allBTN'),
			_top = $allBTN.offset().top;

		// 當網頁捲軸捲動時
		var $win = $(window).scroll(function () {
			// 如果現在的 scrollTop 大於原本的 top 時
			if ($win.scrollTop() >= _top) {
				// 如果座標系統不是 fixed 的話
				if ($allBTN.css('position') != 'fixed') {
					// 設定座標系統為 fixed
					$allBTN.css({
						position: 'fixed',
						top: 15
					});
				}
			} else {
				// 還原座標系統為 absolute
				$allBTN.css({
					position: 'absolute',
					top: '20%'
				});
			}
		});
	}
}