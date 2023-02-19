#!/usr/bin/perl

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++　[ Motto Kakikomitai 多功能晉級留言板 Ver0.864 ]  原程式更新於 2001.02.04 / 中文版更新於 2001.03.04 (二版)
#+++        >>> Copyright (c) 1999.10 Tacky's Room. All rights reserved.
#+++    原作者: Tacky 　　電子郵箱 >>> tackysrm@lily.freemail.ne.jp     個人網站 >>> http://tackysroom.com
#+++    中文化: 驚直　　　電子郵箱 >>> webmaster@kiddiken.net           個人網站 >>> http://kiddiken.net
#+++    ※由於小弟不懂日文，所以程式裡很多地方都是猜出來翻的！如果有什麼地方是誤翻的，請你寫信或在留言板告訴我吧！
#+++
#+++ 設置方法
#+++
#+++ public_html (首頁資料夾)
#+++ |-- mkakikomitai           (777或711)  (任何一個空的資料夾)
#+++   |-- mkakikomitai.cgi     (755或700)  (主程式)
#+++   |-- mkakikomitai.txt     (666或600)  (留言記錄檔 - 開始時是空的)
#+++   |-- mkakikomitai_cnt.txt (666或600)  (晉級狀態記錄檔 - 開始時是空的)
#+++   |-- mkakikomitai.cnt     (666或600)  (計數器記錄檔 - 開始時是空的)
#+++   |-- img                  (755)       (程式圖檔資料夾)
#+++   |   |-- *.gif                 (644)  (程式圖檔)
#+++   |-- cicon                (755)       (計數器圖檔資料夾)
#+++   |   |-- num6_0∼9.gif         (644)  (計數器圖檔)
#+++   |-- icon                 (755)       (留言板圖檔資料夾)
#+++   |   |-- *.gif                 (644)  (留言板圖檔)
#+++   |-- old                  (755)       (舊留言集存放位置 - 啟動留言板之前必須先建立這個資料夾)
#+++
#+++ 　　■括號()內的數字表示該資料夾或檔案要設成的檔案權限數值。
#+++ 　　■除了gif檔案是使用二進位模式(Binary Mode)上傳外，其餘檔案必須使用純文字模式(ASCII Mode)上傳到伺服器。
#+++ 　　■mkakikomitai.lock這個檔案在有需要的時候會自動產生及刪除。
#+++ 　　■在下面基本設定填入檔名的時候，如果有需要(例如檔案放在別處)，便要使用完整路徑(http://∼)來指定。
#+++
#+++ >>> 原日文版更新歷程...
#+++     2001.02.04(Ver0.864) >>  把圖檔一覽表的「返回」連結加回去(不適用於中文版)。「一氣回覆」套用留言內容最高字數的限制。
#+++     2001.01.31(Ver0.863) >>  修正當刪除留言記錄後，留言編號的數值沒有清空的臭蟲。
#+++     2001.01.22(Ver0.862) >>  修正&nbsp;語法錯誤。
#+++     2001.01.16(Ver0.861) >>  修正設定管理者專用圖檔時一個錯誤的變數。
#+++     2001.01.13(Ver0.86)  >>  加入了專為管理者而設的「一氣回覆」功能。
#+++                              加入了提供留言記錄下載功能，讓使用者可以離線閱讀。目的是要節省電話費。(^-^)
#+++                              管理者專用圖檔＆常連者專用圖檔使用不同矩陣，前者並加入密碼維護安全。
#+++                              晉級說明及晉級狀態的連結改以表單按鈕進入，列表加強表格顯示。
#+++                              改變各種GIF圖檔指定IMG語法的設定模式，使其可以加入圖檔闊度與高度的值。這樣可以避免頁面顯示出來的時候移來移去。（笑）
#+++                              使用sendmail程式寄發郵件通知的功能加入了一個設定值，可以讓你避免連自己寫入的留言記錄也要通知。
#+++     2000.10.29(Ver0.851) >>  修正因檔案鎖定程序錯誤而引致的計數器問題．．．m(_ _)m
#+++     2000.10.28  >>  圖檔一覽表加入管理者及常連者專用圖檔。
#+++                     簡化檢查重複輸入留言的程序。
#+++     2000.08.07  >>  修正留言內容輸入表單的表格錯誤語法。
#+++     2000.07.26  >>  修正關於多重刪除留言記錄的臭蟲。
#+++     2000.07.14  >>  修正當不使用留言標題($titleset=0)的時候，「送出留言」按鈕跳到別處的錯誤。
#+++     2000.07.12  >>  修正檔案鎖定之問題。
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
$ver                        = '0.864';                                  #(驚直修改 - 加入程式版本編號)
#─＜基本設定開始＞────────────────────────────────────────────────────────
$url                        = "http://www2.nsysu.edu.tw/physdemo/";                    #首頁的網址
$script                     = './phy-kh1.cgi';                     #主程式檔名
$logfile                    = './phy-kh1.txt';                     #留言記錄檔名
$lockfile                   = './phy-kh1.lock';                    #鎖定檔檔名
$cntfile                    = './phy-kh1.cnt';                     #計數器記錄檔名 (不使用則改為'')
#$logfile2                  = './phy-kh1.txt';                 #設定記錄留言者留言篇數的晉級狀態記錄檔。(使用晉級制度必須有此檔案,不使用則改為'')

#要使用計數器的功能，必須設定每個計數器圖檔的語法。src=之後的是圖檔路徑。如果你知道每個圖檔的大小，最好也加入闊度(width)和高度(height)的數值。
#設定圖檔路徑時，也可以用類似src=http://www.∼/xxx.gif的語法來指定存在於主機伺服器以外其他位置的圖檔。
#如果不指定計數器圖檔，請改為''，便會使用純文字形式表示。
$cnt_gif[0]                 = '<img src=/physdemo/cgi-bin/cicon/num6_0.gif width=25 height=30>';
$cnt_gif[1]                 = '<img src=/physdemo/cgi-bin/cicon/num6_1.gif width=25 height=30>';
$cnt_gif[2]                 = '<img src=/physdemo/cgi-bin/cicon/num6_2.gif width=25 height=30>';
$cnt_gif[3]                 = '<img src=/physdemo/cgi-bin/cicon/num6_3.gif width=25 height=30>';
$cnt_gif[4]                 = '<img src=/physdemo/cgi-bin/cicon/num6_4.gif width=25 height=30>';
$cnt_gif[5]                 = '<img src=/physdemo/cgi-bin/cicon/num6_5.gif width=25 height=30>';
$cnt_gif[6]                 = '<img src=/physdemo/cgi-bin/cicon/num6_6.gif width=25 height=30>';
$cnt_gif[7]                 = '<img src=/physdemo/cgi-bin/cicon/num6_7.gif width=25 height=30>';
$cnt_gif[8]                 = '<img src=/physdemo/cgi-bin/cicon/num6_8.gif width=25 height=30>';
$cnt_gif[9]                 = '<img src=/physdemo/cgi-bin/cicon/num6_9.gif width=25 height=30>';
$cnt_keta                   = 5;                                        #計數器要顯示幾多位數字？

$title                      = '擺的物理';                             #留言板的標題
$titlelogo                  = '<img src=/physdemo/cgi-bin/img/mkakikomitai.gif width=300 height=35>';   #留言板標題圖檔IMG語法 (不使用則改為'')
$backpicture                = '';                                       #背景圖檔
$bgcolor                    = 'white';                                  #背景顏色
$tbgcolor                   = '';                                       #填寫留言表格的背景顏色
$tcolor                     = 'gray';                                   #文字顏色
$linkcolor                  = 'dimgray';                                #連結顏色 (從未到訪)
$vlinkcolor                 = 'dimgray';                                #連結顏色 (曾經到訪)
$alinkcolor                 = 'firebrick';                              #連結顏色 (正在到訪)
$hovercolor                 = 'red';                                    #連結顏色 (滑鼠經過時)              #i000331
$pt                         = '10pt';                                   #整體字形大小，建議：9,10,11,12     #i000331
$pt_mini                    = '9pt';                                    #微縮字形大小，建議：8,9,10         (驚直加入 - 套用於"圖檔一覽表"連結、顏色方塊、使用者晉級資訊及留言資訊)
$e_font                     = "Tahoma, Verdana, Arial";                 #英文專屬字形集                     (驚直加入)
$res_gif                    = '/physdemo/cgi-bin/img/res.gif';                          #設定讓訪客「回覆留言」的圖檔。(不使用則改為'',便會以純文字形式表示)
$gif_spacer                 = '/physdemo/cgi-bin/img/spacer.gif';                       #調整空位的DUMMY圖檔

$name_color                 = 'white';                                  #每篇留言之中，留言者名字等資訊的顏色
$msg_color                  = 'white';                                  #每篇留言之中，留言內容的背景顏色

$titleset                   = 0;                                        #每篇留言都要有標題嗎？(0:不要 1:要)

$homelinklogo               = '<img src=/physdemo/cgi-bin/img/kakikomitai_linkhome.gif width=50 height=12 border=0 alt=個人網站>';	#留言者個人網站連結圖檔IMG語法 (不使用則改為'')
$maillinklogo               = '<img src=/physdemo/cgi-bin/img/kakikomitai_linkmail.gif width=50 height=12 border=0 alt=電子郵箱>';	#留言者電子郵箱連結圖檔IMG語法 (不使用則改為'')

$top_l                      = '<img src=/physdemo/cgi-bin/img/top_l_h.gif width=8 height=8>';       #造成留言框圓角效果的圖檔IMG語法 (左上角) (不使用則改為'')
$top_r                      = '<img src=/physdemo/cgi-bin/img/top_r_h.gif width=8 height=8>';       #造成留言框圓角效果的圖檔IMG語法 (右上角) (不使用則改為'')
$bottom_l                   = '<img src=/physdemo/cgi-bin/img/bottom_l_h.gif width=8 height=8>';    #造成留言框圓角效果的圖檔IMG語法 (左下角) (不使用則改為'')
$bottom_r                   = '<img src=/physdemo/cgi-bin/img/bottom_r_h.gif width=8 height=8>';    #造成留言框圓角效果的圖檔IMG語法 (右下角) (不使用則改為'')

$datamax                    = 100 ;                                     #最新的留言集，保留的留言篇數 (只要留言達到這個數目，最原先的留言便會存入舊留言集)
$pagemax                    = 20 ;                                      #１頁可顯示之留言篇數
$password                   = 'pass';                                   #管理者密碼
$tag                        = 'yes';                                    #允許使用HTML碼？(yes,no)
$resflag                    = 'yes';                                    #最新回覆的留言搬到最頂？(yes,no)
$hostflag                   = 'yes';                                    #顯示留言者的HOST位址？(yes,no)

$row                        = 4;                                        #輸入留言內容方塊的列數(高度)
$col                        = 56;                                       #輸入留言內容方塊的欄數(闊度)
$t_width                    = 540;                                      #每篇留言的闊度(以像素計)

#設定留言可用之背景顏色．原作者的設定：@COLORS_B = ('#666666','#003399','#990000','#669900','#cc3399','#ff6633','#cccc00');
@COLORS_B = ('blue','red','brown','black','grey');    #(驚直修改 - 使用文字顏色碼並加入更多顏色)
$colb_use                   = 0;            #(0:顏色由留言者選擇 1:顏色由管理者指定)
$colb                       = 'silver' ;    #如果上面的值是'1'，全部留言都使用這個指定的背景顏色
#設定留言可用之文字顏色．原作者的設定：@COLORS_F = ('#666666','#003399','#990000','#669900','#cc3399','#ff6633','#cccc00','#000000');
@COLORS_F = ('blue','red','brown','black','grey');  #(驚直修改 - 使用文字顏色碼並加入更多顏色)
$colf_use                   = 0;            #(0:顏色由留言者選擇 1:顏色由管理者指定)
$colf                       = 'black' ;     #如果上面的值是'1'，全部留言都使用這個指定的文字顏色

#留言表格的各個欄目（名字、電子郵箱、個人網站、標題等）可以使用一套圖檔顯示出來
$gif_flg            = 1;                    #想要使用留言表格欄目圖檔嗎？(0:不使用 1:使用)

#設定留言表格的各個欄目圖檔
$gif_name           = '/physdemo/cgi-bin/img/kakikomitai_name.gif';     #(名字)
$gif_email          = '/physdemo/cgi-bin/img/kakikomitai_email.gif';    #(電子郵箱)
$gif_home           = '/physdemo/cgi-bin/img/kakikomitai_homepage.gif'; #(個人網站)
$gif_title          = '/physdemo/cgi-bin/img/kakikomitai_title.gif';    #(標題)
$gif_message        = '/physdemo/cgi-bin/img/kakikomitai_message.gif';  #(留言內容)

$icon_use           = 'yes';                            #留言內容使用圖檔嗎？(yes,no)

