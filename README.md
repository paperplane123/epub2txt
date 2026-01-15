# EPUB2TXT

一个简单的EPUB电子书转TXT文本工具。

## 项目缘由

因为我在看epub电子书时，发现电脑上没有装趁手的阅读器，用WPS将就着看吧，看到想蛐蛐的地方，发现wps对epub的支持实在是简陋，查了一圈在wps官方论坛上确认了不支持。想起来，早年间edge是支持的，结果一查又使我回忆起傻逼微软又把好功能砍掉了。。。。索性就拿IDE试试，果然是意料之中的打不开，把报错结果扔给cursor的auto模型，没想到几番折腾，自己给我干成了txt，算是实现了我要标注的需求，遂发此仓库，不为功能，主要为感慨。

## 功能

- 提取EPUB文件中的所有文本内容
- 自动提取书籍元数据（书名、作者等）
- 按章节组织文本内容
- 输出为UTF-8编码的TXT文件，方便在任何文本编辑器中打开和标注

## 安装依赖

```bash
pip install -r requirements.txt
```

## 使用方法

### 基本用法

```bash
python extract_epub.py your_book.epub
```

输出文件将自动命名为 `your_book_完整文本.txt`

### 指定输出文件

```bash
python extract_epub.py your_book.epub -o output.txt
```

## 依赖

- `ebooklib` - EPUB文件解析
- `beautifulsoup4` - HTML内容解析
- `lxml` - BeautifulSoup的解析器（推荐）

## 许可证

MIT License

## 致谢

感谢 Cursor 的 Auto 模型，在几番折腾后帮我实现了这个简单的需求。
