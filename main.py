import sys
from html2epub import html2epub

if __name__ == '__main__':
    path = raw_input('请输入需要转换的HTML存放目录：')
    ToPath = raw_input('请输入生成的epub存放目录：')
    book_name = raw_input('请输入生成的epub文件名')
    content = raw_input('请输入epub文件的描述')

    zh = html2epub.html2epub(Path, Topath, book_name, content)
    zh.start()
