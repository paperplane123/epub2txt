#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
EPUB文件文本提取工具
提取EPUB文件中的所有文本内容并保存为文本文件
"""

import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
import os
import sys
import argparse


def extract_text_from_epub(epub_path, output_path=None):
    """从EPUB文件中提取所有文本内容"""
    if not os.path.exists(epub_path):
        print(f"错误: 文件不存在: {epub_path}")
        return False
    
    if output_path is None:
        base_name = os.path.splitext(epub_path)[0]
        output_path = f"{base_name}_完整文本.txt"
    
    all_text = []
    chapter_count = 0
    
    try:
        # 打开EPUB文件
        book = epub.read_epub(epub_path)
        
        # 获取书籍元数据
        title = book.get_metadata('DC', 'title')
        author = book.get_metadata('DC', 'creator')
        
        if title:
            all_text.append(f"书名: {title[0][0]}\n")
        if author:
            all_text.append(f"作者: {author[0][0]}\n")
        all_text.append("\n" + "="*80 + "\n\n")
        
        # 遍历所有项目（章节）
        for item in book.get_items():
            if item.get_type() == ebooklib.ITEM_DOCUMENT:
                # 获取HTML内容
                content = item.get_content()
                
                # 使用BeautifulSoup解析HTML
                soup = BeautifulSoup(content, 'html.parser')
                
                # 移除script和style标签
                for script in soup(["script", "style", "meta", "link"]):
                    script.decompose()
                
                # 提取文本
                text = soup.get_text(separator='\n')
                
                # 清理文本
                lines = []
                for line in text.splitlines():
                    line = line.strip()
                    if line and len(line) > 1:  # 忽略单字符行
                        lines.append(line)
                
                if lines:
                    chapter_count += 1
                    chapter_text = '\n'.join(lines)
                    
                    # 获取章节名称
                    chapter_name = item.get_name()
                    all_text.append(f"\n\n{'='*80}\n")
                    all_text.append(f"章节 {chapter_count}: {chapter_name}\n")
                    all_text.append(f"{'='*80}\n\n")
                    all_text.append(chapter_text)
                    all_text.append("\n")
        
        # 保存提取的文本
        if all_text:
            full_text = ''.join(all_text)
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(full_text)
            
            print(f"✓ 文本提取完成！")
            print(f"  输出文件: {output_path}")
            print(f"  提取了 {chapter_count} 个章节")
            print(f"  文本总长度: {len(full_text)} 字符")
            return True
        else:
            print("✗ 未提取到任何文本内容")
            return False
        
    except Exception as e:
        print(f"✗ 提取文本时出错: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    parser = argparse.ArgumentParser(
        description='EPUB文件文本提取工具',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python extract_epub.py book.epub
  python extract_epub.py book.epub -o output.txt
        """
    )
    parser.add_argument('epub_file', help='EPUB文件路径')
    parser.add_argument('-o', '--output', help='输出文件路径（可选，默认为原文件名_完整文本.txt）')
    
    args = parser.parse_args()
    
    extract_text_from_epub(args.epub_file, args.output)


if __name__ == "__main__":
    main()
