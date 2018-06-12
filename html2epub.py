import os
import shutil
import htmlcl
import zipFile

def cmp(a):
    return int(a.split('-', 1)[0])

class Html2epub:
    def __init__(self, Path, Topath, book_name, content):

        self.path = self.Path2Std(Path)
        self.toPath = self.Path2Std(Topath)
        self.book_name = book_name
        self.content = content

    def start(self):
        if os.path.exists('temp'):
            shutil.rmtree('temp')

        shutil.copytree('resource', 'temp')
        os.makedirs('temp/oebps/image')

        navPoint_tmplate = '''
        <navPoint id="{id}" playOrder="{playOrder}">
              <navLabel>
                <text>{text}</text>
              </navLabel>
              <content src="Text/{src}.html"/>
        </navPoint>
        '''

        item_template = '''
        <item href="Text/{title}.html" id="{id}" media-type="application/xhtml+xml"/>
        '''

        item_ref_template = '''
        <itemref idref="{id}"/>
        '''

        toc = ''
        item = ''
        item_ref = ''
        opf_file = open(r'temp/content.opf', 'r', encoding='utf-8')
        opf_content = opf_file.read()

        opf_file.close()

        toc_file = open(r'temp/toc.ncx', 'r', encoding='utf-8')
        toc_content = toc_file.read()
        toc_file.close()

        all_file = os.listdir(self.path)


        all_file = sorted(all_file , key=cmp, reverse=True)

        for _id, html_name in enumerate(all_file, start=1):

            print(html_name)

            if not html_name.endswith('.html'):
                continue

            name = html_name
            FilePath = self.path + name

            title = name.replace('.html', '')
            toc = toc + navPoint_tmplate.format(id=_id, playOrder=_id, text=title, src=title) + '\n'
            item = item + item_template.format(title=title, id=_id) + '\n'
            item_ref = item_ref + item_ref_template.format(id=_id) + '\n'

            html_file = open(FilePath, 'r', encoding='utf-8')
            html_content = html_file.read()
            html_content = '<h1>' + title + '</h1>\n' + html_content
            html_file.close()

            replaced_html = [html_content]
            Parser = htmlcl.get_img(html=replaced_html, path=r'temp/')

            Parser.feed(html_content)

            html_file = open(r'temp/Text/' + title + '.html', 'w', encoding='utf-8')
            html_file.write(replaced_html[0])
            html_file.close()

        toc_file = open(r'temp/toc.ncx', 'w', encoding='utf-8')
        toc_file.write(toc_content.format(toc))
        toc_file.close()

        opf_file = open(r'temp/content.opf', 'w', encoding='utf-8')
        opf_file.write(opf_content.format(title=self.book_name, content1=self.content, content2=self.content, item=item,
                                          item_ref=item_ref))
        opf_file.close()

        zipFile.zip_dir(r'temp', self.toPath + self.book_name + '.epub')
        shutil.rmtree('temp')
        print('已完成')

    def Path2Std(self, Path):

        Path = Path.replace('\\', '/')

        if Path.endswith('/'):
            pass
        else:
            Path += '/'
        return Path
