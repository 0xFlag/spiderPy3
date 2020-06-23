# kuaishou_parse
快手解析去水印</br>
为了分清结构就把代码分开写了</br></br>
文件注释：</br>
1.py 把快手分享的链接放入s.txt中，正则提取短链接写入u.txt中</br>
~~jx1.0.py 目前1.0无法使用，快手增加了滑块验证，支持单个或批量解析~~
</br>
~~jx1.1.py 硬刚滑块验证，使用了两个头部就饶过了滑块验证，2020/04/25 'NoneType' object has no attribute 'attrs'~~
</br>
jx1.2py 解决'NoneType' object has no attribute 'attrs'，2020/06/23
</br>
3.py 视频地址排序并去重</br>
4.py 去重</br>
</br>
使用方法：</br>
单个: python jx1.2.py https://v.kuaishou.com/xxxxxx</br>
批量: python jx1.2.py u.txt</br>
</br>
解析方法：</br>
其实解析方法很简单，和抖音解析方法基本上一样，不上传截图了，懒</br>
浏览器打开审查元素找到网络（Network）并切换手机响应模式下（火狐或Chrome）</br>
访问分享的短链接，注意审查元素中网络的变化：</br>
第一个域名为f.kuaishou.com或者v.kuaishou.com，这是短链接的地址，状态为302</br>
第二个域名ali.static.yximgs.com或者其他的，状态为200，可以查看源代码，封面和无水印视频地址就存放在里面</br></br>
所以代码也很好理解就是通过第一个域名获取第二个域名后再通过源代码解析出视频地址</br>
绕过滑块验证也很好理解，第一个域名和第二个域名的访问头部不同</br>
最后有一点就是注意cookie的存活周期，使用此代码前修改下代码中的请求头部cookie</br>
2020/06/23</br>
jx1.1.py 解析时报错'NoneType' object has no attribute 'attrs'，顺藤摸瓜发现快手改了代码，没有hide-pagedata这个标签改成了<script type="text/javascript">window.pageData</script></br>
另外使用前需要修改代码中的两个请求头部cookie
