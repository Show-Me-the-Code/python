## 第 0005 题
你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。

## change_size.py

处理前图片：当前目录下的 test 文件夹里

处理后图片：当前目录下的 result 文件夹里

支持 .jpg .png .bmp 等图片格式，转换后不改变原格式

## 知识点学习总结
### PIL

**mac 上给python3安装PIL**

```
▶ which python
/usr/local/bin/python

▶ which python3
/usr/local/bin/python3

▶ which pip3
/usr/local/bin/pip3

▶ pip3 install Pillow
Collecting Pillow
  Downloading Pillow-4.2.1-cp36-cp36m-macosx_10_6_intel.macosx_10_9_intel.macosx_10_9_x86_64.macosx_10_10_intel.macosx_10_10_x86_64.whl (3.5MB)
    100% |████████████████████████████████| 3.5MB 348kB/s
Collecting olefile (from Pillow)
  Using cached olefile-0.44.zip
Building wheels for collected packages: olefile
  Running setup.py bdist_wheel for olefile ... done
  Stored in directory: /Users/xiaqunfeng/Library/Caches/pip/wheels/20/58/49/cc7bd00345397059149a10b0259ef38b867935ea2ecff99a9b
Successfully built olefile
Installing collected packages: olefile, Pillow
Successfully installed Pillow-4.2.1 olefile-0.44
```

在修改尺寸的时候，使用的 `thumbnail()` 函数，并没有使用 `resize()`。 `Image.resize()`和`Image.thumbnail()` 这两个函数都是对图片进行缩放, 两者的主要区别如下:

- resize()函数会返回一个Image对象, thumbnail()函数返回None
- resize()修改后的图片在返回的Image中, 而原图片没有被修改; thumbnail()直接对内存中的原图进行了修改, 但是修改需要保存
- resize()中的size参数直接设定了resize之后图片的规格, 而thumbnail()中的size参数则是设定了x/y上的最大值. 也就是说, 经过resize()处理的图片可能会被拉伸, 而经过thumbnail()处理的图片不会被拉伸
- thumbnail()函数内部调用了resize(), 可以认为thumbnail()是对resize()的一种封装

基本调用方式如下：

```
from PIL import Image
# Image.resize usage
with Image.open("test.jpg") as img:
    resized = img.resize((new_x, new_y), resample=Image.LANCZOS)
    resized.save("resized.jpg", format="jpeg")

# Image.thumbnail usage
with Image.open("test.jpg") as img:
    img.thumbnail((max_x, max_y), resample=Image.LANCZOS)
    img.save("thumbnail.jpg", format="jpeg")
```

### OS

**os.walk()**

`os.walk()` 方法为我们遍历目录树， 每次进入一个目录，它会返回一个三元组，包含相对于查找目录的相对路径，一个该目录下的目录名列表， 以及那个目录下面的文件名列表。

```
for root, dirs, files in os.walk(dir_name)
```

- root: 相对于 dir_name 的相对路径
- dirs: 该路径下的目录名列表，没有为空
- files: 目录下文件名列表

**os.path**

对于任何的文件名的操作，都应该使用 `os.path` 模块，而不是使用标准字符串操作来构造自己的代码。

```
os.path.join(path1[, path2[, ...]])
```

用于将分离的各部分分组合成一个路径名