#↓設定管理者專用圖檔。除了管理者以外，沒有其他人可以使用這個圖檔。
#你可以在$oiconpass為這個屬於你的專用圖檔設定一個密碼，留言內容掃出來的時候驗證密碼＆名字如果跟記錄所載相同才會顯示出來，否則會使用一般圖檔。
#醬子就算有人要冒充你來寫留言，也必須知道你的專用圖檔密碼才能夠成功盜用你的身份。(不使用則改為$oiconpass = '';)
$oicon_gif    = '/physdemo/cgi-bin/icon/d_ahiru.gif' ;      $oiconpass = 'opass';           $oicon_gif_w = 32 ; $oicon_gif_h = 32 ;

#↓設定常連者專用圖檔。你可以為你的朋友或經常上來寫留言的網友(常連者)增加其他圖檔如$jicon_gif[2]...[5]等，餘此類推。
#留言內容掃出來的時候，會驗證留言者的名字是否跟這裡所設定的$jiconnm一樣，如是者便會出現對應的個人圖檔，不受自行選擇之圖檔影響。
$jicon_gif[0] = '/physdemo/cgi-bin/icon/kuma.gif' ;         $jiconnm[0] = 'Ａ君' ;          $jicon_gif_w[0] = 38 ; $jicon_gif_h[0] = 38 ;
$jicon_gif[1] = '/physdemo/cgi-bin/icon/parappa.gif' ;      $jiconnm[1] = 'Ｂ君' ;          $jicon_gif_w[1] = 37 ; $jicon_gif_h[1] = 35 ;

#↓設定留言者一般可選擇之圖檔。可以依個人需要增加其他圖檔如$icon_gif[11]...[20]等，餘此類推。
$icon_gif[0] = '/physdemo/cgi-bin/icon/motion.gif' ;       $iconnm[0] = 'motion' ;          $icon_gif_w[0] = 32 ; $icon_gif_h[0] = 32 ;
$icon_gif[1] = '/physdemo/cgi-bin/icon/Emc2.gif' ;       $iconnm[1] = 'Emc2' ;          $icon_gif_w[1] = 32 ; $icon_gif_h[1] = 32 ;
$icon_gif[2] = '/physdemo/cgi-bin/icon/碰撞.gif' ;       $iconnm[2] = '碰撞' ;          $icon_gif_w[2] = 32 ; $icon_gif_h[2] = 32 ;
$icon_gif[3] = '/physdemo/cgi-bin/icon/電力線.gif' ;       $iconnm[3] = '電力線' ;          $icon_gif_w[3] = 32 ; $icon_gif_h[3] = 32 ;
$icon_gif[4] = '/physdemo/cgi-bin/icon/波.gif' ;       $iconnm[4] = '波' ;          $icon_gif_w[4] = 32 ; $icon_gif_h[4] = 32 ;
$icon_gif[5] = '/physdemo/cgi-bin/icon/二極體.gif' ;       $iconnm[5] = '二極體' ;          $icon_gif_w[5] = 32 ; $icon_gif_h[5] = 32 ;
$icon_gif[6] = '/physdemo/cgi-bin/icon/重力場.gif' ;       $iconnm[6] = '重力場' ;          $icon_gif_w[6] = 32 ; $icon_gif_h[6] = 32 ;
$icon_gif[7] = '/physdemo/cgi-bin/icon/白努力.gif' ;       $iconnm[7] = '白努力' ;          $icon_gif_w[7] = 32 ; $icon_gif_h[7] = 32 ;
$icon_gif[8] = '/physdemo/cgi-bin/icon/光柵.gif' ;       $iconnm[8] = '光柵' ;          $icon_gif_w[8] = 32 ; $icon_gif_h[8] = 32 ;

$icon_line          = 3 ;                   #顯示圖檔一覽表時，每行顯示幾多個圖檔？

$method             = 'POST';               #METHOD方式(POST或GET)

#設定有問題的網域清單。只要符合這清單的網域都會被攔截(禁止寫入留言)。
#  設定 "xxx?.com" 即包括了 "xxx1.com","xxx2.com" 等，「?」可以是任何１個字元。
#  設定 "xxx*.com" 即包括了 "xxx1.com","xxx12345.com" 等，「*」可以是０個或以上的任何字元。
@DANGER_LIST=("xxx.com","yyy.com","zzz*.org.tw");

#設定留言內容的最高字數(以字元計算)。如果不設定最高字數，改為''即可。這個數值不能夠設得太大，最好是5000或以下，否則可能會出現錯誤信息。
$maxword = '2000';		#2000個字元即代表1000個中文字。

#設定晉級制度的每個類別。
@rank = ('幼稚園生','小學校低學年','小學校中學年','小學校高學年','中學生','高校生','大學生','大學院生','平社員','課長','部長','社長');
#設定每個類別的晉級資格，數目為留言篇數。
@rankno = ('0','5','10','20','30','50','70','100','130','150','180','250');

#你想要根據各人的晉級狀態來指定圖檔嗎？如果你使用這個模式，留言者在留言時毋須選擇圖檔。
#此外，圖檔的數目須與晉級制度的級數互相對應。（註：除管理者專用圖檔外，其餘常連者專用圖檔會失效）
#例:
#  $icon_gif[0] = 'xx1.gif'; $iconnm[0] = '第一級';
#  $icon_gif[1] = 'xx2.gif'; $iconnm[1] = '第二級';
#  $icon_gif[2] = 'xx3.gif'; $iconnm[2] = '第三級';
#  @rank = ('第一級','第二級','第三級');
#  @rankno = ('0','10','100');  ※設定３個晉級類別，便要設定３個圖檔，而每個圖檔分別代表這３個類別。
$icon_rank      = 0;        #0:不要根據晉級狀態指定圖檔（留言時自行選擇圖檔） 1:根據晉級狀態指定圖檔

#設定sendmail程式的路徑。此項資料可向網路管理者查詢。(一般是/usr/sbin/sendmail或/usr/lib/sendmail)
#如果你想要在有新留言的時候把留言資料寄到你的電子郵箱，便要設定，否則可保留為$sendmail = "";
$sendmail       = "";

#設定寄發郵件通知時，要收件的電子郵箱。「@」之前的一個「\」符號是必須加上的。如果沒有了「\」這符號，會出現Internal Server Error錯誤訊息。
#（使用sendmail程式送信才需要設定）
$smail_address  = "xxxx\@xxxx.xxxx.com.tw";

$sendsw         = 1;    #當使用寄發郵件通知功能時，連你自己寫入的留言記錄(以上面的郵箱作對照)也要利用郵件通知嗎？(0:忽略 1:全部都要通知)

$hiho           = 0;    #設為「1」即可使用「hi-ho」形式傳送郵件。某些伺服器不支援。　※使用sendmail程式送信才需要設定

#留言密碼的加密程序(使用crypt函數將密碼暗號化)
$ango           = 1;    #0: 不使用 1:使用　（建議使用）

#舊留言集的設定…指定一個資料夾($olddir)存放"01.txt".."10.txt"等等的舊留言記錄檔。
$olddir         = './old/';     #保存舊留言集的資料夾所在。(不使用則改為'')
$oldmax         = 100;          #每個舊留言集可容納之留言串列數。每當超過這個串列數後，會建立另一個舊留言集。

#你想要使用像『nyaponika學習帳』留言板的「橫線隔行」功能嗎？
$nya            = 0 ;   #留言內容的換行符號(<br>)要用橫線(<hr>)取代嗎？(0:否 1:是)
$maru           = 1 ;   #留言框要使用圓角嗎？(0:否 1:是)…如果「否」，則可以不要$top_l,r,$bottom_l,r這些圖檔。

#=============================================================================================================================================================================================
#設定ＣＳＳ樣式表　※如果不使用，請改為 $css_style = "";　有需要的話，可以輸入２行或以上的文字(只要設定在兩個EOM標記之間就可以)。
$css_style = <<"EOM";		#(一般輸入欄位的樣式表設定,套用於表單中的textarea及input type=text,password)
style="font-size:$pt;	font-family:'新細明體','PMingLiU';
	color:dimgray;	background-color:white; border-width:1px; border-style:solid; border-color:lightgrey;"
	onFocus="this.style.backgroundColor='ivory'" onBlur="this.style.backgroundColor='white'"
EOM
$css_style_e = <<"EOM";		#(驚直加入 - 英數文字輸入欄位的樣式表設定,套用於表單中的[電子郵箱/個人網站/留言編號]欄位)
style="font-size:$pt;	font-family:$e_font;
	color:dimgray;	background-color:white; border-width:1px; border-style:solid; border-color:lightgrey;"
	onFocus="this.style.backgroundColor='ivory'" onBlur="this.style.backgroundColor='white'"
EOM
$css_button = <<"EOM";		#(驚直加入 - 按鈕專用的樣式表設定,套用於表單中的input type=submit,reset,button)
style="font-size:$pt;	font-family:'新細明體','PMingLiU';	line-height:12pt;
	color:gray;		background-color:white; border-width:1px; border-style:solid; border-color:lightgrey;"
	onMouseOver="this.style.color='dimgray';this.style.backgroundColor='ivory'" onMouseOut="this.style.color='gray';this.style.backgroundColor='white'"
EOM
$css_select = <<"EOM";		#(驚直加入 - 下拉選單專用的樣式表設定,套用於表單中的select)
style="font-size:$pt;	font-family:'新細明體','PMingLiU';		color:gray;		background-color:white;"
	onFocus="this.style.backgroundColor='ivory'" onBlur="this.style.backgroundColor='white'"
EOM
$css_style_ = <<"EOM";		#(驚直加入 - 針對非IE瀏覽器的一般輸入欄位的樣式表設定)
style="font-size:$pt;	font-family:'新細明體','PMingLiU';		color:dimgray;	background-color:white; padding-left:2px;"
	onFocus="this.style.backgroundColor='ivory'" onBlur="this.style.backgroundColor='white'"
EOM
$css_style_e_ = <<"EOM";	#(驚直加入 - 針對非IE瀏覽器的英數文字輸入欄位的樣式表設定)
style="font-size:$pt;	font-family:$e_font;					color:dimgray;	background-color:white; padding-left:2px;"
	onFocus="this.style.backgroundColor='ivory'" onBlur="this.style.backgroundColor='white'"
EOM
$css_button_ = <<"EOM";		#(驚直加入 - 針對非IE瀏覽器的按鈕專用的樣式表設定)
style="font-size:9pt;	font-family:'新細明體','PMingLiU';		color:gray;		background-color:white;"
	onMouseOver="this.style.color='dimgray';this.style.backgroundColor='ivory'" onMouseOut="this.style.color='gray';this.style.backgroundColor='white'"
EOM

#■↓以下這個功能目的是要惡作劇留言者，使用隨機數目回扣留言者的留言篇數，如果不想使用請設為「$rdm = 0;」。
$rdm = 0;                       #數值範圍是0∼30，隨機變化。
@DOWN = (1,2,3,5,7,10);         #隨機回扣留言篇數的數目，建議數值在15以下。

$kaisu_disp = 1;    #留言內容顯示留言者的最新留言篇數？(0:否 1:是)

$ikkiflg    = 1 ;   #你想要使用「一氣回覆模式」嗎？(0:否 1:是)

#當留言板轉換到「一氣回覆模式」的時候，在留言輸入表單與留言內容之間會出現以下文字，提醒使用者要注意的事情。
$ikkimsg = <<"EOM";
<table width=500 align=center><tr><td>
■現在你進入了「一氣回覆模式」，你可以同時回覆多篇留言。只要在想要回覆的留言串列下面的留言框，把對應的留言分別填寫好，然後再按上面表單的「一氣回覆」按鈕即可。（注意：你只可以選擇一個圖檔。）如果你按下「關閉一氣回覆」，即可回到正常模式，所有留言串列下面的留言框隨即消失。
</td></tr></table>
EOM

#檢查留言內容的危險語法標籤
@errtag = ('table','meta','form','!--','embed','html','body','tr','td','th','a');       #危險語法標籤

#─＜基本設定結束＞────────────────────────────────────────────────────────

