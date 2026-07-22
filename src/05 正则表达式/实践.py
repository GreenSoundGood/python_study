import re

def main():
    print("=" * 50)
    print(" Python 正则表达式 (re模块) 知识点全解析 ")
    print("=" * 50)

    # ==========================================
    # 1. 基础字符匹配
    # ==========================================
    print("\n【1. 基础字符匹配】")
    
    # . 匹配除换行符外的任意单个字符
    print(". 匹配:", re.search(r'a.c', 'abc a2c a\nc').group())  # 输出: abc
    
    # [] 字符集合
    print("[] 匹配:", re.findall(r'[aeiou]', 'hello world'))  # 输出: ['e', 'o', 'o']
    
    # [^] 否定字符集合
    print("[^] 匹配:", re.findall(r'[^0-9]', 'a1b2c3'))  # 输出: ['a', 'b', 'c']
    
    # [a-z] 字符范围
    print("[-] 范围:", re.findall(r'[a-zA-Z]', '123abcABC'))  # 输出: ['a', 'b', 'c', 'A', 'B', 'C']
    
    # 预定义字符集 \d, \D, \w, \W, \s, \S
    print("\\d 数字:", re.findall(r'\d', 'a1b2'))  # 输出: ['1', '2']
    print("\\w 单词:", re.findall(r'\w', 'a_b-c'))  # 输出: ['a', '_', 'b', 'c']
    print("\\s 空白:", re.findall(r'\s', 'a b\tc'))  # 输出: [' ', '\t']


    # ==========================================
    # 2. 边界匹配（定位符）
    # ==========================================
    print("\n【2. 边界匹配】")
    
    # ^ 和 $ 匹配开头和结尾
    print("^ 开头:", re.search(r'^Hello', 'Hello World').group())  # 输出: Hello
    print("$ 结尾:", re.search(r'World$', 'Hello World').group())  # 输出: World
    
    # \b 单词边界
    print("\\b 单词边界:", re.findall(r'\bcat\b', 'the cat scattered the catnip'))  # 输出: ['cat', 'cat']
    
    # \B 非单词边界
    print("\\B 非边界:", re.findall(r'\Bcat\B', 'the cat scattered the catnip'))  # 输出: ['cat'] (匹配 scattered 中的 cat)


    # ==========================================
    # 3. 量词（重复匹配）
    # ==========================================
    print("\n【3. 量词】")
    
    # *, +, ?
    print("* (0或多):", re.findall(r'ab*c', 'ac abc abbc'))  # 输出: ['ac', 'abc', 'abbc']
    print("+ (1或多):", re.findall(r'ab+c', 'ac abc abbc'))  # 输出: ['abc', 'abbc']
    print("? (0或1):", re.findall(r'ab?c', 'ac abc abbc'))  # 输出: ['ac', 'abc', 'abc'] (abbc中的abc被匹配)
    
    # {n}, {n,}, {n,m}
    print("{n} 精确:", re.findall(r'a{3}', 'aa aaa aaaa'))  # 输出: ['aaa', 'aaa']
    
    # 贪婪 vs 非贪婪
    text_html = '<b>hello</b>'
    print("贪婪模式:", re.search(r'<.*>', text_html).group())  # 输出: <b>hello</b>
    print("非贪婪模式:", re.search(r'<.*?>', text_html).group())  # 输出: <b>


    # ==========================================
    # 4. 分组与选择
    # ==========================================
    print("\n【4. 分组与选择】")
    
    # () 捕获分组
    m = re.search(r'(abc)+', 'abcabcabc')
    print("捕获分组(整体):", m.group(0))  # 输出: abcabcabc
    print("捕获分组(组1):", m.group(1))  # 输出: abc (注意：重复匹配时，捕获的是最后一次匹配的内容)
    
    # (?:) 非捕获分组
    m = re.search(r'(?:abc)+', 'abcabc')
    print("非捕获分组:", m.group(0))  # 输出: abcabc
    
    # | 逻辑或
    print("| 逻辑或:", re.findall(r'cat|dog', 'I have a cat and a dog'))  # 输出: ['cat', 'dog']
    
    # \1 反向引用
    print("\\1 反向引用:", re.findall(r'(.)\1', 'aabbccdd'))  # 输出: ['a', 'b', 'c', 'd']


    # ==========================================
    # 5. 零宽断言（前瞻与后顾）
    # ==========================================
    print("\n【5. 零宽断言】")
    # 注意：Python 的 re 模块要求后顾断言 (?<=...) 和 (?<!...) 中的模式必须是【固定宽度】的
    
    # (?=) 正向先行断言
    print("正向先行:", re.search(r'Windows(?=10)', 'Windows10 Windows11').group())  # 输出: Windows
    
    # (?!) 负向先行断言
    print("负向先行:", re.search(r'Windows(?!10)', 'Windows10 Windows11').group())  # 输出: Windows (匹配 Windows11 中的)
    
    # (?<=) 正向后行断言
    print("正向后行:", re.search(r'(?<=@)gmail', '@gmail.com').group())  # 输出: gmail
    
    # (?<!) 负向后行断言
    print("负向后行:", re.search(r'(?<!@)gmail', 'gmail.com').group())  # 输出: gmail


    # ==========================================
    # 6. 转义字符
    # ==========================================
    print("\n【6. 转义字符】")
    
    # 匹配特殊符号
    print("转义点号:", re.search(r'\.', 'a.b').group())  # 输出: .
    # 匹配反斜杠 (在 raw string 中需要写两个反斜杠)
    print("转义反斜杠:", re.search(r'\\', 'a\\b').group())  # 输出: \


    # ==========================================
    # 7. 修饰符（Flags）
    # ==========================================
    print("\n【7. 修饰符 (Flags)】")
    
    # re.IGNORECASE (re.I) 忽略大小写
    print("忽略大小写:", re.findall(r'cat', 'Cat cat CAT', re.I))  # 输出: ['Cat', 'cat', 'CAT']
    
    # re.MULTILINE (re.M) 多行模式
    text_multi = "Hello\nWorld"
    print("多行模式^:", re.findall(r'^World', text_multi, re.M))  # 输出: ['World']
    
    # re.DOTALL (re.S) 单行模式 (让 . 匹配换行符)
    print("单行模式.:", re.search(r'a.b', 'a\nb', re.S).group())  # 输出: a\nb


    # ==========================================
    # 8. 常用正则表达式示例 (使用 re.compile 提升性能)
    # ==========================================
    print("\n【8. 常用正则表达式实战】")
    
    # 1. 验证中国大陆手机号
    phone_re = re.compile(r'^1[3-9]\d{9}$')
    print("手机号验证:", phone_re.match('13812345678') is not None)  # 输出: True
    
    # 2. 验证电子邮箱
    email_re = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    print("邮箱验证:", email_re.match('test@example.com') is not None)  # 输出: True
    
    # 3. 提取 HTML 标签中的文本 (非贪婪)
    html_text = '<p>Hello <b>World</b></p>'
    # 提取 <b> 标签内的内容
    print("HTML提取:", re.findall(r'<b>(.*?)</b>', html_text))  # 输出: ['World']
    
    # 4. 验证强密码 (至少8位，包含大小写、数字、特殊字符)
    pwd_re = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$')
    print("强密码验证:", pwd_re.match('Pass123!') is not None)  # 输出: True
    
    # 5. 匹配 IPv4 地址
    ip_re = re.compile(r'\b(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\b')
    print("IP提取:", ip_re.findall('IP: 192.168.1.1 and 256.1.1.1'))  # 输出: ['192.168.1.1']


if __name__ == '__main__':
    main()