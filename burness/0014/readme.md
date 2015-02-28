## txt2xls.py


- 读入txt内容，为保证其结构，和方便存储，使用json保存:json.load()。以后做读入文本时**尽量使用结构化的库，这样方便操作**。
- 利用xlwt3库，新建workbook对象：xls_workbook = xlwt3.Workbook(),Workbook中添加sheet：xls_wordbook.add_sheet('sheet_name')；然后对表进行操作，写入数据：write()。首先是写入列数，即1，2，3；然后对应列写入对应的数据。
- 保存后，乱码解决方法：1,字体问题，网上有贴表示可能是字体问题，发现使用Simsun字体后，还是会存在乱码，不是字体产生的。2，后来发现，不是程序的问题，是之前，我为了偷懒，直接拷贝的github上面的student.txt的内容，可能直接造成了编码的错误，之后自己在txt文件中写后，程序运行不存在乱码错误。

