一 青龙 自动 HTTPS 自动  自动 HTTPS 工作模式  自动


测试一下自动镜像  再次测试 什么时候修改  测试自动修改欧尼  好像不是实时同步  明天再看吧




1 cd /usr/local/bin  进入安装目录

2 wget -O frpc https://getfrp.sh/d/frpc_linux_arm64 # 如命令报错 尝试这条:curl -Lo frpc

3 权限777

4 启动 frpc -f token:隧道ID

5 自启动 frpc.ini(如果没生成，在官网下载)放在root/根目录下  启动命令放在青龙extra.sh配置文件

6 内部检查更新需要重新执行以上操作

二 梅林 自动 HTTPS 禁用 自动 HTTPS 工作模式  自动

1 wget -O frpc https://getfrp.sh/d/frpc_linux_arm64

2 从/tmp/home/root/ 拖出来放到 /jffs/scripts/下  否则路由重启文件消失

3 权限777

4 启动 /jffs/scripts/frpc -f token:隧道ID

5 自启动 /jffs/scripts/目录下wan-start文件 中末尾加入启动命令 权限777

三 核实确定情况 重启设备之后

https://www.natfrp.com/tunnel/  隧道名称前变绿点 表示成功

迁移隧道  网址会发生改变 通过SSH运行一次命令以确定正确网址

JS脚本定时方法 在脚本顶部插入以下代码

[task_local]

30 1,7,12,18,22 * * *

[Script]

cron "30 1,8,12,17 * * *"

https://github.moeyy.xyz/ 放在青龙配置文件里边的 代理地址 值  里边

![截屏图片](https://github.com/klcb2010/ZDYJB/assets/32628414/07bbb2cc-3958-435d-a412-1dac09d56f79)