###############################################################################
#### Main Process  START  #####################################################
###############################################################################
$agent = $ENV{'HTTP_USER_AGENT'};
$agent =~ s/,/./g; $col2 = 1; $col2e = 1;	#(驚直加入 - 調整英數欄位在Netscape瀏覽器的闊度)
if ($agent =~ /Mozilla/i && $agent !~ /compatible/i && $agent !~ /Opera/i) { $col2 = 0.8; $col2e = 0.6; }	#(驚直修改 - 不套用於Opera瀏覽器)
$ENV{'TZ'} = "CST=UTC-8:00";   #(驚直修改 - 使用中國及台灣地區時間)
($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime(time);    #取得系統時間
$year  = sprintf("%02d",$year + 1900);  $month = $mon + 1;  #(驚直修改 - 月日不前置０或空白)
$hour  = sprintf("%02d",$hour); $min   = sprintf("%02d",$min);
$week = ('Sun','Mon','Tue','Wed','Thu','Fri','Sat') [$wday];    $today = "$year/$month/$mday($week) $hour:$min";    #(驚直修改 - 加入年份顯示)
if ($agent !~ /MSIE/i || $agent =~ /Opera/i) {	#(驚直修改 - 非IE瀏覽器使用特別樣式表)
	$css_style = $css_style_; $css_style_e = $css_style_e_; $css_button = $css_button_;
}
&logchk ;
&cookieget;																		#取得COOKIE資訊
&decode ;																		#過濾留言內容
if ( $FORM{'action'} eq 'icondisp' )	{ &icondisp ; }							#顯示圖檔一覽表
if ( $FORM{'action'} eq 'maintenance' )	{										#進入管理模式
	&Maintenance;
	&dataread ;																	#讀取記錄檔
}
if ( $FORM{'action'} eq 'update' )	{											#更新記錄檔（編輯時）
	&update ;
	&cookieget;																	#取得COOKIE資訊
	&dataread ;																	#讀取記錄檔
}
if ( $FORM{'action'} eq 'regist' )	{											#寫入留言記錄
	&regist ;
	&cookieget;																	#取得COOKIE資訊
	&dataread ;																	#讀取記錄檔
	&logchk ;
	$FORM{'action'} = "" ;
}
if ( $FORM{'action'} eq 'info' )		{ &info ; }								#顯示晉級資格說明
if ( $FORM{'action'} eq 'download' )	{ &dataread ; &download ; }				#下載留言記錄	#i001112
if ( $FORM{'action'} eq 'rankdisp' )	{ &rankdisp ; }							#顯示各人晉級狀態
&dataread ;																		#讀取記錄檔
&header ;																		#顯示HTML頁首
&header2 ;
&forminput if ( $FORM{'action'} ne 'oldlogfind' || $FORM{'oldlogno'} == 0 ) ;	#輸入留言內容
&view ;																			#顯示留言記錄
&footer ;																		#顯示HTML頁尾
exit;
###############################################################################
#### Main Process  END  #######################################################
###############################################################################
###<--------------------------------------------------------------
###<---   過濾留言內容＆代入變數
###<--------------------------------------------------------------
sub decode{
    if ($ENV{'REQUEST_METHOD'} eq "POST") {
        read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
    } else { $buffer = $ENV{'QUERY_STRING'}; }
    @pairs = split(/&/,$buffer);
    foreach $pair (@pairs) {
        ($name, $value) = split(/=/, $pair);
        $value =~ tr/+/ /;
        $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
        if ($tag eq 'yes') {
            #禁止使用危險語法!!!
            foreach ( @errtag ) {
				if ($value =~ /<$_(.|\n)*/i) { &error("抱歉，留言板禁止使用危險語法！"); }	#(驚直修改 - 針對"<!--"這個問題語法修正原程式缺陷)
            }
        }   else    {
            $value =~ s/</&lt;/g;
            $value =~ s/>/&gt;/g;
        }
        $value =~ s/\,/&#44;/g; #(驚直修改 - 使用半形逗號)
        $FORM{$name} = $value;
    }
    $FORM{'hp'}   =~ s/^http\:\/\///;
    $FORM{'comment'} =~ s/\r\n/<br>/g;  $FORM{'comment'} =~ s/\r|\n/<br>/g;

    for ( 1..$pagemax ) {   #i001103
        $wk = "rescomment" . $_ ;
        if ( $FORM{$wk} ne '' ) {
            $FORM{$wk} =~ s/\r\n/<br>/g;    $FORM{$wk} =~ s/\r|\n/<br>/g;
        }
    }
}
###<--------------------------------------------------------------
###<---   輸入留言內容
###<--------------------------------------------------------------
sub forminput {
    if ( $FORM{'action'} ne 'res' ) {
        if ( $FORM{'action'} ne 'maintenance' ) {
            $c_name = $COOKIE{'nm'} ;   $c_email = $COOKIE{'em'} ;  $c_hp = $COOKIE{'hp'} ;
            $c_color = $COOKIE{'cl'} ;  $c_color_f = $COOKIE{'cl_f'} ;
            $c_icon = $COOKIE{'icon'} ; $c_pass = $COOKIE{'ps'} ;
            $c_title = '' ; $c_comment = '' ;
        }   else    {
            print "<center><font size=3 color=$tcolor>編輯留言內容</font></center><br>\n";
            if ( $FORM{'proc'} eq 'delete' )    {
                $c_name = $COOKIE{'nm'} ;   $c_email = $COOKIE{'em'} ;  $c_hp = $COOKIE{'hp'} ;
                $c_color = $COOKIE{'cl'} ;  $c_color_f = $COOKIE{'cl_f'} ;
                $c_icon = $COOKIE{'icon'} ; $c_pass = $COOKIE{'ps'} ;
                $c_title = '' ; $c_comment = '' ;
            }
        }
    }   else    {
        $c_name = $COOKIE{'nm'} ;   $c_email = $COOKIE{'em'} ;  $c_hp = $COOKIE{'hp'} ;
        $c_color = $COOKIE{'cl'} ;  $c_color_f = $COOKIE{'cl_f'} ;
        $c_icon = $COOKIE{'icon'} ; $c_pass = $COOKIE{'ps'} ;
        $c_title = '' ; $c_comment = '' ;
    }
    print "<form action=$script name=inputform method=$method>\n";
    if ( $FORM{'action'} eq 'maintenance' ) {
        print "<input type=hidden name=\"action\" value=\"update\">\n";
        print "<input type=hidden name=\"no\" value=\"$FORM{'no'}\">\n";
        print "<input type=hidden name=\"proc\" value=\"edit\">\n";
    }   else    {
        print "<input type=hidden name=\"action\" value=\"regist\">\n";                 #i001103
        print "<input type=hidden name=\"disppage\" value=$FORM{'disppage'}>\n";        #i001103
        print "<input type=hidden name=\"kflg\" value=\"$FORM{'kflg'}\">\n";            #i001103
    }
    if ( $tbgcolor ) { $padd = 2 ; } else { $padd = 1 ; }
    print "<table align=center cellspacing=0 cellpadding=$padd>\n";

    if ( $tbgcolor ) { $tbgcolor="bgcolor=$tbgcolor"; } else { $tbgcolor="";}   #u000807

    #名字
    print "<tr><td $tbgcolor>\n";
    if ( $gif_flg == 1 )    {
        print "<img src=\"$gif_name\"></td>\n";
    }   else    {
        print "　　名字：</td>\n";
    }
    print "<td $tbgcolor>";
    print "<input type=text name=\"name\" size=23% value=\"$c_name\" $css_style></td></tr>\n";
    #電子郵箱
    #print "<tr><td $tbgcolor>\n";   #u000807
    #if ( $gif_flg == 1 )    {
    #    print "<img src=\"$gif_email\"></td>\n";
    #}   else    {
    #    print "電子郵箱：</td>\n";
    #}
    #print "<td $tbgcolor>";
	#print "<input type=text name=\"email\" size=23% value=\"$c_email\" $css_style></td></tr>\n";	#(驚直修改 - 使用英數欄位樣式表)
    #個人網站
    #print "<tr><td $tbgcolor>\n";
    #if ( $gif_flg == 1 )    {
    #    print "<img src=\"$gif_home\"></td>\n";
    #}   else    {
    #    print "個人網站：</td>\n";
    #}
    #print "<td $tbgcolor>";
	#print "<input type=text name=\"hp\" size=23% value=\"http://$c_hp\" $css_style>\n";	#(驚直修改 - 使用英數欄位樣式表)
    #if ( $FORM{'action'} ne 'res' && $c_resno eq '' )   {
    #    if ( $titleset == 0 || $FORM{'kflg'} )  {                                               #i000714
    #        if ( $FORM{'kflg'} ) { $k = "一氣回覆"; } else { $k = "送出留言" }                  #(驚直加入 - 判別一氣回覆模式時,送出按鈕上的文字)
    #        print "&nbsp;&nbsp;&nbsp;<input type=submit value=$k $css_button>&nbsp;&nbsp;\n";   #i000714
    #        print "&nbsp;<input type=reset value=重設資料 $css_button>\n";                      #i000714
    #    }                                                                                       #i000714
    #    print "</td>\n";
    #}   else    {
    #    print "&nbsp;&nbsp;<input type=submit value=送出回覆 $css_button>\n";
    #    print "<input type=hidden name=\"resno\" value=$FORM{'no'}>\n";
    #    print "&nbsp;<input type=reset value=重設資料 $css_button></td>\n";
    #}
    #print "</tr>\n";
    #留言標題
    if ( $FORM{'kflg'} eq '' )  {
        if  ( $FORM{'action'} ne 'res' && $c_resno eq '' )  {
            if ( $titleset == 1 ) {
                print "<tr><td $tbgcolor>\n";
                if ( $gif_flg == 1 )    {
                    print "<img src=\"$gif_title\"></td>\n";
                }   else    {
                    print "留言標題：</td>\n";
                }
		print "<td $tbgcolor>";
		#print "<input type=text name=\"title\" size=",36 * $col2," value=\"$c_title\" $css_style>\n";
		print "<input type=text name=\"title\" size=23% value=\"$c_title\" $css_style>\n";
		print "</td></tr>\n";
		#print "&nbsp;&nbsp;&nbsp;<input type=submit value=送出留言 $css_button>&nbsp;&nbsp;\n";
		#print "&nbsp;<input type=reset value=重設資料 $css_button></td></tr>\n";
            }
        }
        #留言內容
        print "<tr><td $tbgcolor>\n";
        if ( $gif_flg == 1 )    {
            print "<img src=\"$gif_message\"></td>\n";
        }   else    {
            print "留言內容：</td>\n";
        }
        print "<td $tbgcolor>";
        if ( $nya == 0 ) { $dmy = "wrap=soft" ; } else { $dmy = "wrap=hard" ; }
	#print "<textarea name=\"comment\" cols=",$col * $col2," rows=\"$row\" $dmy $css_style>$c_comment</textarea></td></tr>\n";	#(驚直修改 - 調整欄位在Netscape瀏覽器的闊度)
		print "<textarea name=\"comment\" cols=20% rows=\"$row\" $dmy $css_style>$c_comment</textarea></td></tr>\n";	#(驚直修改 - 調整欄位在Netscape瀏覽器的闊度)
        #窗框顏色
        if ( $colb_use != 1 && $FORM{'action'} ne 'res' && $c_resno eq '')  {
            print "<tr><td $tbgcolor>窗框顏色：</td>\n";
            print "<td $tbgcolor>\n";
            foreach (0 .. $#COLORS_B) {
                if ( $c_color == $_ || ($c_color eq '' && $_ == 0)) {   $dmy = "checked";   }   else    {   $dmy = "" ; }
                print "<input type=radio name=color value=\"$_\" $dmy>";
				print "<span style=font-size:$pt_mini;color:$COLORS_B[$_]>■</span>\n";	#(驚直修改 - 改以微縮字形大小顯示)
            }
            print "</td></tr>\n";
        }
    }
    #文字顏色
    if ( $colf_use != 1 )   {
        print "<tr><td $tbgcolor>文字顏色：</td>\n";
        print "<td $tbgcolor>\n";
        foreach (0 .. $#COLORS_F) {
            if ( $c_color_f == $_ || ($c_color_f eq '' && $_ == 0)) {   $dmy = "checked";   }   else    {   $dmy = "" ; }
            print "<input type=radio name=color_f value=\"$_\" $dmy>";
			print "<span style=font-size:$pt_mini;color:$COLORS_F[$_]>■</span>\n";	#(驚直修改 - 改以微縮字形大小顯示)
        }
        print "</td></tr>\n";
    }
    print "<tr>\n";
    #圖檔選擇
    if ( $icon_rank == 0 && $icon_use eq 'yes') {
        print "<td $tbgcolor>\n";
        print "圖檔選擇：</td>\n";
        print "<td nowrap $tbgcolor>";
        print "<select name=\"icon\" $css_select>\n";
        $i = 0 ;
        for ( @iconnm ) {
            if ( $i == $c_icon )    {   $dmy = "selected";  }   else    {   $dmy = "" ; }
            print "<option value=$i $dmy>$iconnm[$i]\n";
            $i++ ;
        }
        print "</select>\n";
		print "&nbsp;&nbsp;<span style=font-size:$pt_mini>[ <a href=\"$script?action=icondisp\" target=_blank>圖檔一覽表</a> ]</span></td></tr></table>\n";	#(驚直修改 - 改以新視窗方式開啟,以微縮字形大小顯示)
        #留言密碼
	#print "&nbsp;&nbsp;&nbsp;&nbsp;留言密碼：\n";
	print "<table align=\"center\" ><tr><td>";
	print "<br><td>留言密碼：\n";
        print "<input type=password name=\"pass\" size=8 value=\"$c_pass\" $css_style>&nbsp;&nbsp;(修改刪除留言時用)</td>\n";
        print "</tr></table>";
	print "<table align=\"center\"><tr><td>";
	#by LeoPicasso 2012/06/19
		#產生四個數字驗證碼
		@s[0] = int(rand()*10);#產生第一數字驗證碼
		@s[1] = int(rand()*10);#產生第二數字驗證碼
		@s[2] = int(rand()*10);#產生第三數字驗證碼
		@s[3] = int(rand()*10);#產生第四數字驗證碼
		print "<table align=\"center\"><tr><td>";
		print "驗證碼：";
		print "@s[0]"; 		#顯示第一驗證碼 by LeoPicasso 2012/06/19
		print "@s[1]";		#顯示第二驗證碼 by LeoPicasso 2012/06/19
		print "@s[2]";		#顯示第三驗證碼 by LeoPicasso 2012/06/19
		print "@s[3]";		#顯示第四驗證碼 by LeoPicasso 2012/06/19
		open SAVECHECKNO,'>check.txt'; #儲存驗證碼 by LeoPicasso 2012/06/19
		print SAVECHECKNO @s;
		close(SAVECHECKNO);
		print "&nbsp;&nbsp;<input type=text name=\"check\" size=8% value=\"\" >";		#產生"輸入驗證碼"框 by LeoPicasso 2012/06/19

        print "&nbsp;&nbsp;&nbsp;<input type=submit value=送出留言 $css_button>&nbsp;&nbsp;\n";
	print "&nbsp;<input type=reset value=重設資料 $css_button></td></tr></table>\n";
        print "</form>" if ( $FORM{'kflg'} eq '' ); #i001103
        if ( $FORM{'kflg'} ne '' ) {    print "<pre>$ikkimsg</pre>" ; }
        return ;
    }
    #留言密碼
    print "<td $tbgcolor>留言密碼：</td>\n";
    print "<td $tbgcolor>";
    print "<input type=password name=\"pass\" size=8 value=\"$c_pass\" $css_style>&nbsp;&nbsp;(修改刪除留言時用)</td>\n";
    print "</tr></table>";
    print "<table align=\"center\"><tr><td>";
   
    print "&nbsp;<input type=reset value=重設資料 $css_button></td></tr></table>\n";
    print "</form>" if ( $FORM{'kflg'} eq '' ); #i001103
    if ( $FORM{'kflg'} ne '' ) {    print "$ikkimsg" ; }
}
###<--------------------------------------------------------------
###<---   HTML表頭部份
###<--------------------------------------------------------------
sub header {
    print "Content-type: text/html; charset=utf-8\n\n";
    print "<html>\n<head>\n";
    print "<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\">\n";
    if  ( $FORM{'action'} eq 'icondisp' )       {   print "<title>$title【圖檔一覽表】</title>\n";      }
    elsif   ( $FORM{'action'} eq 'rankdisp' )   {   print "<title>$title【各人晉級狀態】</title>\n";    }
    elsif   ( $FORM{'action'} eq 'info' )       {   print "<title>$title【晉級資格說明】</title>\n";    }
    else {  print "<title>$title</title>\n";    }   #(驚直修改 - 判別其他新頁面的名稱來定義標題)
	#<<<CSS樣式表開始>>>
    print "<style type=\"text/css\">\n";
    print "<!--\n";
	print "a,a:link  {color:$linkcolor;text-decoration:none}\n";	#(驚直修改 - 連結文字跟隨整體字形大小)
    print "a:visited {color:$vlinkcolor;text-decoration:none}\n";
    print "a:active  {color:$alinkcolor;text-decoration:none}\n";
    print "a:hover   {color:$hovercolor;text-decoration:underline}\n";
	print "body,tr,td {font-size:$pt;word-break:break-all}\n";		#(驚直修改 - 加入work-break屬性,防止被惡意破壞版面)
    print "-->\n";
    print "</style>\n";
	#<<<CSS樣式表結束>>>
    print "</head>\n";
    if ($backpicture) { $set = "background=\"$backpicture\""; if ( $bgcolor ) { $set .= " bgcolor=\"$bgcolor\"" ; } }
    elsif ($bgcolor ) { $set = "bgcolor=\"$bgcolor\""; }
    print "<body $set text=$tcolor link=$linkcolor vlink=$vlinkcolor alink=$alinkcolor>\n";
}
###<--------------------------------------------------------------
###<---   顯示HTML頁首
###<--------------------------------------------------------------
sub header2 {
    print "<table width=100% align=center cellspacing=0 cellpadding=0><tr><td>\n";
    #print "<table cellspacing=0 cellpadding=0><tr><form><td>";  #(驚直修改 - 外加表格)
    #print "<input type=button value=\"ＨＯＭＥ\" ";
    #print "onClick=\"top.location.href=\'$url\'\" $css_button></td></form>\n";    #(驚直修改 - 改以全視窗方式開啟)
    if ( $logfile2 && $FORM{'action'} ne 'download')    {
	    #print "<td width=5>&nbsp;</td><form><td><input type=button value=\"晉級資格說明\" ";
	    #print "onClick=\"window.open('$script?action=info');\" $css_button></td></form>\n";     #(驚直修改 - 改以新視窗方式開啟)
	    #print "<td width=5>&nbsp;</td><form><td><input type=button value=\"各人晉級狀態\" ";
	    #print "onClick=\"window.open('$script?action=rankdisp');\" $css_button></td></form>\n"; #(驚直修改 - 改以新視窗方式開啟)
    }
    if ( $ikkiflg == 1 )    {
        print "<td width=5>&nbsp;</td><form><td>\n";
        if ( $FORM{'kflg'} eq '' )  {
		#    print "<input type=button value=\"啟動一氣回覆\" ";
		#print "onClick=\"location.href=\'$script?kflg=1\'\" $css_button></td></form>\n";  #(驚直修改 - 改以同一視窗方式開啟)
        }   else    {
		#print "<input type=button value=\"關閉一氣回覆\" ";
		#print "onClick=\"location.href=\'$script\'\" $css_button></td></form>\n";         #(驚直修改 - 改以同一視窗方式開啟)
        }
    }
    if ( $#oldcnt >= 0 ) {
        print "<td width=10>&nbsp;</td><form action=\"$script\" method=\"$method\"><td nowrap>\n";  #(驚直修改 - 加入空白表格欄)
        print "&nbsp;&nbsp;<select name=\"oldlogno\" $css_select>\n";
        print "<option value=0>最新的留言集";
        $i = 2010 ;
        foreach ( @oldcnt ) {
            $i = sprintf("%02d",$i ) ;
            if ( $FORM{'oldlogno'} == $i ) { $dmy = "selected" ; } else { $dmy = "" ;}
            print "<option value=$i $dmy >$i留言集";
            $i++ ;
        }
        print "</select>\n";
        print "<input type=hidden name=\"action\" value=\"oldlogfind\">\n";
        print "<input type=submit value=\"顯示\" $css_button></td></form>\n";
    }
    print "</tr></table></td><td align=right>";
    if ( $cntfile ) {
        #顯示計數器
        $edt = "%0" .$cnt_keta . "d" ;
        $COUNT = sprintf("$edt",$COUNT) ;
        if ( $cnt_gif[0] )  {
            for ( $i = 1 ; $i <= $cnt_keta ; $i++ ) {
                $c  = substr($COUNT,$i - 1 , 1 ) ;
                print "$cnt_gif[$c]";
            }
        }   else    {
            print "瀏覽人次 → <font face=\"$e_font\">$COUNT</font>";   #(驚直修改 - 使用英文字形顯示純文字計數器)
        }
    }   else    {
        print "&nbsp;";
    }
    print "</td></tr></table>\n";
    print "<center><br>\n";
    #if ( $titlelogo )   {
    #    print "$titlelogo<br>\n";
    #}   else    {
        print "<font size=+1 color=\"$tcolor\">$title</font><br>\n";
	#}
	print "</center>\n";
}
###<--------------------------------------------------------------
###<---   顯示HTML頁尾
###<--------------------------------------------------------------
sub footer {
    #<<<↓以下版權宣告部份不得刪除，但可略作修改。（尊重智慧財產權 — 請勿將中文化作者刪掉或改為你自己的名字）
	print "<div align=right><span style=font-size:9pt>\n";
    print "<a href=http://tackysroom.com target=_blank style=\"font-family:$e_font\">mkakikomitai Ver$ver Created by Tacky\'s Room</a><br>\n";
    print "中文化：<a href=http://kiddiken.net target=_blank>天真的驚直</a> <font face=\"$e_font\">[2001.3.4]</font></span></div>\n";
    print "</body></html>\n";
}
###<--------------------------------------------------------------
###<---   讀取記錄檔
###<--------------------------------------------------------------
sub dataread    {
    #讀取記錄檔
    if ( ( $FORM{'action'} ne 'oldlogfind' && $FORM{'action'} ne 'download' ) || $FORM{'oldlogno'} == 0 ) {
        if ( !(open(IN,"$logfile")))    {   &error("記錄檔 <font face=\"$e_font\">($logfile)</font> 讀取失敗。");   }
    }   else    {
        $wk = $olddir . $FORM{'oldlogno'} . ".txt" ;
        if ( !(open(IN,"$wk")))         {   &error("記錄檔 <font face=\"$e_font\">($wk)</font> 讀取失敗。");    }
    }
    @LOG = <IN>;
    close(IN);
    @RESLOG = () ; @MAINLOG = () ;
    $MAXNO = '';
    @SVLOG = () ;
    foreach ( @LOG )    {
        ($no,$name,$email,$hp,$ttl,$comment,$regdate,$color_f,$color,$resno,$hst,$ksu,$pass,$dmy,$dmy,$icon) = split(/,/,$_);
        if ( $resno eq '' ) {
            push(@MAINLOG,$_) ;
        }   else    {
            push(@RESLOG,$_) ;
        }
        push(@SVLOG,"$_");
        if ( $no >= $MAXNO ) {
            $MAXNO = $no ;
        }
    }
    if ( $FORM{'action'} ne 'oldlogfind' || $FORM{'oldlogno'} == 0 ) {  #I991220
        @RESLOG = reverse @RESLOG ;
    }                                                                   #I991220

    #<<<讀取計數器記錄檔
    if ( $cntfile && $FORM{'action'} ne 'download' )    {   #u001112
        if ( !(open(IN,"$cntfile")))    {   &error("計數器記錄檔 <font face=\"$e_font\">($cntfile)</font> 讀取失敗。"); }
        $COUNT = <IN>;
        close(IN);
        if ( $FORM{'action'} eq '') {
            $COUNT++ ;
            if ( !(open(OUT,">$cntfile")))  {   &error("計數器記錄檔 <font face=\"$e_font\">($cntfile)</font> 讀取失敗。"); }
            print OUT $COUNT;
            close(OUT);
        }
    }
}
###<--------------------------------------------------------------
###<---   顯示留言記錄
###<--------------------------------------------------------------
sub view    {
    print "<hr width=70% size=1 noshade color=black>\n";
    #計算留言記錄所需之頁數
    $dm = @MAINLOG;
    if ( $dm % $pagemax == 0) {
        $p = $dm / $pagemax ;
    }   else    {
        $p = $dm / $pagemax + 1;
    }
    $p = sprintf("%3d",$p);
    if ( $FORM{'page'} eq "下一頁" )    {
        if ( $FORM{'disppage'} == 0 ) { $FORM{'disppage'} = 1 } ;
        $d = ($FORM{'disppage'} + 1) * $pagemax - $pagemax ;
        $FORM{'disppage'} = $FORM{'disppage'} + 1 ;
    }   elsif   ( $FORM{'page'} eq "上一頁" )   {
        $d = ($FORM{'disppage'} - 1) * $pagemax - $pagemax ;
        $FORM{'disppage'} = $FORM{'disppage'} - 1 ;
    }   elsif   ( $FORM{'disppage'} ne "" )     {       #I991123
        $d = $FORM{'disppage'} * $pagemax - $pagemax ;  #I991123
    }   else    {
        $d = 0  ;
        $FORM{'disppage'} = 1 ;
    }
    if ( $msg_color ) { $tbbg = "bgcolor=\"$msg_color\"" ; } else { $tbbg = "" ; }
    $z = 1 ;

    if ( $FORM{'action'} eq 'download' ) { #i001112
        $d = 0 ; $pagemax = $dm ; $maru = 0 ; $maillinklogo=""; $homelinklogo=""; $icon_use = "no";
        print "<br><center><font size=3>$title</font></center>\n";
    }

    for ( $i = $d ; ( $z <= $pagemax ) && ( $i < $dm ); $i++ )  {
        ($no,$name,$email,$hp,$ttl,$comment,$regdate,$color_f,$color,$resno,$host,$ksu,$pass,$dmy,$dmy,$icon) = split(/,/,$MAINLOG[$i]);
        if  ( ($FORM{'action'} ne 'res' || ($FORM{'action'} eq 'res' && $FORM{'no'} eq $no)) || $FORM{'action'} eq 'download' ) {   #u001112
            if  ( $FORM{'action'} ne 'res' && $FORM{'kflg'} eq '' ) {   #i001103
                print "<form action=$script method=$method>";
                print "<input type=hidden name=\"action\" value=\"res\">";
                print "<input type=hidden name=\"no\" value=\"$no\">";
                print "<input type=hidden name=\"disppage\" value=$FORM{'disppage'}>\n";    #I991123
            }
            if ( $nya == 0 ) {
                $comment =~ s/([^=^\"]|^)(http|ftp)([\w|\!\#\&\=\-\%\@\~\;\+\:\.\?\/]+)/$1<a href=\"$2$3\" target=_blank><font face=\"$e_font\"><b>LINK HERE<\/b><\/font><\/a>/g;   #(驚直修改 - 改為LINK HERE英文字樣及開新視窗)
            }   else    {
                $comment =~ s/<br>/<br><hr size=1 noshade>/g;
            }
            if ( $colf_use != 1 )   { $color_f = $COLORS_F[$color_f] ; }    #留言者選擇的文字顏色
                            else    { $color_f = $colf ; }                  #管理者指定的文字顏色
            if ( $colb_use != 1 )   { $color = $COLORS_B[$color] ; }        #留言者選擇的背景顏色
                            else    { $color = $colb ; }                    #管理者指定的背景顏色

            print "<br>\n";
	    #print "<table align=center cellspacing=0 cellpadding=0 width=\"$t_width\">\n";
            print "<table align=center cellspacing=0 cellpadding=0 width=70%>\n";
            if ( $maru == 1 ) { #使用圓角留言框的場合
                print "<tr>\n";
				print "<td bgcolor=$color>$top_l</td>\n";
				print "<td bgcolor=$color><img src=\"$gif_spacer\" width=1 height=1></td>\n";
				print "<td bgcolor=$color align=right valign=top>$top_r</td>\n";
                print "</tr>\n";
            }   else    {
                print "<tr>\n";
				if  ( $FORM{'action'} ne 'download' ) {	#kxxk20010217
					print "<td bgcolor=$color colspan=3 height=8><img src=\"$gif_spacer\" width=1 height=8></td>\n";
				} else {
					print "<td bgcolor=$color colspan=3 height=8>&nbsp;</td>\n";
				}
                print "</tr>\n";
            }
            print "<tr>\n";
			if  ( $FORM{'action'} ne 'download' ) {	#kxxk20010217
				print "<td width=8 bgcolor=$color><img src=\"$gif_spacer\" width=1 height=1></td>\n";
			} else {
				print "<td width=8 bgcolor=$color>&nbsp;</td>\n";
			}
            print "<td bgcolor=\"$color\">\n";
                if ( $titleset == 1 ) {
                    if ( !($ttl) )  {   $ttl = "(無題)";    }
                    print "<font color=\"$name_color\">■ $ttl</font><br>\n";
                }
                print "<font color=\"$name_color\">$name&nbsp;&nbsp;&nbsp;";
                if ( $logfile2 ne '' )  {
                    $ranking = &rankget($ksu) ;
					print "&nbsp;&nbsp;<span style=font-size:$pt_mini>($ranking)";	#(驚直修改 - 以微縮字形大小顯示)
                    if ( $kaisu_disp == 1 ) { print "　∼第<font face=\"$e_font\">$ksu</font>篇∼"; }   #(驚直修改 - 留言篇數用英文字形顯示)
                    print "</span>\n";
                }
				print "</font>&nbsp;&nbsp;&nbsp;";	#(驚直修改 - 修正原程式</font>語法錯誤)
				if ( $email ne '' ) {
					if ( $maillinklogo ) { print "<a href=mailto:$email>$maillinklogo</a>\n";
					} else { print "<font color=$name_color>[ <a href=mailto:$email><font face=\"$e_font\">MAIL</font></a> ]</font>\n"; }	#(驚直修改 - 美化字形)
				}
				if ( $hp ne '' ) {
					if ( $homelinklogo ) { print "<a href=http://$hp target=_blank>$homelinklogo</a>\n";
					} else { print "<font color=$name_color>[ <a href=http://$hp target=_blank><font face=\"$e_font\">HP</font></a> ]</font>\n"; }	#(驚直修改 - 美化字形)
				}
                if  ( $FORM{'action'} ne 'res' && $FORM{'oldlogno'} == 0  && $FORM{'kflg'} eq '' && $FORM{'action'} ne 'download' ) {   #i001103
                    if ( $res_gif ) {
						print "&nbsp;&nbsp;&nbsp;&nbsp;<input type=image name=send src=\"$res_gif\" border=0 alt=\"回覆留言\">\n";
                    }   else    {
                        print "&nbsp;&nbsp;&nbsp;<input type=submit value=\"回覆\" $css_button>\n";
                    }
                }
            print "</td>\n";
			if  ( $FORM{'action'} ne 'download' ) {	#kxxk20010217
				print "<td width=8 bgcolor=$color><img src=\"$gif_spacer\" width=1 height=1></td>\n";
			} else {
				print "<td width=8 bgcolor=$color>&nbsp;</td>\n";
			}
            print "</tr><tr>\n";
			if  ( $FORM{'action'} ne 'download' ) {	#kxxk20010217
				print "<td width=8 bgcolor=$color><img src=\"$gif_spacer\" width=1 height=1></td>\n";
			} else {
				print "<td width=8 bgcolor=$color>&nbsp;</td>\n";
			}
            print "<td bgcolor=\"$color\">\n";
                print "<hr size=1 noshade color=white>";
				print "<table cellspacing=0 cellpadding=3 width=100%>\n";	#(驚直修改 - 刪除原程式多餘的<div>語法)
				print "<tr><td $tbbg rowspan=2>\n";	#(驚直修改 - 美化留言內容排列)
                #顯示圖檔
                if ( $icon_use eq 'yes' )   {   &icon_set($name) ;  }   else    {   print "&nbsp;"; }
				print "</td><td $tbbg width=95% valign=top>\n";	#(驚直修改 - 留言內容靠上顯示)
                print "<font color=$color_f>$comment</font>\n"; #(驚直修改 - 修正原程式</div>語法位置錯誤)
				print "</td></tr><tr><td $tbbg align=right valign=bottom>";	#(驚直修改 - 留言資訊靠下顯示)
                $no = sprintf("%d",$no);
				print "<span style=\"font-size:$pt_mini;font-family:$e_font;color:$color_f\">";	#(驚直修改 - 改用span語法,自定英文字形集,以微縮字形大小顯示)
                if ( $hostflag eq 'yes')    {       print "($host) ";   }
				print ".. $regdate \[$no\]</span></td></tr></table><hr size=1 noshade color=white>";	#kxxk20010130
                #顯示訪客回應的留言
                $j = 0 ;
                foreach $buf ( @RESLOG )    {
                    ($no2,$name,$email,$hp,$ttl,$comment,$regdate,$col_f,$col_b,$resno,$host,$ksu,$pass,$dmy,$dmy,$icon) = split(/,/,$buf); #u001103
                    if ( $no eq $resno )    {
                        if ( $colf_use != 1 )   { $col_f = $COLORS_F[$col_f] ; }    #留言者選擇的文字顏色（背景顏色與原留言者相同）
                                        else    { $col_f = $colf ; }                #管理者指定的文字顏色
                        print "<div align=right><table cellspacing=0 cellpadding=0 width=85%>\n";
                        print "<tr><td bgcolor=\"$color\">\n";
                            print "<table cellpadding=3 cellspacing=0 width=100%>\n";
                            print "<tr><td bgcolor=\"$color\" colspan=2 nowrap>\n";
                            print "<font color=\"$name_color\">$name&nbsp;&nbsp;&nbsp;";    #(驚直修改 - 修正原程式</font>語法錯誤)
                            if ( $logfile2 ne '' )  {
                                $ranking = &rankget($ksu) ;
								print "&nbsp;&nbsp;<span style=font-size:$pt_mini>($ranking)";	#(驚直修改 - 以微縮字形大小顯示)
                                if ( $kaisu_disp == 1 ) { print "　∼第<font face=\"$e_font\">$ksu</font>篇∼"; }   #(驚直修改 - 留言篇數用英文字形顯示)
                                print "</span>\n";
                            }
                            print "</font>&nbsp;&nbsp;&nbsp;";    #(驚直修改 - 修正原程式</font>語法錯誤)
							if ( $email ne '' ) {
								if ( $maillinklogo ) { print "<a href=mailto:$email>$maillinklogo</a>\n";
								} else { print "<font color=$name_color>[ <a href=mailto:$email><font face=\"$e_font\">MAIL</font></a> ]</font>\n"; }	#(驚直修改 - 美化字形)
							}
							if ( $hp ne '' ) {
								if ( $homelinklogo ) { print "<a href=http://$hp target=_blank>$homelinklogo</a>\n";
								} else { print "<font color=$name_color>[ <a href=http://$hp target=_blank><font face=\"$e_font\">HP</font></a> ]</font>\n"; }	#(驚直修改 - 美化字形)
							}
							print "</td></tr>\n";
							print "<tr><td $tbbg rowspan=2>\n";	#(驚直修改 - 美化留言內容排列)
                            #顯示圖檔
                            if ( $icon_use eq 'yes' )   {   &icon_set($name) ;  }   else    {   print "&nbsp;"; }
							print "</td><td $tbbg width=95% valign=top>\n";	#(驚直修改 - 留言內容靠上顯示)
                            if ( $nya == 0 ) {
                                $comment =~ s/([^=^\"]|^)(http|ftp)([\w|\!\#\&\=\-\%\@\~\;\+\:\.\?\/]+)/$1<a href=\"$2$3\" target=_blank><font face=\"$e_font\"><b>LINK HERE<\/b><\/font><\/a>/g;   #(驚直修改 - 改為LINK HERE英文字樣及開新視窗)
                            }   else    {
                                $comment =~ s/<br>/<br><hr size=1 noshade>/g;
                            }
                            print "<font color=$col_f>$comment</font><br>\n";
							print "</td></tr><tr><td $tbbg align=right valign=bottom>";	#(驚直修改 - 留言資訊靠下顯示)
                            $no2 = sprintf("%d",$no2);
							print "<span style=\"font-size:$pt_mini;font-family:$e_font;color:$col_f\">";	#(驚直修改 - 改用span語法,自定英文字形集,以微縮字形大小顯示)
                            if ( $hostflag eq 'yes')    {
                                print "($host) ";
                            }
							print ".. $regdate \[$no2\]</span></td></tr></table>\n";	#kxxk20010130
                        print "</td></tr></table></div>\n";
                        $j++;
                    }
                }
            print "</td>\n";
			if  ( $FORM{'action'} ne 'download' ) {	#kxxk20010217
				print "<td width=8 bgcolor=$color><img src=\"$gif_spacer\" width=1 height=1></td>\n";
			} else {
				print "<td width=8 bgcolor=$color>&nbsp;</td>\n";
			}
            print "</tr>\n";
            if ( $maru == 1 ) { #使用圓角留言框的場合
                print "<tr>\n";
                print "<td bgcolor=\"$color\">$bottom_l</td>\n";
                print "<td bgcolor=\"$color\"><img src=\"$gif_spacer\" width=1 height=1></td>\n";
                print "<td bgcolor=\"$color\" align=\"right\" valign=\"bottom\">$bottom_r</td>\n";
                print "</tr>\n";
            }   else    {
                print "<tr>\n";
				if  ( $FORM{'action'} ne 'download' ) {	#kxxk20010217
					print "<td bgcolor=$color colspan=3 height=8><img src=\"$gif_spacer\" width=1 height=8></td>\n";
				} else {
					print "<td bgcolor=$color colspan=3 height=8>&nbsp;</td>\n";
				}
                print "</tr>\n";
            }
            print "</table>";   #u001103
            if ( $FORM{'kflg'} == 1 && $FORM{'action'} ne 'download' ) {    #i001112
                print "<center><input type=hidden name=\"resno$z\" value=$no>\n";   #i001103
                print "▲請把回覆上面的留言內容寫在下面這個留言框▼\n"; #i001103
                print "<br><textarea name=\"rescomment$z\" cols=\"$col\" rows=\"$row\" $dmy $css_style>$c_comment</textarea></center><br>\n";   #i001103
            }   #i001103
            print "</form>\n" if ( $FORM{'kflg'} eq '' ) ;  #i001103
        }
        $z++;
    }
    print "</form>\n" if ( $FORM{'kflg'} == 1 ) ;   #i001112

    if  ( $FORM{'action'} ne 'res' && $FORM{'action'} ne 'download')    {
        $dm = @MAINLOG;
        if ( $dm % $pagemax == 0) {
            $p = $dm / $pagemax ;
        }   else    {
            $p = $dm / $pagemax + 1;
        }
        $p = sprintf("%3d",$p);
        print "<center><form action=$script method=$method>\n";
        print "<input type=hidden name=\"disppage\" value=$FORM{'disppage'}>\n";
        print "<input type=hidden name=\"action\" value=$FORM{'action'}>\n";
        print "<input type=hidden name=\"oldlogno\" value=$FORM{'oldlogno'}>\n";
        print "<input type=hidden name=\"kflg\" value=\"$FORM{'kflg'}\">\n";            #i001103
        if ( $FORM{'disppage'} != 0 && $FORM{'disppage'} !=1)   {
            print "<input type=submit name=\"page\" value=上一頁 $css_button>\n";
        }
        if ( $FORM{'disppage'} + 1 <= $p )  {
            print "<input type=submit name=\"page\" value=下一頁 $css_button>\n";
        }
        print "</form></center>\n";
    }
    if ( $FORM{'action'} eq 'download' ) { return; }    #i001112

    print "<hr size=1 noshade color=black>\n" ;
    print "<center><form action=\"$script\" method=\"$method\">\n";
    print "<input type=hidden name=\"action\" value=\"download\">\n";
    print "<input type=hidden name=\"oldlogno\" value=$FORM{'oldlogno'}>\n";
    print "<input type=submit value=\"下載目前的留言記錄檔\" $css_button>\n";
    print "<br>下載時，請把檔名加上 <font face=\"$e_font\">.htm 或 .html</font>。";
    print "</form></center>\n";
    if ( $FORM{'oldlogno'} == 0 )   {
        print "<hr width=70% size=1 noshade color=black>\n";
        print "<div align=\"right\"><form action=\"$script\" method=\"$method\">";  #(驚直修改 - 修正原程式<form>語法位置錯誤)
        print "<font color=\"$tcolor\">\n";
		print "留言編號：<input type=text name=\"no\" size=4 $css_style_e>\n";	#(驚直修改 - 使用英數欄位樣式表)
        print "密碼：<input type=password name=\"pass\" size=10 $css_style>\n";
        print "</font>\n";
        print "<select name=\"proc\" $css_select>\n";
        print "<option value=\"edit\">編輯\n";
        print "<option value=\"delete\">刪除\n";
        print "</select>\n";
        print "<input type=hidden name=\"action\" value=\"maintenance\">\n";
        print "<input type=hidden name=\"oldlogno\" value=$FORM{'oldlogno'}>\n";
        print "<input type=submit value=\"管理留言\" $css_button>\n";
        print "</form></div>\n";
    }
}
###<--------------------------------------------------------------
###<---   寫入記錄檔
###<--------------------------------------------------------------
sub regist  {
    #取得留言者的伺服器名稱
    $host  = $ENV{'REMOTE_HOST'};
    $addr  = $ENV{'REMOTE_ADDR'};
    if ($host eq "" || $host eq "$addr") {
        ($p1,$p2,$p3,$p4) = split(/\./,$addr);
        $temp = pack("C4",$p1,$p2,$p3,$p4);
        $host = gethostbyaddr("$temp", 2);
        if ($host eq "") { $host = $addr; }
    }
    #檢查危險語法標籤
    foreach $buf(@DANGER_LIST){
        if ( $buf ) {
            $buf=~ s/\./\\./g;      $buf=~ s/\?/\./g;       $buf=~ s/\*/\.\*/g;
            if ($host =~ /$buf/gi) { &error("抱歉，你所屬的網域名稱已被禁止在這個留言板使用。"); }
        }
    }
	open LOADCHECKNO,'check.txt'; #載入驗證碼 by LeoPicasso 2012/06/19
	$s= <LOADCHECKNO> ;
	close(LOADCHECKNO);
	$s= sprintf '%d',$s;#驗證碼轉為string by LeoPicasso 2012/06/19
	if ( $FORM{'check'} eq '')   {   &error("你還沒有填入驗證碼喔！"); } #確認是否填入驗證碼 by LeoPicasso 2012/06/19
	if ( length($FORM{'check'}) ne length($s) ) {&error("驗證碼輸入長度不符！");} #確認驗證碼長度 by LeoPicasso 2012/06/19
	if ($FORM{'check'} =~ m/\D/) {&error( "請輸入數字！" );} #確認驗證碼是數字 by LeoPicasso 2012/06/19
	if ($FORM{'check'} != $s) {&error("驗證碼輸入錯誤!");} #確認驗證碼是否正確 by LeoPicasso 2012/06/19
    if ( $FORM{'name'} eq '')   {   &error("你還沒有填入你的名字喔！"); }
    if ( $FORM{'kflg'} eq '' ) {    #i001103
        if ( $FORM{'comment'} eq '')    {   &error("為什麼留言內容是空的呢？"); }
        if ( $maxword ne '' && (length($FORM{'comment'}) > $maxword))   {   &error("你的留言內容太長了。留言內容不可超過 <font face=\"$e_font\">$maxword</font> 個字元！"); }
    }                               #i001103
	for ( $i = $pagemax ; $i >= 1 ; $i-- )	{
		$wk = "resno" . $i ;
		$rno = $FORM{$wk} ;
		$wk = "rescomment" . $i ;
		$rcom = $FORM{$wk} ;
		if ( $rno ne '' && $rcom ne '' )	{
			if ( $maxword ne '' && (length($rcom) > $maxword))	{	&error("你的留言內容太長了。留言內容不可超過 <font face=\"$e_font\">$maxword</font> 個字元！");	}
		}
	}
    &filelock ;	#檔案鎖定
    &dataread ;	#讀取記錄檔

    if ( $FORM{'kflg'} eq '' ) {    #i001103
    ($oyano,$name,$email,$hp,$ttl,$comment,$regdate,$color_f,$color,$resno,$hst,$ksu,$pass,$dmy,$dmy,$icon) = split(/,/,$SVLOG[0]);
    if ( $name eq $FORM{'name'} && $ttl eq $FORM{'title'} && $comment eq $FORM{'comment'} ) {
        &fileunlock ;   &error("不能再次寫入一模一樣的留言。可能你重複按了兩次按鈕嘍！") ;
    }
    if ( $logfile2 ne '' && ( $FORM{'action'} ne 'oldlogfind' || $FORM{'oldlogno'} == 0 ))  {
        if ( !(open(IN2,"$logfile2")))  {   &fileunlock ;   &error("晉級狀態記錄檔 <font face=\"$e_font\">($logfile2)</font> 讀取失敗。");  }
        $flg = 0 ;
        while ( <IN2> ) {
            ($n,$k) = split(/,/,$_);
            $k =~ s/\n//;
            if ( $FORM{'name'} eq $n )  {
                if ( $rdm != 0 )    {
                    #■隨機回扣留言篇數
                    srand(time ^ ($$ + ($$ << 15)));
                    $w  = int(rand(30)) ;
                    $p = 0 ;
                    #■根據$rdm的設定回扣留言篇數
                    if ( $w % $rdm == 0 )  {
                        $k  = $k - $DOWN[int(rand($#DOWN))] ;
                        if ( $k < 0 ) { $k = 0 ; }
                    }   else    {
                        $k++;
                    }
                }   else    {
                    $k++ ;
                }
                $dcnt = $k ;
                $flg = 9;
            }
            push(@sv,"$n,$k\n");
        }
        if ( $flg == 0 )    {
            push(@sv,"$FORM{'name'},1\n");
            $dcnt = 1;
        }
        close(IN2);
        if ( !(open(OUT2,">$logfile2")))    {   &fileunlock ;   &error("晉級狀態記錄檔 <font face=\"$e_font\">($logfile2)</font> 讀取失敗。");  }
        print OUT2 @sv;
        close(OUT2);
    }

    $dcnt2 = @SVLOG;
    if ( $dcnt2 < 1 )   {
        $no = 1;    #第１篇留言
    }   else    {
        $no = $MAXNO + 1;
    }

    #寫入訪客回覆的留言記錄時，將該篇留言整串移回最頂端的處理
    if ( $resflag eq 'yes' && $FORM{'resno'} ne '') {
        $cnt = 0 ;  $oyacnt = 1 ;
        foreach $buf ( @SVLOG ) {
            ($oyano,$name,$email,$hp,$ttl,$comment,$regdate,$color_f,$color,$resno,$hst,$ksu,$pass,$dmy,$dmy,$icon) = split(/,/,$buf);
            if ( $oyano eq $FORM{'resno'} ) {
                $sv_title = $ttl ;
                splice(@SVLOG,$cnt,1);
                $wk = "$oyano,$name,$email,$hp,$ttl,$comment,$regdate,$color_f,$color,$resno,$hst,$ksu,$pass,$dmy,$dmy,$icon";
                unshift(@SVLOG,$wk);
                last ;
            }
            $cnt++ ;
        }
    }   else    {
        if ( $sendmail ) {
            foreach $buf ( @SVLOG ) {
                ($oyano,$name,$email,$hp,$ttl,$comment,$regdate,$color_f,$color,$resno,$hst,$ksu,$pass,$dmy,$dmy,$icon) = split(/,/,$buf);
                if ( $oyano eq $FORM{'resno'} ) {
                    $sv_title = $ttl ;
                    last ;
                }
            }
        }
    }

    if ( $olddir ) {    #舊留言集的處理
        if ( !($FORM{'resno'}) && $#MAINLOG + 1 >= $datamax ) {
            ($oyano,$name,$email,$hp,$ttl,$comment,$regdate,$color_f,$color,$resno,$hst,$ksu,$pass,$dmy,$dmy,$icon) = split(/,/,$MAINLOG[$#MAINLOG]);
            @OLD = () ;
            if ( $#oldcnt >= 0 ) {
                if ( !(open(IN,"$oldfile")))    {   &fileunlock ;   &error("過去記錄檔 <font face=\"$e_font\">($oldfile)</font> 讀取失敗。");   }
                @OLD = <IN>;
                close(IN);
                if ( $#OLD + 1 >= $oldmax ) {
                    $i = sprintf("%02d",$#oldcnt + 2) ;
                    $oldfile = "$olddir$i" . ".txt" ;
                    @OLD = () ;
                }
            }   else    {
                    $oldfile = "$olddir" . "01.txt" ;
            }
            $cnt = 0 ;
            @SVLOG2 = @SVLOG ; @SVLOG = () ;
            foreach $buf ( @SVLOG2 ) {
                ($oyano2,$name,$email,$hp,$ttl,$comment,$regdate,$color_f,$color,$resno2,$hst,$ksu,$pass,$dmy,$dmy,$icon) = split(/,/,$buf);
                if ( $oyano == $oyano2 || $oyano == $resno2) {
                    unshift(@OLD,$buf) ;
                }   else    {
                    push(@SVLOG,$buf);
                }
                $cnt++ ;
            }
            if ( !(open(OUT,">$oldfile")))  {   &fileunlock ;   &error("過去記錄檔 <font face=\"$e_font\">($oldfile)</font> 讀取失敗。");   }
            print OUT @OLD;
            close(OUT);
            #更改檔案權限   (驚直提示 - 可設成更安全的0600)
            chmod(0666,"$oldfile");
        }
    }   else    {
        if ( !($FORM{'resno'}) && $#MAINLOG + 1 >= $datamax ) {
            ($oyano,$name,$email,$hp,$ttl,$comment,$regdate,$color_f,$color,$resno,$hst,$ksu,$pass,$dmy,$dmy,$icon) = split(/,/,$MAINLOG[$#MAINLOG]);
            @SVLOG2 = @SVLOG ; @SVLOG = () ;
            foreach $buf ( @SVLOG2 ) {
                ($oyano2,$name,$email,$hp,$ttl,$comment,$regdate,$color_f,$color,$resno2,$hst,$ksu,$pass,$dmy,$dmy,$icon) = split(/,/,$buf);
                if ( $oyano == $oyano2 || $oyano == $resno2) {
                }   else    {
                    push(@SVLOG,$buf);
                }
            }
        }
    }
    #留言密碼的加密程序（將密碼暗號化）
    if ($FORM{'pass'} ne "") { &pass_enc($FORM{'pass'}); }
    else    { $pass = '' ; }
    unshift(@SVLOG,"$no,$FORM{'name'},$FORM{'email'},$FORM{'hp'},$FORM{'title'},$FORM{'comment'},$today,$FORM{'color_f'},$FORM{'color'},$FORM{'resno'},$host,$dcnt,$pass,$dmy,$dmy,$FORM{'icon'}\n");
    if ( !(open(OUT,">$logfile")))  {   &fileunlock ;   &error("記錄檔 <font face=\"$e_font\">($logfile)</font> 讀取失敗。");   }
    print OUT @SVLOG;
    close(OUT);
	&fileunlock ;	#解除檔案鎖定
	$wk = $smail_address ;  $wk =~ s/\\//g;
	if ( $sendmail && ($sendsw == 1 || ( $sendsw == 0 && $FORM{'email'} ne $wk ) ) ) { &SMail ; }

    }   else    {           #↓i001103
    for ( $i = $pagemax ; $i >= 1 ; $i-- )  {
        $wk = "resno" . $i ;
        $rno = $FORM{$wk} ;
        $wk = "rescomment" . $i ;
        $rcom = $FORM{$wk} ;
        if ( $rno ne '' && $rcom ne '' )    {
            &dataread ;	#讀取記錄檔
            if ( $logfile2 ne '' )  {
                if ( !(open(IN2,"$logfile2")))  {   &fileunlock ;   &error("晉級狀態記錄檔 <font face=\"$e_font\">($logfile2)</font> 讀取失敗。");  }
                $flg = 0 ;
                @sv = ();
                while ( <IN2> ) {
                    ($n,$k) = split(/,/,$_);
                    $k =~ s/\n//;
                    if ( $FORM{'name'} eq $n )  {
                        $k++ ;
                        $dcnt = $k ;
                        $flg = 9;
                    }
                    push(@sv,"$n,$k\n");
                }
                if ( $flg == 0 )    {
                    push(@sv,"$FORM{'name'},1\n");
                    $dcnt = 1;
                }
                close(IN2);
                if ( !(open(OUT2,">$logfile2")))    {   &fileunlock ;   &error("晉級狀態記錄檔 <font face=\"$e_font\">($logfile2)</font> 讀取失敗。");  }
                print OUT2 @sv;
                close(OUT2);
            }
            $dcnt2 = @SVLOG;
            if ( $dcnt2 < 1 )   {
                $no = 1;    #第１篇留言
            }   else    {
                ($no,$name,$email,$hp,$ttl,$comment,$regdate,$color_f,$color,$resno,$hst,$ksu,$pass,$dmy,$dmy,$icon) = split(/,/,$SVLOG[0]);
                $no++;
            }
            #寫入訪客回覆的留言記錄時，將該篇留言整串移回最頂端的處理
            if ( $resflag eq 'yes') {
                $cnt = 0 ;  $oyacnt = 1 ;
                foreach $buf ( @SVLOG ) {
                    ($oyano,$name,$email,$hp,$ttl,$comment,$regdate,$color_f,$color,$resno,$hst,$ksu,$pass,$dmy,$dmy,$icon) = split(/,/,$buf);
                    if ( $oyano eq $rno )   {
                        splice(@SVLOG,$cnt,1);
                        $wk = "$oyano,$name,$email,$hp,$ttl,$comment,$regdate,$color_f,$color,$resno,$hst,$ksu,$pass,$dmy,$dmy,$icon";
                        unshift(@SVLOG,$wk);
                        last ;
                    }
                    $cnt++ ;
                }
            }
            #留言密碼的加密程序（將密碼暗號化）
            if ($FORM{'pass'} ne "") { &pass_enc($FORM{'pass'}); }
            else    { $pass = '' ; }
            unshift(@SVLOG,"$no,$FORM{'name'},$FORM{'email'},$FORM{'hp'},,$rcom,$today,$FORM{'color_f'},,$rno,$host,$dcnt,$pass,$dmy,$dmy,$FORM{'icon'}\n");
            if ( !(open(OUT,">$logfile")))  {   &fileunlock ;   &error("記錄檔 <font face=\"$e_font\">($logfile)</font> 讀取失敗。");   }
            print OUT @SVLOG;
            close(OUT);
			&fileunlock ;	#解除檔案鎖定
			$wk = $smail_address ;  $wk =~ s/\\//g;
			if ( $sendmail && ($sendsw == 1 || ( $sendsw == 0 && $FORM{'email'} ne $wk ) ) ) { &SMail ; }	#(驚直修改 - 修正原程式的寄發郵件通知功能不支援一氣回覆)
        }
    }
    }                       #↑i001103
    #COOKIE設定
    &cookieset ;
}
###<--------------------------------------------------------------
###<---   管理模式
###<--------------------------------------------------------------
sub Maintenance {
    if ( $FORM{'pass'} eq "")   {   &error("必須輸入密碼。");   }

    @DELWORD = split(/ /,$FORM{'no'});
    if ($FORM{'pass'} eq $password && $FORM{'proc'} eq 'delete' && @DELWORD > 1 ) {
        &update ;   return ;
    }

    &dataread ;	#讀取記錄檔
    $found = 0 ;
    foreach ( @SVLOG )  {
        ($no,$c_name,$c_email,$c_hp,$c_title,$c_comment,$regdate,$c_color_f,$c_color,$c_resno,$host,$ksu,$passwd,$dmy,$dmy,$c_icon) = split(/,/,$_);
        if ( $FORM{'no'} eq $no )   {
            if ($FORM{'pass'} ne $password && (&pass_dec($passwd))) {
                &fileunlock ;   #解除檔案鎖定
                &error("密碼不正確！");
            }
            $found = 1 ;
            if ( $FORM{'proc'} eq "delete" )    {
				$c_resno="";	#i010131
				&update ;
                return;
            }
            &header ;
            $c_pass = $FORM{'pass'} ;
            $c_comment =~ s/<br>/\n/g;
            &forminput ;
            last;
        }
    }
    if ( $found == 0 )  {
        &fileunlock ;   #解除檔案鎖定
        &error("找不到這個留言編號的記錄！");
    }
    &footer ;
    exit;
}

###<--------------------------------------------------------------
###<---   更新記錄檔
###<--------------------------------------------------------------
sub update {
    &filelock ;	#檔案鎖定
    &dataread ;	#讀取記錄檔
    $j = 0 ;    @new = () ;
    foreach $buf (@SVLOG) {
        ($no,$name,$email,$hp,$ttl,$comment,$regdate,$color_f,$color,$resno,$host,$ksu,$pass,$dmy,$dmy,$icon) = split(/,/,$buf);
        if ( $FORM{'no'} eq $no || ( $FORM{'proc'} eq 'delete' && $FORM{'no'} eq $resno ) ) {           #<<<符合進入管理模式的條件
            if ( $FORM{'proc'} eq "edit" )  {
                #寫入留言密碼及加密程序（將密碼暗號化）
                if ($FORM{'pass'} ne "") { &pass_enc($FORM{'pass'}); }
                else    { $pass = '' ; }
                if ( $rno eq '' )   {
                    push(@new,"$no,$FORM{'name'},$FORM{'email'},$FORM{'hp'},$FORM{'title'},$FORM{'comment'},$regdate,$FORM{'color_f'},$FORM{'color'},$resno,$host,$ksu,$pass,$dmy,$dmy,$FORM{'icon'}\n");
                }   else    {
                    push(@new,"$no,$FORM{'name'},$FORM{'email'},$FORM{'hp'},$ttl,$FORM{'comment'},$regdate,$FORM{'color_f'},$FORM{'color'},$resno,$host,$ksu,$pass,$dmy,$dmy,$FORM{'icon'}\n");
                }
            }
        }   else    {
            $found = 0 ;
            if ( $FORM{'proc'} eq 'delete' ) {
                @DELWORD = split(/ /,$FORM{'no'});
                foreach $word ( @DELWORD )  {
                    if ( $word && ( $no eq $word || $resno eq $word ) ) { $found = 1 ; last ; } #u000726
                }
            }
            if ( $found == 0 ) { push(@new,$buf);   }
        }
    }
    if ( !(open(OUT,">$logfile")))  {   &fileunlock ;   &error("記錄檔 ($logfile) 讀取失敗。");   }
    print OUT @new;
    close(OUT);
    &fileunlock ;   #解除檔案鎖定
    $FORM{'action'} = '' ;
}
###<--------------------------------------------------------------
###<---   顯示圖檔一覽表
###<--------------------------------------------------------------
sub icondisp    {
    &header ;           #<<<HTML表頭部份
	print "<a href=\"javascript:window.close();\">關閉視窗</a><br><center>\n";	#(驚直修改 - 使用JavaScript連結關閉視窗)
    print "■■■ 圖檔一覽表 ■■■<br><br>\n";
    print "<table cellpadding=5 cellspacing=0>\n";
    $i = 0 ; $j = 0 ;
    while ( 1 ) {
        print "<tr>\n";
        for ( $ln = 1 ; $j <= $#icon_gif && $ln <= $icon_line ; ) {
            print "<td align=\"center\"><img src=\"$icon_gif[$j]\"></td>\n";
            print "<td align=\"center\">$iconnm[$j]</td>\n";
            $j++ ; $ln++ ;
        }
        if ( $j > $#icon_gif ) {
            if ( $ln < $icon_line ) {
                for ( ; $ln <= $icon_line ; ) {
                    print "<td>&nbsp;</td><td>&nbsp;</td>\n";
                    $ln++ ;
                }
            }
            print "</tr>\n";
            last ;
        }
        print "</tr>\n";
        $i++;
    }
    print "</table>";
    if ( $jiconnm[0] ne '' )    {
        print "<hr width=80% size=1>\n";
        print "<br>▼常連者專用圖檔▼<br><table cellpadding=5 cellspacing=0>\n";
        $i = 0 ; $j = 0 ;
        while ( 1 ) {
            print "<tr>\n";
            for ( $ln = 1 ; $j <= $#jicon_gif && $ln <= $icon_line ; ) {
                print "<td align=\"center\"><img src=\"$jicon_gif[$j]\"></td>\n";
                print "<td align=\"center\">$jiconnm[$j]</td>\n";
                $j++ ; $ln++ ;
            }
            if ( $j > $#jicon_gif ) {
                if ( $ln < $icon_line ) {
                    for ( ; $ln <= $icon_line ; ) {
                        print "<td>&nbsp;</td><td>&nbsp;</td>\n";
                        $ln++ ;
                    }
                }
                print "</tr>\n";
                last ;
            }
            print "</tr>\n";
            $i++;
        }
        print "</table>";
    }
    print "</center><br><br>\n";
    &footer ;           #<<<顯示HTML頁尾
    exit;
}
###<--------------------------------------------------------------
###<---   顯示正確的圖檔
###<--------------------------------------------------------------
sub icon_set    {
    if ( $icon_rank == 0 ) {    #不使用晉級模式的情況
        #如果是常連者留言，使用常連者專用圖檔
        $found = 0 ;
        for ( $k = 0 ; $k <= $#jiconnm ; $k++ ) {
            if ( $_[0] eq $jiconnm[$k] )    {
                $found = 1 ;
            if ( $jicon_gif_w[$k] != 0 ) { $dmy = "width=\"$jicon_gif_w[$k]\" height=\"$jicon_gif_h[$k]\"" ; } else { $dmy = "" ; }
                print "<img src=\"$jicon_gif[$k]\" $dmy>";
                last ;
            }
        }
        #如果是管理者留言，使用管理者專用圖檔
        if ( $oiconpass )   {
            if ( $ango == 1 ) { $wpass = crypt($oiconpass, $oiconpass); }
            else    {   $wpass = $oiconpass ;   }
            if ( $pass eq $wpass && $found == 0 ) { #(驚直修改 - 修正原作者一個不起眼的臭蟲:當常連者準確輸入管理者專用圖檔密碼留言的時候,會同時出現兩種專用圖檔)
                $found = 1 ;
                if ( $oicon_gif_w != 0 ) { $dmy = "width=\"$oicon_gif_w\" height=\"$oicon_gif_h\"" ; } else { $dmy = "" ; }
                print "<img src=\"$oicon_gif\" $dmy>";
            }
        }
        if ( $found == 0 )  {
            if ( !($icon) ) {   $icon = 0 ; }
            if ( $icon_gif_w[$icon] != 0 ) { $dmy = "width=\"$icon_gif_w[$icon]\" height=\"$icon_gif_h[$icon]\"" ; } else { $dmy = "" ; }
            print "<img src=\"$icon_gif[$icon]\" $dmy>";
        }
    }   else    {   #使用晉級模式的情況
        #如果是管理者留言，使用管理者專用圖檔
        $found = 0 ;
        if ( $oiconpass )   {
            if ( $ango == 1 ) { $wpass = crypt($oiconpass, $oiconpass); }
            else    {   $wpass = $oiconpass ;   }
            if ( $pass eq $wpass && $found == 0 ) { #(驚直修改 - 修正原作者一個不起眼的臭蟲:當常連者準確輸入管理者專用圖檔密碼留言的時候,會同時出現兩種專用圖檔)
                $found = 1 ;
                if ( $oicon_gif_w != 0 ) { $dmy = "width=\"$oicon_gif_w\" height=\"$oicon_gif_h\"" ; } else { $dmy = "" ; }
                print "<img src=\"$oicon_gif\" $dmy>";
            }
        }
        if ( $found == 0 )  {
            print "<img src=\"$icon_gif[$rank_idx]\">";
        }
    }
}
###<--------------------------------------------------------------
###<---   取得COOKIE資訊
###<--------------------------------------------------------------
sub cookieget   {
    $cookies = $ENV{'HTTP_COOKIE'};
    @pairs = split(/;/,$cookies);
    foreach $pair (@pairs) {
        ($name, $value) = split(/=/, $pair);
        $name =~ s/ //g;
        $DUMMY{$name} = $value;
    }
    @pairs = split(/,/,$DUMMY{'mkakikomitai'});
    foreach $pair (@pairs) {
        ($name, $value) = split(/\!/, $pair);
        $COOKIE{$name} = $value;
    }

    if ($FORM{'name'})    { $COOKIE{'nm'}   = $FORM{'name'}; }
    if ($FORM{'email'})   { $COOKIE{'em'}   = $FORM{'email'}; }
    if ($FORM{'hp'})      { $COOKIE{'hp'}   = $FORM{'hp'}; }
    if ($FORM{'pass'})    { $COOKIE{'ps'}   = $FORM{'pass'}; }
    if ($FORM{'icon'})    { $COOKIE{'icon'} = $FORM{'icon'}; }
    if ($FORM{'color'})   { $COOKIE{'cl'}   = $FORM{'color'}; }
    if ($FORM{'color_f'}) { $COOKIE{'cl_f'} = $FORM{'color_f'}; }
}
###<--------------------------------------------------------------
###<---   設定COOKIE
###<--------------------------------------------------------------
sub cookieset {
    ($secg,$ming,$hourg,$mdayg,$mong,$yearg,$wdayg,$ydayg,$isdstg)
        =gmtime(time + 30*24*60*60);
    $yearg  += 1900 ;
    if ($secg  < 10)  { $secg  = "0$secg";  }
    if ($ming  < 10)  { $ming  = "0$ming";  }
    if ($hourg < 10)  { $hourg = "0$hourg"; }
    if ($mdayg < 10)  { $mdayg = "0$mdayg"; }
    $mong = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec')[$mong];
    $youbi = ('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday')[$wdayg];
    $date_gmt = "$youbi, $mdayg\-$mong\-$yearg $hourg:$ming:$secg GMT";
    $cook="nm\!$FORM{'name'},em\!$FORM{'email'},hp\!$FORM{'hp'},cl_f\!$FORM{'color_f'},cl\!$FORM{'color'},ps\!$FORM{'pass'},icon\!$FORM{'icon'}";
    print "Set-Cookie: mkakikomitai=$cook; expires=$date_gmt\n";
}
###<--------------------------------------------------------------
###<---   顯示錯誤訊息
###<--------------------------------------------------------------
sub error {
    &header ;
    print "<font color=red>$_[0]</font><br><br>\n"; #(驚直修改 - 改以紅字顯示)
    &footer;
    exit;
}
###<--------------------------------------------------------------
###<---   檔案鎖定程序
###<--------------------------------------------------------------
sub filelock {
    if (-e $lockfile) {
        ($ftm) = (stat($lockfile))[9];
        if ($ftm < time - 150) { unlink($lockfile); }
    }
    foreach (1 .. 5) {
        if (-e $lockfile) { sleep(1); }
        else {
            open(LOCK,">$lockfile");
            close(LOCK);
            return;
        }
    }
    &error("同時有其他人正在寫入留言。請返回上一頁待稍後再試一次吧。<br>假如情況持續，可能因為留言板給鎖定了，請通知留言板管理者刪除鎖定檔 <font face=\"$e_font\">($lockfile)</font> 。");
}
###<--------------------------------------------------------------
###<---   解除檔案鎖定
###<--------------------------------------------------------------
sub fileunlock {
    if (-e $lockfile) { unlink($lockfile); }
}
###<--------------------------------------------------------------
###<---   取得留言者的留言篇數
###<--------------------------------------------------------------
sub rankget {
    $set = 0 ;
    $tmax = $#rankno ;
    for ( $j = 0 ; $j <= $tmax ; $j++ ) {
        if ( $_[0] >= $rankno[$j] ) {
            $ranking = $rank[$j] ;
            $rank_idx = $j ;
        }
    }
    return ($ranking);
}
###<--------------------------------------------------------------
###<---   顯示晉級資格說明
###<--------------------------------------------------------------
sub info    {
    &header ;           #<<<HTML表頭部份
    print "<a href=\"javascript:window.close();\">關閉視窗</a><br><center>\n";  #(驚直修改 - 改為關閉視窗)
    print "■■■ 晉級資格說明 ■■■<br><br>\n";
    print "只要達到以下的留言篇數，你就可以晉級喔！<br><br>\n";
    $i =  0;
    print "<table cellpadding=1 cellspacing=0 bgcolor=black><tr><td>\n";
    print "<table cellpadding=5 cellspacing=1>\n";
    $k = $#rank ;
    for ( @rank )   {
        print "<tr><td bgcolor=white width=100 nowrap>$rank[$i]</td>\n";
        print "<td bgcolor=white align=right width=150 nowrap>";
        $j = $rankno[$i+1] - 1 ;
        if ( $i != $k ) {   #(驚直修改 - 加入英文字形)
            print "<font face=\"$e_font\">$rankno[$i]</font> ∼ <font face=\"$e_font\">$j</font> 篇\n";
        }   else    {
            print "<font face=\"$e_font\">$rankno[$i]</font> 篇以上\n";
        }
        print "</td></tr>\n";
        $i++;
    }
    print "</table></td></tr></table></center><br><br>";
    &footer ;           #<<<顯示HTML頁尾
    exit;
}
###<--------------------------------------------------------------
###<---   寄發郵件通知
###<--------------------------------------------------------------
sub SMail {
    $name = $FORM{'name'};
    $email = $FORM{'email'};
    $ttl = $FORM{'title'};
    $ttl2 = $title;
	if ( $FORM{'kflg'} eq '' ) {	#(驚直修改 - 修正原程式的寄發郵件通知功能不支援一氣回覆)
		$comment = $FORM{'comment'};
	}	else	{
		$comment = "$rcom\n(留言編號#$rno之回覆)";
	}
    $comment =~ s/<br>/\n/g;

    if ($FORM{'resno'} ne "") { $ttl = "$sv_title"; }
    elsif ($FORM{'resno'} eq "" && $ttl eq "") { $ttl = "(無題)"; }
    $comment =~ s/&lt;/</g;
    $comment =~ s/&gt;/>/g;
    $comment =~ s/&#44;/\,/g;   #(驚直加入 - 轉換半形逗號)

    if ($ttl eq "") { $ttl = "(無題)"; }                                    #(驚直修改 - 原程式漏寫的一行)

	#(驚直修改 - 加入$ttlsubj變數用來放在信件標題使之更清晰)
	if ( $FORM{'kflg'} ne '' ) {	#(驚直加入 - 一氣回覆時顯示的信件標題)
		$ttlsubj = "有一篇訪客使用「一氣回覆模式」寫入的留言已經灌進留言板嘍";
	} else {
		if ($FORM{'resno'} eq "") {
			if ($ttl eq "(無題)")	{$ttlsubj = "有一篇沒有標題的新留言已經寫在留言板上嘍";}
				else				{$ttlsubj = "有一篇新的留言「$ttl」已經寫在留言板上嘍";}
		} else {
			if ($ttl eq "(無題)")	{$ttlsubj = "有一篇訪客回覆、沒有標題的留言已經寫在留言板上嘍";}
			else					{$ttlsubj = "有一篇訪客回覆的留言「$sv_title」已經寫在留言板上嘍";}
		}
	}

    if ( !($email) ) { $email = $smail_address ; }

    if ( $hiho == 1 )   {
        open(MAIL,"| $sendmail -s \"$ttlsubj\" -f \"$email\" $smail_address") || &error("寄信程式出了問題！");  #(驚直修改 - 信件標題改用$ttlsubj變數)
    }   else    {
        open(MAIL,"| $sendmail -t") || &error("寄信程式出了問題！");
        print MAIL "X-Mailer: mkakikomitai Ver$ver\n";                          #(驚直修改 - 改為程式名稱)
        print MAIL "To: $smail_address\n";
        if ($FORM{'email'} ne "") { print MAIL "Reply-to: $name <$email>\n"; }  #(驚直修改 - 加入對方名字,無提供電子郵箱則忽略)
        print MAIL "Subject: $ttlsubj\n";                                       #(驚直修改 - 信件標題改用$ttlsubj變數)
        print MAIL "Content-Transfer-Encoding: 8bit\n";                         #(驚直修改 - 改為8bit傳送)
        print MAIL "Content-type: text/plain; charset=utf8\n";                  #(驚直修改 - 改為繁體中文語系標籤)
    }

    print MAIL "<<< $ttl2 >>>\n\n";
    print MAIL "────────────────────────────────────────\n";
    print MAIL "留言時間: $today\n";
    print MAIL "訪客名字: $name\n";
    if ($FORM{'email'} ne "")   { print MAIL "電子郵箱: $email\n"; }            #(驚直修改 - 無提供電子郵箱則忽略)
    if ($FORM{'hp'} ne "")      { print MAIL "個人網站: http://$FORM{'hp'}\n"; }
	if ($FORM{'kflg'} eq '')    { print MAIL "留言標題: $ttl\n"; }				#(驚直修改 - 一氣回覆時不顯示標題)
    print MAIL "────────────────────────────────────────\n";    #(驚直修改 - 加入分隔橫線)
    print MAIL "$comment\n";
    print MAIL "────────────────────────────────────────\n";
    close(MAIL);
}
###<--------------------------------------------------------------
###<---   密碼加密程序
###<--------------------------------------------------------------
sub pass_enc {
    if ( $ango == 1 ) { $pass = crypt($_[0], $_[0]);    }
    else    {   $pass = $_[0];  }
}
###<--------------------------------------------------------------
###<---   檢查密碼
###<--------------------------------------------------------------
sub pass_dec {
    if ( $ango == 1 ) {
        if ($_[0] ne '' && ( crypt($FORM{'pass'}, $_[0]) eq $_[0]) )  { return 0 ;  }
    }   else    {   if ($FORM{'pass'} eq $_[0]) {   return 0 ;  }   }
    return 1;
}
###<--------------------------------------------------------------
###<---   檢查過去記錄檔
###<--------------------------------------------------------------
sub logchk {
    if ( $olddir ) {    #如果要保留舊留言集，此資料夾必須存在
        if ( !(opendir(DIR,"$olddir"))) {   &error("儲存過去記錄檔的資料夾 ($olddir) 並不存在，請立即建立此資料夾。");    }
        @oldcnt = grep(/\.txt/,readdir(DIR));
        $i = sprintf("%02d",$#oldcnt + 1) ;
        $oldfile = "$olddir$i" . ".txt" ;
        closedir(DIR) ;
    }
}
###<--------------------------------------------------------------
###<---   顯示各人晉級狀態
###<--------------------------------------------------------------
sub rankdisp    {
    if ( !(open(IN,"$logfile2")))   {   &error("晉級狀態記錄檔 <font face=\"$e_font\">($logfile2)</font> 讀取失敗。");  }
    while ( <IN> )  {
        ($n,$k) = split(/,/,$_);
        $k =~ s/\n//g;
        push(@RANKDATA,"$k,$n") ;
    }
    close(IN);
    @RANKDATA = sort { $a <=> $b } @RANKDATA ;
    @RANKDATA = reverse @RANKDATA ;

    &header ;           #<<<HTML表頭部份
    print "<a href=\"javascript:window.close();\">關閉視窗</a><br><center>\n";  #(驚直修改 - 改為關閉視窗)
    print "■■■ 各人晉級狀態 ■■■<br><br>\n";
    print "<table cellpadding=1 cellspacing=0 bgcolor=black><tr><td>\n";
    print "<table cellpadding=5 cellspacing=1>\n";
    print "<tr><td bgcolor=whitesmoke>留言者</td>\n";   #(驚直修改 - 改變表格標題列的背景顏色)
    print "<td bgcolor=whitesmoke>留言次數</td>\n";
    print "<td bgcolor=whitesmoke>晉級狀態</td></tr>\n";
    foreach ( @RANKDATA )   {
        ($k,$n) = split(/,/,$_);
        for ( $j = 0 ; $j <= $#rankno ; $j++ )  {
            if ( $k >= $rankno[$j] )    {
                $ranking = $rank[$j] ;
                $rank_idx = $j ;
            }
        }
        print "<tr><td bgcolor=white>$n</td>\n";
        print "<td bgcolor=white align=right><font face=\"$e_font\">$k</font> 篇</td>\n"; #(驚直修改 - 加入英文字形)
        print "<td bgcolor=white>$ranking</td></tr>\n";
    }
    print "</table></td></tr></table><br><br>\n";
    &footer ;           #<<<顯示HTML頁尾
    exit ;
}
###<--------------------------------------------------------------
###<---   下載留言記錄檔 i001112
###<--------------------------------------------------------------
sub download {
    print "Content-type: text/download; charset=utf8\n\n";  #(驚直修改 - 加入繁體中文語系標籤)
    print "<html><head>\n";
    print "<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf8\">\n";   #(驚直修改 - 加入繁體中文語系識別語法)
    print "<title>$title</title>";
	#<<<CSS樣式表開始>>>	#(驚直加入 - 下載回來的記錄檔也使用樣式表)
    print "<style type=\"text/css\">\n";
    print "<!--\n";
	print "a,a:link  {color:$linkcolor;text-decoration:none}\n";	#(驚直修改 - 連結文字跟隨整體字形大小)
    print "a:visited {color:$vlinkcolor;text-decoration:none}\n";
    print "a:active  {color:$alinkcolor;text-decoration:none}\n";
    print "a:hover   {color:$hovercolor;text-decoration:underline}\n";
	print "body,tr,td {font-size:$pt;word-break:break-all}\n";		#(驚直修改 - 加入work-break屬性,防止被惡意破壞版面)
    print "-->\n";
    print "</style>\n";
	#<<<CSS樣式表結束>>>
    print "</head>\n";
    $wk = "bgcolor=\"$bgcolor\"";
    print "<body $wk text=$tcolor link=$linkcolor vlink=$vlinkcolor alink=$alinkcolor>\n";
    &view ;
    print "<br><br>\n";
    &footer ;
    exit;
}
