# 中文使用说明文档

## 环境配置

### 操作系统安装
* 建议安装 ubuntu 16.04

有三个选择： 
1. 在自己电脑上装双系统；
2. 在自己电脑上安装虚拟机
3. 自己租用google、aws服务器，上边自带linux系统

### 安装anaconda3
安装可以参考：https://www.jianshu.com/p/f7c341085746

### 创建虚拟环境
```python
conda create -n word python=3.5
conda activate word
```
### 安装库
```python
pip install tensorflow==0.12.0
pip install nltk pandas scikit-learn
```

cd到项目文件夹
运行我写的demo脚本demo.py即可 （demo.py里有注释）
```python
python demo.py
```