# JUST-Daily-Check

![python version](https://img.shields.io/badge/python-3.6+-orange.svg)
![support os](https://img.shields.io/badge/os-linux%2C%20win%2C%20mac-yellow.svg)

## 注意!!!

**打卡系统中所提交的信息来自于上一次打卡所填写的信息，因此如有信息更改，请手动填写一次！**

**有任何问题请联系ljw_rookie@163.com**

## Introduction
* **website: http://justdailycheck.co.ax:17206/index**
  - Due to the procedure, you have to wait for five seconds while submit. 
  - student number is your student ID.
  - student passsword is your password used for login portal of JUST.
* check time: 6:05 every morning
## Installation

### Prerequisites

* python >= 3.6

### Step 1 
Download chrome rpm package [download url](https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm)


### Step 2
Download required package
```shell
yum install -y lsb

yum install -y libXScrnSaver
```
### Step 3
Install chrome
```shell
rpm -ivh google-chrome-stable_current_x86_64.rpm
# rmp -ivh 后面跟的是下载的chrome rpm包全名,注意rpm路径。
```
### Step 4
```shell
sudo yum localinstall google-chrome-stable_current_x86_64.rpm
```
### Step 5
* Install Tesseract in Linux system, [Tutorial](https://blog.csdn.net/wanght89/article/details/78329546)
## More Info
* If you have some develop, please PR.

* Team  ***JUST-NLP***
