# AI大模型开发—20前端css和js和AI-DD

> 作者：芯源-邢朋辉

# 0.课程内容

## 0.1 晨考

https://ks.wjx.com/vm/wbkDJ2T.aspx# 

## 0.2 课程回顾

FastApi Python语言中开发Api接口的库

请求方式

参数形式

路由模式

参数校验（自处理）

异步接口，同步接口

文件上传（采用云服务器的对象存储）

前端三剑客：1.Html 页面，显示内容，通过固定的标签

FastApi和SqlAlchemy综合使用

> 会开发
>
> 全栈：数据库+后端+前端+测试+运维+产品+项目管理 +AI工具



# 1.Css

## 1.0 Html

前后端分离开发：

前端：源码单独，单独部署

后端：源码独立，单独部署

fastapi库可以挂在前端，但是不能太大

> Nginx软件 代理访问前端

Html 超文本标记语言

主流的页面开发的技术

固定的标签，不同的标签实现效果各不相同

常用基础标签

```html
<!DOCTYPE html>
<html lang="en">
<!--head 头-->
<head>
    <meta charset="UTF-8">
<!--    title 设置标题-->
    <title>html网页</title>
</head>
<!--body 正文内容-->
<body>
<!--    各种各样标签-->
<!--div 块 划分一块-->
<div>
<!--    基础标签-->
    <h1>标题1标签</h1>
    <h2>标题2标签</h2>
    <h6>标题6标签</h6>
<!--    列表标签-->
<!--    ol有序列表-->
    <ol>
        <li>第一名</li>
        <li>第二名</li>
        <li>第三名</li>
    </ol>
<!--    ul无序标签-->
    <ul>
        <li>第一个</li>
        <li>第二个</li>
        <li>第三个</li>
    </ul>
<!--    a标签 超链接-->
    <a href="https://www.baidu.com">百度一下</a>
<!--    br 单标签 换行-->
    <br/>
<!--    img标签 图片-->
    <img width="100" height="100" src="https://n.sinaimg.cn/news/1_img/upload/0680838e/219/w2048h1371/20260421/597f-fd619c3bc5e6454f75466f45270977bd.jpg" />
    <br/>
<!--    table表格标签 实现一个表格 行和列-->
    <table>
        <thead>
            <tr>
                <th>序号</th>
                <th>姓名</th>
                <th>坐标</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>1</td>
                <td>白鑫雨</td>
                <td>1,9</td>
            </tr>
            <tr>
                <td>2</td>
                <td>李威</td>
                <td>1,8</td>
            </tr>
        </tbody>
        <tfoot>
            <tr>
                <td colspan="3">
                    <button>首页</button>
                    <button>上一页</button>
                    <button>下一页</button>
                </td>
            </tr>
        </tfoot>
    </table>

</div>
</body>
</html>
```

![1776737378512](D:\class\2603\随堂笔记\第四周\AI大模型开发—20前端css和js和AI-DD.assets\1776737378512.png)

表单标签

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Html表单标签</title>
</head>
<body>
<div>
<!--    表单 类型标签-->
    <form action="" method="get">
        <div>
<!--            label 文本标签-->
            <label>姓名：</label>
<!--            input 输入框 type=text 普通输入框-->
            <input type="text" placeholder="请输入姓名">
        </div>
        <div>
            <label>密码：</label>
<!--            input 输入框 type=text 普通输入框-->
            <input type="password" placeholder="请输入密码">
        </div>
        <div>
            <label>性别：</label>
<!--            input 输入框 type=radio 单选框-->
            <input type="radio" name="sex">男
            <input type="radio" name="sex">女
            <input type="radio" name="sex">第三性别

        </div>
        <div>
            <label>爱好：</label>
<!--            input 输入框 type=checkbox 单选框-->
            <input type="checkbox" name="hobby">跑步
            <input type="checkbox" name="hobby">钓鱼
            <input type="checkbox" name="hobby">爬山
        </div>
        <div>
            <label>家乡：</label>
<!--            select 下拉框-->
            <select>
                <option>--请选择家乡--</option>
                <option>湖南</option>
                <option>湖北</option>
                <option>陕西</option>
                <option>河南</option>
                <option>天津</option>
                <option>贵州</option>
                <option>河北</option>
            </select>
        </div>
        <div>
            <label>上传头像：</label>
<!--            input type=file 文件上传-->
            <input type="file">
        </div>
        <div>
            <label>个人简介：</label>
<!--            textarea 多行输入框 rows 设置行数-高度 cols 设置列数-宽度-->
            <textarea rows="5" cols="10" ></textarea>

        </div>
        <div>
            <button>确认新增</button>
            <button>重载内容</button>
        </div>
    </form>
</div>
</body>
</html>
```

![1776737359155](D:\class\2603\随堂笔记\第四周\AI大模型开发—20前端css和js和AI-DD.assets\1776737359155.png)

## 1.1 Css

Css 层叠样式表，作用：美化html页面

Css语法格式：

```
选择器 {
    css属性名:值
    ……
}
```

css选择器：

1.标签选择器 语法：直接写标签

2.id选择器 语法：#id名

3.class选择器 语法：.class名 

> class名可以重复，多个标签可以用同一个名
>
> id名不可重复，唯一

css属性名：

文本 text

字体 font

间距 padding margin

背景 backgroundxx

大小 width height

颜色 color

边框 border

css使用方式：3种

1.在html页面的head标签内部，通过 style标签，内部写上 选择器 {属性名:值}

2.在html标签上使用 style属性，在这个属性里写对应的css属性名和值

3.单独创建css文件，在html使用link标签导入css文件



> 设置间距使用padding或margin
>
> margin:外边距，距离其他的边距，大小-组件本身大小不会改变
>
> padding:内边距，内容距离组件边框的距离，大小--组件本身大小会改变

# 2.javascript

## 2.1 JavaScript

JavaScript:js，浏览器交互脚本语言

可以操作html、css

编程语言：自己的语法规则

数据类型--动态类型推断

变量

运算符

分支

循环

函数

dom操作

bom操作

fetch--请求Api接口

## 2.2 js语法

基础语法：

```javascript
// js的语法  代码
// number 数字类型
console.log(11)
console.log(11.2)
// boolean 布尔类型
console.log(true)
// string 字符串
console.log('abc')

