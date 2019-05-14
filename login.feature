# Created by doudou at 2018/5/6

Feature:bss

 Scenario Outline: login bss success
    Given Access bss website
    When  Input  <username> enter  <passwords>
    And Click button "登录"

  Examples:Amphibians
  |   username   |   passwords     |
  | 18401504837  |   whd19931121   |


  Scenario Outline: caozuo
    Given login success
    When  I click the <operating>
    Then  I can see <result>

   Examples: casesuccess
  |   operating    |   result      |
  |    组织架构     |    人员管理     |
#  |    人员管理     |    新增人员     |
#  |  13500000001   |  测试金融销售01  |
#  |    退出         |   手机号        |

