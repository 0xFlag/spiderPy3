# kuaishou_parse
快手解析去水印</br>
为了分清结构就把代码分开写了</br></br>
文件注释：</br>
1.py 把快手分享的链接放入s.txt中，正则提取短链接写入u.txt中</br>
jx1.0.py 目前1.0无法使用，快手增加了滑块验证，支持单个或批量解析</br>
jx1.1.py 硬刚滑块验证，使用了两个头部就饶过了滑块验证，目前可以使用 2020/04/25</br>
</br>
使用方法：</br>
单个: python jx1.1.py https://v.kuaishou.com/xxxxxx</br>
批量: python jx1.1.py u.txt</br>
