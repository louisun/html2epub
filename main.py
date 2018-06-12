from html2epub import Html2epub

if __name__ == '__main__':
    path = input('请输入HTML存放目录(绝对路径)：')
    toPath = input('请输入epub存放目录(绝对路径)：')
    book_name = input('请输入epub文件名(不需带.epub):')
    content = input('请输入epub文件的描述')

    zh = Html2epub(path, toPath, book_name, content)
    zh.start()
