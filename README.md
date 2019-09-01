### push

### first push

```
首先创建repositories 记下来名称
git@github.com:zjw14174/myweb.git
然后在项目目录里使用git
```

#### git从本地第一次使用

```
生成密钥
ssh-keygen -t rsa -C "136671988@qq.com"
复制公钥到网页
https://github.com/settings/key
测试密钥登陆
ssh -T git@github.com
添加git全局信息
git config --global user.name "zjw14174"
git config --global user.email "136671988@qq.com"
初始化git
git init
添加要推送的文件
git add .
提交修改
git commit -m "blogweb test"
设置远程仓库地址
git remote add origin git@github.com:zjw14174/blogweb.git
推送到远程仓库
git push -u origin master
```

#### git修改文件后提交操作

```
遍历检查当前文件夹下所有文件
git add .
提交更改,-m后面是描述信息
git commit -m "modify test"
推送到远程仓库
git push -u origin master

```



