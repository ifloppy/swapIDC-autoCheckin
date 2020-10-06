# swapIDC-autoCheckin
自动签到SwapIDC搭建的网站用Python+Actions

如何使用?直接Fork一份这个仓库，设置一下Secrets，再push一下，以后就会自动签到了

Secrets设置内容:
SITE:一个用SwapIDC搭建的网站(就是你要签到的那个网站)，结尾不要加斜杠，例如:https://iruanp.com
NAME:用户名
PSWD:密码
请放心，NAME和PSWD中储存的值会被保存在Github，且不会有别人看到你设置的这两个值，Actions中只会输入包含SITE内容的文本，如果你介意，可以修改源代码

这仓库写完就弃坑，三分钟热度XD
