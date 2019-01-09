# 快速上手

## 发送请求

使用 Requests 发送网络请求非常简单。

一开始要导入 Requests 模块：

`>>> import requests`

然后，尝试获取某个网页。本例子中，我们来获取 Github 的公共时间线：

`>>> r = requests.get('https://api.github.com/events')`

现在，我们有一个名为 r 的 Response 对象。我们可以从这个对象中获取所有我们想要的信息。

Requests 简便的 API 意味着所有 HTTP 请求类型都是显而易见的。例如，你可以这样发送一个 HTTP POST 请求：

`>>> r = requests.post('http://httpbin.org/post', data = {'key':'value'})`

漂亮，对吧？那么其他 HTTP 请求类型：PUT，DELETE，HEAD 以及 OPTIONS 又是如何的呢？都是一样的简单：

`>>> r = requests.put('http://httpbin.org/put', data = {'key':'value'})`
`>>> r = requests.delete('http://httpbin.org/delete')`
`>>> r = requests.head('http://httpbin.org/get')`
`>>> r = requests.options('http://httpbin.org/get')`