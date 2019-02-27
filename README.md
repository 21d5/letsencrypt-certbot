## 申请证书

特别说明： --manual-auth-hook 指定的 hook 文件（au.sh），其他操作完全相同。
```
测试是否有错误
$ ./certbot-auto certonly --manual --preferred-challenges dns --manual-auth-hook /脚本目录/au.sh -d *.example.com --manual-public-ip-logging-ok --dry-run

实际申请
$ ./certbot-auto certonly --manual --preferred-challenges dns --manual-auth-hook /脚本目录/au.sh -d *.example.com --manual-public-ip-logging-ok  
```
参数解释（可以不用关心）：

* certonly：表示采用验证模式，只会获取证书，不会为 web 服务器配置证书
* --manual：表示插件
* --preferred-challenges dns：表示采用 DNS 验证申请者合法性（是不是域名的管理者）
* --dry-run：在实际申请/更新证书前进行测试，强烈推荐
* -d：表示需要为那个域名申请证书，可以有多个。
* --manual-auth-hook：在执行命令的时候调用一个 hook 文件
* --manual-public-ip-logging-ok：允许公共 IP 日志记录

如果你想为多个域名申请通配符证书（合并在一张证书中，也叫做 SAN 通配符证书），直接输入多个 -d 参数即可，比如：
```
./certbot-auto certonly --manual --preferred-challenges dns --manual-auth-hook /脚本目录/au.sh -d example.com -d *.example.com --manual-public-ip-logging-ok 
```
