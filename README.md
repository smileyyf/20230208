# test_ui
# web-UI 自动化测试示例

---

## 框架设计

- pytest
- selenium
- POM页面对象模型（Page Object Model）

---

## 目录结构

    common                 ——公共类
    page_base              ——基类
    page_locators          ——页面元素类
    page_object            ——页面对象类
    TestCase               ——测试用例
    conftest.py            ——pytest胶水文件
    pytest.ini             ——pytest配置文件

---

## 运行

### 安装依赖

```shell
pip install -r requirements.txt
```

### 执行主文件

* 在项目根目录执行`run_case.py xxx xxx`文件即可运行项目
* 第一个参数xxx: 
  * test 测试环境
  * pre 预发布环境
  * prod 正式环境
* 第二个参数xxx：
  * true 发送钉钉消息
  * false 不发送钉钉消息
  * 不传默认不发送


# allure参数说明


- pytest --alluredir `result-path`
    - --clean-alluredir 清除历史生成记录
- allure generate `result-path`
    - -c 生成报告前删除上一次生成的报告
    - -o 指定生成的报告目录
- allure open `report-path`