//变量 语法格式：let 变量名=初始值
let num1=101
nu1='abbw'
var num2=11.11
console.log(num1)
let str1='abcd'
console.log(str1)
let b1=false
console.log(b1)
// 常量 语法格式：const 常量名=值
const VERSION=1.1
console.log(VERSION)

str2='123'
// 类型转换 Number 转换为数字类型
let num3=Number(str2)
// String 转换为字符串类型
let str3=String(num3)
// Boolean 转换为布尔类型
let b2=Boolean(1)

//运算符
//算术运算符：+ - * / % ++ --
let num11=1,num22=11
console.log("算术运算符："+(num11+num22))
console.log("算术运算符："+(num11-num22))
console.log("算术运算符："+(num11*num22))
console.log("算术运算符："+(num11/num22))
console.log("算术运算符："+(num11%num22))
num22++
console.log("自增：",num22)
num11--
console.log("自减：",num11)
//赋值运算符 = += -= *= /=
let num33=101
num33+=10
num33-=8
num33*=3
console.log("赋值运算符：",num33)
// 比较运算符 == === > <
let num44=11
let str44='11'
console.log("比较运算符："+(num44===str44))
// 逻辑运算符 &&并且 ||或者 !取反
let n1=10,n2=8
console.log("逻辑运算符："+(n1>n2 && n2%2===0))
console.log("逻辑运算符："+(!false))
// 位运算符 采用二进制进行计算
```

> 数字类型：number
>
> 变量：let
>
> 常量：const
>
> 逻辑运算符：&& || !

进阶语法：

```javascript
// 分支 循环 函数
//分支 有选择的执行代码块
let s=88
//if语句实现分支结构
if(s>=60){
    console.log("及格了")
}else {
    console.log("不及格")
}
let sex=1
if(sex===1){
    console.log("女孩")
}else if (sex===2){
    console.log("男孩")
}else {
    console.log("是人")
}
//循环 满足条件就重复执行
//for语句 实现循环结构 需要三部分组成：1.变量初始化 2.条件判断(是否进行循环) 3.条件改变
for(let i=1;i<=10;i++){
    console.log("循环：",i)
}
// 循环控制关键字
//10-3 3的倍数 不显示
for(j=10;j>0;j--){
    if(j%3===0){
        //跳过循环
        continue
    }
    console.log("数字：",j)
}
console.log("break结束循环")
for(j=10;j>0;j--){
    if(j%3===0){
        // 结束循环
        break
    }
    console.log("数字：",j)
}
// 函数 实现特定功能的代码块
function add(num1,num2){
    return num1+num2
}
// 调用函数
console.log("调用函数：",add(1,1))
```

结合html使用

DOM、BOM

# 3.AI-DD

## 3.1 AI-DD

AI-DD AI驱动开发（Vibe Coding 氛围编程）

使用AI编程工具驱动项目的开发

是目前主流的开发范式

不少企业都要求AI的代码量占比60%、80%



## 3.2 国内AI编程工具

Trae、Qcoder、CodeBuddy、LingMa

推荐使用AI编程的IDE，不使用插件

Trae：https://www.trae.cn/

Qcoder：https://qoder.com/

LingMa：https://lingma.aliyun.com/

CodeBuddy：https://www.codebuddy.cn/home/



## 3.3 国外AI编程工具

Cursor、Claude Code、Codex、Open Code

> 推荐：Claude Code 



## 3.4 AI编程工具实战

基于Trae的SOLO模式实现全栈开发

采用PyCharm新建一个项目

再使用Trae打开项目

切换到SOLO模式

输入内容：自然语言即可

基于Python语言实现一个喜欢歌曲的小项目，技术栈使用：Mysql+SqlAlchemy+FastApi+Html+Css+Js+Git

,项目模块：用户模块、歌曲模块

```
基于Python语言实现一个喜欢歌曲的小项目，技术栈使用：Mysql+SqlAlchemy+FastApi+Html+Css+Js+Git

,项目模块：用户模块、歌曲模块。整个开发采用企业级标准，同时按照完整软件工程，各个节点的文档保存到docs目录下。
```

再点击 优化提示词

最后点击执行

进入等待

> 一般白天11点之后有时就开始排队，一直到18点左右
>
> 其余时间还可以

看第一次的结果，可能需要几次交互，修正问题

![1776761744862](D:\class\2603\随堂笔记\第四周\AI大模型开发—20前端css和js和AI-DD.assets\1776761744862.png)

# 4.综合练习

基于Trae免费版实现下面的需求：

1.基于学过的知识，实现一个考勤小系统

目的：60%-70% AI生成，30%-40% 人开发



# 5.今日总结

html 显示内容，固定标签

css 样式，美化html标签

js 交互脚本语言，语法、html交互（dom）

AI-DD

国产AI编程工具：Trae

> 前端三剑客 速成，知道语法，多敲几遍代码，熟练编写规范即可
>
> 高频内容，需要记一下



# 6.作业

1.前端三剑客练习

熟练语法

