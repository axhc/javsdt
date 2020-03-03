# -*- coding:utf-8 -*-
import os
from configparser import RawConfigParser
from shutil import copyfile
from traceback import format_exc

try:
    print('>>正在重写ini...')
    config_settings = RawConfigParser()
    config_settings.add_section("收集nfo")
    config_settings.set("收集nfo", "是否跳过已存在nfo的文件夹？", "否")
    config_settings.set("收集nfo", "是否收集nfo？", "是")
    config_settings.set("收集nfo", "nfo中title的格式", "车牌+空格+标题")
    config_settings.set("收集nfo", "是否去除标题末尾可能存在的演员姓名？", "否")
    config_settings.set("收集nfo", "是否将系列作为特征？", "是")
    config_settings.set("收集nfo", "是否将片商作为特征？", "是")
    config_settings.set("收集nfo", "额外将以下元素添加到特征中", "")
    config_settings.add_section("重命名影片")
    config_settings.set("重命名影片", "是否重命名影片？", "是")
    config_settings.set("重命名影片", "重命名影片的格式", "车牌+空格+标题")
    config_settings.add_section("修改文件夹")
    config_settings.set("修改文件夹", "是否重命名或创建独立文件夹？", "是")
    config_settings.set("修改文件夹", "新文件夹的格式", "【+全部演员+】+车牌")
    config_settings.add_section("归类影片")
    config_settings.set("归类影片", "是否归类影片？", "否")
    config_settings.set("归类影片", "针对文件还是文件夹？", "文件夹")
    config_settings.set("归类影片", "归类的根目录", "所选文件夹")
    config_settings.set("归类影片", "归类的标准", "影片类型\全部演员")
    config_settings.add_section("下载封面")
    config_settings.set("下载封面", "是否下载封面海报？", "是")
    config_settings.set("下载封面", "DVD封面的格式", "视频+-fanart.jpg")
    config_settings.set("下载封面", "海报的格式", "视频+-poster.jpg")
    config_settings.add_section("字幕文件")
    config_settings.set("字幕文件", "是否重命名已有的字幕文件？", "是")
    config_settings.set("字幕文件", "是否跳过已有字幕的影片？", "是")
    config_settings.set("字幕文件", "已有字幕即nfo包含", "-C、中字、中文字幕、㊥")
    config_settings.add_section("kodi专用")
    config_settings.set("kodi专用", "是否收集演员头像？", "否")
    config_settings.add_section("emby/jellyfin")
    config_settings.set("emby/jellyfin", "网址", "http://localhost:8096/")
    config_settings.set("emby/jellyfin", "API ID", "b55d950becc74bbebbf4698d995db826")
    config_settings.set("emby/jellyfin", "是否覆盖以前上传的头像？", "否")
    config_settings.add_section("代理")
    config_settings.set("代理", "是否使用代理？", "否")
    config_settings.set("代理", "代理IP及端口", "127.0.0.1:1080")
    # config_settings.set("其他设置", "是否将全部演员（多个）表现为“n人共演？", "否")
    config_settings.add_section("原影片文件的性质")
    config_settings.set("原影片文件的性质", "无视无码视频文件名中多余的字母数字", "1080p、Caribbean、Carib、1Pondo、1pondo、1pon、FHD、fhd、ALL、Tokyo-hot、Tokyo-Hot、TokyoHot、3xplanet、full")
    config_settings.set("原影片文件的性质", "是否中字即文件名包含", "-c、-C、_C、中字、中文字幕")
    config_settings.set("原影片文件的性质", "是否中字的表现形式", "㊥")
    config_settings.set("原影片文件的性质", "是否xx即文件名包含", "流出")
    config_settings.set("原影片文件的性质", "是否xx的表现形式", "无码流出")
    config_settings.set("原影片文件的性质", "有码", "有码")
    config_settings.set("原影片文件的性质", "无码", "无码")
    config_settings.set("原影片文件的性质", "素人", "素人")
    config_settings.set("原影片文件的性质", "FC2", "FC2")
    config_settings.add_section("信息来源")
    config_settings.set("信息来源", "是否用javlibrary整理影片时收集网友的热评？", "是")
    config_settings.set("信息来源", "是否用javlibrary整理影片时同样去javbus获取系列？", "是")
    config_settings.set("信息来源", "列出车牌(素人为主，可自行添加)", "LUXU、MIUM、GANA、NTK、ARA、DCV、MAAN、HOI、NAMA、SWEET、SIRO、SCUTE、CUTE、SQB、JKZ、URF、SIMM、ORETD、PER、EZD、EVA、JAC、ORE、ION")
    config_settings.add_section("其他设置")
    config_settings.set("其他设置", "简繁中文？", "简")
    config_settings.set("其他设置", "javlibrary网址", "http://www.p42u.com/")
    config_settings.set("其他设置", "javbus网址", "https://www.cdnbus.cloud/")
    config_settings.set("其他设置", "javdb网址", "https://javdb4.com/")
    config_settings.set("其他设置", "扫描文件类型", "mp4、mkv、avi、wmv、iso、rmvb、flv、ts、MP4、MKV、AVI、WMV、ISO、RMVB、FLV、TS")
    config_settings.set("其他设置", "重命名中的标题长度（50~150）", "50")
    config_settings.add_section("百度翻译API")
    config_settings.set("百度翻译API", "是否需要日语简介？", "是")
    config_settings.set("百度翻译API", "是否翻译为中文？", "否")
    config_settings.set("百度翻译API", "app id", "")
    config_settings.set("百度翻译API", "密钥", "")
    config_settings.add_section("百度人体分析")
    config_settings.set("百度人体分析", "是否需要准确定位人脸的poster？", "否")
    config_settings.set("百度人体分析", "appid", "")
    config_settings.set("百度人体分析", "api key", "")
    config_settings.set("百度人体分析", "secret key", "")
    config_settings.write(open('【点我设置整理规则】.ini', "w", encoding='utf-8-sig'))
    print('写入ini文件成功！')
    os.system('pause')
except:
    print(format_exc())
    print('\n创建ini失败，解决上述问题后，重新打开exe创建ini！')
    os.system('pause')
