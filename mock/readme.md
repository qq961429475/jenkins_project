# 运行单个json文件

`java -jar <path-to-moco-runner> http -p <monitor-port> -c <configuration-file>`

# 运行配置文件（即多个json文件一起生效）

# java -jar <path-to-moco-runner> http -p <monitor-port> -g <configuration-file>

------------jar包的路径--------------------http服务监听的端口----配置文件路径
`java -jar moco-runner-1.5.0-standalone.jar http -p 10086 -g config.json`

