# kuaishou_parse
快手解析去水印</br>
为了分清结构就把代码分开写了</br></br>
文件注释：</br>
1.py 把快手分享的链接放入s.txt中，正则提取短链接写入u.txt中</br>
jx1.0.py 目前1.0无法使用，快手增加了滑块验证，支持单个或批量解析</br>
jx1.1.py 硬刚滑块验证，使用了两个头部就饶过了滑块验证，目前可以使用 2020/04/25</br>
3.py</br>
4.py 去重</br>
</br>
使用方法：</br>
单个: python jx1.1.py https://v.kuaishou.com/xxxxxx</br>
批量: python jx1.1.py u.txt</br>
</br>
解析方法：</br>
其实解析方法很简单，和抖音解析方法基本上一样，不上传截图了，懒</br>
浏览器打开审查元素找到网络（Network）并切换手机响应模式下（火狐或Chrome）</br>
访问分享的短链接</br>
第一个域名为f.kuaishou.com或者v.kuaishou.com，这是短链接的地址，状态为302</br>
第二个域名ali.static.yximgs.com或者其他的，状态为200，可以查看源代码，封面和无水印视频地址就存放在里面</br>
