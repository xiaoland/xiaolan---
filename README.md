# 小蓝--中文语音交互智能家居机器人(在linux系统上运行)
- 这是一个中文的智能家居控制对话机器人——因为看到悟空机器人(wukong-robot)而自己也想做一个而来
- 目前还未完成，所以发上来，希望大家一起研发，一个人研发也没那么多点子和经验

- 对不起！因为我的编程水平非常辣鸡，所以如果有任何觉得使用不方便或者错误的地方，希望多多谅解
- 如果大家有好的主意的话，请在github issues上提出来讨论

## 鸣谢
- chengguoguo哥哥

## 帮助改进唤醒词
- 本机器人采用snowboy唤醒引擎，因此安装的时候还得注意swig的安装
- snowboy有一个特点，就是不管什么语言都可以支持，虽然本身对英文的支持比较优秀
- 但是snowboy的唤醒词是越多人说则效果越好，因此希望大家能帮忙改进一下，只需要点击下面的网址并录三次音就可以啦
- **访问这里帮助改进唤醒词**：https://snowboy.kitt.ai/hotword/29200 （记得录音时说“小蓝同学”，谢谢啦）
- 当然，你也可以在snowboy上新建或选择一个你喜欢的唤醒词，然后下载模型并在setting.json中设置即可

## 关于安装等问题
- [Wiki：https://github.com/xiaoland/xiaolan/wiki](https://github.com/xiaoland/xiaolan/wiki)
![服务架构](https://github.com/xiaoland/xiaolan-dev/blob/master/%E5%B0%8F%E8%93%9D%E6%9C%8D%E5%8A%A1%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE.PNG)

## 更新：（有时间先后顺序）
- 利用讯飞AIUI平台实现了语义理解（NLU）！
  - 已经完成云端的语义理解（NLU）
  - 对用户的指令理解更加准确
- 实现开机自启！（使用install_all.sh脚本进行一键安装，自带开机启动设置）
- 说出唤醒词训练即可训练唤醒词！
- 智能家居插件已经可以控制灯、开关、遥控和获取传感器的数据（可以控制灯的颜色）
- 新闻、翻译、智能家居、音乐等插件已经加入了一句话功能
- 使用Alexa.pmdl唤醒可以三米以内唤醒
- 发布了[小蓝-V2.5 成熟稳定版本](https://github.com/xiaoland/xiaolan/releases)
- 一句话功能放置到nlp.py中，加快速度
- 加快tuling.py的相应速度
- 删去不必要的元素
- 开机只需请求一次百度token，大大提升速度
- 添加百度音乐技能
- 添加第三方邮箱邮件发送技能
- 重写所有基本文件，将speaker改为player
- 改为流式语音播报
- 重写hass技能
- 重写tuling技能
- 重写了一些技能
- 改进nlu机制
- 全部采用相对路径
- 改进技能呼叫机制
  - “打开XXX”，XXX是预设的技能名称
- 改进recorder
- 添加log机制
















shanjusuiyuez 的PS:我想去fork 这个xiaoland。太阳。