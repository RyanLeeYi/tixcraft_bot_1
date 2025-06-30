#!/usr/bin/env python3
# 詳細的Edge WebDriver診斷

import os
import sys
import platform
sys.path.insert(0, '.')

def diagnose_edge_setup():
    print("=== Edge WebDriver 詳細診斷 ===\n")
    
    # 1. 檢查系統資訊
    print("1. 系統資訊:")
    print(f"   作業系統: {platform.system()} {platform.release()}")
    print(f"   架構: {platform.machine()}")
    print(f"   Python版本: {platform.python_version()}")
    
    # 2. 檢查模組導入
    print("\n2. 模組導入檢查:")
    try:
        import util
        print("   ✓ util模組導入成功")
    except Exception as e:
        print(f"   ❌ util模組導入失敗: {e}")
        return False
    
    try:
        from selenium import webdriver
        from selenium.webdriver.edge.service import Service
        from selenium.webdriver.edge.options import Options
        print("   ✓ Selenium Edge模組導入成功")
    except Exception as e:
        print(f"   ❌ Selenium Edge模組導入失敗: {e}")
        return False
    
    # 3. 檢查路徑設置
    print("\n3. 路徑檢查:")
    try:
        Root_Dir = util.get_app_root()
        webdriver_path = os.path.join(Root_Dir, "webdriver")
        edge_driver_path = os.path.join(webdriver_path, "msedgedriver.exe")
        
        print(f"   應用根目錄: {Root_Dir}")
        print(f"   WebDriver目錄: {webdriver_path}")
        print(f"   Edge Driver路徑: {edge_driver_path}")
        
        if os.path.exists(webdriver_path):
            print("   ✓ WebDriver目錄存在")
        else:
            print("   ❌ WebDriver目錄不存在")
            return False
            
        if os.path.exists(edge_driver_path):
            print("   ✓ Edge Driver存在")
            # 檢查檔案大小
            size = os.path.getsize(edge_driver_path)
            print(f"   檔案大小: {size:,} bytes")
        else:
            print("   ❌ Edge Driver不存在")
            return False
            
    except Exception as e:
        print(f"   ❌ 路徑檢查失敗: {e}")
        return False
    
    # 4. 檢查Edge選項創建
    print("\n4. Edge選項創建:")
    try:
        from chrome_tixcraft import get_chrome_options
        
        config_dict = {
            "browser": "edge",
            "homepage": "https://www.google.com",
            "advanced": {
                "chrome_extension": False,
                "headless": False,
                "proxy_server_port": "",
                "verbose": True
            }
        }
        
        edge_options = get_chrome_options(webdriver_path, config_dict)
        print("   ✓ Edge選項創建成功")
        print(f"   選項類型: {type(edge_options)}")
        
    except Exception as e:
        print(f"   ❌ Edge選項創建失敗: {e}")
        return False
    
    # 5. 創建Edge服務
    print("\n5. Edge服務創建:")
    try:
        edge_service = Service(edge_driver_path)
        print("   ✓ Edge服務創建成功")
    except Exception as e:
        print(f"   ❌ Edge服務創建失敗: {e}")
        return False
    
    # 6. 測試Edge WebDriver創建
    print("\n6. Edge WebDriver測試:")
    try:
        print("   正在創建Edge WebDriver...")
        driver = webdriver.Edge(service=edge_service, options=edge_options)
        print("   ✓ Edge WebDriver創建成功！")
        
        print("   正在測試基本功能...")
        driver.get("https://www.google.com")
        title = driver.title
        url = driver.current_url
        
        print(f"   ✓ 頁面標題: {title}")
        print(f"   ✓ 當前URL: {url}")
        
        driver.quit()
        print("   ✓ WebDriver已正常關閉")
        
        return True
        
    except Exception as e:
        print(f"   ❌ Edge WebDriver測試失敗: {e}")
        print(f"   錯誤類型: {type(e).__name__}")
        
        # 提供詳細錯誤分析
        error_str = str(e).lower()
        if "session not created" in error_str:
            print("   分析: WebDriver版本與瀏覽器版本不匹配")
        elif "timeout" in error_str:
            print("   分析: 連接超時，可能是防火牆或網路問題")
        elif "permission" in error_str:
            print("   分析: 權限問題，嘗試以管理員身份運行")
        elif "cannot find" in error_str or "no such file" in error_str:
            print("   分析: 檔案路徑或瀏覽器安裝問題")
        
        return False

def main():
    success = diagnose_edge_setup()
    
    print(f"\n=== 診斷結果 ===")
    if success:
        print("🎉 Edge WebDriver設置完全正常，可以使用！")
        print("\n建議:")
        print("1. 您的程式現在可以正常使用Edge瀏覽器")
        print("2. 確保settings.json中browser設置為'edge'")
        print("3. 可以開始運行您的爬蟲程式了")
    else:
        print("❌ Edge WebDriver設置有問題")
        print("\n建議:")
        print("1. 檢查Edge瀏覽器是否已安裝並更新到最新版本")
        print("2. 嘗試重新下載對應版本的msedgedriver.exe")
        print("3. 確保防火牆或防毒軟體沒有阻擋")
        print("4. 嘗試以管理員身份運行程式")

if __name__ == "__main__":
    main()
