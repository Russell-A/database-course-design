### Instructions of the airline ticket booking system

The demo system is developed with two Python package: PyQt5 and pyodbc. The database we use is SQL SERVER 2008 R2.

* Instructions befrore usage：
  1. The user needs to install Python package: PyQt5 and pyodbc before usage.
  2. The user needs to ensable super account "sa" in the database to allow us to modify the database. Please refer to https://blog.csdn.net/ren6370/article/details/73409989
  3. The adminstrator can carry out "crbas.sql" to create sample data sheets in the database. He can also carry out "trigger.sql", "sqlviews.sqk", "PD_search.sql", "copy_table.sql" to create the view, trigger, and process needed for the program.
   
* Instructions of the functions:
    Register and log in module:
    Users can register and log in in the "register" menu.
    The program will automatically distinguish whether the user is an administrator or a common customer.
    The program enables the new users to register. The new users need to input their file name and passcode.
    Users can log out the system by clicking "Log out"

    Searching and buying tickets in module:
    Before logging in, the users can search on the main page whether this is any ticket available by departure date, departure place, destination and flight class. The program wull show all the available tickets and it's flight number, departure time, arrival time, tickets left, and price.
    After logging in, the users can buy tickets. Buy searching and clicking the available tickets, the users can click "buy" to buy tickets. Ther users need to choose flight class. They also need to input their sex, identity and phone number. When clicking the "but" button, the program uses a lock to lock the inquired line, preventing other process to modify these data to solve the problem of high mutiprocesssing.
    
    The data management module:
    The usrs can modify his passcode and contact in formation. They can also searching for their used and unused tickets, it will shows the departure airport, destination airport and flight time, and they can return the unused tickets.
    The adminstrators can add new fligts. In this way, the left tickets will be generated automatically by searching for the flight's maximum available seats. The function is implemented with trigger. They can search for specific flight and modify it. They can also inquiry the customers' information, but the customers' privacy is protected by differential privacy.



### 航空票务系统使用说明

* 本系统基于PyQt5以及pyodbc两个模块以及SQL SERVER 2008 R2开发，开发小组保留所有权

* 系统使用说明：
  1. 使用前,用户需要安装PyQt5以及pyodbc两个模块
  2. 由于购票模块使用了pyodbc模块，用户需要在数据库上打开sa超级账户，给予软件数据库的访问修改权限。具体打开方式请见：
    https://blog.csdn.net/ren6370/article/details/73409989
  3. 数据库的管理人员可以执行crbas.sql在数据库中创建相应的数据表，并执行trigger.sql,sqlviews.sqk,PD_search.sql,copy_table.sql 创建程序需要的视图，触发器以及存储过程 
   
* 功能模块说明：
    注册和登录模块：
    在注册菜单下有注册和登录功能。
    通过用户名和密码登录，将会由软件识别登录的是管理员还是普通用户。
    支持注册新普通用户，需输入用户名和密码，有二次输入密码校验功能。
    点击“退出登录”即可完成登录退出功能。

    查询和购票：
    在未登录的情况下，游客可以在主页上通过出发日期、出发地、到达地和舱位来进行查询是否有机票，软件将会显示机票航程号、航班号、出发时间、到达时间、剩余票数和票价。
    在登录后，普通用户可以进行购票操作，通过查询并选中可购买的航程，点击购买可进入购买界面。在购买界面普通用户可选择舱位，并输入性别、乘客类别、身份证号和电话号码之后，若订购的航程还有余票则能进行购买，否则购买不成功。在点击购票按钮后采用行排它锁在整个事务中锁定需要查询和更改的行，阻止其他线程访问和修改这些数据，来解决高并发买票的问题。

    数据管理模块：
    在菜单中的功能项目下，对于普通用户，可通过菜单中的功能->用户->修改个人信息，来修改用户的密码和联系方式。
    并且，在“我的订单”中可以查询用户的出行和未出行的票务，显示对应的出发机场、目的机场、航班时间等信息，并且可在该界面进行退票。

    在功能->管理员菜单下，有添加航程功能，可通过输入飞行计划表中的各项数据来插入新的数据，在该功能下，剩余机票将会由程序通过查询航班的最大载客量自动填充座位数，该功能由触发器完成。
    查看\修改航程功能则通过航程号或航班号查询特定航程，在表中对各项信息修改，点击“提交修改”后完成对飞行计划表的更新。并且支持添加新航程和删除航程信息的功能，分别通过点击“添加一行”和“删除选中行”完成。点击“取消修改”可以撤销未提交的修改记录。
    在该菜单下同时支持通过航班号查询，对航班表进行修改；通过飞机编号查询，对飞机登记表进行修改；通过查询飞机机型，对飞机表进行修改；通过查询机场代码或机场所在城市，对机场表进行修改。上述模块同时具有修改、删除和增加行的功能。
    另外，管理员可以查询特定航程号的乘客信息，显示航班信息、购买该航班的乘客信息，其中隐私信息如身份证号，乘客类别，通过差分隐私的逻辑进行加工，对数据做了部分遮盖和模糊，以保护用户隐私。

