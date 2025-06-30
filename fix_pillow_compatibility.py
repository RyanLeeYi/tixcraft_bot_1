#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Pillow 兼容性修復
為了修復 ddddocr 與新版 Pillow 的兼容性問題
"""

def fix_pillow_compatibility():
    """
    修復 Pillow 兼容性問題
    在新版 Pillow 中，ANTIALIAS 被移除了，這會導致 ddddocr 報錯
    """
    try:
        from PIL import Image
        
        # 如果 ANTIALIAS 不存在，則添加兼容性支持
        if not hasattr(Image, 'ANTIALIAS'):
            # 在新版 Pillow 中，ANTIALIAS 被 LANCZOS 替代
            Image.ANTIALIAS = Image.LANCZOS
            print("✓ 已修復 Pillow ANTIALIAS 兼容性問題")
            return True
        else:
            print("✓ Pillow ANTIALIAS 屬性已存在")
            return True
            
    except ImportError:
        print("✗ Pillow 未安裝")
        return False
    except Exception as e:
        print(f"✗ 修復 Pillow 兼容性時發生錯誤: {e}")
        return False

def test_ddddocr_with_fix():
    """
    測試修復後的 ddddocr 功能
    """
    print("=== 測試修復後的 ddddocr 功能 ===")
    
    # 先應用修復
    if not fix_pillow_compatibility():
        return False
    
    try:
        import ddddocr
        print("✓ ddddocr 導入成功")
        
        # 測試初始化
        ocr = ddddocr.DdddOcr()
        print("✓ ddddocr 初始化成功")
        
        # 創建一個簡單的測試圖像
        from PIL import Image
        import io
        
        # 創建 100x30 的白色測試圖像
        img = Image.new('RGB', (100, 30), color='white')
        img_byte_array = io.BytesIO()
        img.save(img_byte_array, format='PNG')
        img_bytes = img_byte_array.getvalue()
        
        # 測試 OCR 分類
        result = ocr.classification(img_bytes)
        print(f"✓ OCR 分類測試成功，結果: {result}")
        
        return True
        
    except Exception as e:
        print(f"✗ ddddocr 測試失敗: {e}")
        return False

if __name__ == "__main__":
    success = test_ddddocr_with_fix()
    if success:
        print("\n🎉 所有測試通過！OCR 功能已準備就緒。")
    else:
        print("\n❌ 測試失敗，請檢查環境配置。")
