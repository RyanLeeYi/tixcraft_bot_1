import util

# 測試關鍵字解析
test_string = '"2025/07/27 (日) 09:00","2025/07/26 (六) 09:00"'
result = util.parse_keyword_string_to_array(test_string)
print("輸入:", repr(test_string))
print("輸出:", result)
print("長度:", len(result))

# 測試 Unicode 編碼版本
unicode_string = '"2025/07/27 (\u65e5) 09:00","2025/07/26 (\u516d) 09:00"'
unicode_result = util.parse_keyword_string_to_array(unicode_string)
print("\nUnicode 輸入:", repr(unicode_string))
print("Unicode 輸出:", unicode_result)
print("Unicode 長度:", len(unicode_result))

# 測試匹配功能
text_to_match = "2025/07/27 (日) 09:00"
match_result = util.is_text_match_keyword(test_string, text_to_match)
print("\n匹配測試:")
print("關鍵字:", repr(test_string))
print("測試文本:", repr(text_to_match))
print("匹配結果:", match_result)
