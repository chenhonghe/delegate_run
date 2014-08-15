https://bitsharestalk.org/index.php?topic=6351.0

"目前delegate长时间运行会大量丢块，BM建议每天重启一次钱包程序"

上面是alt贴子中提到的有的原话，但贴子中没看到相应的脚本，所以周末花了点时间写了这个脚本。

写差不多了才看到 alt 在英文版的已经有贴出脚本了，即然写了，就给写完整吧。


如何使用：

1、将run.exp和kill_bc.py两个脚本放在bitshares_client程序目录下，修改 run.exp  bc_path 这个变量，指的是bitshares_client的基本路径同时修改的钱包名、及RPC的用户名及密码

2、

$screen -S bcs

$cd /data/src/bitsharesx/programs/client/

$./run.exp


3、输入相应钱包的密码

4、ctrl+a+d 让screen进入后台运行。

5、可以使用screen -r bcs 进入之前的screen