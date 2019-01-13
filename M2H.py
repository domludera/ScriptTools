import markdown
import os
import sys
import codecs


thisdir = os.getcwd()

if len(sys.argv)>1:
    thisdir = sys.argv[1]


def convert(path, MDfile):
    name = MDfile
    nameHTML = name[:-2]+'html'
    preHtml = '<!DOCTYPE html><html><head><meta charset="UTF-8"><title>'+name+'</title></head><body>'
    postHtml = '</body></html>'
    print(path)
    input_file = codecs.open(path+'/'+MDfile, mode='r', encoding='utf-8')
    data = input_file.read()
    print('Taking care of: '+name)
    
    html = preHtml+markdown.markdown(data)+postHtml
    try:
        output_file = codecs.open(nameHTML, 'a', encoding='utf-8', errors='xmlcharrefreplace')
        output_file.write(html)
        output_file.close()

    except Exception as e:
        print(e)
        sys.exit(0)

for r, d, f in os.walk(thisdir):
    for file in f:
        if '.md' in file:
                convert(thisdir, file)



