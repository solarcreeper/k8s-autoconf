# 基础镜像
FROM jenkins:latest
# 维护者信息
MAINTAINER ianworks@outlook.com
# 拷贝最新war
COPY jenkins.war /usr/share/jenkins/
# root用户
USER root
RUN echo '' > /etc/apt/sources.list.d/jessie-backports.list \
&& echo "deb http://mirrors.aliyun.com/debian jessie main contrib non-free" > /etc/apt/sources.list \
&& echo "deb http://mirrors.aliyun.com/debian jessie-updates main contrib non-free" >> /etc/apt/sources.list \
&& echo "deb http://mirrors.aliyun.com/debian-security jessie/updates main contrib non-free" >> /etc/apt/sources.list
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN apt-get update && apt-get install -y rsync
# 手动替换国内源 https://mirrors.tuna.tsinghua.edu.cn/jenkins/updates/update-center.json
