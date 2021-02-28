# Restful/Python3 Example for Aliyun Intelligent Speech Interaction Service 

The Official document only provide python 2.x version of speech synthesis example for long text. This repo provide an example of python 3 version and save private information like tokens into text files and ignore them with .gitignore.

## Official Documentation

Offical documentation can be found [here](https://help.aliyun.com/document_detail/119258.html).

## File Organization

Please create new folders `config`, `text` and `audio` and save `accesskeyid`, `accesskeysecret` and `appkey` into `config`. `text` folder is for input text and `audio` is for output audio.

![folders](./assets/folders.png)

## Files

`update_token.py` is for updating tokens from server. It read necessary information from `config` and save token into the same folder.

`short.py` is for short speech synthesis.

`long.py` is for long speech synthesis.


# 阿里云语音合成Resutful/Python3示例

阿里云官方文档中，长文本语音合成的Restful API只有python2版本，因此修改为python3版本，并将token等隐私信息存入文本文件通过gitignore忽略。

## 官方文档

官方文档详见[链接](https://help.aliyun.com/document_detail/119258.html)。

## 目录结构

请先本仓库下新建`config`, `text`, `audio`三个文件夹，并在`config`文件夹下保存`accesskeyid`, `accesskeysecret`, `appkey`，在`text`文件夹下保存需要合成的文本，`audio`文件夹用于如下图所示。

![folders](./assets/folders.png)

## 文件说明

`update_token.py`用于更新token，从`config`中读取所需信息，运行后会将token以文本形式保存至`config`文件夹。

`short.py`为短文本语音合成程序。

`long.py`为长文本语音合成程序。
